#!/usr/bin/env python3
"""Zero-dependency static validator for the canonical skill and plugin manifest."""
import json
import re
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/premium-frontend-director/SKILL.md'


def validate():
    problems = []
    body = SKILL.read_text(encoding='utf-8')
    parts = body.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        problems.append('SKILL.md requires YAML frontmatter bounded by ---')
        return problems
    front = parts[1]
    name = re.search(r'^name:\s*([^\n]+)$', front, flags=re.M)
    desc = re.search(r'^description:\s*([^\n]+)$', front, flags=re.M)
    if not name or name.group(1).strip() != SKILL.parent.name:
        problems.append('frontmatter name must equal directory name')
    if not desc or not 1 <= len(desc.group(1).strip()) <= 1024:
        problems.append('description must have 1..1024 characters')
    if name and not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name.group(1).strip()):
        problems.append('name must be lowercase kebab-case')
    if len(parts[2].splitlines()) >= 500:
        problems.append('SKILL.md should stay under 500 lines')
    for file in ['references/creative-direction.md','references/implementation.md','references/quality-gates.md','references/dependencies.md','assets/design-template.md','scripts/visual-audit.mjs']:
        if not (SKILL.parent / file).is_file(): problems.append(f'missing skill resource: {file}')
    plugin = json.loads((ROOT/'.claude-plugin/plugin.json').read_text())
    market = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())
    if plugin.get('name') != SKILL.parent.name: problems.append('plugin name mismatch')
    if len(market.get('plugins',[]))!=1 or market['plugins'][0].get('source')!='./':
        problems.append('marketplace must target this repo')
    if not (ROOT/'LICENSE').is_file(): problems.append('missing LICENSE')
    return problems


if __name__ == '__main__':
    errors=validate()
    if errors:
        for e in errors: print('ERROR:',e)
        sys.exit(1)
    print('PASS: canonical SKILL.md, metadata, resources and plugin manifests')
