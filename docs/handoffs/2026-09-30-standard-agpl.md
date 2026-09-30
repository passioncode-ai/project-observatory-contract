# 2026-09-30 — repository standard and the AGPL-3.0 licence

**Objective.** Bring this repository onto the PassionCode.ai repository standard
(fabric-workspace `knowledge/repository-standard.md`, rules F1–F11) and the licence decided in
Fabric ADR-0092: `AGPL-3.0-only OR LicenseRef-PassionCode-Commercial`.

## Done

- `LICENSE` is the AGPL-3.0 text, byte for byte `knowledge/templates/LICENSE-AGPL-3.0.txt`
  (SHA-256 `0d96a4ff…abcb0`); `COMMERCIAL-LICENSE.md` and `CLA.md` are the templates byte for byte;
  `SECURITY.md` added (the repository is public).
- `README.md`: first heading `# Project Observatory Contract`, a *Quick start for a new teammate*
  (Install / Configure / MCP / Develop) and the licensing.md `## License` wording. The earlier MIT
  grant is named exactly: the files as of `0c79d1c` (identical to `rev-4` in `schemas/`,
  `fixtures/`, `probes/` — `git diff --stat rev-4 0c79d1c -- schemas fixtures probes` is empty)
  stay under MIT; `rev-2`–`rev-4` carry no `LICENSE` (`git show rev-4:LICENSE` → not in `rev-4`).
- `AGENTS.md` begins with the template's *Read first* block and ends with *After work*; keeps the
  org-index link `check_index.py` requires; names the new gate. `CLAUDE.md` stays `@AGENTS.md`.
- `scripts/check.py` — the repository's first gate. Watched failing on two planted defects: a
  fixture without its required `owner` (exit 1, `'owner' is a required property`) and a schema
  with `"type": "objekt"` (exit 1, not a valid JSON Schema); green on the tree (exit 0,
  `8 schemas, 6 fixtures, 0 finding(s)`).
- No manifest exists here (no `package.json`, `pyproject.toml`, `Cargo.toml`, plugin manifest), so
  F11 has nothing to declare. No release: this repository publishes `rev-N` tags from the source
  repository's publisher, and a licence change is not a new provider revision.

## Open — the exact next task

1. **The publisher's `README` template** (the `README` constant in the private Project
   Observatory source's `tools/publish_contract.py`) still carries the old README with the MIT
   section. Before the next `--publish`, replace it with this repository's `README.md`, or that
   publication reverts the licence section and the quick start. Its stage step writes only
   `schemas/`, `fixtures/`, `probes/` and `README.md` and deletes nothing, so this repository's
   own files survive a publication.
2. **CO-KB-02** (knowledge base, licensing.md): whether the schemas stay AGPL or become a
   permissive exception so a closed-source host can copy them. The operator's decision.
3. org-index `repositories.json` still says "MIT, so any host can implement it" for this
   repository, `test: null`; it should say AGPL-3.0 or commercial and `python3 scripts/check.py`.
   The GitHub repository description still ends in "MIT." — updated with this change if the
   landing agent had the rights, otherwise the operator's step.

## Checks actually run

- `python3 scripts/check.py` → exit 0.
- org-index `scripts/check_format.py --offline --repo project-observatory-contract` in a scratch
  sibling layout → recorded in the landing PR.
