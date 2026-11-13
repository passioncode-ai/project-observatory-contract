# Course check in AGENTS.md: handoff, 2026-11-13

## Objective and source

The fabric-workspace announcement of 2026-11-12 (board thread `2aa32848`, message `7a62a183`)
asks every passioncode-ai repository to add item 1a of the
[AGENTS.md template](https://github.com/passioncode-ai/fabric-workspace/blob/main/knowledge/templates/AGENTS.md)
to its *Read first* block: the course check of
[rules §0](https://github.com/passioncode-ai/fabric-workspace/blob/main/knowledge/rules.md#0-the-course-check-the-plan-and-the-north-star-before-every-change).
Served row: the roadmap's *Organization* row, which names this repository.

## Done

- `AGENTS.md`: item 1a copied from the template, plus one line naming the roadmap row this
  repository sits in.
- No schema, fixture, probe, licence or tag changed.

## Clock sync (same thread, message `54bb0e84`)

- Branches and pull requests: before this change origin held only `main`; 0 open pull requests
  (`git branch -r`, `gh pr list`). The stale tracking ref `codex/org-quality-2026-10-01` was
  already gone on origin and was pruned locally.
- This repository has no step of its own in S4.1 (organization from one prompt): it is the
  historical, immutable contract surface; current schemas ship with the engine release.

## Checks run

| Check | Result |
|---|---|
| `python3 scripts/check.py` (jsonschema via `uv run --with`) | exit 0; 8 schemas, 6 fixtures, 0 findings |
| `git diff --check` | exit 0 |
| org-index `scripts/check_private.py . --json` | 0 findings, 0 stale allows |

## Open and next task

Nothing open here. `docs/backlog.md` has no rows. Next task: none until a new provider revision
is planned (a new `rev-N` tag, never a moved one).
