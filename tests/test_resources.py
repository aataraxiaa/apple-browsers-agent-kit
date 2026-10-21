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
            self.assertIn('resource report',report['systemMessage'])
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
                r.lease(inventory,'other',456,'18','phone',root)
            with self.assertRaises(ValueError):
                r.release(dict(token,token='stale'),root)
            r.release(token,root)
            r.lease(inventory,'other',456,'18','phone',root)

    def test_lifecycle_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            calls=[]
            ident='12345678-1234-1234-1234-123456789abc'
            def execute(*args):
                calls.append(args)
                return ident
            created=r.lifecycle('create',[],root,{'session':'run','pid':123},'agent','type','runtime',execute)
            record=created['provenance']
            lease=created['lease']
            r.lifecycle('shutdown',[],root,lease,execute=execute)
            r.release(lease,root)
            record['lastUsed']=0
            (root/'.sim-created'/ (ident+'.json')).write_text(json.dumps(record))
            self.assertEqual(r.lifecycle('delete-stale',[{'uuid':ident,'name':'agent','state':'Shutdown'}],root,execute=execute),[ident])
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

if __name__ == '__main__':
    unittest.main()
