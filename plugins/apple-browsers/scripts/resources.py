#!/usr/bin/env python3
"""Bounded Apple browsers cache and simulator ownership operations (stdlib only)."""
import argparse
import errno
import fcntl
from functools import wraps
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import time
import uuid

ROOT = Path.home() / 'code/apple-browsers-worktrees'
TARGET = 60 * 1024**3


def run(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True, stderr=subprocess.DEVNULL, timeout=8).strip()


def safe(path, root):
    path, root = Path(path).absolute(), Path(root).absolute()
    if path == root or not path.is_relative_to(root):
        raise ValueError('Path escapes resource root')
    for item in (path, *path.parents):
        if item.is_symlink():
            raise ValueError('Symlink resource path refused')
        if item == root:
            break
    return path


def canonical(checkout, root=ROOT):
    checkout = Path(checkout).absolute()
    if checkout.is_symlink():
        raise ValueError("Symlink checkout refused")
    cache = safe(Path(root) / '.dd' / checkout.name, Path(root) / '.dd')
    metadata = cache / '.apple-owner.json'
    if metadata.exists() and json.loads(metadata.read_text())['checkout'] != str(checkout):
        raise ValueError('Derived-data basename ownership collision')
    if cache.exists() and not metadata.exists() and any(cache.iterdir()):
        raise ValueError('Existing cache has no proven owner')
    return cache


def live_paths(output):
    paths = set()
    for line in output.splitlines():
        if 'xcodebuild' not in line:
            continue
        try:
            tokens = shlex.split(line)
            for index, token in enumerate(tokens):
                if token == '-derivedDataPath' and index + 1 < len(tokens):
                    
                    if index + 2 < len(tokens) and not tokens[index + 2].startswith('-'):
                        raise ValueError('Ambiguous process derived-data path; refusing cleanup')
                    paths.add(str(Path(tokens[index + 1]).absolute()))
                elif token.startswith('-derivedDataPath='):
                    paths.add(str(Path(token.split('=', 1)[1]).absolute()))
        except ValueError:
            raise ValueError('Cannot safely parse live build process')
    return paths


def processes():
    return live_paths(run('ps', '-axo', 'command='))


def size(path):
    total = 0
    for base, dirs, files in os.walk(path, followlinks=False):
        dirs[:] = [d for d in dirs if not (Path(base) / d).is_symlink()]
        for name in files:
            total += (Path(base) / name).lstat().st_size
    return total


def cache_plan(root, current, live):
    plans = []
    dd = Path(root) / '.dd'
    if dd.is_symlink():
        raise ValueError('Symlink cache root')
    for cache in dd.iterdir() if dd.exists() else []:
        if cache == current or str(cache.absolute()) in live:
            continue
        try:
            safe(cache, dd)
            meta = json.loads((cache / '.apple-owner.json').read_text())
            owner = Path(meta['checkout'])
            if owner.is_symlink():
                continue
            rank = 0 if not owner.exists() else 2
            if rank:
                try:
                    run('git', 'merge-base', '--is-ancestor', 'HEAD', 'origin/main', cwd=owner)
                    rank = 1
                except subprocess.SubprocessError:
                    try:
                        upstream = run('git', 'rev-parse', '--abbrev-ref', '@{upstream}', cwd=owner)
                        if upstream.startswith('origin/'):
                            run('git', 'ls-remote', '--exit-code', 'origin', 'HEAD', cwd=owner)
                            if not run('git', 'ls-remote', '--heads', 'origin', upstream.removeprefix('origin/'), cwd=owner):
                                rank = 1
                    except subprocess.SubprocessError:
                        pass
            plans.append((rank, meta.get('lastUsed', 0), cache))
        except (OSError, ValueError, KeyError, subprocess.SubprocessError):
            continue
    return [item[2] for item in sorted(plans)]


def prepare(checkout, root=ROOT, free=None, live=None):
    cache = canonical(checkout, root)
    cache.mkdir(parents=True, exist_ok=True)
    owner = cache / '.apple-owner.json'
    metadata = {'checkout': str(Path(checkout).absolute()), 'lastUsed': time.time(), 'estimatedBytes': None}
    try:
        with owner.open('x') as stream:
            json.dump(metadata, stream)
    except FileExistsError:
        if json.loads(owner.read_text())['checkout'] != metadata['checkout']:
            raise ValueError('Derived-data basename ownership collision')
        temporary = cache / ('.owner-' + str(uuid.uuid4()))
        metadata['estimatedBytes'] = json.loads(owner.read_text()).get('estimatedBytes')
        metadata['merged'] = json.loads(owner.read_text()).get('merged')
        temporary.write_text(json.dumps(metadata))
        temporary.replace(owner)
    free = free or (lambda: shutil.disk_usage(root).free)
    before = free()
    removed, errors = [], []
    try:
        initial_live = processes() if live is None else live()
        for candidate in cache_plan(root, cache, initial_live) if before < TARGET else []:
            if free() >= TARGET:
                break
            if candidate not in cache_plan(root, cache, processes() if live is None else live()):
                continue
            safe(candidate, Path(root) / '.dd')
            amount = size(candidate)
            shutil.rmtree(candidate)
            removed.append({'path': str(candidate), 'bytes': amount})
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        errors.append(str(error))
    after = free()
    return {'derivedDataPath': str(cache), 'removed': removed, 'freeBefore': before, 'freeAfter': after,
            'freeDelta': after - before, 'belowTarget': after < TARGET, 'errors': errors}


