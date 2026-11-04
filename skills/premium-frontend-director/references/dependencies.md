# Requirements, optional integrations and fallbacks

## Required for instruction execution

- A coding agent that recognizes Agent Skills / `SKILL.md` (Codex, Claude Code, or compatible agent).
- Access to a project and permission to read it. Write permissions are required to change implementation.
- A working application build/runtime if the task includes running a live frontend. No universal Node or React version is required: follow the actual project toolchain.

## Not required: other skills

This skill is **self-contained**. Do not refuse work because another design skill is missing. Detect optional skills from the agent's actual registered skill inventory; don't infer their installation from guessed directory names. Available complementary examples:

| Optional skill | Use when available | Fallback |
| --- | --- | --- |
| `frontend-skill` (OpenAI) | Restraint, composition, motion | `creative-direction.md` |
| `frontend-design` (Anthropic) | Expressive UI design | `creative-direction.md` |
| `design-taste-frontend` | Additional visual heuristics | `creative-direction.md` |
| `impeccable` | Finishing and audit workflows | `quality-gates.md` |
| `image-to-code` | Translating approved reference images | Manual composition breakdown |

Do not automatically install any of these, assume they are official to this project, or make their instructions override the user brief.

## Capabilities and truthful degradation

| Capability | Benefit | If unavailable |
| --- | --- | --- |
| Browser + Playwright or similar | Responsive screenshot/interaction review | Static-only review; browser gates NOT RUN |
| Image generation / licensed library | Brand-specific visuals | Use existing licensed assets or clearly labeled placeholders |
| Figma design integration | Import approved design specs | Design tokens and `design.md` |
| axe / accessibility tool | Automated detection of common issues | Manual semantic/keyboard inspection; automated gate NOT RUN |
| Lighthouse / performance trace | Performance measurements | Basic bundle/network examination; performance metric NOT RUN |
| Git | Versioned implementation | Record changed files manually |

## Playwright installation guidance

First inspect existing project tooling. If Playwright is already present, reuse it. Otherwise request approval before modifying dependencies. Typical Node commands (run in the **target application**, not in this skill repository):

```bash
npm install --save-dev @playwright/test
npx playwright install chromium
```

Browser downloads may require network access and platform dependencies. Never promise universal installation success. For other package managers adapt commands to the repository.

## Compatibility & dependencies policy

- Do not pin frontend framework or UI library as a dependency of this skill.
- Do not use an external skill as a runtime requirement.
- Avoid global installs when project-local commands work.
- Never require payment or proprietary design software.
- Follow the user's architecture and licensing constraints.
