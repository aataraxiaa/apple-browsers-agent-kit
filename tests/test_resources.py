import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('resources', Path(__file__).parents[1] / 'plugins/apple-browsers/scripts/resources.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Resources(unittest.TestCase):
    def test_process_paths(self):
        self.assertEqual(r.live_paths('xcodebuild -derivedDataPath="/tmp/a b"\nxcodebuild -derivedDataPath "/tmp/c d"'), {'/tmp/a b', '/tmp/c d'})

    def test_reclamation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            current = root / 'current'
            current.mkdir()
            orphan = root / '.dd/orphan'
            orphan.mkdir(parents=True)
            (orphan / '.apple-owner.json').write_text(json.dumps({'checkout':str(root / 'gone'), 'lastUsed':1}))
            live = root / '.dd/live'
            live.mkdir()
            (live / '.apple-owner.json').write_text(json.dumps({'checkout':str(root / 'gone2'), 'lastUsed':0}))
            result = r.prepare(current, root, free=lambda:0, live=lambda:{str(live)})
            self.assertFalse(orphan.exists())
            self.assertTrue(live.exists())
            self.assertTrue(Path(result['derivedDataPath']).exists())
            self.assertEqual([x['path'] for x in result['removed']], [str(orphan)])

    def test_reclaim_order_and_threshold(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, used in [('orphan', 99), ('merged', 20), ('gone', 30), ('lru', 1), ('recent', 2), ('live', 0), ('current', 0)]:
                owner = root / name
                if name != 'orphan':
                    owner.mkdir()
                cache = root / '.dd' / name
                cache.mkdir(parents=True)
                (cache / 'product').write_bytes(b'cache')
                (cache / '.apple-owner.json').write_text(json.dumps({'checkout': str(owner), 'lastUsed': used}))
            def git(*args, cwd=None):
                if args[1] == 'merge-base' and Path(cwd).name == 'merged':
                    return ''
                if args[1] == 'rev-parse' and Path(cwd).name == 'gone':
                    return 'origin/gone'
                if args[1] == 'ls-remote':
                    return 'head' if args[-1] == 'HEAD' else ''
                raise subprocess.CalledProcessError(1, args)
            protected = lambda: {str(root / '.dd/live')}
            with patch.object(r, 'run', side_effect=git):
                result = r.prepare(root / 'current', root, free=lambda: 0, live=protected)
            self.assertEqual([Path(x['path']).name for x in result['removed']], ['orphan', 'merged', 'gone', 'lru', 'recent'])
            self.assertTrue((root / '.dd/current/product').exists())
            self.assertTrue((root / '.dd/live/product').exists())
            self.assertTrue(result['belowTarget'])
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('one', 'two'):
                cache = root / '.dd' / name
                cache.mkdir(parents=True)
                (cache / '.apple-owner.json').write_text(json.dumps({'checkout': str(root / name), 'lastUsed': 0}))
            free = lambda: r.TARGET if not (root / '.dd/one').exists() else 0
            result = r.prepare(root / 'current', root, free=free, live=lambda: set())
            self.assertEqual(len(result['removed']), 1)
            self.assertTrue((root / '.dd/two').exists())

    def test_path_traversal_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                r.safe(Path(tmp) / '.dd/../other', Path(tmp) / '.dd')

    def test_process_failure_preserves_caches(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            orphan = root/'.dd/orphan'
            orphan.mkdir(parents=True)
            (orphan/'.apple-owner.json').write_text(json.dumps({'checkout':str(root/'gone')}))
            with patch.object(r,'processes',side_effect=OSError('ps failed')):
                result = r.prepare(root/'current',root,free=lambda:0)
            self.assertTrue(orphan.exists())
            self.assertTrue(result['errors'])
        with self.assertRaises(ValueError):
            r.live_paths('xcodebuild -derivedDataPath /tmp/space path -scheme iOS')

    def test_stop_subprocess(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            checkout = root/'worktree'
            (checkout/'DuckDuckGo.xcworkspace').mkdir(parents=True)
            (checkout/'iOS/DuckDuckGo-iOS.xcodeproj').mkdir(parents=True)
            hook = Path(__file__).parents[1]/'plugins/apple-browsers/hooks/ios_policy.py'
            output = subprocess.check_output(['python3',str(hook),'--root',str(root)],input=json.dumps({'cwd':str(checkout),'hook_event_name':'Stop'}),text=True)
            report = json.loads(output)
            self.assertIn('Apple browsers caches',report['systemMessage'])
            self.assertNotIn('decision',report)

    def test_collision_and_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            r.prepare(root/'a/foo',root,free=lambda:r.TARGET,live=lambda:set())
            with self.assertRaises(ValueError):
                r.canonical(root/'b/foo',root)
            (root/'.dd/link').symlink_to(root/'.dd/foo')
            with self.assertRaises(ValueError):
                r.canonical(root/'link',root)

    def test_lease_exclusive(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inventory = [{'uuid':'12345678-1234-1234-1234-123456789abc','os':'18','idiom':'phone','state':'Booted'}]
            token = r.lease(inventory,'session',os.getpid(),'18','phone',root)
            with self.assertRaises(ValueError):
                r.lease(inventory,'other',os.getpid(),'18','phone',root)
            with self.assertRaises(ValueError):
                r.release(dict(token,token='stale'),root)
            r.release(token,root)
            r.lease(inventory,'other',os.getpid(),'18','phone',root)

    def test_hook_uses_explicit_workspace(self):
        hook_path = Path(__file__).parents[1] / 'plugins/apple-browsers/hooks/ios_policy.py'
        spec = importlib.util.spec_from_file_location('resource_hook', hook_path)
        hook = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(hook)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('chat', 'target'):
                (root / name / 'DuckDuckGo.xcworkspace').mkdir(parents=True)
                (root / name / 'iOS/DuckDuckGo-iOS.xcodeproj').mkdir(parents=True)
            event = {'cwd': str(root / 'chat'), 'hook_event_name': 'PreToolUse', 'tool_name': 'mcp__mobilebuild__build_sim',
                     'tool_input': {'workspacePath': str(root / 'target/DuckDuckGo.xcworkspace'), 'simulatorId': '12345678-1234-1234-1234-123456789abc'}}
            with patch.object(hook.resources, 'ROOT', root), patch.object(hook.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, json.dumps({'derivedDataPath': str(root / '.dd/target')}), '')):
                output = hook.handle(event)['hookSpecificOutput']
            self.assertEqual(output['updatedInput']['derivedDataPath'], str(root / '.dd/target'))
            self.assertNotIn('permissionDecision', output)

    def test_invalid_owner_cannot_claim(self):
        with tempfile.TemporaryDirectory() as tmp:
            inventory = [{'uuid':'12345678-1234-1234-1234-123456789abc','os':'18','idiom':'phone','state':'Booted'}]
            for session, pid in [('', os.getpid()), ('owner', None), ('owner', -1)]:
                with self.assertRaises(ValueError):
                    r.lease(inventory, session, pid, '18', 'phone', Path(tmp))
            self.assertFalse((Path(tmp) / '.sim-locks').exists())

    def test_lifecycle_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            calls=[]
            ident='12345678-1234-1234-1234-123456789abc'
            def execute(*args):
                calls.append(args)
                return ident
            created=r.lifecycle('create',[],root,{'session':'run','pid':os.getpid()},'agent-test','type','runtime',execute)
            record=created['provenance']
            lease=created['lease']
            r.lifecycle('shutdown',[],root,lease,execute=execute)
            r.release(lease,root)
            record['lastUsed']=0
            (root/'.sim-created'/ (ident+'.json')).write_text(json.dumps(record))
            self.assertEqual(r.lifecycle('delete-stale',[{'uuid':ident,'name':'agent-test','state':'Shutdown'}],root,execute=execute),[ident])
            self.assertEqual([call[2] for call in calls],['create','shutdown','delete'])

    def test_real_worktree_cleanup(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args,cwd=root):
                return r.run('git',*args,cwd=cwd)
            git('init','--bare',str(root/'remote'))
            git('clone',str(root/'remote'),str(root/'main'))
            main = root/'main'
            git('config','user.email','test@example.com',cwd=main)
            git('config','user.name','Test',cwd=main)
            (main/'file').write_text('base')
            git('add','file',cwd=main)
            git('commit','-m','base',cwd=main)
            git('branch','-M','main',cwd=main)
            git('push','-u','origin','main',cwd=main)
            git('worktree','add','-b','task',str(root/'task'),cwd=main)
            task=root/'task'
            (task/'file').write_text('new')
            git('add','file',cwd=task)
            git('commit','-m','task',cwd=task)
            with patch.object(r,'processes',return_value=set()):
                with self.assertRaises(ValueError):
                    r.cleanup(task,root)
                git('push','-u','origin','task',cwd=task)
                (task/'untracked').write_text('work')
                with self.assertRaises(ValueError):
                    r.cleanup(task,root)
                (task/'untracked').unlink()
                r.cleanup(task,root)
            self.assertFalse(task.exists())



class HookResourceFallbacks(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location('resource_hook', Path(__file__).parents[1] / 'plugins/apple-browsers/hooks/ios_policy.py')
        self.hook = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.hook)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.checkout = self.root / 'worktree'
        (self.checkout / 'DuckDuckGo.xcworkspace').mkdir(parents=True)
        (self.checkout / 'iOS/DuckDuckGo-iOS.xcodeproj').mkdir(parents=True)
        self.cache = self.root / '.dd/worktree'
        self.cache.mkdir(parents=True)
        self.event = {'cwd': str(self.checkout), 'hook_event_name': 'PreToolUse',
                      'tool_name': 'mcp__mobilebuild__build_sim',
                      'tool_input': {'simulatorId': '12345678-1234-1234-1234-123456789abc',
                                     'derivedDataPath': '/tmp/caller-cache'}}
        self.argv = patch.object(self.hook.sys, 'argv', ['ios_policy.py', '--root', str(self.root)])
        self.argv.start()
        self.addCleanup(self.argv.stop)

    def assert_fallback(self, output):
        specific = output.get('hookSpecificOutput', {})
        self.assertNotIn('permissionDecision', specific)
        self.assertNotIn('updatedInput', specific)
        self.assertIn('warning', specific.get('additionalContext', '').lower())
        self.assertEqual(self.event['tool_input']['derivedDataPath'], '/tmp/caller-cache')

    def test_invalid_cache_ownership_in_real_hook_process(self):
        owner = self.cache / '.apple-owner.json'
        product = self.cache / 'product'
        product.write_text('keep')
        for metadata in ['{', '{}', '[]', 'null', '{"checkout": "/another/worktree"}']:
            with self.subTest(metadata=metadata):
                owner.write_text(metadata)
                result = subprocess.run(['python3', self.hook.__file__, '--root', str(self.root)],
                                        input=json.dumps(self.event), capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assert_fallback(json.loads(result.stdout))
                prepared = subprocess.run(['python3', r.__file__, 'prepare', str(self.checkout), '--root', str(self.root)],
                                          capture_output=True, text=True)
                self.assertEqual(prepared.returncode, 0, prepared.stderr)
                self.assertTrue(json.loads(prepared.stdout)['continueBuild'])
                self.assertNotIn('derivedDataPath', json.loads(prepared.stdout))
                self.assertEqual(owner.read_text(), metadata)
                self.assertEqual(product.read_text(), 'keep')

    def test_malformed_stop_metadata_in_real_hook_process(self):
        (self.cache / '.apple-owner.json').write_text('null')
        result = subprocess.run(['python3', self.hook.__file__, '--root', str(self.root)],
                                input=json.dumps(dict(self.event, hook_event_name='Stop')),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        self.assertEqual(set(output), {'systemMessage'})
        self.assertIn('warning', output['systemMessage'].lower())

    def test_symlink_cache_and_owner_are_not_prepared(self):
        target = self.root / 'other'
        target.mkdir()
        for owner_link in (False, True):
            with self.subTest(owner_link=owner_link):
                if owner_link:
                    self.cache.unlink()
                    self.cache.mkdir()
                    metadata = target / 'owner.json'
                    metadata.write_text(json.dumps({'checkout': str(self.checkout)}))
                    (self.cache / '.apple-owner.json').symlink_to(metadata)
                else:
                    self.cache.rmdir()
                    self.cache.symlink_to(target, target_is_directory=True)
                with patch.object(self.hook.subprocess, 'run') as prepare:
                    self.assert_fallback(self.hook.handle(self.event))
                prepare.assert_not_called()

    def test_preparation_failures_leave_input_unchanged(self):
        for error in [OSError('cannot start helper'), subprocess.TimeoutExpired('prepare', 2), subprocess.CalledProcessError(1, 'prepare')]:
            with self.subTest(error=error), patch.object(self.hook.subprocess, 'run', side_effect=error):
                self.assert_fallback(self.hook.handle(self.event))
        for code, stdout in [(0, 'not json'), (0, '{}'), (0, 'null'), (0, json.dumps({'warning': 'owner changed', 'continueBuild': True})), (0, json.dumps({'derivedDataPath': '/wrong/cache'}))]:
            with self.subTest(code=code, stdout=stdout), patch.object(self.hook.subprocess, 'run', return_value=subprocess.CompletedProcess([], code, stdout, 'prepare failed')):
                self.assert_fallback(self.hook.handle(self.event))
        with patch.object(self.hook.resources, 'canonical', side_effect=OSError('cannot read owner')), patch.object(self.hook.subprocess, 'run') as prepare:
            self.assert_fallback(self.hook.handle(self.event))
        prepare.assert_not_called()

    def test_stop_failures_warn_without_blocking(self):
        event = dict(self.event, hook_event_name='Stop')
        for error in [OSError('cannot inspect cache'), TypeError('invalid owner'),
                      AttributeError('invalid owner'), subprocess.TimeoutExpired('report', 0.5)]:
            with self.subTest(error=error), patch.object(self.hook.resources, 'report', side_effect=error):
                output = self.hook.handle(event)
                self.assertEqual(set(output), {'systemMessage'})
                self.assertIn('warning', output['systemMessage'].lower())

    def test_resource_failure_does_not_bypass_simulator_or_defaults_guards(self):
        with patch.object(self.hook.resources, 'canonical', side_effect=OSError('unavailable')) as canonical:
            event = dict(self.event, tool_input={})
            self.assertEqual(self.hook.handle(event)['hookSpecificOutput']['permissionDecision'], 'deny')
            event = dict(self.event, tool_name='mcp__mobilebuild__session_set_defaults')
            self.assertEqual(self.hook.handle(event)['hookSpecificOutput']['permissionDecision'], 'deny')
        canonical.assert_not_called()


if __name__ == '__main__':
    unittest.main()
