import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate as validator

class PackageTests(unittest.TestCase):
    def test_static_manifest(self):
        self.assertEqual(validator.validate(), [])
    def test_one_canonical_skill(self):
        self.assertEqual(len(list(ROOT.rglob("SKILL.md"))), 1)
    def test_claude_plugin_manifest(self):
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(plugin["name"], "premium-frontend-director")
        self.assertEqual(marketplace["plugins"][0]["name"], plugin["name"])
        self.assertEqual(marketplace["plugins"][0]["source"], "./")
    def test_honest_reporting(self):
        body = (ROOT / "skills/premium-frontend-director/SKILL.md").read_text()
        self.assertIn("NOT RUN", body)
        self.assertIn("Playwright", body)
    def test_no_required_external_skill(self):
        deps = (ROOT / "skills/premium-frontend-director/references/dependencies.md").read_text()
        self.assertIn("self-contained", deps)
    def test_missing_manifest_fails_cleanly(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "skills/premium-frontend-director").mkdir(parents=True)
            (root / "skills/premium-frontend-director/SKILL.md").write_text(
                "---\nname: premium-frontend-director\ndescription: Test\n---\n")
            with patch.object(validator, "ROOT", root), patch.object(
                validator, "SKILL", root / "skills/premium-frontend-director/SKILL.md"
            ):
                errors = validator.validate()
            self.assertTrue(any("cannot parse .claude-plugin/plugin.json" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
