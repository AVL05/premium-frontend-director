# Requirements, companion skills, integration roles and fallbacks

## Required for instruction execution

- A coding agent supporting Agent Skills / `SKILL.md` (Codex, Claude Code, or compatible host).
- Read access to the frontend project and write permission for implementation.
- The target project's own build/runtime tools for running the frontend; the skill imposes no framework or Node version.

## Recommended high-end design setup (NOT required)

The director is **self-contained**, with a complete creative-direction and quality-gate fallback. Companion skills may improve results, but they are **not transitive dependencies**, and their upstream versions, scripts and licenses are maintained independently.

| Priority | Companion | Official / upstream source | Unique contribution | Fallback |
| --- | --- | --- | --- | --- |
| Highly recommended | `design-taste-frontend` (Taste Skill) | https://www.tasteskill.dev/docs | Visual taste, distinctive layout, type hierarchy, motion and avoiding generic templates | `creative-direction.md` |
| Highly recommended | `impeccable` | https://impeccable.style/tutorials/getting-started/ | Design critique, polish and optional agent-specific checks | `quality-gates.md` |
| Optional | `frontend-skill` (OpenAI) | https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5.4 | A restrained alternative creative-direction perspective | `creative-direction.md` |
| Optional | `frontend-design` (Anthropic) | https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design | An expressive alternative creative-direction perspective | `creative-direction.md` |
| Task-specific | `image-to-code` | https://www.tasteskill.dev/docs | Turn an approved visual reference into source layout | Manual reference breakdown |

Taste Skill's default v2 is described as experimental by its author; ensure its requirements and installation method are compatible with the host version before opting in.

### Recommended installation commands

From the frontend project's directory, after reviewing the third-party tools:

```bash
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend
npx impeccable install
```

Impeccable also has `npx skills add pbakaus/impeccable` for shared-skill distribution. The CLI installer may configure additional agent-specific integrations; inspect prompts and request user approval. Never automatically install it.

### Composition and instruction precedence

0. User's explicit objective, existing project rules, security, accessibility and maintainability constraints always win.
1. **Director owns orchestration**: project audit, creative brief, three candidate directions, `design.md`, implementation gates and honest handoff.
2. If *registered* and relevant, **Taste Skill contributes during art direction**. Adopt a cohesive subset of its ideas; avoid independent competing design systems.
3. `frontend-skill` (Codex) or `frontend-design` (Claude) may serve as an **alternative visual guide**, not mandatory parallel instructions.
4. After building, if *registered*, **Impeccable contributes to critique and polish**. Turn feedback into actionable corrections that remain consistent with approved design tokens.
5. Use `image-to-code` only when source reference imagery genuinely exists and the agent can inspect it.
6. Director then verifies actual browser rendering, performance and accessibility with whatever tools are available, reporting PASS / FAIL / NOT RUN.

Discover companion skills through the host's *registered skill inventory*. Do not infer availability from guessed filesystem paths or silently pretend to have loaded skills. Agent hosts differ in how they expose, load, or invoke another skill; if composition is not supported, ask the user to invoke it separately or use the fallback documentation. Do not invent slash commands or call skills simply by writing their names when the host cannot resolve them.

**Avoid context conflicts:** do not load all design skills simultaneously without purpose; do not give a third-party skill permission to replace the user's design direction, introduce unapproved dependencies or ignore tests.

## Capabilities and truthful degradation

| Capability | Benefit | If unavailable |
| --- | --- | --- |
| Browser + Playwright or similar | Responsive screenshot / interaction review | Static-only review; browser gates NOT RUN |
| Image generation / licensed library | Brand-specific visuals | Use approved existing assets or labeled placeholders |
| Figma integration | Approved design specs | Design tokens and `design.md` |
| axe / accessibility tool | Find common issues | Manual semantics/keyboard review; automated gate NOT RUN |
| Lighthouse / performance trace | Measured performance | Basic analysis; performance metric NOT RUN |
| Git | Versioned implementation | Document files changed |

## Playwright guidance

Reuse existing browser tooling. If absent, request permission before changing target project dependencies. A typical Node setup is:

```bash
npm install --save-dev @playwright/test
npx playwright install chromium
```

Browser downloads require network and may need OS dependencies. Adjust commands to the project's existing package manager.

## Dependency policy

- Keep the core skill fully functional with **zero other skills installed**.
- Do not install third-party code, external assets, paid services or new tooling without permission.
- Do not pin a frontend framework or UI library globally.
- Review installed companion skills for security, license, compatibility and possible conflicting directives.
- Do not claim that more skills always produce better aesthetics; evaluate visual output with actual browser evidence and human review.
