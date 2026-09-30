# Security

Report a vulnerability privately through this repository's
[private vulnerability reporting](https://github.com/passioncode-ai/project-observatory-contract/security/advisories/new),
or by email to contact@passioncode.ai. Do not open a public issue containing a credential,
a machine path or project data.

## What this repository is

JSON Schemas, admission fixtures and probe assertions, and nothing that runs. A schema flaw
that would let a host admit a provider it should refuse — a missing `required`, an
`additionalProperties` left open, a probe that could publish or read a credential — is a
security report. The provider that answers these capabilities is Project Observatory; report
its issues in [its repository](https://github.com/passioncode-ai/project-observatory-dashboard/security).
