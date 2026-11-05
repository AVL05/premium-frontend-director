# Getting started

> **One command for Core. No templates to copy, files to edit or paid services required.** For Premium and Studio, the additional tools are optional and are installed separately.

## Requirements

- A compatible coding agent (Codex, Claude Code or another agent that recognizes `SKILL.md`).
- A frontend project to work on.
- **Node.js 22.20+** if using `npx skills` (the installer requirement; the Director's instructions themselves are plain Markdown).
- The frontend project's normal runtime and package manager.
- A browser/automation tool **only if you want actual visual/browser QA evidence**. Without one, those checks are `NOT RUN`.

You do **not** need Python, GSAP, Three.js, Impeccable, paid subscriptions or a new framework for Core.

## 1. Install Core in your project

Open a terminal from the root of your **website/app**, then run:

```bash
npx skills add AVL05/premium-frontend-director --skill premium-frontend-director
```

Select the correct agent and **project-local** scope. Avoid the `-g` switch if you want to keep installations isolated.

Explicit agent commands (also project-local):

```bash
npx skills add AVL05/premium-frontend-director --skill premium-frontend-director -a codex
npx skills add AVL05/premium-frontend-director --skill premium-frontend-director -a claude-code
```

Run **one** of these installation routes, not all three. If your coding agent is neither Codex nor Claude Code, use the interactive installer and select its name.

The installer normally registers a canonical skill under the project's agent-skills location and may create a symlink in an agent-specific directory. Exact paths differ by host and install method.

### Claude Code plugin marketplace

As an **alternative** to the Skills CLI install, run inside Claude Code:

```text
/plugin marketplace add AVL05/premium-frontend-director
/plugin install premium-frontend-director@premium-frontend-director-marketplace
```

Confirm plugin discovery in the Claude Code UI before invoking it. Do not install a second manual copy of the same skill.

## 2. Verify discovery

From your project:

```bash
npx skills list
```

Open a **new agent session** and ask:

```text
List the installed project skills. Confirm whether premium-frontend-director
is registered and invocable in this session. Do not change any files.
```

A folder existing on disk is **not** proof of a successful agent invocation. If the skill is not discovered, restart the agent and verify that the installer targeted the correct host and scope.

## 3. Start your first design

```text
Use $premium-frontend-director with Core profile and Expressive ambition.
Audit this project's existing UI and goals. Propose three different art
directions, implement the best-fitting one in the current framework,
document design.md, inspect mobile/desktop rendering when possible,
and report actual PASS / FAIL / NOT RUN quality gates. Preserve behavior.
```

You may instead select **Refined** (careful polish) or **Immersive** (cinematic / spatial ambition with a working first prototype). The **profile controls available companion tools; the ambition controls the expected visual impact.** Neither changes the framework automatically.

## 4. Upgrade to Premium (optional)

The **four companions** are independent and remain outside the Director package. Install them **in the project**, after deciding you need their capability. See [exact Codex and Claude Code instructions](companion-profiles.md#premium--four-optional-companions).

| Companion | Purpose | Additional setup |
| --- | --- | --- |
| UI UX Pro Max | Searchable design intelligence | Own CLI; Python 3 for search scripts |
| Taste Skill | Art direction / distinctive UI | Skills CLI; check its current browser/runtime requirements |
| Impeccable | Independent critique and polish | Interactive installer; optional hooks may need approval |
| Web Design Guidelines | UI code/UX heuristics | Skills CLI |

**The Director does not automatically provision or configure these tools**. Without them, it uses its bundled references and reports them NOT AVAILABLE.

## 5. Optional browser smoke test

The repo includes `skills/premium-frontend-director/scripts/visual-audit.mjs`. This is an **optional** helper, not a required part of using the skill.

If your target app already uses Playwright, reuse it. If not, ask for authorization before adding it:

```bash
npm install --save-dev @playwright/test
npx playwright install chromium
```

Then run from your target project's root (change the path to the actual installed skill directory):

```bash
node /absolute/path/to/premium-frontend-director/scripts/visual-audit.mjs --url http://127.0.0.1:3000 --out ./artifacts/visual-audit
```

The script is a smoke check for local URLs, screenshot viewports and basic semantics. It does not provide comprehensive accessibility or performance certification.

## Updating / removing

```bash
npx skills check
npx skills update
npx skills list
```

See `npx skills --help` for [remove and scope options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md). UI UX Pro Max and Impeccable have separate installers and must be updated/uninstalled with their **own** documented workflows.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| `npx` or installer fails | Node.js **22.20+**, npm/npx availability, network/repository access |
| Skill not visible in Codex/Claude Code | Correct project directory; agent targeted; restart session; inspect `npx skills list` |
| Duplicate / contradictory design skills | Avoid installing both marketplace + Skills CLI copies; keep one visual-direction owner per phase |
| UI UX Pro Max search fails | Python 3, vendor CLI resources, correct `--ai` target |
| Taste Skill scripts cannot run | Upstream documented Node/browser requirements |
| Impeccable overlay or hook missing | Vendor installer prompts and local host hook permissions; do not report an unrun audit as PASS |
| No screenshots | Start your app, configure a browser tool; report visual QA as NOT RUN otherwise |
| G11 fails | Prototype a real structural/interactive difference before expanding to other pages |
| External skill unavailable | Continue in Core-compatible fallback; never invent an invocation |

## Further reading

- [Profiles and optional integrations](companion-profiles.md)
- [Creative ambition and G11](../skills/premium-frontend-director/references/ambition-modes.md)
- [Manual cross-agent validation](manual-testing.md)
- [Reproducible browser fixture](../examples/visual-audit-fixture/README.md)

The software is delivered as-is under the [MIT license](../LICENSE). Review third-party package scripts before executing them.
