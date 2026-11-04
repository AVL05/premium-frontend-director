# Premium Frontend Director

**A cross-agent creative director for distinctive, production-minded frontend design.** Plan the art direction, document the system, implement within the existing stack, critique the real page and report actual browser evidence.

[**Guía de instalación en español**](docs/GUIA-ES.md) · [Detailed profile guide (English)](docs/companion-profiles.md) · [Manual agent tests](docs/manual-testing.md)

> **Release status:** Source and CI-validated development version. Real end-to-end installations in Codex and Claude Code and generated-design evaluations remain **NOT RUN**. A skill cannot guarantee design value, bug-free output or WCAG compliance.

## Install in 60 seconds

Open a terminal in your frontend project and choose **Codex** or **Claude Code** when asked by the installer:

```bash
npx skills add https://github.com/AVL05/premium-frontend-director --skill premium-frontend-director
```

Or use the Claude Code plugin marketplace **instead of installing a second copy**:

```text
/plugin marketplace add AVL05/premium-frontend-director
/plugin install premium-frontend-director@premium-frontend-director-marketplace
```

Restart the agent and confirm it has discovered the skill. Detailed native paths and Windows PowerShell instructions: [manual testing](docs/manual-testing.md).

## Choose your profile

| Profile | Install these skills | Additional prerequisites |
| --- | --- | --- |
| **Core** | **Premium Frontend Director** only | Agent supporting skills; frontend project. Browser testing is optional but necessary to claim visual sign-off. |
| **Premium** (recommended for high-end sites) | **Core** + **UI UX Pro Max** + **Taste Skill** (`design-taste-frontend`) + **Impeccable** + **Web Design Guidelines** | Node.js 22+, Python 3 (UI UX searches), Chrome/Edge/Chromium (Taste/browser workflows) |
| **Studio** (larger products) | **Premium** + **Design System Patterns**; add **Vercel React Best Practices** if using React/Next.js, and **Responsive Design**, **Accessibility Compliance**, **Tailwind Design System** only when relevant | Same as Premium, plus the project's own framework/toolchain |

**Only the Director is mandatory.** Companion skills enhance specific phases; none is auto-installed. Studio is *not* "install everything."

### Premium add-on commands

Run these **after installing Core**, using the vendor's current installer:

```bash
# UI UX Pro Max — choose ONE for your agent:
npx ui-ux-pro-max-cli init --ai codex
# OR
npx ui-ux-pro-max-cli init --ai claude

# Taste Skill
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend

# Impeccable — follow the interactive prompts
npx impeccable install

# Web Design Guidelines
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
```

For **Studio**: `npx skills add wshobson/agents --skill design-system-patterns`. For React/Next.js: `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices`. Optional responsive/accessibility/Tailwind commands and Agent Browser setup are in the [Spanish guide](docs/GUIA-ES.md) and [profile details](docs/companion-profiles.md). Review third-party code and choose project/global scope deliberately.

## How to use

Open **your frontend application** in Codex or Claude Code, then paste:

```text
Use premium-frontend-director in Premium mode on this frontend.
Inspect the code and actual registered companion skills.
Propose three distinct visual directions, then implement the most appropriate.
Create design.md with the design tokens and decisions.
Use UI UX Pro Max for research, Taste Skill for art direction and Impeccable
for a final critique only if they are really available.
Check the rendered app in a browser at mobile, tablet and desktop widths,
fix visible defects, preserve existing functionality and document
PASS / FAIL / NOT RUN results with actual evidence.
Never auto-install other skills or invent verification results.
```

**Core:** replace `Premium` with `Core`. **Studio:** replace it with `Studio` for complex SaaS/dashboard projects. The Director selects only relevant companions: a single primary taste contributor, framework-specific implementation advice and independent QA.

## What the skill does

1. Audits the brief and existing project and proposes **three meaningful art directions**.
2. Establishes one coherent identity and produces a project-specific **`design.md`**.
3. Builds the experience in the project's **existing framework** and preserves behavior.
4. Runs a focused critique and refines hierarchy, typography, spacing, states and motion.
5. Inspects the real interface via a browser at **375, 768, 1440, 1920 px** when tooling is available.
6. Reports quality gates as **PASS / FAIL / NOT RUN** — never fake screenshots or WCAG/Lighthouse results.

## Browser quality check

The repository contains an optional read-only [Playwright smoke helper](skills/premium-frontend-director/scripts/visual-audit.mjs). Install Playwright in the **target app** when authorized and run it from the app root:

```bash
npm install --save-dev @playwright/test
npx playwright install chromium
node /path/to/skill/scripts/visual-audit.mjs --url http://localhost:3000 --out ./artifacts/visual-audit
```

The last path is illustrative: replace it with the **actual installed path** to the script. Use existing browser tooling rather than installing duplicates. This checks screenshot, overflow, console/network and elementary semantics; it is **not** a full accessibility, visual regression, interaction or performance audit. [Reproducible fixture](examples/visual-audit-fixture/README.md).

## CI, maintenance and status

- `python scripts/validate.py`
- `python -m unittest discover -s tests -v`
- GitHub Actions: package checks on Windows/Linux; Chromium fixture screenshots and report.
- Cross-agent integration and visual comparisons: **manual acceptance required**. [Testing guide](docs/manual-testing.md) · [Release gate](https://github.com/AVL05/premium-frontend-director/issues/3).
- Optional third-party skills/tools are external, are **not bundled**, and can change independently. [Upstream URLs, installers and fallback behavior](docs/companion-profiles.md).
- Contributions welcome: [CONTRIBUTING.md](CONTRIBUTING.md).

**License:** MIT. No affiliation with OpenAI, Anthropic, Vercel or the authors of companion skills.
