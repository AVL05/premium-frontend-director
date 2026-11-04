# Manual acceptance test — Codex and Claude Code

This is a **manual verification checklist**. The repository CI validates packaging and a Chromium fixture, but cannot certify agent-specific skill discovery or the quality of a generated website.

## Prerequisites

- Git, a supported Codex or Claude Code installation, and a disposable frontend test project with a known-good starting commit.
- For visual validation: Node.js, Playwright, Chromium and a running local frontend. Browser tools may require an initial download.
- The other design skills mentioned in README are **optional**, never prerequisites.
- Verify the source URL and inspect scripts before installing third-party code.

## A. Codex, native installation

In a terminal (PowerShell on Windows also works):

```powershell
git clone https://github.com/AVL05/premium-frontend-director.git
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
Copy-Item -Recurse -Force ".\premium-frontend-director\skills\premium-frontend-director" "$HOME/.agents/skills/"
```

Launch Codex in the **disposable frontend project**, not in this skill repository. Confirm that `premium-frontend-director` is listed as available. Test explicit invocation:

```text
Use $premium-frontend-director. Audit this sample frontend, propose three art directions, pick a coherent option, create design.md, implement it, and run visual/browser quality gates with real evidence.
```

## B. Claude Code, native installation

In a fresh PowerShell working directory after cloning the repo:

```powershell
New-Item -ItemType Directory -Force "$HOME/.claude/skills" | Out-Null
Copy-Item -Recurse -Force ".\premium-frontend-director\skills\premium-frontend-director" "$HOME/.claude/skills/"
```

Open Claude Code in the sample frontend and request `premium-frontend-director` by name. Verify the skill loaded its references and produced `design.md`.

## C. Claude Code marketplace (separate clean setup)

Inside Claude Code:

```text
/plugin marketplace add AVL05/premium-frontend-director
/plugin install premium-frontend-director@premium-frontend-director-marketplace
```

Confirm the plugin is enabled and can be invoked without a second manual skill copy. If not, record the exact command output and Claude Code version.

## D. Optional portable installer

Inspect the current CLI instructions with `npx skills --help`, then test:

```bash
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director
```

Select Codex or Claude Code when prompted. Confirm which directory was written and whether the host discovers the skill. Do not assume a successful installer exit implies successful agent loading.

## E. Shared test brief and evaluation

Use **the same test frontend and brief** in each agent:

> Redesign this sample creative-studio homepage as a distinctive editorial brand. Preserve navigation and semantics, produce three different creative concepts, document the chosen design system, implement a responsive result, and inspect actual rendering at 375, 768, 1440 and 1920 px. Respect reduced motion. Report real PASS/FAIL/NOT RUN gates with screenshot paths.

Record:

| Check | Codex native | Claude native | Claude plugin | npx installer |
| --- | --- | --- | --- | --- |
| Skill discovered | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| References loaded | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| 3 distinct directions | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| design.md created | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Build/tests pass | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Real viewport screenshots | NOT RUN | NOT RUN | NOT RUN | NOT RUN |
| Human visual review | NOT RUN | NOT RUN | NOT RUN | NOT RUN |

Attach OS, agent version, command transcript, screenshots, build logs, failures and limitations to [the release gate issue](https://github.com/AVL05/premium-frontend-director/issues/3). Only update a cell after observing the actual result. Do not represent an automated scan as WCAG conformance or a subjective design comparison as a formal certification.

## Optional local fixture browser test

The repository CI runs Chromium on `examples/visual-audit-fixture`; consult its README to reproduce that same smoke test. It is **not** a generated-design acceptance test.

## Branch housekeeping after merged PRs

GitHub's web interface: **Code → branches → delete** `fix/release-readiness` and `feat/visual-audit-fixture` after checking both PRs are merged. Keep `main`. Alternatively, with authenticated GitHub CLI:

```bash
gh api -X DELETE repos/AVL05/premium-frontend-director/git/refs/heads/fix/release-readiness
gh api -X DELETE repos/AVL05/premium-frontend-director/git/refs/heads/feat/visual-audit-fixture
```

These commands delete only branch references and preserve commits already squash-merged into `main`.
