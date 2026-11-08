<div align="center">

# Premium Frontend Director

### Stop generating generic interfaces. Start directing experiences.

**Art direction · Frontend engineering · Visual proof**

An open-source, portable Agent Skill that helps coding agents turn a creative brief into a distinctive, working frontend—with deliberate visual decisions and verifiable quality checks.

**For Codex, Claude Code, and Agent Skills-compatible coding agents.**

[**Explore the live showcase**](https://the-art-of-direction.netlify.app) · [**Install the skill**](#quick-start) · [Read the documentation](docs/getting-started.md)

[![MIT License](https://img.shields.io/badge/license-MIT-222222?style=flat-square)](LICENSE)
![Agent Skill](https://img.shields.io/badge/format-Agent_Skills-323232?style=flat-square)
![No required companions](https://img.shields.io/badge/companions-optional-465849?style=flat-square)
[![Validate Skill](https://github.com/AVL05/premium-frontend-director/actions/workflows/validate.yml/badge.svg)](https://github.com/AVL05/premium-frontend-director/actions/workflows/validate.yml)

</div>

---

> **See the direction in action:** [The Art of Direction](https://the-art-of-direction.netlify.app) is a standalone, cinematic website created to showcase the project's design philosophy. It is **one live experience**, not a before/after gallery or a claim of independently measured outcomes. [Showcase source](https://github.com/AVL05/premium-frontend-director-showcase).

## What is Premium Frontend Director?

Premium Frontend Director is **an Agent Skill, not a template, component library, theme, or hosted design service**. It guides your coding agent through creative discovery, frontend implementation, browser inspection, and a transparent handoff.

It adapts to the project's existing framework and requirements. **Core works on its own**; external design skills and browser tooling are optional. Your agent and project still need their normal runtimes and tools.

## Why this skill?

Most design prompts stop at a good-looking mockup. Premium Frontend Director provides an **end-to-end design workflow**: understand the product, propose meaningful creative directions, implement in the existing stack, inspect the rendered result, and report what was *actually* verified.

| **Creative direction** | **Real implementation** | **Evidence-first review** |
| :--- | :--- | :--- |
| Brand-appropriate concepts, typography, composition, imagery and motion | Existing framework, reusable components, semantic HTML and accessible interactions | Browser screenshots, functional tests and PASS / FAIL / NOT RUN gates |
| Three genuinely different directions—not palette swaps | Small vertical slices, with a prototype first for ambitious redesigns | **G11 Visual Ambition** catches cosmetic changes disguised as radical redesigns |

**No required paid product. No companion skill required. No custom project configuration for Core.** Your agent still needs the target project and its normal development tools. Browser automation and optional integrations require their own tooling.

## Built with Premium Frontend Director

The maintainer reports using this skill with **Codex and Claude Code** across three real websites, each with a distinct design brief. These are published applications of the workflow, **not** controlled benchmarks, blanket compatibility certification or claims that every project was built with both agents.

| Project | Experience | Links |
| :--- | :--- | :--- |
| **ALEVICLOP** | Professional full-stack developer portfolio with editorial frontend design | [Website](https://www.aleviclop.dev/) · [Source](https://github.com/AVL05/Portfolio) |
| **raw.vives** | Image-led, bilingual photography experience | [Website](https://rawvives.aleviclop.dev/) · [Source](https://github.com/AVL05/alexgallery) |
| **The Art of Direction** | Cinematic showcase and interactive configuration/installation guide | [Live experience](https://the-art-of-direction.netlify.app/) · [Source](https://github.com/AVL05/premium-frontend-director-showcase) |

**Evidence and limitations:** [real-world usage record](docs/manual-testing.md#real-world-usage-reported-by-the-project-owner-2026-11-07) · [compatibility/release checklist](docs/compatibility-testing.md). The skill's [automated validation](https://github.com/AVL05/premium-frontend-director/actions/runs/42378205798) passed for commit `6c3bafd` on 2026-11-07; individual host installation logs and independent output assessments are not yet archived.

## Quick start

**Install in your own frontend repository.** No need to clone this repository or deploy the showcase.

**1.** Open a terminal in the **frontend project you want to work on** (not this repository).

**2.** Install the single self-contained skill:

```bash
npx skills add AVL05/premium-frontend-director --skill premium-frontend-director
```

Choose your coding agent and **project** scope when prompted. To explicitly target an agent:

```bash
# Codex — project scope
npx skills add AVL05/premium-frontend-director --skill premium-frontend-director -a codex

# Claude Code — project scope
npx skills add AVL05/premium-frontend-director --skill premium-frontend-director -a claude-code
```

The installer needs **Node.js 22.20+**. This is a requirement of the installer, not of the skill's instruction files. Do **not** add `-g` unless you intentionally want a global installation. <https://github.com/vercel-labs/skills>

**3.** Restart or open a new agent session, then prompt:

```text
Use $premium-frontend-director with the Core profile and Expressive ambition.
Inspect this project, propose three genuinely different visual directions,
choose one that fits the content, implement it in the existing stack,
and verify the rendered result. Report PASS / FAIL / NOT RUN gates.
Do not install anything else without permission.
```

That's all for **Core**. Check installation with `npx skills list` and start a new agent session. If your agent does not discover the skill, see the [troubleshooting guide](docs/getting-started.md#troubleshooting). For Claude Code you may alternatively use the [native plugin marketplace](docs/getting-started.md#claude-code-plugin-marketplace)—**do not install both copies**.

## How it works

1. **Discover:** inspect the existing UI, audience, content, constraints, and codebase.
2. **Direct:** propose three materially different creative directions, then choose a coherent concept.
3. **Document:** record the visual thesis, design decisions, motion, and accessibility requirements.
4. **Build:** implement the approved direction within the existing stack, starting with a focused prototype for ambitious work.
5. **Verify:** inspect real browser output when tools are available and report quality gates as **PASS / FAIL / NOT RUN**.

The skill does **not** guarantee a specific visual result or run browser tests without browser-capable tooling. It requires evidence rather than invented scores.

## Choose a tool profile

A **profile** decides which external tools the agent may consult. The Director always works on its own; optional companions can be added selectively.

| Profile | Install | Best for |
| :--- | :--- | :--- |
| **Core** | **Premium Frontend Director only** | Any frontend; fastest setup and smallest skill footprint |
| **Premium** | Core + **UI UX Pro Max**, **Taste Skill**, **Impeccable**, **Web Design Guidelines** | Portfolios, studios, distinctive brands, high-end launches |
| **Studio** | Premium + **Design System Patterns**, plus framework-specific tools only when relevant | SaaS, multi-page products, large component systems |

**Premium is not automatically installed with Core.** Each optional companion is an independent third-party tool; the [profile guide](docs/companion-profiles.md) includes exact installation instructions and prerequisites. Missing companions never prevent Core from running.

### Choose creative ambition separately

| Ambition | Outcome | Proof expected |
| :--- | :--- | :--- |
| **Refined** | Precise, restrained design | Coherence, usability and responsive review |
| **Expressive** | Distinctive visual identity and narrative | Structural design difference and a signature interaction |
| **Immersive** | Cinematic or spatial experience; 3D only if appropriate | **First-viewport working prototype, signature transition, matching before/after evidence, accessible fallback** |

Use **Premium + Immersive** for an ambitious photography experience; **Studio + Refined** is equally valid for a complex dashboard. **Immersive does not imply mandatory WebGL.**

For a radical redesign, **G11 Visual Ambition** fails when the result is essentially a typography/palette/spacing update, even if lint and build pass. [How G11 works](skills/premium-frontend-director/references/ambition-modes.md).

## Run your first design task

Copy a prompt below into your coding agent **after installing the skill**. The examples describe different project goals; they are not separate showcase websites.

**Existing website — expressive redesign**

```text
Use $premium-frontend-director. Profile: Core. Ambition: Expressive.
Review the existing project and keep its functional contracts.
Propose three materially different concepts, document design.md,
implement the strongest concept and inspect the real browser output.
Compare before/after at matching viewports and report G11.
Do not publish or modify unrelated files.
```

**Cinematic experience — Premium + Immersive**

```text
Use $premium-frontend-director. Profile: Premium. Ambition: Immersive.
This must be a perceivable structural redesign, not a typography refresh.
Use my real content. Propose three experiential directions, then build
ONLY the defining first-viewport prototype and its signature transition.
Consider spatial layering or WebGL only if justified by the brief.
Compare real before/after screenshots and observe the interaction.
Validate mobile, reduced motion, no-WebGL fallback and G11.
If G11 fails, revise the prototype before expanding the site.
Report which optional skills actually ran. No automatic installs or deployment.
```

**Product interface — Studio + Refined**

```text
Use $premium-frontend-director. Profile: Studio. Ambition: Refined.
Audit the existing product, reuse its framework, design tokens and data flows.
Improve hierarchy, forms, responsive layouts, keyboard interaction and states.
Use only available framework-specific companion skills where useful.
Validate the relevant routes and report reproducible test results.
```

Additional [installation instructions](docs/getting-started.md) · [Profile details and optional specialists](docs/companion-profiles.md) · [Acceptance test checklist](docs/manual-testing.md)

## Optional specialists: only when a project needs them

These **are not** additional default Premium requirements.

| Existing need | Optional guidance | Role |
| :--- | :--- | :--- |
| Complex GSAP/ScrollTrigger timelines | [GreenSock GSAP Skills](https://github.com/greensock/gsap-skills) | Motion choreography, lifecycle, teardown |
| True Three.js/WebGL scene | [CloudAI-X Three.js Skills](https://github.com/CloudAI-X/threejs-skills) | 3D scene implementation and fallbacks |
| Lighthouse / Core Web Vitals investigation | [Web Quality Skills](https://github.com/addyosmani/web-quality-skills) | Measured performance diagnostics |

Choose only a relevant skill from each upstream repository after reviewing its source and license. **The Director never downloads or executes a third-party companion automatically.** [Details and installation discovery](docs/companion-profiles.md#task-specific-specialists).

## What the quality gates reject

Three [reproducible negative fixtures](examples/failing-fixtures/README.md) show a cosmetic-only Immersive redesign (**G11**), a mouse-only control (**G4/G6**), and mobile horizontal overflow (**G5**). Automated browser checks verify the specific keyboard/overflow defects and corrected controls; matched G11 screenshots support a **qualitative review**, not automated aesthetic certification.

## Quality and honest reporting

The Director aims to deliver:

1. A creative brief with three genuine directions.
2. A project-specific `design.md` with visual decisions, tokens and trade-offs.
3. A working implementation that preserves the project's real behavior.
4. Desktop and mobile browser evidence (typically **375 / 768 / 1440 / 1920 px**, when available).
5. Accessible keyboard states, reduced-motion fallbacks and performance awareness.
6. **PASS / FAIL / NOT RUN** results, including **G11** for redesigns.

The optional [visual-audit helper](skills/premium-frontend-director/scripts/visual-audit.mjs) captures viewport screenshots and performs basic browser smoke checks. It **does not** certify WCAG, Lighthouse scores, polished aesthetics or complete functional coverage. [Run the example fixture](examples/visual-audit-fixture/README.md).

## Repository layout

```text
skills/premium-frontend-director/
├── SKILL.md                   # Single canonical Agent Skill entrypoint
├── references/
│   ├── dependencies.md       # Profiles, optional skills and routing
│   ├── ambition-modes.md     # Refined / Expressive / Immersive and G11
│   ├── immersive-design.md   # Spatial composition and fallbacks
│   ├── creative-direction.md
│   ├── implementation.md
│   └── quality-gates.md
├── assets/design-template.md
└── scripts/visual-audit.mjs

docs/
├── getting-started.md
├── companion-profiles.md
├── manual-testing.md
└── compatibility-testing.md
```

## Documentation at a glance

| Resource | Contents |
| --- | --- |
| [Getting started](docs/getting-started.md) | Installation, discovery, troubleshooting and removal |
| [Tool profiles](docs/companion-profiles.md) | Optional companion skills and their prerequisites |
| [Creative ambition](skills/premium-frontend-director/references/ambition-modes.md) | Refined, Expressive, Immersive and G11 |
| [Quality gates](skills/premium-frontend-director/references/quality-gates.md) | What must be checked and how results are reported |
| [Manual acceptance](docs/manual-testing.md) | Human verification across coding agents |
| [Live showcase](https://the-art-of-direction.netlify.app) | The project's single cinematic demonstration |

## Compatibility, contribution and status

- **Format:** Agent Skills; designed for Codex, Claude Code and compatible agents.
- **Distribution:** project-local install via Skills CLI, or a separate Claude Code marketplace option.
- **CI:** validates structure on Linux and Windows and runs a local Chromium fixture. [Latest checks](https://github.com/AVL05/premium-frontend-director/actions/workflows/validate.yml).
- **Real-world use:** the maintainer confirms projects built using the skill with Codex and Claude Code. [Published examples and evidence levels](docs/manual-testing.md). Clean-install compatibility and independent output-quality evaluation remain separate checks; CI is not an aesthetic certification.
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md).
- **License:** [MIT](LICENSE).

**Independent open-source project.** Not affiliated with OpenAI, Anthropic, Vercel or the companion-skill maintainers. External projects remain subject to their own licenses and installation policies.
