# Tool profiles and integrations

The only **required** install is **Premium Frontend Director**. Third-party companions are optional, independently distributed, and subject to their own licenses and install procedures.

**Never treat a companion's mention in a prompt as evidence that it was installed or invoked.** In every run, detect what is actually registered and report USED / NOT AVAILABLE / NOT NEEDED.

## Profiles at a glance

| Profile | Includes | Use case |
| --- | --- | --- |
| **Core** | Director only | Any frontend with zero companion dependencies |
| **Premium** | Core + UI UX Pro Max + Taste Skill + Impeccable + Web Design Guidelines | Art-directed sites, photography, premium launches |
| **Studio** | Premium + Design System Patterns and relevant framework-specific guidance | Large applications, SaaS, scalable components |

**Refined / Expressive / Immersive are independent creative ambition modes.** You can select any combination, e.g. Core + Immersive or Studio + Refined. The mode determines **what must be demonstrated**, not how many skills to install.

## Core — the only required install

From your target project:

```bash
npx skills add AVL05/premium-frontend-director --skill premium-frontend-director
```

For `npx skills`, install Node.js 22.20+ first. Choose your agent and local project scope. See [Getting started](getting-started.md) for direct Codex/Claude targets, alternative Claude marketplace install and verification.

## Premium — four optional companions

These instructions are sourced from each upstream maintainer's public install guidance. Run each in the **target app directory**, not inside the Director repository.

### 1. UI UX Pro Max — research and visual design intelligence

[Upstream project](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · [Installer documentation](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill#installation)

Use its **own CLI**. For Codex:

```bash
npx ui-ux-pro-max-cli init --ai codex
```

For Claude Code, run **instead**:

```bash
npx ui-ux-pro-max-cli init --ai claude
```

Preview without writing:

```bash
npx ui-ux-pro-max-cli init --ai codex --dry-run
```

Python 3 is needed for its built-in search scripts. The free/basic upstream distribution is sufficient. **Do not** substitute only a generic `SKILL.md` copy if the vendor's data/search assets are required.

### 2. Taste Skill — one primary art-direction voice

[Upstream project](https://github.com/Leonxlnx/taste-skill) · [Install docs](https://www.tasteskill.dev/docs)

```bash
npx skills add Leonxlnx/taste-skill --skill design-taste-frontend
```

Use project scope. The Director assigns Taste to the **art-direction phase**, avoiding contradictory creative styles from additional generic design skills.

### 3. Impeccable — critique and refinement

[Upstream project and installer](https://impeccable.style/docs/)

```bash
npx impeccable install
```

Select your agent and **project** scope. Review optional hooks and approve them only if desired. The installer can add host-specific integrations; a generic skills-only install may omit them.

### 4. Web Design Guidelines — UX and interface heuristics

[Upstream Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)

```bash
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
```

This evaluates code/interaction patterns, **not** actual Lighthouse results or the artistic success of a page.

### Verify Premium

Open a new agent session and ask it to name the five available skills and which it can **actually invoke**. Do not add more generic taste/aesthetic skills by default.

If a companion is missing, use the Director's internal references; the core process remains fully operational.

## Studio — only what your stack requires

Start from Premium, then select relevant entries:

```bash
# Design tokens and reusable component architecture
npx skills add wshobson/agents --skill design-system-patterns

# React/Next.js only — confirm the current advertised skill name upstream
npx skills add vercel-labs/agent-skills --list

# When responsive layouts need a specialist
npx skills add wshobson/agents --skill responsive-design

# When a dedicated accessibility specialist is warranted
npx skills add wshobson/agents --skill accessibility-compliance

# Tailwind-specific component system, only if present
npx skills add wshobson/agents --skill tailwind-design-system
```

Choose only what matches the project. **Studio is not a "install everything" bundle.**

## Task-specific specialists

These do **not** become default members of Core, Premium or Studio.

| Trigger | Repository | Installation discovery | Contribution |
| --- | --- | --- | --- |
| Complex GSAP/ScrollTrigger choreography | [GreenSock GSAP Skills](https://github.com/greensock/gsap-skills) | `npx skills add greensock/gsap-skills --list` | Timelines, ScrollTrigger and cleanup |
| Genuine Three.js/WebGL spatial scene | [Three.js Skills](https://github.com/CloudAI-X/threejs-skills) | `npx skills add CloudAI-X/threejs-skills --list` | 3D scene architecture and fallbacks |
| Measured Lighthouse/Core Web Vitals diagnosis | [Web Quality Skills](https://github.com/addyosmani/web-quality-skills) | `npx skills add addyosmani/web-quality-skills --list` | Reproducible browser performance investigation |

After inspecting the listed skill names, choose the appropriate one using `--skill <actual-name>`. Do **not** install all skills from an upstream repository by default. No specialist is installed or invoked automatically. Immersive does **not** require a 3D library.

## Orchestration, precedence and costs

| Phase | Owner | Optional collaborator |
| --- | --- | --- |
| Brief, scope, ambition and G11 | **Director** | None required |
| Research | Director | UI UX Pro Max |
| Art direction | Director | Taste Skill (one primary aesthetic voice) |
| Architecture and components | Director | Design System Patterns / framework skill if actually relevant |
| Motion or WebGL | Director | GSAP / Three.js specialist **if already relevant and registered** |
| Critique | Director | Impeccable |
| UX heuristics | Director | Web Design Guidelines |
| Runtime quality | Director | Web Quality guidance **only with real measurements**, plus browser tooling |

Prioritize user brief, project rules, rights, accessibility and functional contracts over external stylistic opinions. Skip irrelevant companions. If a tool is absent, never invent its invocation. Reduce context and agent usage by reading only task-specific references, proving the first slice before expanding, and avoiding redundant audits.

**No mandatory subscription or external API is built into this skill.** Coding-agent model access, browser installation and third-party services may have their own costs.

## Related guidance

[Getting started](getting-started.md) · [Creative ambition modes](../skills/premium-frontend-director/references/ambition-modes.md) · [Manual acceptance testing](manual-testing.md)