def serialized(function):
    @wraps(function)
    def invoke(*args, **kwargs):
        root = kwargs.get('root', args[5] if function.__name__ == 'lease' and len(args) > 5 else args[1] if function.__name__ == 'release' and len(args) > 1 else ROOT)
        Path(root).mkdir(parents=True, exist_ok=True)
        guard = safe(Path(root) / '.sim-guard', root)
        with guard.open('a') as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            return function(*args, **kwargs)
    return invoke


@serialized

def lease(inventory, session, pid, os_version, idiom, root=ROOT):
    locks = Path(root) / '.sim-locks'
    locks.mkdir(parents=True, exist_ok=True)
    safe(locks / 'probe', root)
    candidates = [s for s in inventory if s['os'] == os_version and s['idiom'] == idiom]
    for sim in sorted(candidates, key=lambda s: s['state'] != 'Booted'):
        ident = str(uuid.UUID(sim['uuid']))
        token = {'session': session, 'pid': pid, 'token': str(uuid.uuid4()), 'uuid': ident}
        path = locks / (ident + '.json')
        try:
            with path.open('x') as stream:
                json.dump(token, stream)
            touch_created(ident, root)
            return token
        except FileExistsError:
            existing = json.loads(path.read_text())
            try:
                os.kill(int(existing['pid']), 0)
            except ProcessLookupError:
                path.unlink()
                with path.open('x') as stream:
                    json.dump(token, stream)
                touch_created(ident, root)
                return token
            except (KeyError, ValueError, PermissionError):
                pass
            continue
    raise ValueError('No matching unleased simulator; lifecycle creation requires authorized provider support')


@serialized
def release(token, root=ROOT):
    path = safe(Path(root) / '.sim-locks' / (str(uuid.UUID(token['uuid'])) + '.json'), root)
    if json.loads(path.read_text()) != token:
        raise ValueError('Lease ownership mismatch')
    touch_created(token['uuid'], root)
    path.unlink()


def touch_created(ident, root):
    path = Path(root) / '.sim-created' / (ident + '.json')
    if path.exists():
        safe(path, Path(root) / '.sim-created')
        record = json.loads(path.read_text())
        record['lastUsed'] = time.time()
        path.write_text(json.dumps(record))


def lifecycle(action, inventory, root=ROOT, token=None, name=None, device_type=None, runtime=None, execute=run):
    """Only create/shutdown/delete; provenance is independent of lease ownership."""
    provenance = Path(root) / '.sim-created'
    provenance.mkdir(parents=True, exist_ok=True)
    safe(provenance / 'probe', root)
    if action == 'create':
        if not token or not token.get('session') or not token.get('pid'):
            raise ValueError('Stable session and PID required')
        ident = str(uuid.UUID(execute('xcrun', 'simctl', 'create', name, device_type, runtime)))
        record = {'uuid': ident, 'name': name, 'created': time.time(), 'lastUsed': time.time(),
                  'session': token['session'], 'pid': token['pid']}
        with (provenance / (ident + '.json')).open('x') as stream:
            json.dump(record, stream)
        locks = Path(root) / '.sim-locks'
        locks.mkdir(parents=True, exist_ok=True)
        lease_token = {'session': token['session'], 'pid': token['pid'], 'token': str(uuid.uuid4()), 'uuid': ident}
        with (locks / (ident + '.json')).open('x') as stream:
            json.dump(lease_token, stream)
        return {'provenance': record, 'lease': lease_token}
    if action == 'shutdown':
        record = json.loads((provenance / (str(uuid.UUID(token['uuid'])) + '.json')).read_text())
        if record['session'] != token['session'] or record['pid'] != token['pid']:
            raise ValueError('Only the creating run may shut down a simulator')
        lease_path = Path(root) / '.sim-locks' / (record['uuid'] + '.json')
        if json.loads(lease_path.read_text()) != token:
            raise ValueError('Simulator lease ownership mismatch')
        execute('xcrun', 'simctl', 'shutdown', record['uuid'])
        record['lastUsed'] = time.time()
        (provenance / (record['uuid'] + '.json')).write_text(json.dumps(record))
        return record
    if action != 'delete-stale':
        raise ValueError('Unsupported lifecycle action')
    removed = []
    for path in provenance.glob('*.json'):
        safe(path, provenance)
        record = json.loads(path.read_text())
        ident = str(uuid.UUID(record['uuid']))
        if path.name != ident + '.json' or time.time() - record['lastUsed'] < 7 * 86400:
            continue
        if (Path(root) / '.sim-locks' / (ident + '.json')).exists():
            continue
        matches = [sim for sim in inventory if sim['uuid'] == ident and sim['name'] == record['name'] and sim['state'] == 'Shutdown']
        if len(matches) != 1:
            continue
        locks = Path(root) / '.sim-locks'
        locks.mkdir(parents=True, exist_ok=True)
        reservation = locks / (ident + '.json')
        try:
            with reservation.open('x') as stream:
                json.dump({'maintenance': True}, stream)
        except FileExistsError:
            continue
        try:
            execute('xcrun', 'simctl', 'delete', ident)
            path.unlink()
            removed.append(ident)
        finally:
            reservation.unlink()
    return removed


