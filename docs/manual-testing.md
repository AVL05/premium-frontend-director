# Manual acceptance — real agents and generated websites

> **This is a testing plan, not a claim of successful cross-agent verification.** GitHub Actions checks the skill package and a local Chromium fixture; it cannot certify creative output in Codex or Claude Code.

## Matrix

| Test | Codex (Skills CLI) | Claude Code (Skills CLI) | Claude Code (Marketplace) |
| --- | --- | --- | --- |
| Installs without editing project configuration | NOT RUN | NOT RUN | NOT RUN |
| Agent discovers `premium-frontend-director` | NOT RUN | NOT RUN | NOT RUN |
| Agent loads bundled references | NOT RUN | NOT RUN | NOT RUN |
| Three distinct visual directions | NOT RUN | NOT RUN | NOT RUN |
| Project-specific `design.md` | NOT RUN | NOT RUN | NOT RUN |
| Build and functional tests | NOT RUN | NOT RUN | NOT RUN |
| Browser screenshots and accessibility checks | NOT RUN | NOT RUN | NOT RUN |
| G11 (redesign) with matched before/after | NOT RUN | NOT RUN | NOT RUN |
| Human assessment against original brief | NOT RUN | NOT RUN | NOT RUN |

The user may record separate observed Codex results; do not silently transfer them to other installs or hosts.

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
