# Working in project-observatory-contract

## Read first

1. The organization's
   [roadmap](https://github.com/passioncode-ai/fabric-workspace/blob/main/knowledge/roadmap.md) —
   every major feature and release across PassionCode.ai as `RM-*` tracks with owner, phase and
   state. It is the entry point: a task here that serves a track names it, and the track's status
   is edited only in the roadmap.
2. The PassionCode.ai knowledge base — `fabric-workspace/knowledge/` in your clone (org-index
   `scripts/clone_all.sh` makes it) or https://wiki.passioncode.ai/knowledge — at least its
   [README](https://github.com/passioncode-ai/fabric-workspace/blob/main/knowledge/README.md),
   vision, principles and how-to-work.
3. This file, then the organization's
   [CONTRIBUTING.md](https://github.com/passioncode-ai/.github/blob/main/CONTRIBUTING.md).

## What this repository is

Project Observatory Contract: the historical public Fabric contract surface of Project Observatory — the
JSON Schemas, admission fixtures and probe assertions a Fabric host compiles and runs before any
credential or project data is exchanged, published under immutable `rev-N` tags (`README.md`).
It declares against the public Fabric Agent Contract `0.1.0`. Current engine releases carry
their schemas in the engine repository; see [current and historical contracts](README.md#current-and-historical-contracts).

## Commands

| What | Command |
|---|---|
| Install | `python3 -m pip install jsonschema` (the gate's only dependency) |
| Test (the gate) | `python3 scripts/check.py` — every schema a valid JSON Schema, every fixture valid against its capability's input schema; exit 0 green, 1 on a finding, 2 not run |
| Build | none — nothing is built |
| MCP (register + proving call) | none of its own; Project Observatory's server answers these capabilities by name — its README's *Quick start for a new teammate* |

CI (`.github/workflows/check.yml`) runs the same gate on every push to `main` and on every pull
request. The engine checks its own release-pinned schema bytes separately; this repository's
gate validates the historical surface locally.

## Where things live

| Path | What a host does with it | Written by |
|---|---|---|
| `schemas/*.schema.json` | validates the input and output of each capability | historical publisher; immutable revisions |
| `fixtures/*.json` | bounded, non-publishing admission probes | historical publisher; immutable revisions |
| `probes/assertions.md` | what each probe asserts, in prose | historical publisher; immutable revisions |
| `README.md` | what the contract is, the quick start, the licence | this repository |
| `LICENSE`, `COMMERCIAL-LICENSE.md`, `CLA.md`, `SECURITY.md`, `AGENTS.md`, `CLAUDE.md`, `scripts/`, `docs/` | this repository's own files | this repository |

Keep historical schema, fixture and probe bytes unchanged unless a new provider revision is
explicitly planned. Current engine releases publish their contract alongside their package;
the engine's `tools/publish_contract.py` refuses `--stage` and `--publish` (covered by
`tests/test_publish_contract.py`). This repository owns its README and documentation.
The old 2026-09-30 handoff's template-replacement warning describes a retired publisher.

## Local rules

- A `rev-N` tag is never moved or repointed. A changed schema is a new provider revision and a new
  tag (`README.md`).
- This repository is public. Nothing private may be added: no machine paths, no credentials, no
  content from private repositories.
- Licence: `AGPL-3.0-only OR LicenseRef-PassionCode-Commercial` since 2026-09-30 (Fabric
  ADR-0092). The files as of `0c79d1c` stay available under MIT, and the open question whether the
  schemas should be a permissive exception is the knowledge base's CO-KB-02, not decided here.
- Land: a PR, squash-merged or fast-forwarded after `python3 scripts/check.py` exits 0.
- **Shared registers are edited under a lease.** [docs/AGENT_SYNC.md](docs/AGENT_SYNC.md)
  (generated from `.claude/agent-sync.json` by `agent_sync.py setup`; never edited by hand) lists
  the guarded files and the gate. Run `agent_sync.py acquire <file>` before editing one and
  `agent_sync.py release <file>` after, on every path including failure. The lease is a ref under
  `refs/agent-sync/leases/` on `origin`, so another contributor's agent sees it
  (`git ls-remote origin 'refs/agent-sync/leases/*'`); the record plane is local (`fs`), and
  `.agent-sync/` is git-ignored. No register here carries a "Next free ID" line, so nothing is
  reserved yet; a register that gains one is declared under `idRegisters` and taken with
  `agent_sync.py reserve <REG>`.

## Organisation

This repository is one of the `passioncode-ai` repositories. **The org map lives in
[passioncode-ai/org-index](https://github.com/passioncode-ai/org-index)** (private; readable by
every org member): [which repository owns what](https://github.com/passioncode-ai/org-index#repositories)
and [ONBOARDING.md](https://github.com/passioncode-ai/org-index/blob/main/ONBOARDING.md). The
shared rules are the knowledge base's
[rules.md](https://github.com/passioncode-ai/fabric-workspace/blob/main/knowledge/rules.md).
Where this file is stricter, this file wins. A change to this repository's role, dependencies or
test command updates its row in `org-index/repositories.json` in the same change.

## Shared backlog

[docs/backlog-sources.json](docs/backlog-sources.json) declares this repository's canonical
local task sources and their vision goals. The [common backlog contract](https://github.com/passioncode-ai/fabric-workspace/blob/main/knowledge/backlog.md)
owns aggregation; [the workspace backlog](https://wiki.passioncode.ai/backlog) is a derived view.
Edit a task only in its canonical source under an agent-sync lease, retain stable IDs and
closure receipts, and declare any new source in the manifest. Do not edit generated task
status in the workspace or copy another repository's task into a second editable row.
Land the source change, then run `node scripts/workspace.mjs sync` from a Fabric checkout
(or use the scheduled sync); check the published source commit before calling it current.

## After work

In the same run: update this repository's docs with the change; if a cross-repository fact changed
(a product, a version, a plan row, a principle), update the page in `fabric-workspace/knowledge/`
that owns it; land both; publish (`node scripts/workspace.mjs sync` from a Fabric checkout) or
leave it to the scheduled sync. Leave a handoff with the exact next task.
