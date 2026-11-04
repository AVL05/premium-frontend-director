import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate import validate

class PackageTests(unittest.TestCase):
    def test_static_manifest(self):
        self.assertEqual(validate(),[])
    def test_one_canonical_skill(self):
        skills=list(ROOT.rglob('SKILL.md'))
        self.assertEqual(len(skills),1)
    def test_claude_plugin_manifest(self):
        data=json.loads((ROOT/'.claude-plugin/plugin.json').read_text())
        self.assertEqual(data['name'],'premium-frontend-director')
    def test_gates_require_honest_reporting(self):
        body=(ROOT/'skills/premium-frontend-director/SKILL.md').read_text()
        self.assertIn('NOT RUN',body)
        self.assertIn('Playwright',body)
    def test_no_required_external_skill(self):
        deps=(ROOT/'skills/premium-frontend-director/references/dependencies.md').read_text()
        self.assertIn('self-contained',deps)

if __name__=='__main__': unittest.main()
