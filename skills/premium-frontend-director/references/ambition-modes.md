# Creative ambition modes — independent of skill profiles

**Core / Premium / Studio select tools. Refined / Expressive / Immersive select the intended visual transformation.** Any pairing is valid: e.g., Premium + Immersive for cinematic photography or Studio + Refined for a dense dashboard. Neither "premium" nor "expensive-looking" automatically means WebGL.

## Modes

| Mode | Intent | Evidence |
| --- | --- | --- |
| **Refined** | Content-led, restrained refinement for maintenance, established brands and simpler interfaces | Coherent typography, spacing, semantics and responsive browser review |
| **Expressive** | Strongly recognizable concept, deliberate storytelling and original composition | A meaningful structural difference and a tested signature moment when redesigning |
| **Immersive** | Experience-first, cinematic or spatial transformation with perceptible impact | Working first-viewport prototype and signature interaction, before/after evidence and an accessible fallback |

**Select from the user's brief, not habit.** "Radically redesign", "cinematic", "experimental", "immersive", "spectacular", "3D" or explicit dissatisfaction with cosmetic changes all indicate potential **Immersive**. Preserve approved functional contracts but do not use an existing conservative aesthetic as a veto on an authorized visual transformation. For ambiguous substantial branding decisions, document the recommendation and request approval when materially necessary.

## Visual hypothesis and proof-of-concept

For **Expressive and Immersive redesigns**, the first implementation milestone is a **real browser-rendered proof of concept** of the defining viewport and its first meaningful transition. Do not redesign every route before it is reviewed.

1. Record **before** screenshots of the exact route, viewport, scroll position and state. Capture existing interactions when relevant.
2. Describe what will **structurally** change: first-frame image scale, composition, spatial layering, scene progression or interaction. Name the **signature moment**.
3. Present three materially different concepts, not three font/color treatments. Choose with reference to the real assets and user goals.
4. Implement a small, reversible, working first slice. Test in a browser and capture **after** evidence at matching views. If possible record a short real interaction video; otherwise use sequenced frames and exact reproduction steps.
5. Review G11 in `quality-gates.md`. If the difference is largely palette, fonts, captions and margins after an explicit request for radical transformation, **G11 FAIL**. Revise the concept **before** extending it. A green build cannot override this.
6. Verify accessibility and performance costs and provide static/reduced-motion fallback. If browser evidence is unavailable, **G11 NOT RUN**—do not assert creative completion.
7. Proceed to additional sections only once the signature moment meets the brief and its basic fallbacks/functional contracts work. Record user approval where necessary.

**Immersive ≠ WebGL.** Strong image composition, cinematographic 2D transitions and narrative editing may serve the brief better. See `immersive-design.md` for optional 3D and graceful degradation.

## Assessment checklist

- Is the first viewport visibly different for the **reasons the user requested**, or just prettier?
- Has the spatial/structural composition changed, rather than only typography and colors?
- Can a human observe the signature interaction on a real browser?
- Is the mobile direction equivalently deliberate?
- Does the experience still work without motion, without optional WebGL and with the keyboard?
- Have runtime costs and constraints been measured or transparently marked NOT RUN?

Do not invent a numerical "premium score", financial valuation, award or evidence of user approval. G11 PASS is a qualitative, explicitly reasoned judgement, not independent certification.
