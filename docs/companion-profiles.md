# Companion profiles, routing and verified installation paths

This catalog is **curated guidance, not a bundled dependency lockfile**. Premium Frontend Director remains useful by itself. All external tools/skills are owned and updated by their respective authors. Review licensing and executable code before installation.

## Profiles

| Profile | Always included | Recommended add-ons | Intended use |
| --- | --- | --- | --- |
| **Core** | Premium Frontend Director | Existing project tools; Playwright or equivalent for browser QA | Any frontend, no other skill required |
| **Premium** (recommended) | Core | UI UX Pro Max for research, Taste Skill for one visual direction, Impeccable for final critique, Web Design Guidelines for QA | Brand-led websites and high-end product interfaces |
| **Studio** (conditional) | Premium | Design System Patterns for scalable token libraries, React Best Practices **only for React/Next.js**, Responsive Design when complex, Accessibility Compliance for deeper review, optional Tailwind Design System for Tailwind projects | Large SaaS, multi-page products and design systems |

**Browser choice:** Playwright and Agent Browser are alternatives or complementary tools. Agent Browser is an executable CLI, **not** a required Agent Skill and **not** installed with `npx skills add vercel-labs/agent-browser`.

## Role matrix and precedence

| Phase | Owner | Optional contributor | Selection / fallback |
| --- | --- | --- | --- |
| Discovery | Director | **UI UX Pro Max** (`ui-ux-pro-max`) | Consult its style, palette and typography data if installed and available; otherwise use the supplied brief and `creative-direction.md`. Python 3 is needed for its search scripts. |
| Art direction | Director | **Taste Skill** (`design-taste-frontend`) | One coherent taste pass. If unavailable use `creative-direction.md`. Do **not** combine contradictory styles. |
| Design-system modeling | Director | **Design System Patterns** | Use for multi-page token/component architecture; skip for small landing pages. Keep `design.md` canonical. |
| Implementation | Director | **React Best Practices**, responsive-design, tailwind-design-system | Select only skills matching the actual framework. No React advice in a PHP-only/static app. |
| Critique | Director | **Impeccable** | Visual critique and polish after a working implementation. Without it, use the Director's quality gates. |
| QA | Director | **Web Design Guidelines**, **accessibility-compliance** | Heuristics/audit guidance only. Run real browser checks and verify actual interactions separately. |
| Browser evidence | Director | **Playwright or Agent Browser** | Require real screenshots and logs for PASS. Never infer a run from a tool being installed. |

At most one primary visual-direction contributor per phase. If both Taste and the agent's native frontend skill are installed, select one for the initial concept and ask for critique separately when useful. Never pretend a companion was executed because its name appears in an instruction.

## Installation — verified upstream documentation

Run installers in a trusted project folder and restart your agent to refresh registered skills where necessary. Commands below are **documented by the upstream authors**, but this repository's CI does not execute third-party installers or certify host-specific skill discovery.

### Core

```bash
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director
```

### Premium optional additions

```bash
# Taste Skill (Node.js 22+, installed Chrome/Edge/Chromium for its scripts)
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend

# Impeccable (follow host prompts; inspect upstream instructions)
npx impeccable install

# Vercel web design checks (portable skill)
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
```

UI UX Pro Max is distributed by its **own CLI**, not by assuming that a generic skills installer extracts the required data files:

```bash
# Codex
npx ui-ux-pro-max-cli init --ai codex

# Claude Code (run this INSTEAD of codex on Claude projects)
npx ui-ux-pro-max-cli init --ai claude
```

Python 3.x is required to execute UI UX Pro Max search scripts. Use `npx ui-ux-pro-max-cli init --ai codex --dry-run` to inspect generated files before installation. Its optional premium/commercial features are not requirements for the Director.

### Studio: install only what your project needs

```bash
# React or Next.js only
npx skills add vercel-labs/agent-skills --skill react-best-practices

# Multi-page/component design system
npx skills add wshobson/agents --skill design-system-patterns

# If extra responsive / accessibility guidance is needed
npx skills add wshobson/agents --skill responsive-design
npx skills add wshobson/agents --skill accessibility-compliance
```

Some community skill catalogs may not mirror the upstream version or installation layout. Confirm the selected upstream skill and its license before accepting the install. A skill's name alone does not imply its capability is registered or callable by every host.

### Browser CLI (alternative to existing Playwright tools)

```bash
npm install -g agent-browser
agent-browser install
```

On Linux, the upstream documentation also offers `agent-browser install --with-deps` for browser system libraries. The Director's included `visual-audit.mjs` still expects project-local Playwright; Agent Browser is an **alternate interactive browser workflow**, not a drop-in replacement for that script.

### Optional reference-to-code skill (different repository)

```bash
npx skills add https://github.com/Leonxlnx/imagegen-skills --skill image-to-code
```

Only use when the user supplies or approves an actual visual reference. Do not fetch or reuse copyrighted examples without an appropriate license.

## Provenance

- UI UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Taste Skill v2.1.x: https://github.com/Leonxlnx/taste-skill ; `image-to-code` moved to https://github.com/Leonxlnx/imagegen-skills
- Impeccable: https://impeccable.style/
- Vercel Agent Skills: https://github.com/vercel-labs/agent-skills
- Vercel Agent Browser CLI: https://github.com/vercel-labs/agent-browser
- Design System Patterns and optional UI skills: https://github.com/wshobson/agents

## Safety, conflicts and evidence

- Do **not** auto-install companion code, grant network access or add paid dependencies merely because a profile is selected.
- Profiles control **recommendations**, not promises. Absent integrations are `NOT AVAILABLE`, not `PASS`; browser checks not performed are `NOT RUN`.
- Existing design tokens, architecture and explicit brand guidance override conflicting companion instructions.
- Test mobile, tablet and desktop screenshots, meaningful keyboard flows, reduced-motion behavior, basic accessibility and performance using observed evidence.
- For an A/B experiment, compare the same brief with Core and Premium, retain both screenshots and human review notes. Do not manufacture taste scores or performance metrics.
