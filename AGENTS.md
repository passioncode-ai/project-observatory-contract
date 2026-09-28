# project-observatory-contract — working in this repository

## Role

This is the public contract surface of Project Observatory for Fabric hosts. It holds the JSON
Schemas, the admission fixtures and the probe assertions that a host compiles and runs before any
credential or project data is exchanged. Everything is published under immutable `rev-N` tags.
Source: `README.md`. It declares against
[fabric-agent-contract](https://github.com/passioncode-ai/fabric-agent-contract) `0.1.0`.

## Build and test

There is no build, test or CI in this repository. Its files are published from the private
Project Observatory source. The source repository's publisher fetches every URI anonymously and
compares the bytes with its source (`README.md`), so a stale publication fails that repository's
gate, not this one.

## Where things live

| Path | What a host does with it |
|---|---|
| `schemas/*.schema.json` | validates the input and output of each capability |
| `fixtures/*.json` | bounded, non-publishing admission probes |
| `probes/assertions.md` | what each probe asserts, in prose |

`schemas/`, `fixtures/`, `probes/` and `README.md` are written by the publisher. Do not edit them
here: the next publication overwrites them. The implementation and its provider manifest stay
private (`README.md`).

## Rules in this repository

- A `rev-N` tag is never moved or repointed. A changed schema is a new provider revision and a new
  tag (`README.md`).
- This repository is public. Nothing private may be added: no machine paths, no credentials, no
  content from private repositories.

## Organisation

This repository is one of the `passioncode-ai` repositories. **The org map, the shared
rules and onboarding live in [passioncode-ai/org-index](https://github.com/passioncode-ai/org-index)**
(private; readable by every org member):

- [README](https://github.com/passioncode-ai/org-index#repositories): which repository owns what, and how they connect
- [RULES.md](https://github.com/passioncode-ai/org-index/blob/main/RULES.md): branches, commits, CI, leases, secrets, handoffs
- [ONBOARDING.md](https://github.com/passioncode-ai/org-index/blob/main/ONBOARDING.md): setting up a new contributor's machine

Where this file is stricter than RULES.md, this file wins. A change to this repository's
role, dependencies or test command updates its row in `org-index/repositories.json` in the same change.
