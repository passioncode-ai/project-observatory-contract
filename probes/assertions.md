# Admission probe assertions

**What a host is promised, in prose, beside the machine-readable manifest.** Every
line under a probe below is copied from `fabric-agent.json` and
`tools/check_docs.py` fails if one drifts — text by text, not by count. That is
the same discipline `tools/run_probes.py` applies to the runner: comparing
counts hides a swapped assertion, and this document exists to be read by someone
who cannot run the probes.

**Four capabilities, six probes.** This file described three probes and one
capability for four days after `project.record` shipped — a published contract
understating what the provider does, which is the failure mode that matters most
in a document a host reads before it trusts anything.

It happened again, one level up, and worse. `estate.survey` declared THREE
required tools under ONE output schema, and two of them could not satisfy it:
measured 2026-09-07, `observatory_project` was rejected with
`'project' was unexpected` and `observatory_timeline` with
`'events', 'projectId', 'since' were unexpected`. A host doing exactly what this
contract tells it — validate the answer against the published schema — would
have rejected two of the three tools it was promised. Neither had a probe, which
is what an unprobed required feature is for. They are their own capabilities
now, each with one tool, its own schemas and its own probe.

No probe publishes, messages, charges, deploys, mutates production, or reads a
credential. Each has an explicit timeout and a side-effect ceiling; a probe
failure is `probe-failed`, and a missing negotiated MCP capability is a
`declaration-invalid` rather than a failed probe.

## `estate.survey` — a read capability, `effect: none`

### P1 — `survey-single-project` (the admission fixture)

One project scope, answered from the registry alone.

- result validates against capability-output.schema.json
- counts.projects == 1 and projects[0].id equals the requested id
- membershipRules has exactly one entry per repository
- evidence is non-empty and every entry resolves to a registry source id
- degraded is present, even when empty
- registry git status and ledger max revision are unchanged after the call

The last of those is the one worth reading twice: a read capability must leave
the git status of the registry and the ledger's maximum revision exactly as it
found them. A survey that writes is not a survey.

### P2 — `survey-rejects-name-inference`

A project scope whose notes name some of an owner's repositories and not others.
This is fixture **T1** from `docs/knowledge-pack.md`, and it is a probe rather
than only a unit test because it is the defect most likely to return as a
well-meaning improvement: an organisation-adoption heuristic once gave one
project thirty-six repositories it had no claim to.

- result validates against capability-output.schema.json
- every repository returned is one the project's notes name or a link verified by hand
- every repository of that owner which is absent is absent because it anchors its own project
- every returned repository is named in a membershipRules entry

> **Corrected 2026-09-07.** This section used to say "an owner that holds twelve"
> and "the other ten do not". The fixture had changed and the prose had not, so a
> host reading this was told about a probe that does not run. The assertions above
> are now copied from the manifest and checked against it.

### P3 — `survey-declares-degradation`

The whole estate, with the event store deliberately unreachable.

- with the event store unreachable the call still returns a typed result
- degraded names the store and its reason
- degraded names each bitbucket workspace whose listing was not read, carrying the collector's own reason; it is silent when every workspace was listed
- repositories known only from a local remote carry discoveredBy=local-remote-only

> **Corrected twice.** It first asserted that removing the GitHub token would make
> `degraded` name GitHub — that token gates the *collector*, not this capability,
> which reads the registry, so the assertion could never have run. It then
> asserted a fixed sentence about sixteen Bitbucket repositories; `survey.py`
> removed that string on the grounds that **a degradation notice which cannot stop
> being true is not a measurement**, and the notice is now read from the
> collector's own reason. A probe that cannot be executed as written is a false
> declaration, and declaring it is worse than having one probe fewer.

## `project.detail` — a read capability, `effect: none`

### P4 — `detail-carries-every-section`

One real project, asked for in full: identity and membership, the weekly activity
series, the latest value of every plugin metric, the conclusions drawn about it,
and the findings open against it or its repositories.

- result validates against project-detail-output.schema.json
- the requested project is the one returned
- every section is present, so an empty one means measured-and-empty
- a note carries the state that qualifies it, never a bare sentence
- a finding says whether it is about the project or one of its repositories
- registry git status and ledger max revision are unchanged after the call

**Why the third matters to a host.** An absent section and an empty one are
different claims: `measurements: []` says the plugins measured nothing for this
project, while a missing key would say this provider cannot answer that question
at all. A renderer must be able to tell "no data" from "no capability", and only
the section's presence carries that.

**Why the fourth is not decoration.** The observatory's automated writer may
only PROPOSE; a conclusion is qualified by its state, and a host that renders
the sentence without it turns a proposal into an assertion — which is the one
thing this provider's whole write discipline exists to prevent.

## `project.timeline` — a read capability, `effect: none`

### P5 — `timeline-answers-in-camel-case-with-parsed-payloads`

The events of one project, newest first, bounded by `limit`.

- result validates against project-timeline-output.schema.json
- every event carries occurredAt, never the store's column name
- the payload is an object, not a JSON string the caller must parse
- the events are newest first
- registry git status and ledger max revision are unchanged after the call

This tool's output was governed by no schema before rev-4, and it handed the
store's own column names — `occurred_at`, `payload_json` — straight to the wire,
with the payload as a JSON string the caller had to parse. Publishing a schema
over that would have made this provider's internal serialisation part of the
contract.

## `project.record` — a write capability, `effect: draft`

### P6 — `record-proposes-and-refuses`

The capability this file omitted entirely. It writes, so the probe's FIRST
assertion is about what it must not touch.

- the probe runs against a scratch store; no row reaches the operator's ledger
- a well-formed write is accepted in state 'proposed', never higher
- a write with no owner is refused before the ledger is touched
- a stale expectedRevision returns RevisionConflict carrying the current revision
- another owner's record cannot be corrected: OwnerRefused
- a registry proposal leaves registry/projects.json byte-identical

Nothing on this surface can promote anything. Every accepted write lands
`proposed` with confidence below 1; promotion is the operator's act at a terminal
or a second independent corroboration, and there is no flag that bypasses either.

## Cross-cutting

- Receipts for every run are in `fabric/probe-receipts.json`, each carrying the
  manifest content hash it was measured against.
- `tools/run_probes.py --check` re-runs every probe and writes nothing, so the
  gate can verify them without dirtying the tree.
- The runner compares assertion **texts** with the manifest and reports
  `declaredButNotEvaluated` and `evaluatedButNotDeclared`. Counting instead would
  have hidden a swapped assertion, which is how this document drifted.
