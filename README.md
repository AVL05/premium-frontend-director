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

## Recommended design stack (optional, for stronger creative results)

**Premium Frontend Director is self-contained and does not require additional design skills.** For more ambitious art direction and a stronger finishing pass, the **recommended premium setup** is:

| Tool | Purpose | Recommendation |
| --- | --- | --- |
| **Premium Frontend Director** | Owns the brief, three concepts, decisions, implementation, validation and handoff | **Required** |
| **[Taste Skill](https://www.tasteskill.dev/docs)** (`design-taste-frontend`) | Provides stronger aesthetic heuristics, typography, layout, motion and anti-template guidance | **Highly recommended** |
| **[Impeccable](https://impeccable.style/)** (`impeccable`) | Provides design critique, visual audits and final polish; its native installer may offer agent-specific checks | **Highly recommended** |
| [OpenAI `frontend-skill`](https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5.4) | Optional composition and restrained motion guidance in Codex | Optional alternative |
| [Anthropic `frontend-design`](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) | Optional expressive design guidance in Claude Code | Optional alternative |
| [`image-to-code`](https://www.tasteskill.dev/docs) | Helps translate an approved visual reference into frontend code | Task-specific |

**You do not need to install all of these.** We recommend **Premium Frontend Director + Taste Skill + Impeccable** for a high-taste workflow. If another design-focused skill is already active, use its strengths selectively instead of stacking conflicting design directives. The default Taste Skill v2 is currently described by its author as **experimental**; review updates before rolling it out widely.

### Install the recommended stack (Codex or Claude Code)

Install the director first, then optional companions in the project directory. These commands use the upstream publishers' installation methods (review third-party code before running):

```bash
# 1. Main coordinator
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director

# 2. Optional: additional creative direction (Taste Skill v2, experimental)
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend

# 3. Optional: design critique and polish (choose target agent in installer)
npx impeccable install
```

For Impeccable, `npx skills add pbakaus/impeccable` also installs a portable shared skill, but **`npx impeccable install` is recommended** when you want its native agent integration and optional automatic design checks. Claude Code users can alternatively use `/plugin marketplace add pbakaus/impeccable` and then install Impeccable from the plugin browser. The exact available options depend on the current agent version.

To verify what was installed, open a new agent session and inspect its registered skills. **Do not assume success merely because an installer exited without errors.**

### How they cooperate

1. **Director — discover:** read the user brief and project conventions; detect *registered* companion skills, not just file names.
2. **Taste Skill — concept phase:** if installed, use it for *one* creative direction pass and select a coherent visual thesis. Director retains final authority over the project brief.
3. **Director — implementation:** create `design.md`, implement in the existing stack and protect user-facing behavior. Do not blindly merge incompatible instructions from multiple design skills.
4. **Impeccable — critique/polish phase:** if installed, request its critique/audit/polish capabilities to identify concrete improvements. Keep accepted changes within the approved design system.
5. **Director — browser sign-off:** review actual rendering with Playwright or equivalent, run tests and report PASS / FAIL / NOT RUN. Neither Taste nor Impeccable replaces independent verification.

If any companion skill is missing, **continue using the director's built-in references** and mark the integration as *not available*, rather than failing the design task. Never auto-install or execute a third-party plugin without authorization, and never silently override project instructions.

### Example prompt for the recommended stack

```text
Use premium-frontend-director as the lead skill. If design-taste-frontend is installed,
use it in the creative direction phase to produce distinctive editorial layouts,
strong typography and an intentional motion language. Implement the selected design
without changing the existing framework. If impeccable is installed, use its design
critique and polish guidance for a final refinement pass. Validate the real rendered
frontend in the browser, preserve accessibility and performance, and report real
evidence with PASS / FAIL / NOT RUN gates. Do not claim missing skills were used.
```

The companion skills are independently maintained and not redistributed by this repository. Check their licenses, behavior, requirements and installation instructions upstream.

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
