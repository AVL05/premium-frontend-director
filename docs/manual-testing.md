# Manual acceptance — real agents and generated websites

> **Owner-reported real-world use is documented below.** This is evidence that Premium Frontend Director has been used with Codex and Claude Code on actual websites; it is **not** a clean-install certification or a controlled cross-agent benchmark. The automated package and browser-fixture checks are independently recorded in GitHub Actions.

## Real-world usage reported by the project owner (2026-11-07)

The maintainer confirms using **Premium Frontend Director with both Codex and Claude Code** during development of the following three projects. This is firsthand maintainer-reported usage, not an independent reproduction. The precise agent-to-project assignments, installation routes, profile combinations, versions and execution transcripts were not supplied; do not assume every project used both agents, every companion, or every ambition mode.

| Project | Public result | Source repository | What it demonstrates |
| --- | --- | --- | --- |
| ALEVICLOP | [Professional portfolio](https://www.aleviclop.dev/) | [AVL05/Portfolio](https://github.com/AVL05/Portfolio) | An editorial, production-oriented developer portfolio |
| raw.vives | [Photography website](https://rawvives.aleviclop.dev/) | [AVL05/alexgallery](https://github.com/AVL05/alexgallery) | A photography-focused editorial experience |
| The Art of Direction | [Live showcase](https://the-art-of-direction.netlify.app/) | [AVL05/premium-frontend-director-showcase](https://github.com/AVL05/premium-frontend-director-showcase) | A cinematic, interactive showcase and skill installation guide |

The showcase repository also documents a 2026-11-07 production audit in [DESIGN.md](https://github.com/AVL05/premium-frontend-director-showcase/blob/main/DESIGN.md): lint and build passed, Setup/Install were reviewed at 375/768/1440/1920 px, core selection/copy interactions were exercised, and no-WebGL/Motion-off fallbacks were checked. This evidence applies **to the showcase**, not automatically to the other two sites or to a clean skill installation. The audit explicitly leaves Lighthouse/frame-rate measurement, screen-reader review, and system reduced-motion emulation unverified.

### Evidence levels

- **CONFIRMED BY MAINTAINER:** the skill was used in genuine website development with Codex and Claude Code across the named projects.
- **REPOSITORY-DOCUMENTED:** project code, deployed URLs and the showcase's written audit can be inspected.
- **AUTOMATED CI PASS:** [validation workflow](https://github.com/AVL05/premium-frontend-director/actions/runs/42378205798) succeeded for skill commit `6c3bafd` on 2026-11-07 (Windows/Linux package tests and the Chromium fixture).
- **NOT DOCUMENTED:** clean-room installation logs for each host, agent discovery transcripts, the exact companion skills invoked in each project, marketplace installation, and reproducible side-by-side results.

## Acceptance matrix

These cells refer specifically to **reproducible host-level acceptance evidence**, not to whether a finished project exists. Do not convert a maintainer's usage report into a PASS for a particular installation route.

| Test | Codex (Skills CLI) | Claude Code (Skills CLI) | Claude Code (Marketplace) |
| --- | --- | --- | --- |
| Used with Premium Frontend Director in real development | **MAINTAINER CONFIRMED** (route unspecified) | **MAINTAINER CONFIRMED** (route unspecified) | NOT DOCUMENTED |
| Clean project-local installation with command/output | NOT DOCUMENTED | NOT DOCUMENTED | NOT DOCUMENTED |
| Fresh-session discovery and skill invocation trace | NOT DOCUMENTED | NOT DOCUMENTED | NOT DOCUMENTED |
| Bundled reference loading verified by host logs | NOT DOCUMENTED | NOT DOCUMENTED | NOT DOCUMENTED |
| Three distinct directions captured per host | NOT DOCUMENTED | NOT DOCUMENTED | NOT DOCUMENTED |
| Generated project-specific `design.md` verified per host | NOT DOCUMENTED | NOT DOCUMENTED | NOT DOCUMENTED |
| Agent-specific build/test logs attributed to skill run | NOT DOCUMENTED | NOT DOCUMENTED | NOT DOCUMENTED |
| Agent-specific browser screenshots and accessibility results | NOT DOCUMENTED | NOT DOCUMENTED | NOT DOCUMENTED |
| G11 matched before/after evidence per host | NOT DOCUMENTED | NOT DOCUMENTED | NOT DOCUMENTED |
| Independent human acceptance for a fixed brief | NOT DOCUMENTED | NOT DOCUMENTED | NOT DOCUMENTED |

**Important:** “NOT DOCUMENTED” means evidence is not available in this repository; it does not mean the test was never attempted or failed. The production showcase's own quality-gate results are recorded in its DESIGN.md and should not be conflated with these host-level checks.

## Reproducible acceptance sequence

1. Use a clean, **disposable** frontend project with a known starting commit and the same assets/brief.
2. For each agent use only **one** distribution route. Follow [Getting started](getting-started.md), recording OS, agent version, Node and CLI versions, install command, source scope and discovery evidence.
3. Prompt: `Use $premium-frontend-director. Profile: Core. Ambition: Expressive. Preserve navigation and content. Propose three distinct concepts; implement one; produce design.md; capture matching viewport screenshots; report G11 and quality gates.`
4. Record the actual tool and skill invocation evidence. Browser tools absent means screenshots/interaction QA are NOT RUN.
5. Run build/test/lint for the target project. Capture commands, logs and failures.
6. Repeat with optional Premium companions in a separate clean environment only if comparing their impact. A different result does not automatically prove causation.
7. For Immersive, build the first-viewport **working prototype** and confirm a real signature interaction **before** expanding the entire redesign. Compare **same** route, state and viewport at 375/768/1440/1920 px.
8. Ask a human to review whether the outcome matches the requested visual transformation, content and interaction. Do not invent a 10/10 design score or monetary value.
9. Attach screenshots, short browser recording/frames when available, findings, actual CLI output and unrun gates to [release issue #3](https://github.com/AVL05/premium-frontend-director/issues/3).

## What a passing CI proves

- One canonical `SKILL.md`, required bundled references and Claude plugin manifests exist.
- Standard-library Python validation and regression tests pass in Windows and Linux runners.
- A reproducible local HTML fixture renders in Chromium and produces screenshot/report artifacts.

**What it does not prove:** automatic agent discovery on every machine; external companion installation; cross-agent compatibility; subjective design quality; performance or WCAG certification.

See [CI workflow](../.github/workflows/validate.yml), [fixture README](../examples/visual-audit-fixture/README.md) and [compatibility notes](compatibility-testing.md).
