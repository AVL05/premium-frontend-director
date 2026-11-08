# G11: cosmetic-only Immersive redesign

## Creative brief
“Radically redesign the studio into an **Immersive** experience: a new spatial or editorial composition, deliberate narrative progression, and a **working signature interaction** in the first viewport. Preserve content and navigation, and provide accessible responsive fallbacks.”

## Controlled evidence
- `before.html` — conventional, working baseline.
- `after-cosmetic.html` — **identical markup/content**, with only fonts, palette and spacing changed.
- Same fictional brand, content, viewport, scroll position and state; all assets local.

## Expected human/agent judgement
**G11 FAIL.** The candidate lacks a substantial structural/experiential transformation and any working signature moment. A passing build or screenshot capture does not override the brief.

The automated fixture runner **does not score design**. It captures matched baseline/candidate screenshots at 375×812 and 1440×900 and confirms the fixture uses the same DOM structure. It reports **G11 NOT RUN** until a reviewer actually inspects the screenshots and interactive behavior, then records an evidence-based **FAIL**.

## Reproduce
Run `node scripts/test-failing-fixtures.mjs` from the repository root in a workspace where Playwright and Chromium are available. Inspect the generated screenshots in `artifacts/failing-fixtures/`, compare the pair at each viewport and verify the absence of a signature interaction.

See [issue #4](https://github.com/AVL05/premium-frontend-director/issues/4). This is a negative test case, not a new public showcase.
