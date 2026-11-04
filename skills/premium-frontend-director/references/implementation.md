# Frontend implementation practices

1. Audit current components/routes/styles and preserve functional contracts, content, data flows, SEO metadata and semantics.
2. Establish tokens for type, spacing, color, borders, radii, surfaces and motion; prefer existing CSS conventions.
3. Implement page structure as accessible landmarks and correct heading hierarchy. Buttons are buttons, links are links. Add usable form labels and error messages.
4. Work mobile-first and test key widths; use fluid type and responsive media. Protect against long translated copy and missing assets.
5. Build appropriate states: hover, focus-visible, active, disabled, loading, error, empty, success.
6. Avoid unnecessary dependencies. For each new dependency, explain purpose, alternative, bundle impact and version compatibility.
7. Reserve layout space for images/media; use responsive images, meaningful alt text, and optimized assets. Respect copyright/licensing.
8. Motion should be purposeful, not obligatory. Honor `prefers-reduced-motion` and avoid interactions requiring hover alone.
9. Protect Core Web Vitals where feasible; check for layout shift, oversized media, unnecessary JS, and critical render blockers.
10. Never silently rewrite large parts of a user's app or delete assets. Maintain reversible changes and run existing tests.

## Implementation sequence

- Define a smallest useful design slice: hero or core dashboard flow.
- Implement with real content and realistic browser dimensions.
- Inspect screenshots, iterate proportions and typography.
- Extend components/layout using the validated system.
- Verify interactivity and mobile/responsive states.
- Run quality gates and report evidence.

## Special cases

- **Dashboards:** prioritize information architecture, density, navigation and data legibility over decorative hero layouts.
- **Portfolios:** emphasize authentic work, project outcomes and clear contact paths.
- **Commerce:** preserve trust, discoverability, checkout and accessibility.
- **Marketing:** clarify value proposition, trust evidence and CTA hierarchy.
- **Existing brands:** align to the established design system rather than substituting a fashionable aesthetic.

## G11 proof-of-concept implementation gate

For Expressive/Immersive redesigns, create a **real browser-rendered prototype** of the defining first viewport and signature transition before rebuilding the rest of the site. Record the old view at the same viewport/state, then compare against the prototype and test the signature interaction. If the changes are primarily typography, palette, spacing and captions while the user requested a radical transformation, **G11 FAIL**: revise the creative approach before expanding changes. Build/lint/E2E passing never waives G11. Use `ambition-modes.md` and `immersive-design.md`. Keep changes reversible, and preserve data, accessibility, behavior, asset rights, and measured performance. Immersive does not mandate WebGL.