def cleanup(checkout, root=ROOT):
    checkout = Path(checkout).absolute()
    if checkout.is_symlink():
        raise ValueError("Symlink checkout refused")
    cache = canonical(checkout, root)
    entries = run('git', 'worktree', 'list', '--porcelain', cwd=checkout).split('\n\n')
    if entries[0].splitlines()[0] == 'worktree ' + str(checkout):
        raise ValueError('Main checkout refused')
    if run('git', 'status', '--porcelain', '--untracked-files=all', '--ignored', cwd=checkout):
        raise ValueError('Dirty or untracked checkout refused')
    if str(cache) in processes():
        raise ValueError('Live build refused')
    branch = run('git', 'symbolic-ref', '--short', 'HEAD', cwd=checkout)
    merged = False
    try:
        run('git', 'merge-base', '--is-ancestor', 'HEAD', 'origin/main', cwd=checkout)
        merged = True
    except subprocess.SubprocessError:
        pass
    remote = run('git', 'ls-remote', '--heads', 'origin', branch, cwd=checkout).split()
    if not merged and (not remote or remote[0] != run('git', 'rev-parse', 'HEAD', cwd=checkout)):
        raise ValueError('Branch is not proven pushed at its current HEAD')
    main = Path(entries[0].splitlines()[0].removeprefix('worktree '))
    run('git', 'worktree', 'remove', str(checkout), cwd=main)
    if cache.exists():
        safe(cache, Path(root) / '.dd')
        shutil.rmtree(cache)
    run('git', 'branch', '-d' if merged else '-D', branch, cwd=main)
    run('git', 'worktree', 'prune', cwd=main)
    return {'removedWorktree': str(checkout), 'removedCache': str(cache), 'branch': branch}


def report(root=ROOT, scan=False):
    dd = Path(root) / '.dd'
    rows = []
    if dd.is_symlink():
        return {'error': 'Symlink cache root refused'}
    for cache in list(dd.iterdir())[:100] if dd.exists() else []:
        try:
            safe(cache, dd)
            meta = json.loads((cache / '.apple-owner.json').read_text())
            if scan:
                meta['estimatedBytes'] = size(cache)
                meta['sizeObservedAt'] = time.time()
                try:
                    run('git', 'merge-base', '--is-ancestor', 'HEAD', 'origin/main', cwd=meta['checkout'])
                    meta['merged'] = True
                except (OSError, subprocess.SubprocessError):
                    meta['merged'] = None
                (cache / '.apple-owner.json').write_text(json.dumps(meta))
            rows.append({'cache': str(cache), 'checkout': meta['checkout'], 'gone': not Path(meta['checkout']).exists(), 'merged': meta.get('merged'), 'sizeObservedAt': meta.get('sizeObservedAt'), 'estimatedBytes': size(cache) if scan else meta.get('estimatedBytes'),
                         'cleanupCommand': 'python3 resources.py cleanup ' + shlex.quote(meta['checkout'])})
        except (OSError, ValueError, KeyError):
            continue
    return {'cacheCount': len(rows), 'sizes': 'cached estimates from previous prepare; unknown values are null', 'caches': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'cleanup', 'report', 'lease', 'release', 'create', 'shutdown', 'delete-stale'])
    parser.add_argument('checkout', nargs='?')
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--inventory', type=Path)
    parser.add_argument('--token', type=Path)
    parser.add_argument('--session')
    parser.add_argument('--pid', type=int)
    parser.add_argument('--os')
    parser.add_argument('--idiom')
    parser.add_argument('--name')
    parser.add_argument('--device-type')
    parser.add_argument('--runtime')
    args = parser.parse_args()
    if args.action in ('prepare', 'cleanup'):
        result = globals()[args.action](args.checkout, args.root)
    elif args.action == 'lease':
        result = lease(json.loads(args.inventory.read_text()), args.session, args.pid, args.os, args.idiom, args.root)
    elif args.action == 'release':
        release(json.loads(args.token.read_text()), args.root)
        result = {'released': True}
    elif args.action in ('create', 'shutdown', 'delete-stale'):
        result = lifecycle(args.action, json.loads(args.inventory.read_text()) if args.inventory else [], args.root,
                           json.loads(args.token.read_text()) if args.token else None, args.name, args.device_type, args.runtime)
    else:
        result = report(args.root, scan=True)
    print(json.dumps(result))


if __name__ == '__main__':
    main()
