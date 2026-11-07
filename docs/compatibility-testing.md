# Compatibility and release verification

The canonical implementation is `skills/premium-frontend-director/`. No third-party skill source is vendored into this repository. It follows the [Agent Skills](https://agentskills.io/) format and is designed for hosts that support `SKILL.md`.

## Distribution paths

| Host | Recommended path | Alternative | Known caveat |
| --- | --- | --- | --- |
| Codex | `npx skills add AVL05/premium-frontend-director --skill premium-frontend-director -a codex` | Manual skill-folder install | Confirm discovery in a **new** Codex session |
| Claude Code | Same installer with `-a claude-code` | Native Claude marketplace | Do not install two copies of the same skill |
| Other Agent Skills hosts | Interactive `npx skills add` and select host | Copy skill directory if host documents it | Host-specific invocation/discovery is not universally tested |

**Installation requirements:** the Skills CLI currently needs Node.js 22.20+. The skill's Markdown content does not depend on Node, Python or a paid provider. The optional browser helper and optional companions have separate requirements.

## Current validation evidence (2026-11-07)

**Maintainer-confirmed in real use:** Premium Frontend Director has been used with **Codex and Claude Code** across the developer portfolio, the raw.vives photography site, and The Art of Direction showcase. Projects and the distinction between reported usage and route-specific checks are documented in the [manual acceptance record](manual-testing.md#real-world-usage-reported-by-the-project-owner-2026-11-07).

**Automated validation:** the [2026-11-07 CI run](https://github.com/AVL05/premium-frontend-director/actions/runs/42378205798) for commit `6c3bafd` concluded successfully. It exercises package validation on Windows and Linux and a Chromium fixture, not proprietary agents.

**Showcase-specific QA:** [the showcase DESIGN.md](https://github.com/AVL05/premium-frontend-director-showcase/blob/main/DESIGN.md) records production build/lint, responsive inspection, installer UI interactions, and motion/WebGL fallback checks. Its outstanding performance and accessibility checks remain outstanding.

**Still unverified with reproducible records:** exact Skills CLI host-install transcripts, fresh-session discovery logs, native marketplace installation, which companions actually ran in each project, controlled cross-agent comparison and independent aesthetic outcomes. Public website existence does not by itself prove these steps.

## Release gates

- [x] Automated Windows/Linux package validation and Chromium fixture passed for commit `6c3bafd` ([run](https://github.com/AVL05/premium-frontend-director/actions/runs/42378205798)); **recheck the actual release commit**.
- [ ] Codex: maintainer confirms real use; clean installation + fresh-session discovery logs not yet attached.
- [ ] Claude Code: maintainer confirms real use; clean installation + fresh-session discovery logs not yet attached.
- [ ] Native Claude marketplace install is independently verified.
- [ ] Real projects are documented for both agents collectively; a **same-brief, per-host** reproducible implementation with recorded screenshots is not attached.
- [ ] G11 baseline/candidate first-viewport and interaction evidence on an ambitious redesign.
- [ ] Showcase responsive/interactive checks are documented; full browser accessibility and performance evidence is not yet recorded.
- [ ] Optional companions validated only if their use is claimed.
- [ ] Project-owner acceptance of real project use is reported; independent visual review against a fixed brief is not attached.
- [ ] Version/tag/release description reflects *verified* compatibility only.

Use **PASS / FAIL / NOT RUN**, not assumptions. See [manual acceptance matrix](manual-testing.md) and [release issue](https://github.com/AVL05/premium-frontend-director/issues/3).

## Maintenance

- Keep the skill **self-contained**; docs outside `skills/premium-frontend-director/` may not ship in project-only installs.
- Preserve the single canonical `SKILL.md`, clear `references/` paths and no required integrations.
- Verify external install commands against upstream publisher docs when changing them.
- Run `python scripts/validate.py`, `python -m unittest discover -s tests -v` and the browser-smoke fixture.
- Do not require proprietary agents to run in CI or silently claim unverified manual results.
