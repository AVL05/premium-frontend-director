# Requirements, capabilities and coordinated companion skills

The Director is **self-contained**: other design skills are optional. Its default fallback is `references/creative-direction.md`, `references/implementation.md`, and `references/quality-gates.md`.

Read [companion profiles and installation](../../../docs/companion-profiles.md) to choose Core, Premium or Studio and for verified upstream installer guidance.

## Capability detection and routing

1. Identify current project's frontend framework, complexity, design system, real assets, routes, test commands and user constraints.
2. Choose **Core** unless the user asks for a premium/studio experience, a complex design system exists, or registered companions match the task. **Premium** is recommended for highly distinctive frontends; **Studio** is conditional on architecture.
3. Query the host's **actual registered skills and available tools**. Missing skills must not block the core workflow. Explicitly report `NOT AVAILABLE` when a requested companion cannot be invoked.
4. In the discovery phase, use `ui-ux-pro-max` to consult style/palette/type databases if available. Its search scripts need Python 3. Without it, use the brief and internal creative-direction guidance.
5. In art direction, use **one primary** taste contributor (prefer `design-taste-frontend` if installed), rather than conflicting multiple frontend-design directives.
6. Use design-system-patterns only for scalable design-token/component work. Use react-best-practices only when React/Next.js is actually present. Add responsive/accessibility/tailwind guidance only when relevant.
7. After implementation, use `impeccable` for critique/polish when invocable; use web-design-guidelines for interface audits if available. Neither is a substitute for browser testing.
8. Capture actual results with existing Playwright or other available browser automation. Agent Browser is an external CLI, **not** a required skill and not interchangeable with `visual-audit.mjs`. Browser checks not run are `NOT RUN`.

## Required baseline

- Host able to load `SKILL.md` and access project files.
- Write permission only when implementation is requested.
- The target project's own runtime/build tools for running the app.
- No universal React, Node or Python requirement for **Core instruction execution**.
- Optional companion runtimes are **conditional**; see profile documentation.

## Permission, security and precedence

- Never install third-party skills, packages, binaries, fonts or paid services without authorization.
- Verify the current upstream publisher and license; no skill code is redistributed here.
- User brief, repository rules, security, accessibility and maintainability take precedence.
- `design.md` stays canonical; store source-specific findings without mixing incompatible token systems.
- Distinguish tool present, skill discoverable, skill actually invoked, and validation actually passed.
- Do not pretend a named skill is invocable if the host cannot compose skills.

## Playwright fallback instructions

Use existing project tooling. If absent, request approval before changing dependencies:

```bash
npm install --save-dev @playwright/test
npx playwright install chromium
```

If browser tools remain unavailable, perform static review and document which visual/interaction gates were `NOT RUN`.
