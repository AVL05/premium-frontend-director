# Visual-audit smoke fixture

This sample is deliberately minimal and is **not evidence of AI-generated design quality**. It exercises the static browser checks against a reproducible local page.

## Start a server

From the repository root:

```bash
python -m http.server 8765 --directory examples/visual-audit-fixture
```

In another terminal, install Playwright in a **separate test workspace or explicitly approved frontend project**, then run the script from that workspace:

```bash
node /path/to/premium-frontend-director/skills/premium-frontend-director/scripts/visual-audit.mjs --url http://localhost:8765 --out ./artifacts/visual-audit
```

The test should produce four PNG images and a report.json without findings. The test does not check design taste, functional correctness, WCAG certification or performance.

For real visual sign-off, run the skill in Codex and Claude Code on a dedicated application, collect agent logs and compare iterations against a documented creative brief. See [compatibility-testing.md](../../docs/compatibility-testing.md).
