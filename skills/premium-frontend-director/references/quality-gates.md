# Quality gates and visual review

Report each gate using `PASS`, `FAIL`, or `NOT RUN`, with objective evidence. Do not equate a passed build with design quality.

| Gate | Evidence / review |
| --- | --- |
| G1 Design brief | Audience, goal, chosen creative thesis, content plan and trade-offs |
| G2 Design system | `design.md` with tokens, states, responsive and motion decisions |
| G3 Visual review | Browser screenshots: 375, 768, 1440, 1920px (or note unsupported sizes) |
| G4 Interactions | Keyboard navigation, links/buttons, states, forms and mobile nav |
| G5 Responsive | No unintentional horizontal overflow; robust cropping/wrapping |
| G6 Accessibility | Semantics, contrast, focus, labels, reduced motion; note scope and manual limitations |
| G7 Engineering | Existing lint/tests/build with actual results |
| G8 Performance | Measured load/bundle data when tools permit; otherwise NOT RUN |
| G9 Assets/content | Asset licenses, no fabricated claims, appropriate alt text |
| G10 Regression | Existing business flows checked; explicit unknowns |
| **G11 Visual Ambition** | Matched before/after first view, structural change, proven signature interaction and fit to requested mode; fail merely cosmetic radical redesigns |

## Concrete rejection examples (bounded quality checks)

These negative examples help reviewers explain **what fails and why**. They are decision criteria, not a mandatory extra workflow or an automatic design-taste classifier.

| Rejected outcome | Gate | Evidence needed |
| --- | --- | --- |
| An explicitly **Immersive** redesign only changes palette, font, and spacing while preserving the same layout and offering no working signature moment | **G11 FAIL** | Compare the actual brief, matched before/after browser views, and test the requested interaction. This is a **qualitative judgement**. |
| An action responds to mouse clicks but cannot be focused or activated with **Tab and Enter** | **G4/G6 FAIL** for the demonstrated keyboard defect | Reproduce keyboard navigation and activation in the real browser; a passing screenshot or mouse test cannot override this failure. |
| A fixed-width panel causes unintended horizontal page scrolling at a **375px** viewport | **G5 FAIL** for that viewport | Measure `document.documentElement.scrollWidth > window.innerWidth + 1`; fix and retest. |

These failures are **independent**: passing G5 does not make G11 PASS, and keyboard detection does not certify WCAG conformance. Record `NOT RUN` whenever the relevant inspection was not performed. Do not fail a **Refined** redesign for lacking an Immersive scene the user never requested.

The repository includes optional reproducible baseline/broken/fixed examples and a local Playwright regression script at `examples/failing-fixtures/` and `scripts/test-failing-fixtures.mjs`. **Those repository paths are not part of the standalone installed skill**; do not assume they exist in a consumer project or install anything to get them. The criteria above are self-contained.

## Browser review recipe

1. Start target app using its documented start command; confirm it responds.
2. Capture full-page images at 375×812, 768×1024, 1440×900 and 1920×1080 when possible.
3. Test keyboard-only navigation, visible focus, contrast, reduced motion, and interactive elements.
4. Inspect console errors, failed requests, overflow, content truncation, sticky elements, and images.
5. Compare screenshots with the design brief or user-provided references. Record concrete issues (location, cause, fix), implement, repeat.
6. Avoid grading visual taste with a fabricated numeric score; explain evidence and remaining judgment calls.

## Optional Playwright audit helper

From the skill root, run `node scripts/visual-audit.mjs --url http://localhost:3000 --out ./artifacts/visual-audit` **only if** the target app is running and `playwright` or `@playwright/test` is resolvable. The script will not install packages and writes actual screenshots and a JSON report. It does **not** constitute a full interaction, accessibility or performance audit.

## Handoff format

- Creative direction and reasons
- Design decisions and asset licenses
- Modified files and behavior changes
- Gate status table with commands/evidence
- Screenshot paths (only real ones)
- Known issues and explicit next steps

## G11 — Visual Ambition Gate (redesigns)

**Qualitative evidence, never a fabricated numeric score.** A redesign must match the requested **Refined / Expressive / Immersive** ambition, not merely build and test successfully.

1. Capture **before/after** screenshots of the *same route, viewport, scroll position and UI state*, including the first viewport at mobile and desktop widths. Record which image, composition, visual staging and structural progression changed.
2. For Expressive/Immersive, identify a **signature moment** (interaction or transition). Exercise it in a real browser and record a short video when possible, or sequential frames and reproducible interaction steps. A static screenshot alone does not prove animation.
3. Review the proposed first-frame composition and the mobile equivalent. Compare structural difference—not only fonts, color, margins or metadata.
4. When the user explicitly wanted a spectacular/radical/immersive change and the result is mainly cosmetic, **G11 FAIL**. Rework the prototype **before scaling to other sections**.
5. If comparable screenshots or interaction inspection were not performed, **G11 NOT RUN**. Passing a screenshot scanner does not turn this into PASS.
6. G11 PASS means a reasoned, evidence-based internal judgement that the change meets the requested scope, **not** a declaration of artistic excellence, user approval or financial value.
7. Verify keyboard access, reduced motion and static/low-end fallback; these remain distinct quality gates. Measure performance where possible and report NOT RUN otherwise.
