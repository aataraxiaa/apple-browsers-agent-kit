#!/usr/bin/env python3
"""Compare the shipped source inventory with an explicit Apple browsers checkout."""
import json
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit('Usage: python3 scripts/check_coverage.py /absolute/path/to/apple-browsers')
checkout = Path(sys.argv[1]).resolve()
if not (checkout / 'DuckDuckGo.xcworkspace').is_dir():
    raise SystemExit('Expected an Apple browsers checkout with DuckDuckGo.xcworkspace')
features = Path(__file__).resolve().parents[1] / 'plugins/apple-browsers/skills/verify-ios/features'
manifest = json.loads((features / 'coverage.json').read_text())
rows = manifest['sources']
actual = {str(path.relative_to(checkout)) for path in (checkout / '.maestro').rglob('*.yaml')}
mapped = {row['source'] for row in rows}
errors = []
if len(mapped) != len(rows):
    errors.append('Duplicate source entries')
errors += ['Unmapped source: ' + path for path in sorted(actual - mapped)]
errors += ['Removed source: ' + path for path in sorted(mapped - actual)]
for row in rows:
    if not (features / row['feature']).is_file():
        errors.append('Missing feature guide: ' + row['feature'])
    for dependency in row.get('dependencies', []):
        if not (checkout / dependency).is_file():
            errors.append('Missing dependency: ' + dependency)
source_paths = manifest.get('additional_browser_sources', []) + [path for extension in manifest.get('source_extensions', []) for path in extension['sources']]
for path in source_paths:
    if not (checkout / path).is_file():
        errors.append('Missing supporting source: ' + path)
if errors:
    raise SystemExit('\n'.join(sorted(set(errors))))
scenarios = sum(row['kind'] == 'scenario' for row in rows)
print(f'Coverage inventory matches {len(actual)} YAML files: {scenarios} scenarios and {len(actual)-scenarios} helpers/configuration files.')
print('This validates source inventory only, not runtime behavior or current selector accuracy.')
