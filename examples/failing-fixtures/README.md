# Deliberately failing quality-gate fixtures

**Negative test cases, not premium website examples.** They provide reproducible evidence of what the gates reject. These examples live outside the standalone Core skill folder.

| Fixture | Deliberately broken | Control | Expected result |
| --- | --- | --- | --- |
| G11 — Visual Ambition | [Cosmetic redesign](visual-ambition/after-cosmetic.html) vs. [baseline](visual-ambition/before.html) | Qualitative review of [brief](visual-ambition/brief.md) | **G11 FAIL** only after human/agent inspection (never an automatic artistic verdict) |
| G4/G6 — Keyboard accessibility | [Mouse-only action](keyboard-accessibility/broken.html) | [Native button](keyboard-accessibility/fixed.html) | Broken action cannot be operated with Tab/Enter; fixed works |
| G5 — Responsive overflow | [Rigid mobile panel](responsive-overflow/broken.html) | [Fluid panel](responsive-overflow/fixed.html) | Horizontal overflow at 375px in broken case; none in fixed case |

## Run

In a test workspace with Playwright and Chromium already installed, from the repository root:

```bash
node scripts/test-failing-fixtures.mjs
```

The script **does not install dependencies** or open network URLs. It uses local `file://` fixtures and writes `artifacts/failing-fixtures/report.json` and screenshots.

CI **passes if and only if** the known keyboard and overflow defects are correctly detected and the fixed controls pass. G11 screenshots are evidence for a manual qualitative review only; the script reports **G11 NOT RUN** and documents the expected human FAIL.

These checks are **not** a full WCAG audit, responsive certification, independent design evaluation or controlled agent benchmark. They are intentionally bounded regression examples. See [issues #4](https://github.com/AVL05/premium-frontend-director/issues/4), [#5](https://github.com/AVL05/premium-frontend-director/issues/5), [#6](https://github.com/AVL05/premium-frontend-director/issues/6).
