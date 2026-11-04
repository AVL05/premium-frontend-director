# Immersive design — cinematic and spatial experiences

Read when **Immersive** is selected. This playbook is **not** an instruction to force 3D into every project.

## Art direction

Create a **stage**, not another conventional hero with enlarged typography. State what the user perceives in the first frame (light, scale, negative space, focal subject), what happens on their first interaction and how the next chapter appears. Structure a coherent photographic/narrative sequence and give the primary subject room to breathe.

Evaluate the least complex medium capable of expressing the idea:
1. CSS layout, masking, layered images and composited transforms.
2. Existing GSAP, Web Animations or other animation primitives if relevant to the narrative.
3. Canvas / Three.js / WebGL **only when true depth, camera movement or spatial interaction adds something meaningful**.
4. Licensed video or image sequences when justified; never autoplay sound.

## If using Three.js / WebGL

- Reuse the project's current renderer and scene infrastructure. Avoid a second RAF, scroll engine or conflicting animation provider.
- Make the hero content **meaningful before WebGL loads**: a genuine static image/poster, heading and navigation in semantic HTML.
- Handle unsupported WebGL, context loss, network errors and device limits without blank screens.
- Apply an explicit device pixel ratio/quality budget, pause when hidden, dispose geometries/textures/listeners and avoid uncapped continuous rendering when not necessary.
- Keep the main LCP visual out of a mandatory heavy canvas path. Consider low-cost fake volumetric light rather than costly realtime effects.
- Never add a large library, remote media, font or paid service without permission.
- Check GPU memory, keyboard interaction, content visibility and back/forward navigation in realistic conditions.

## Fallback matrix

| Context | Required experience |
| --- | --- |
| Reduced motion | A beautifully composed static frame; no compulsory camera movement |
| WebGL disabled or context lost | The same content and meaningful imagery with safe navigation |
| Touch or mobile | Coherent composition, no hover-only controls, adequate targets |
| Low-power device | Lower-cost effects or static fallback without delaying input |
| Slow network | Reserved image space, compressed assets, no loader trap |
| Keyboard / screen reader | Semantic DOM content, focus handling, all primary actions outside canvas |
| No JavaScript enhancement | Keep essential HTML/content and accessible routes when supported by the framework |

## Visual evidence and performance

- Save matching screenshots (375, 768, 1440, 1920 px when supported) and show the first **viewport** separately from full-page contact sheets.
- To prove an animation, capture actual video or reproducible sequential frames; a still screenshot proves only the frame.
- Compare script/image transfer, baseline/candidate rendering and interaction metrics using available tooling. If not measured, mark NOT RUN; never invent Lighthouse scores or FPS.
- Run **G11 Visual Ambition**. Cosmetic updates alone cannot pass an explicitly immersive redesign.
- Human judgement and user acceptance are still necessary. Preserve content rights, data, original imagery and functional contracts.
