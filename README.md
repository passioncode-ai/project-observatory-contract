# Project Observatory Contract

Project Observatory Contract preserves the historical revision-4 Fabric contract surface for
[Project Observatory](https://passioncode.ai/observatory/), the PassionCode.ai tool that watches
every project on a machine: the JSON Schemas and admission fixtures a Fabric host must compile
and run **before** any credential or project data is exchanged. It declares Project Observatory
against the Fabric Agent Contract, which is what makes an agent Fabric-compatible; any host that
speaks that contract can use it on its own, without Fabric.

The provider manifest is not published here: it is an installation artefact, required by the
contract to carry a `connection.executableRef` pointing at one machine's executable. It reaches a
host by direct configuration, which the contract's discovery step allows.

| Path | What a host does with it |
|---|---|
| `schemas/capability-*.schema.json` | validates `estate.survey` input and output |
| `schemas/project-detail-*.schema.json` | validates `project.detail` input and output |
| `schemas/project-timeline-*.schema.json` | validates `project.timeline` input and output |
| `schemas/record-*.schema.json` | validates `project.record` input and output |
| `fixtures/*.json` | bounded, non-publishing admission probes |
| `probes/assertions.md` | what each probe asserts, in prose |

## Quick start for a new teammate

**Install.** Nothing to install. Clone the repository, or read one schema at its pinned tag
anonymously:

```bash
git clone https://github.com/passioncode-ai/project-observatory-contract.git
curl -fsSL https://raw.githubusercontent.com/passioncode-ai/project-observatory-contract/rev-4/schemas/capability-input.schema.json
```

**Configure.** No keys and no settings.

**MCP.** This repository is schemas, not a server, so it has no MCP registration of its own.
Project Observatory's MCP server answers these capabilities under their own names
(`estate.survey`, `project.detail`, `project.timeline`, `project.record`); register it and make
the proving call from
[Project Observatory's quick start](https://github.com/passioncode-ai/project-observatory-dashboard#quick-start-for-a-new-teammate).

**Develop.** The gate checks that every schema is a valid JSON Schema and that every fixture
validates against the input schema of its capability:

```bash
python3 -m pip install jsonschema
python3 scripts/check.py        # exit 0 green, 1 on a finding
```

## Current and historical contracts

The `rev-N` tags here are immutable historical provider contracts. Preserve their schemas,
fixtures and identifiers for consumers that pinned them; this documentation change creates
no new revision and does not move a tag.

Current Project Observatory releases carry their own schemas and fixtures in
[`observatory/engine/fabric/`](https://github.com/passioncode-ai/project-observatory-dashboard/tree/main/observatory/engine/fabric).
Use the release and per-file pins in the engine's
[`fabric-contract.lock.json`](https://github.com/passioncode-ai/project-observatory-dashboard/blob/main/observatory/engine/fabric-contract.lock.json).
The engine's publication checker verifies those release-pinned bytes. Its `--stage` and
`--publish` operations are refused; it no longer overwrites this repository's README.
Evidence: [`test_publish_contract.py`](https://github.com/passioncode-ai/project-observatory-dashboard/blob/main/observatory/engine/tests/test_publish_contract.py).

The normative [Fabric Agent Contract](https://github.com/passioncode-ai/fabric-agent-contract)
is public. This historical surface declares contract version `0.1.0`; the installed engine's
manifest and lock, not this repository's old provider revision, describe its current surface.

## License

Open source under the [GNU AGPL-3.0](LICENSE). A [commercial license](COMMERCIAL-LICENSE.md) is
available for use that does not meet the AGPL's terms — contact@passioncode.ai.
The files as of commit `0c79d1c` (the schemas of provider revision 4) were released under the MIT
License and remain available under it; the tags `rev-2` to `rev-4` carry no licence file.
Contributions are accepted under the [CLA](CLA.md).
