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

Install from the public repository:

```bash
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director
```

**Verification:** Published repository confirmed. End-to-end installer behavior is not yet certified for all CLI/agent versions. Inspect commands and run `npx skills --help` for supported options.

### Option B — Codex (native project location)

Copy `skills/premium-frontend-director/` to `.agents/skills/premium-frontend-director/` in the target project, or to `~/.agents/skills/premium-frontend-director/` for personal use. Restart your agent if it doesn't discover the skill. Exact global locations may vary by installed Codex version.

### Option C — Claude Code (native project location)

Copy `skills/premium-frontend-director/` to `.claude/skills/premium-frontend-director/` in the target project, or to `~/.claude/skills/premium-frontend-director/` for personal use.

### Option D — Claude Code plugin marketplace

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

## Skill profiles: Core, Premium and Studio

Choose a profile based on project complexity. **Only the Director is required**. Extra skills never install automatically and are not guaranteed to improve output; browser review and human taste validation remain necessary.

| Profile | Skills / tools | Recommended for |
| --- | --- | --- |
| **Core** | Director + existing frontend tooling, browser QA when available | Any website; no third-party skill dependency |
| **Premium** (recommended) | Core + **UI UX Pro Max** (research) + **Taste Skill** (art direction) + **Impeccable** (polish) + **Web Design Guidelines** (review) | Distinctive portfolios, landing pages and premium products |
| **Studio** | Premium + **Design System Patterns** for larger token systems, **React Best Practices** for React/Next.js only, optional responsive/accessibility/Tailwind-specific guidance | Complex SaaS, dashboards and multi-page systems |

For **exact Codex/Claude install commands, upstream URLs, prerequisites, routing rules, and security caveats**, see **[Companion profiles & installations](docs/companion-profiles.md)**. This is the source of truth for optional installations.

### Recommended quick setup

```bash
# Core / director
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director

# Premium / optional creative direction
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend

# Premium / optional design critique
npx impeccable install

# Premium / optional UI guideline audit
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
```

**UI UX Pro Max requires its dedicated CLI** (plus Python 3 for its search scripts), not merely the generic `skills add` command. Use `npx ui-ux-pro-max-cli init --ai codex` or `--ai claude` as appropriate. **Agent Browser is a separate browser CLI**, not a skill installation; see the guide. Taste Skill's default is maintained at its current v2.x line; older classic skills and `image-to-code` have moved to separate repositories. <https://github.com/Leonxlnx/taste-skill>

### Orchestration

1. **Director** owns scope, three proposed art directions, `design.md`, implementation, tests, and final sign-off.
2. **UI UX Pro Max** contributes discovery data and visual systems, if installed.
3. **Taste Skill** contributes *one* cohesive aesthetic direction. Avoid competing style instructions.
4. **Design System Patterns / React Best Practices** are invoked only for matching Studio project needs.
5. **Impeccable** critiques and polishes the implemented UI. **Web Design Guidelines** adds heuristic review.
6. **Playwright / other real browser automation** checks actual output and reports PASS / FAIL / NOT RUN; no tool substitutes for unperformed tests.

Example prompt:

```text
Use premium-frontend-director in Premium mode. Inspect the existing frontend,
and, only if available, consult UI UX Pro Max for research, Taste Skill for a
single coherent art direction, and Impeccable for final critique. Use Web Design
Guidelines for targeted QA. Create a project-specific design.md, implement
without regressions, capture desktop/mobile screenshots and report observed
PASS/FAIL/NOT RUN gates. Do not auto-install external skills.
```

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
  references/                   Creative direction, implementation, quality, dependencies\ndocs/companion-profiles.md      Core/Premium/Studio matrix, installation, provenance
  assets/design-template.md     Project design.md template
  scripts/visual-audit.mjs      Optional browser smoke check
.github/workflows/              CI validation
scripts/                         Skill packaging checks
LICENSE
CONTRIBUTING.md
```

## Reproducible browser smoke fixture

A standalone sample page and a browser-check recipe are available in [examples/visual-audit-fixture](examples/visual-audit-fixture/README.md). The optional Playwright helper now also flags broken images, missing image alt attributes, unlabeled form controls, missing main/title, and unexpected h1 count. This is **not a substitute for WCAG, Lighthouse or human visual review**.

## Automated CI coverage

On every push to `main` and on pull requests, GitHub Actions validates the skill's manifests and Python unit tests on **Windows and Linux**, checks JavaScript syntax, then runs the local smoke fixture in **Chromium**. Four viewport screenshots plus `report.json` are uploaded as CI artifacts for 14 days. This checks browser execution and the fixture—not the behavior of Codex or Claude Code, the accessibility of arbitrary sites, or the artistic quality of generated designs.

## Development and validation

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

CI validates paths, metadata, referenced files, manifests and basic portability, **not** agent behavior or visual output. Follow the [Windows-friendly manual acceptance guide](docs/manual-testing.md) to test Codex native, Claude native, Claude marketplace, and the optional portable installer using the same reference brief. Record actual PASS / FAIL / NOT RUN results before declaring cross-agent certification.

## Roadmap

- [x] Public GitHub repository published
- [ ] Verified release tag with compatibility evidence
- [ ] Fresh Codex installation and sample-site integration test
- [ ] Fresh Claude Code installation and plugin marketplace test
- [x] CI browser smoke and four screenshot artifacts for the local fixture
- [ ] Automated screenshot comparison baselines and accessibility test recipe
- [ ] Example websites + real before/after evidence

## Release readiness

CI checks package structure, manifests, syntax and unit tests. It does **not** prove that Codex/Claude Code can load the skill on every supported version or guarantee aesthetic outcomes. Before an official stable release, follow [the compatibility test matrix](docs/compatibility-testing.md) and publish actual browser evidence. Report untested combinations as **NOT RUN**.

## License

MIT. The brand names Codex, Claude Code, Figma and others belong to their respective owners. Not affiliated with OpenAI or Anthropic.
