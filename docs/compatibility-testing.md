# Compatibility and release verification

The canonical implementation is `skills/premium-frontend-director/`. No third-party skill source is vendored into this repository. It follows the [Agent Skills](https://agentskills.io/) format and is designed for hosts that support `SKILL.md`.

## Distribution paths

| Host | Recommended path | Alternative | Known caveat |
| --- | --- | --- | --- |
| Codex | `npx skills add AVL05/premium-frontend-director --skill premium-frontend-director -a codex` | Manual skill-folder install | Confirm discovery in a **new** Codex session |
| Claude Code | Same installer with `-a claude-code` | Native Claude marketplace | Do not install two copies of the same skill |
| Other Agent Skills hosts | Interactive `npx skills add` and select host | Copy skill directory if host documents it | Host-specific invocation/discovery is not universally tested |

**Installation requirements:** the Skills CLI currently needs Node.js 22.20+. The skill's Markdown content does not depend on Node, Python or a paid provider. The optional browser helper and optional companions have separate requirements.

## Release gates

- [ ] CI for intended release commit passes on both OS targets and Chromium fixture.
- [ ] Core is installed and discovered by a fresh Codex session.
- [ ] Core is installed and discovered by a fresh Claude Code session.
- [ ] Native Claude marketplace install is independently verified.
- [ ] Same reference brief implemented and browser-reviewed on real host(s), with screenshot paths.
- [ ] G11 baseline/candidate first-viewport and interaction evidence on an ambitious redesign.
- [ ] Browser accessibility/routing tests recorded with actual results.
- [ ] Optional companions validated only if their use is claimed.
- [ ] Human visual review completed; no unsupported artistic or performance certification.
- [ ] Version/tag/release description reflects *verified* compatibility only.

Use **PASS / FAIL / NOT RUN**, not assumptions. See [manual acceptance matrix](manual-testing.md) and [release issue](https://github.com/AVL05/premium-frontend-director/issues/3).

## Maintenance

- Keep the skill **self-contained**; docs outside `skills/premium-frontend-director/` may not ship in project-only installs.
- Preserve the single canonical `SKILL.md`, clear `references/` paths and no required integrations.
- Verify external install commands against upstream publisher docs when changing them.
- Run `python scripts/validate.py`, `python -m unittest discover -s tests -v` and the browser-smoke fixture.
- Do not require proprietary agents to run in CI or silently claim unverified manual results.
