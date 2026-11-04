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
