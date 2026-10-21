import json
from pathlib import Path
import subprocess
import tempfile
import unittest

HOOK = Path(__file__).resolve().parents[1] / 'plugins/apple-browsers/hooks/ios_policy.py'


class PolicyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'DuckDuckGo.xcworkspace').mkdir()
        (self.root / 'iOS/DuckDuckGo-iOS.xcodeproj').mkdir(parents=True)
        (self.root / 'iOS/nested').mkdir()

    def event(self, tool='Bash', command='', cwd=None, **data):
        event = {'hook_event_name': 'PreToolUse', 'cwd': str(cwd or self.root),
                 'tool_name': tool, 'tool_input': {'command': command, **data}}
        result = subprocess.run(['python3', str(HOOK)], input=json.dumps(event), text=True, capture_output=True, check=True)
        return json.loads(result.stdout)

    def test_common_bypasses_are_denied(self):
        for command in ['xcodebuild -workspace DuckDuckGo.xcworkspace', '/Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild', 'xcrun simctl list', '/usr/bin/xcrun simctl boot A', 'maestro test flow.yaml', 'git status && xcodebuild', 'env X=1 xcodebuild', '.maestro/run_ui_tests.sh']:
            with self.subTest(command=command):
                self.assertEqual(self.event(command=command)['hookSpecificOutput']['permissionDecision'], 'deny')

    def test_ordinary_reads_and_git_are_allowed(self):
        for command in ['git status', 'rg xcodebuild .', 'cat simctl', 'echo maestro', 'python3 scripts/validate.py']:
            self.assertEqual(self.event(command=command), {})

    def test_provider_and_alternate(self):
        self.assertEqual(self.event(tool='mcp__mobilebuild__build_macos'), {})
        self.assertEqual(self.event(tool='mcp__xcode__BuildProject')['hookSpecificOutput']['permissionDecision'], 'deny')

    def test_scope_uses_session_and_tool_directories(self):
        other = self.root / 'unrelated'
        other.mkdir()
        self.assertEqual(self.event(command='xcodebuild', cwd='/private/tmp'), {})
        self.assertIn('hookSpecificOutput', self.event(command='xcodebuild', cwd='/private/tmp', workdir=str(self.root / 'iOS/nested')))
        self.assertIn('hookSpecificOutput', self.event(command='xcodebuild', workdir='/private/tmp'))

    def test_codex_exec_command(self):
        self.assertEqual(self.event(tool='exec_command', command='xcodebuild')['hookSpecificOutput']['permissionDecision'], 'deny')

    def test_no_startup_injection(self):
        for name in ['SessionStart', 'SubagentStart']:
            event = {'hook_event_name': name, 'cwd': str(self.root / 'iOS/nested')}
            result = subprocess.run(['python3', str(HOOK)], input=json.dumps(event), text=True, capture_output=True, check=True)
            self.assertEqual(json.loads(result.stdout), {})

    def test_provider_target_and_context(self):
        for provider in ['mobilebuild', 'XcodeBuildMCP', 'plugin_apple-browsers_mobilebuild', 'plugin_apple-browsers_XcodeBuildMCP']:
            for operation in ['build_sim', 'tap', 'screenshot', 'erase_sims', 'debug_attach_sim']:
                with self.subTest(provider=provider, operation=operation):
                    tool = f'mcp__{provider}__{operation}'
                    for invalid in [None, 'booted', '', 'not-a-uuid']:
                        response = self.event(tool=tool, simulatorId=invalid)
                        self.assertEqual(response.get('hookSpecificOutput', {}).get('permissionDecision'), 'deny')
                    response = self.event(tool=tool, simulatorId='12345678-1234-4234-8234-123456789ABC')
                    self.assertNotIn('permissionDecision', response['hookSpecificOutput'])
                    self.assertIn('simulatorId', response['hookSpecificOutput']['additionalContext'])
            for operation in ['list_sims', 'build_macos', 'session_show_defaults']:
                self.assertEqual(self.event(tool=f'mcp__{provider}__{operation}'), {})

    def test_defaults_cannot_be_mutated(self):
        for provider in ['mobilebuild', 'XcodeBuildMCP', 'plugin_apple-browsers_mobilebuild', 'plugin_apple-browsers_XcodeBuildMCP']:
            for operation in ['session_set_defaults', 'session_clear_defaults', 'session_use_defaults_profile', 'sync_xcode_defaults']:
                response = self.event(tool=f'mcp__{provider}__{operation}', simulatorId='12345678-1234-4234-8234-123456789ABC')
                self.assertEqual(response.get('hookSpecificOutput', {}).get('permissionDecision'), 'deny')

    def test_control_panel_and_unrelated_names_are_allowed(self):
        for tool in ['mcp__Claude_Code_iOS_Simulator__attach', 'mcp__Claude_Code_iOS_Simulator__detach', 'mcp__Claude_Code_iOS_Simulator__screenshot', 'mcp__some_simulator_notes__search', 'mcp__notmobilebuild__build_sim', 'mcp__xcode__GetWorkspaceInfo']:
            self.assertEqual(self.event(tool=tool), {})

    def test_clipboard_requires_explicit_uuid_and_preserves_chain_checks(self):
        uuid = '12345678-1234-4234-8234-123456789ABC'
        for prefix in ['xcrun simctl', '/usr/bin/xcrun simctl', 'simctl']:
            for operation in ['pbcopy', 'pbpaste']:
                command = f'{prefix} {operation} {uuid}'
                self.assertEqual(self.event(command=command), {})
                for suffix in [' && xcodebuild', '; maestro test flow.yaml', '\nxcrun simctl list']:
                    self.assertEqual(self.event(command=command + suffix)['hookSpecificOutput']['permissionDecision'], 'deny')
                for target in ['booted', 'not-a-uuid', '']:
                    self.assertEqual(self.event(command=f'{prefix} {operation} {target}')['hookSpecificOutput']['permissionDecision'], 'deny')
        self.assertEqual(self.event(command=f'printf hello | xcrun simctl pbcopy {uuid}'), {})

    def test_denial_prevents_command_effect(self):
        marker = self.root / 'executed'
        command = f'xcodebuild && touch {marker}'
        result = self.event(command=command)
        if result.get('hookSpecificOutput', {}).get('permissionDecision') != 'deny':
            marker.touch()
        self.assertFalse(marker.exists())

    def test_explicit_workspace_from_unrelated_chat(self):
        command = f'xcodebuild -workspace "{self.root}/DuckDuckGo.xcworkspace"'
        self.assertEqual(self.event(command=command, cwd='/private/tmp')['hookSpecificOutput']['permissionDecision'], 'deny')
        self.assertEqual(self.event(tool='mcp__xcode__BuildProject', cwd='/private/tmp', workspacePath=str(self.root / 'DuckDuckGo.xcworkspace'))['hookSpecificOutput']['permissionDecision'], 'deny')

    def test_unrelated_macos_project_is_allowed(self):
        self.assertEqual(self.event(command='xcodebuild -project /private/tmp/Mac.xcodeproj', cwd='/private/tmp'), {})

    def test_command_text_inside_source_read_is_not_executed(self):
        self.assertEqual(self.event(command='rg "xcrun simctl" .'), {})

    def test_server_enables_full_stable_catalog(self):
        config = json.loads((HOOK.parents[1] / '.mcp.json').read_text())['mcpServers']['mobilebuild']
        expected = {'coverage', 'debugging', 'device', 'doctor', 'macos', 'project-discovery', 'project-scaffolding', 'session-management', 'simulator', 'simulator-management', 'swift-package', 'ui-automation', 'utilities', 'xcode-ide'}
        self.assertEqual(set(config['env']['MOBILEBUILDMCP_ENABLED_WORKFLOWS'].split(',')), expected)
        self.assertEqual(config['env']['MOBILEBUILDMCP_DEBUG'], 'true')
        self.assertEqual(config['env']['MOBILEBUILDMCP_EXPERIMENTAL_WORKFLOW_DISCOVERY'], 'false')
        self.assertEqual(config['env']['MOBILEBUILDMCP_DISABLE_XCODE_AUTO_SYNC'], 'true')

    def test_explicit_macos_build_and_xcode_reads_in_apple_checkout(self):
        self.assertEqual(self.event(command='xcodebuild -workspace DuckDuckGo.xcworkspace -scheme "macOS Browser"'), {})
        self.assertEqual(self.event(tool='mcp__xcode__GetWorkspaceInfo'), {})
        self.assertIn('hookSpecificOutput', self.event(command='xcodebuild -scheme "macOS Browser" && xcrun simctl list'))
        self.assertIn('hookSpecificOutput', self.event(command='xcodebuild -scheme "macOS Browser" -sdk iphonesimulator'))

    def test_debugger_calls_require_the_owned_session(self):
        for operation in ['debug_breakpoint_add', 'debug_breakpoint_remove', 'debug_continue', 'debug_detach', 'debug_lldb_command', 'debug_stack', 'debug_variables']:
            tool = f'mcp__mobilebuild__{operation}'
            self.assertEqual(self.event(tool=tool).get('hookSpecificOutput', {}).get('permissionDecision'), 'deny')
            self.assertNotEqual(self.event(tool=tool, debugSessionId='owned-session').get('hookSpecificOutput', {}).get('permissionDecision'), 'deny')
