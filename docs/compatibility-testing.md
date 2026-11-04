# Cross-agent compatibility test matrix

> These are release acceptance tests, not claims that they have been run.

## Baseline
- Test on clean Codex and Claude Code installations; record OS, versions, date and commands.
- For Codex, copy `skills/premium-frontend-director/` to `.agents/skills/`; confirm the skill is discovered and invoked.
- For Claude Code, copy to `.claude/skills/`; confirm skill discovery and invocation.
- Separately run `/plugin marketplace add AVL05/premium-frontend-director`, then `/plugin install premium-frontend-director@premium-frontend-director-marketplace` on a clean Claude Code install.
- Separately check `npx skills add AVL05/premium-frontend-director --skill premium-frontend-director` with currently supported version.
- Verify frontmatter, canonical resources, permissions and that no companion skills are mandatory.
- Run the same reference application in each agent; record generated design.md, source modifications and screenshots (375/768/1440/1920 px).
- Verify runtime/browser gates, keyboard interactions, responsive layouts and reduced-motion behavior.
- Record PASS, FAIL or NOT RUN *per agent and installation method* with reproducible logs.

## Manual frontend smoke fixture
Use an independent public template or a tiny locally created static page with a working menu, a form and a grid. Record the starting commit. Ask the agent to propose three art directions, implement one, and review it. Do not grade visual quality using unsupported numerical scores. Collect before/after screenshots and a short human review against the brief.

## Required evidence for stable release
1. Successful CI from GitHub Actions on the intended release commit.
2. One validated Codex native installation, one Claude native installation and one Claude marketplace installation.
3. Browser captures and quality-gate table from the same reference project.
4. No promises of bug-free output or accessibility certification.

Known limitation: the repository's static tests cannot execute proprietary coding agents. Mark end-to-end results NOT RUN until separately observed.
