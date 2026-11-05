# Profiles and upstream installation (English)

**One required skill:** Premium Frontend Director. Companion skills are independent, optional and not bundled. Their actual availability must be checked in the agent; a directory or successful install command alone is not proof of invocation.

## Install matrix — exact list

| Profile | Install | Conditional requirements |
| --- | --- | --- |
| Core | `premium-frontend-director` | Agent Skills host; browser QA for visual sign-off |
| Premium | Core + `ui-ux-pro-max`, `design-taste-frontend`, `impeccable`, `web-design-guidelines` | Node 22+ and a Chromium-based browser for Taste; Python 3 for UI UX Pro Max searches |
| Studio | Premium + `design-system-patterns` | Add `vercel-react-best-practices` **only** on React/Next.js; `responsive-design` or `accessibility-compliance` when needed; `tailwind-design-system` only when available and applicable |

**Agent Browser** is an optional standalone CLI, not an Agent Skill. Playwright can be used instead; installing either does not guarantee a complete QA run. `image-to-code` is task-specific and lives in [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills). Do not install every skill indiscriminately.

## Core

```bash
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director
```

Or the native Claude Code marketplace:

```text
/plugin marketplace add AVL05/premium-frontend-director
/plugin install premium-frontend-director@premium-frontend-director-marketplace
```

## Premium: install Core plus all four optional companions

1. **UI UX Pro Max** — visual design intelligence (Python 3 for search scripts). Choose your agent:

```bash
npx ui-ux-pro-max-cli init --ai codex
# OR
npx ui-ux-pro-max-cli init --ai claude
```

Use `npx ui-ux-pro-max-cli init --ai codex --dry-run` to preview a Codex installation. The package installs the `uipro` command if installed globally; its own CLI includes data and scripts.

2. **Taste Skill** — high-taste creative direction (Node 22+, Chrome/Edge/Chromium):

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend
```

3. **Impeccable** — critique and polish:

```bash
npx impeccable install
```

Choose the host and scope in the interactive installer. Its design hook may require explicit approval (Codex: `/hooks`). Manual copies omit its hook.

4. **Web Design Guidelines** — UI heuristics:

```bash
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
```

## Studio: install Premium and add relevant specialization

```bash
# Design tokens/components for larger apps
npx skills add wshobson/agents --skill design-system-patterns

# React / Next.js only
npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices

# Add these only when the use case calls for them
npx skills add wshobson/agents --skill responsive-design
npx skills add wshobson/agents --skill accessibility-compliance
```

Tailwind Design System: confirm exact up-to-date availability and installation upstream before installing; do not treat it as a hard requirement. An optional **standalone** browser CLI is `npm install -g agent-browser` and `agent-browser install`.

## Optional conditional specialists (not part of the default five)

**Do not install these globally or indiscriminately.** The director detects the real project stack and suggests only a needed specialist. Names inside upstream repositories can change, so inspect the actual offered skills before selecting and installing.

| Trigger | Source | Installation discovery | Purpose |
| --- | --- | --- | --- |
| Existing GSAP, ScrollTrigger and demanding timelines | [GreenSock GSAP Skills](https://github.com/greensock/gsap-skills) | `npx skills add greensock/gsap-skills` (select relevant entry) | Choreography, cleanup, scroll integration |
| Real Core Web Vitals / Lighthouse investigation | [Addy Osmani Web Quality Skills](https://github.com/addyosmani/web-quality-skills) | `npx skills add addyosmani/web-quality-skills` (select relevant entry) | Performance diagnostics using real measurements |
| True spatial scene using Three.js/WebGL | [CloudAI-X Three.js Skills](https://github.com/CloudAI-X/threejs-skills) | `npx skills add CloudAI-X/threejs-skills` (select relevant entry) | 3D rendering, device fallbacks and resource lifecycle |

**Default remains Core = director; Premium = director plus four design/QA companions; Studio = Premium plus relevant design-system/framework guidance.** GSAP/Three.js/Web Quality are **capability-triggered** tools that can be used in any profile when needed. Do not imply that Immersive requires WebGL or that the existence of a Lighthouse skill proves measured performance.

Suggested routing for `Premium + Immersive`: Director defines and prototypes the signature moment → UI UX Pro Max researches → Taste contributes one visual direction → **one relevant motion/3D specialist** assists implementation → Impeccable critiques → Web Design Guidelines checks interface heuristics → Web Quality assists **only if real performance diagnostics are being run** → browser evidence/G11. Never auto-install. Avoid stacking competing art direction skills.

## Responsibility and conflict policy

| Phase | Director owns | Optional contributor |
| --- | --- | --- |
| Research | Project/audience/brief | UI UX Pro Max for searchable palette/type/style catalog |
| Creative direction | Three concepts + chosen thesis | One primary taste contributor (Taste Skill or one native agent frontend-design skill) |
| Design system | `design.md`, tokens, states | Design System Patterns (Studio) |
| Implementation | Existing framework, behavior, accessible states | Vercel React Best Practices only for React |
| Polish | Fixing actual visual issues | Impeccable |
| Review | Browser evidence and PASS/FAIL/NOT RUN gates | Web Design Guidelines plus actual Playwright or browser CLI |

Do not auto-install, double-apply contradictory visual systems, imply tool execution without logs, or replace human review with fabricated design metrics.

## Original projects and requirements

- [Director](https://github.com/AVL05/premium-frontend-director)
- [UI UX Pro Max — native CLI](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Taste Skill — Node 22+/browser](https://github.com/Leonxlnx/taste-skill)
- [Impeccable — installer and optional hook](https://github.com/pbakaus/impeccable)
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)
- [wshobson/agents](https://github.com/wshobson/agents)
- [Agent Browser CLI](https://github.com/vercel-labs/agent-browser)

Core/profile install commands are based on upstream documentation checked in November 2026; optional specialist commands are catalog leads requiring review of current repository contents; they are **not** tested against every agent/OS. Refer to each upstream project for future changes.
