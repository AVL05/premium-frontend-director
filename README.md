# Premium Frontend Director

**Art direction → design system → implementation → browser review.** A self-contained, open-source Agent Skill for Codex, Claude Code, and compatible coding agents.

> **Status:** v1.0.0 — packaging and static checks validated; real-world Codex / Claude Code installation and live-browser integration are **not yet certified**. No skill can guarantee a €10,000 aesthetic, bug-free output, or WCAG conformance.

## What it does

- Three meaningfully different design directions before implementation.
- A project-specific `design.md` with tokens, imagery, responsiveness, states and motion.
- Frontend implementation that respects the **existing stack**, including JavaScript-only repositories.
- Browser screenshot/overflow/console review and actionable iterative improvements.
- Explicit `PASS`, `FAIL`, and `NOT RUN` gates; no invented tests, metrics or screenshots.
- No paid tools, external design skills, particular framework or build tool required.

## Requirements

| Requirement | Required? | Details |
| --- | --- | --- |
| Codex / Claude Code / Agent Skills-capable host | Yes | Must load `SKILL.md` |
| Access to frontend source code | Yes | Write access for implementation |
| Existing app runtime/build tools | When building/running | Use the target project's toolchain |
| Browser + Playwright | For automated visual sign-off | Not required for planning/static work; missing → gate `NOT RUN` |
| Other design skills | No | Optional enhancement only |
| Figma, image generation, GSAP, Three.js | No | Per-project additions, not dependencies |

See [dependency matrix](skills/premium-frontend-director/references/dependencies.md) for fallbacks and optional skills.

## Install

### Option A — Portable installer (`npx skills`)

After publishing this exact repository under your GitHub account:

```bash
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director
```

**Note:** This command is an intended distribution method, not a tested published URL. The GitHub repository must exist first. Verify the CLI's current supported host flags with `npx skills --help`.

### Option B — Codex (native project location)

Copy `skills/premium-frontend-director/` to `.agents/skills/premium-frontend-director/` in the target project, or to `~/.agents/skills/premium-frontend-director/` for personal use. Restart your agent if it doesn't discover the skill. Exact global locations may vary by installed Codex version.

### Option C — Claude Code (native project location)

Copy `skills/premium-frontend-director/` to `.claude/skills/premium-frontend-director/` in the target project, or to `~/.claude/skills/premium-frontend-director/` for personal use.

### Option D — Claude Code plugin marketplace (after publishing)

Inside Claude Code:

```text
/plugin marketplace add AVL05/premium-frontend-director
/plugin install premium-frontend-director@premium-frontend-director-marketplace
```

This repo includes `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and a single canonical skill in `skills/`. Commands require the repository to be publicly accessible and the user's Claude Code version to support plugins.

## Use

```text
Use $premium-frontend-director to redesign this interface. Audit the current repo, propose three distinct directions, document design.md, implement the chosen system, and review the actual rendering at mobile and desktop widths. Do not claim checks that you could not run.
```

For Claude Code, request the skill by name if your environment doesn't support `$` invocation.

## Optional companion skills

The skill works **without** any of these. You may install them separately from their original authors after reviewing their licenses, current availability and instructions:

- OpenAI: `frontend-skill` (current catalog: `openai/plugins`)
- Anthropic: `frontend-design`
- Community: `design-taste-frontend`, `impeccable`, `image-to-code`

Never redistribute their code inside this repository without explicit license compliance.

## Visual audit helper

For projects with Playwright already available, launch the target frontend and run:

```bash
node /path/to/premium-frontend-director/skills/premium-frontend-director/scripts/visual-audit.mjs --url http://localhost:3000 --out ./artifacts/visual-audit
```

**Important:** Run this command from the target application's root directory. Playwright is resolved from that project's `node_modules`. The helper is intentionally read-only with respect to your app and restricts URLs to localhost. It produces screenshots and `report.json`; not a complete visual, accessibility or performance audit.

## Repository structure

```text
.claude-plugin/                  Claude plugin and marketplace manifests
skills/premium-frontend-director/
  SKILL.md                       Canonical cross-agent workflow
  references/                   Creative direction, implementation, quality, dependencies
  assets/design-template.md     Project design.md template
  scripts/visual-audit.mjs      Optional browser smoke check
.github/workflows/              CI validation
scripts/                         Skill packaging checks
LICENSE
CONTRIBUTING.md
```

## Development and validation

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

CI validates paths, metadata, referenced files, manifests and basic portability, **not** agent behavior or visual output. Test manually in Codex and Claude Code with the same reference app before declaring cross-agent certification.

## Roadmap

- [ ] Public GitHub publication and release tag
- [ ] Fresh Codex installation and sample-site integration test
- [ ] Fresh Claude Code installation and plugin marketplace test
- [ ] Automated screenshot comparison baselines and accessibility test recipe
- [ ] Example websites + real before/after evidence

## License

MIT. The brand names Codex, Claude Code, Figma and others belong to their respective owners. Not affiliated with OpenAI or Anthropic.
