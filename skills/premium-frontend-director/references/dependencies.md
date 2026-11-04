# Self-contained integration contract

Premium Frontend Director requires **no companion skills**. The one installed `SKILL.md` and the references bundled in this directory suffice for Core. External guides in the GitHub checkout are **not required** at runtime: installers may copy only this skill directory.

## Profile matrix (also bundled for portable installations)

- **Core**: Director only; use `creative-direction.md`, `implementation.md` and `quality-gates.md`. Browser QA is `NOT RUN` unless verified.
- **Premium**: Core plus optional **UI UX Pro Max** (`ui-ux-pro-max`), **Taste Skill** (`design-taste-frontend`), **Impeccable** (`impeccable`) and **Web Design Guidelines** (`web-design-guidelines`).
- **Studio**: Premium plus optional **Design System Patterns** (`design-system-patterns`); add **Vercel React Best Practices** (`vercel-react-best-practices`) only for React/Next.js and optional `responsive-design`, `accessibility-compliance` and Tailwind guidance only when needed.

A complete user-friendly setup guide is available in the repository `docs/GUIA-ES.md` and `docs/companion-profiles.md` (not assumed to be present inside an installed skill).

## Routing

1. Inspect the user brief, existing stack, sources, visual assets, tests and project rules. Choose the user-requested profile; default to Core unless the brief clearly requests Premium.
2. Discover the agent's **actually registered and invocable** skills/tools, not guessed filesystem paths.
3. In Premium/Studio research, use UI UX Pro Max's style, palette and font data if available. Python 3 is required to run its search scripts. Otherwise rely on `creative-direction.md`.
4. In art direction, use **one** primary contributor: prefer Taste Skill if available, otherwise another registered native design skill or the bundled reference. Never combine opposing visual presets.
5. In Studio, use Design System Patterns for broad component/token architecture; `vercel-react-best-practices` **only for React/Next.js**.
6. During final refinement, use Impeccable for critique if invocable and Web Design Guidelines for heuristic review, if available. Otherwise use `quality-gates.md`.
7. For real screenshots and interactions, use available Playwright or a browser CLI. **Agent Browser is a separate CLI, not a required skill or a drop-in replacement for `visual-audit.mjs`.**
8. Report each companion as **USED**, **NOT AVAILABLE**, or **NOT NEEDED**; mark unperformed browser/test gates **NOT RUN**. Successful install is not proof that a skill ran.

## Runtime requirements and safe fallbacks

- **Core:** skill-capable Codex/Claude Code host, project read access; write access for implementation.
- **Premium:** optional Node.js 22+ and Chrome/Edge/Chromium for Taste Skill browser scripts; Python 3 for UI UX Pro Max search scripts. Do not assume these are universally available.
- **Studio:** same as Premium; honor the app's own framework build tools.
- **Playwright:** reuse the target project's browser automation. If missing, request authorization before `npm install --save-dev @playwright/test` and `npx playwright install chromium`.
- **Accessibility/performance:** automatic scanners do not certify WCAG or Lighthouse scores without actual measurements; use visible evidence.

## Permissions and precedence

Never install third-party skills, packages, binaries, fonts, assets or paid services without authorization. Respect the user brief, repo rules, security, accessibility, and maintainability. Preserve the canonical `design.md`; don't mix contradictory design systems. No companion is a transitive dependency. Never claim missing tooling was used.

For upstream names and optional commands consult the repo guide if available. If it is not installed, continue autonomously using this file and bundled references.
