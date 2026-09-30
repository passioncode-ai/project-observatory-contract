# Working in project-observatory-contract

## Read first

1. The PassionCode.ai knowledge base — `fabric-workspace/knowledge/` in your clone (org-index
   `scripts/clone_all.sh` makes it) or https://wiki.passioncode.ai/knowledge — at least its
   [README](https://github.com/passioncode-ai/fabric-workspace/blob/main/knowledge/README.md),
   vision, principles and how-to-work.
2. This file, then the organization's
   [CONTRIBUTING.md](https://github.com/passioncode-ai/.github/blob/main/CONTRIBUTING.md).

## What this repository is

Project Observatory Contract: the public Fabric contract surface of Project Observatory — the
JSON Schemas, admission fixtures and probe assertions a Fabric host compiles and runs before any
credential or project data is exchanged, published under immutable `rev-N` tags (`README.md`).
It declares against the Fabric Agent Contract `0.1.0` (a private repository; do not link it from
public files).

## Commands

| What | Command |
|---|---|
| Install | `python3 -m pip install jsonschema` (the gate's only dependency) |
| Test (the gate) | `python3 scripts/check.py` — every schema a valid JSON Schema, every fixture valid against its capability's input schema; exit 0 green, 1 on a finding, 2 not run |
| Build | none — nothing is built |
| MCP (register + proving call) | none of its own; Project Observatory's server answers these capabilities by name — its README's *Quick start for a new teammate* |

There is no hosted CI. The source repository's publisher also fetches every published URI
anonymously and compares the bytes with its source (`README.md`), so a stale publication fails
that repository's gate as well.

## Where things live

| Path | What a host does with it | Written by |
|---|---|---|
| `schemas/*.schema.json` | validates the input and output of each capability | the publisher |
| `fixtures/*.json` | bounded, non-publishing admission probes | the publisher |
| `probes/assertions.md` | what each probe asserts, in prose | the publisher |
| `README.md` | what the contract is, the quick start, the licence | the publisher's `README` template, corrected here |
| `LICENSE`, `COMMERCIAL-LICENSE.md`, `CLA.md`, `SECURITY.md`, `AGENTS.md`, `CLAUDE.md`, `scripts/`, `docs/` | this repository's own files | this repository |

Do not edit the publisher's files here: the next publication overwrites them. `README.md` was
corrected here on 2026-09-29 (no private links, a License section) and on 2026-09-30 (the
organization's repository standard and the AGPL-3.0 licence, Fabric ADR-0092); **the publisher's
`README` template must carry the same text before its next `--publish`, or that publication
reverts it** ([handoff](docs/handoffs/2026-09-30-standard-agpl.md)). The implementation's provider
manifest stays out of this repository (`README.md`).

## Local rules

- A `rev-N` tag is never moved or repointed. A changed schema is a new provider revision and a new
  tag (`README.md`).
- This repository is public. Nothing private may be added: no machine paths, no credentials, no
  content from private repositories.
- Licence: `AGPL-3.0-only OR LicenseRef-PassionCode-Commercial` since 2026-09-30 (Fabric
  ADR-0092). The files as of `0c79d1c` stay available under MIT, and the open question whether the
  schemas should be a permissive exception is the knowledge base's CO-KB-02, not decided here.
- Land: a PR, squash-merged or fast-forwarded after `python3 scripts/check.py` exits 0.

## Organisation

This repository is one of the `passioncode-ai` repositories. **The org map lives in
[passioncode-ai/org-index](https://github.com/passioncode-ai/org-index)** (private; readable by
every org member): [which repository owns what](https://github.com/passioncode-ai/org-index#repositories)
and [ONBOARDING.md](https://github.com/passioncode-ai/org-index/blob/main/ONBOARDING.md). The
shared rules are the knowledge base's
[rules.md](https://github.com/passioncode-ai/fabric-workspace/blob/main/knowledge/rules.md).
Where this file is stricter, this file wins. A change to this repository's role, dependencies or
test command updates its row in `org-index/repositories.json` in the same change.

## After work

In the same run: update this repository's docs with the change; if a cross-repository fact changed
(a product, a version, a plan row, a principle), update the page in `fabric-workspace/knowledge/`
that owns it; land both; publish (`node scripts/workspace.mjs sync` from a Fabric checkout) or
leave it to the scheduled sync. Leave a handoff with the exact next task.
