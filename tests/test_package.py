import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills/premium-frontend-director"
sys.path.insert(0, str(ROOT / "scripts"))
import validate as validator


class PackageTests(unittest.TestCase):
    def content(self, path):
        return (ROOT / path).read_text(encoding="utf-8")

    def test_static_manifest(self):
        self.assertEqual(validator.validate(), [])

    def test_one_canonical_skill(self):
        self.assertEqual([p.relative_to(ROOT).as_posix() for p in ROOT.rglob("SKILL.md")],
                         ["skills/premium-frontend-director/SKILL.md"])

    def test_claude_plugin_manifest(self):
        plugin = json.loads(self.content(".claude-plugin/plugin.json"))
        market = json.loads(self.content(".claude-plugin/marketplace.json"))
        self.assertEqual(plugin["name"], "premium-frontend-director")
        self.assertEqual(market["plugins"][0]["name"], plugin["name"])
        self.assertEqual(market["plugins"][0]["source"], "./")

    def test_self_contained_core(self):
        skill = self.content("skills/premium-frontend-director/SKILL.md")
        deps = self.content("skills/premium-frontend-director/references/dependencies.md")
        self.assertIn("Core requires zero companion skills", skill)
        self.assertIn("no companion skills", deps)
        self.assertIn("Never install third-party skills", deps)
        self.assertIn("NOT RUN", skill)

    def test_profiles_and_routing(self):
        skill = self.content("skills/premium-frontend-director/SKILL.md")
        deps = self.content("skills/premium-frontend-director/references/dependencies.md")
        profile = self.content("docs/companion-profiles.md")
        for mode in ("Core", "Premium", "Studio"):
            for doc in (skill, deps, profile):
                self.assertIn(mode, doc)
        for name in ("ui-ux-pro-max", "design-taste-frontend", "impeccable", "web-design-guidelines"):
            self.assertIn(name, deps)
        for source in ("greensock/gsap-skills", "addyosmani/web-quality-skills", "CloudAI-X/threejs-skills"):
            self.assertIn(source, profile)
            self.assertIn(source, deps)
        self.assertIn("Never", deps)
        self.assertIn("independent", profile.lower())

    def test_ambition_and_g11(self):
        skill = self.content("skills/premium-frontend-director/SKILL.md")
        modes = self.content("skills/premium-frontend-director/references/ambition-modes.md")
        immersive = self.content("skills/premium-frontend-director/references/immersive-design.md")
        gate = self.content("skills/premium-frontend-director/references/quality-gates.md")
        readme = self.content("README.md")
        for name in ("Refined", "Expressive", "Immersive"):
            for doc in (skill, modes, readme):
                self.assertIn(name, doc)
        for doc in (skill, modes, gate, readme):
            self.assertIn("G11", doc)
        self.assertIn("WebGL", immersive)
        self.assertIn("reduced motion", immersive.lower())
        self.assertIn("NOT RUN", gate)
        self.assertIn("FAIL", gate)

    def test_english_onboarding_and_current_install_commands(self):
        self.assertFalse((ROOT / "docs/GUIA-ES.md").exists())
        readme = self.content("README.md")
        quick = self.content("docs/getting-started.md")
        profiles = self.content("docs/companion-profiles.md")
        for doc in (readme, quick):
            self.assertIn("npx skills add AVL05/premium-frontend-director", doc)
        self.assertIn("--skill premium-frontend-director -a codex", quick)
        self.assertIn("--skill premium-frontend-director -a claude-code", quick)
        self.assertIn("/plugin marketplace add AVL05/premium-frontend-director", quick)
        for cmd in ("npx ui-ux-pro-max-cli init --ai codex",
                    "npx ui-ux-pro-max-cli init --ai claude",
                    "npx impeccable install",
                    "npx skills add Leonxlnx/taste-skill --skill design-taste-frontend",
                    "npx skills add vercel-labs/agent-skills --skill web-design-guidelines"):
            self.assertIn(cmd, profiles)
        self.assertIn("Node.js 22.20+", quick)
        self.assertIn("NOT RUN", quick)

    def test_local_markdown_links_exist(self):
        paths = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
        link_re = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
        for file in paths:
            source = file.read_text(encoding="utf-8")
            for link in link_re.findall(source):
                target = link.split("#", 1)[0].split("?", 1)[0]
                if not target or "://" in target or target.startswith(("mailto:", "/")):
                    continue
                with self.subTest(source=file.relative_to(ROOT), link=link):
                    self.assertTrue((file.parent / target).exists(),
                                    f"Broken local link in {file.relative_to(ROOT)}: {link}")

    def test_missing_manifest_fails_cleanly(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "skills/premium-frontend-director").mkdir(parents=True)
            (root / "skills/premium-frontend-director/SKILL.md").write_text(
                "---\nname: premium-frontend-director\ndescription: Test\n---\n",
                encoding="utf-8"
            )
            with patch.object(validator, "ROOT", root), patch.object(
                validator, "SKILL", root / "skills/premium-frontend-director/SKILL.md"
            ):
                errors = validator.validate()
            self.assertTrue(any("cannot parse .claude-plugin/plugin.json" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
