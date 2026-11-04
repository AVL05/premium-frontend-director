#!/usr/bin/env python3
"""Validate canonical Agent Skill and Claude Code distribution. Standard-library only."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/premium-frontend-director/SKILL.md"

def validate():
    problems = []
    try:
        body = SKILL.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"missing or unreadable SKILL.md: {exc}"]
    parts = body.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        return ["SKILL.md needs --- frontmatter"]
    front = parts[1]
    name = re.search(r"^name:\s*([^\n]+)$", front, re.M)
    desc = re.search(r"^description:\s*([^\n]+)$", front, re.M)
    if not name or name.group(1).strip() != SKILL.parent.name:
        problems.append("skill name must match folder")
    if not desc or not 1 <= len(desc.group(1).strip()) <= 1024:
        problems.append("description must contain 1..1024 characters")
    if name and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1).strip()):
        problems.append("skill name must be kebab-case")
    if len(parts[2].splitlines()) >= 500:
        problems.append("SKILL.md must be shorter than 500 lines")
    files = ["references/creative-direction.md", "references/implementation.md",
             "references/quality-gates.md", "references/dependencies.md",
             "assets/design-template.md", "scripts/visual-audit.mjs"]
    for relative in files:
        if not (SKILL.parent / relative).is_file():
            problems.append(f"missing skill resource: {relative}")
    for relative in [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]:
        file = ROOT / relative
        try:
            data = json.loads(file.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                problems.append(f"not a JSON object: {relative}")
            elif relative.endswith("plugin.json") and data.get("name") != SKILL.parent.name:
                problems.append("Claude plugin name differs from skill")
            elif relative.endswith("marketplace.json"):
                plugins = data.get("plugins", [])
                if not isinstance(plugins, list) or len(plugins) != 1 or plugins[0].get("name") != SKILL.parent.name or plugins[0].get("source") != "./":
                    problems.append("marketplace entry must point at this repo")
        except (OSError, ValueError) as exc:
            problems.append(f"cannot parse {relative}: {exc}")
    for relative in [".github/workflows/validate.yml", ".gitignore", "LICENSE", "README.md", "docs/compatibility-testing.md", "docs/companion-profiles.md", "docs/GUIA-ES.md", "docs/manual-testing.md"]:
        if not (ROOT / relative).is_file():
            problems.append(f"missing repository file: {relative}")
    return problems

if __name__ == "__main__":
    errors = validate()
    for error in errors:
        print("ERROR:", error)
    if errors:
        sys.exit(1)
    print("PASS: skill package, Claude plugin, marketplace and CI files")
