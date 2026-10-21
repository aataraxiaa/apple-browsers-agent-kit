#!/usr/bin/env python3
"""Validate portable plugin packaging without changing host configuration."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
market = json.loads((root / '.claude-plugin/marketplace.json').read_text())
entry = market['plugins'][0]
plugin = root / entry['source']
manifests = [json.loads((plugin / kind / 'plugin.json').read_text())
             for kind in ('.claude-plugin', '.codex-plugin')]
assert market['name'] == 'apple-browsers-tools'
assert all(item['name'] == entry['name'] and item['version'] == entry['version']
           for item in manifests), 'Manifest identity or version mismatch'
for name in ('build-ios', 'verify-ios'):
    assert (plugin / manifests[1]['skills'] / name / 'SKILL.md').is_file()
assert all(item['mcpServers'] == './.mcp.json' and item['hooks'] == './hooks/hooks.json' for item in manifests)
server = json.loads((plugin / '.mcp.json').read_text())['mcpServers']
assert list(server) == ['mobilebuild']
assert server['mobilebuild']['command'] == 'npx'
assert server['mobilebuild']['args'] == ['-y', 'mobilebuildmcp@2.7.1', 'mcp']
assert server['mobilebuild']['env']['MOBILEBUILDMCP_DISABLE_XCODE_AUTO_SYNC'] == 'true'
assert server['mobilebuild']['env']['MOBILEBUILDMCP_DISABLE_SESSION_DEFAULTS'] == 'true'
assert set(server['mobilebuild']['env']['MOBILEBUILDMCP_ENABLED_WORKFLOWS'].split(',')) == {'xcode-ide', 'simulator', 'device', 'simulator-management', 'session-management', 'project-scaffolding', 'coverage', 'macos', 'ui-automation', 'utilities', 'project-discovery', 'doctor', 'swift-package', 'debugging'}
assert server['mobilebuild']['env']['MOBILEBUILDMCP_DEBUG'] == 'true'
assert server['mobilebuild']['env']['MOBILEBUILDMCP_EXPERIMENTAL_WORKFLOW_DISCOVERY'] == 'false'
hooks = json.loads((plugin / 'hooks/hooks.json').read_text())['hooks']
assert set(hooks) == {'PreToolUse', 'Stop'}
for entries in hooks.values():
    assert len(entries) == 1
    assert entries[0]['hooks'][0]['command'] == 'python3 "${CLAUDE_PLUGIN_ROOT}/hooks/ios_policy.py"'
assert (plugin / 'hooks/ios_policy.py').is_file()
assert (plugin / 'policy.md').is_file()
for path in root.rglob('*'):
    if '.git' in path.relative_to(root).parts:
        continue
    assert not path.is_symlink(), f'Symlink: {path}'
    if path.suffix != '.md':
        continue
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        assert (path.parent / target.split('#')[0]).exists(), f'Broken link: {path}: {target}'
print('Plugin packaging passed')
