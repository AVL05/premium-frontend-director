# Contributing to Premium Frontend Director

Thanks for considering a contribution. We welcome changes that make the skill **more distinctive, more portable, more accessible, safer and easier to verify**.

## Before opening a pull request

1. Check [issues](https://github.com/AVL05/premium-frontend-director/issues) and explain the user problem your change solves.
2. Keep `skills/premium-frontend-director/SKILL.md` as the **single canonical entrypoint**, with bundled references under the same folder. Avoid duplicate `SKILL.md` files or runtime dependencies on docs that are not shipped in an install.
3. Do not bundle or automatically download third-party skills. Keep integrations **opt-in**, with accurate upstream credits and real invocation checks.
4. Preserve project-controlled stacks, rights, accessibility and explicit user authorization. Don't replace meaningful user goals with conservative styling defaults.
5. Use **English** for README, docs, source instructions, templates, test messages and contributions. Examples may show user content in any language.
6. Add/update regression tests when changing profiles, routing, references, quality gates or install paths.

## Validate locally

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
node --check skills/premium-frontend-director/scripts/visual-audit.mjs
```

For UI or browser-related changes, run the [reproducible fixture](examples/visual-audit-fixture/README.md) and include screenshot/report evidence. For behavior changes, use a real coding agent and a disposable app, then capture an honest PASS / FAIL / NOT RUN record using the [manual test matrix](docs/manual-testing.md).

## Pull request checklist

- What changed, why and who benefits?
- Are Core installs still self-contained and dependency-free?
- Do optional profiles remain optional and project-local by default?
- Are examples and instructions consistent across README and docs?
- Are failure modes and unverified quality claims explicit?
- Are relevant tests, logs and screenshots attached?

No secrets, copied proprietary assets, speculative benchmarks, fabricated visual metrics or false agent-compatibility claims. Code and docs are [MIT licensed](LICENSE), subject to upstream third-party licenses.
