# Research ledger

Concierge engineering is only allowed to "know" external facts through dated, classified records
([Contract Program §2](../program/CONCIERGE_FOUNDATION_EXECUTABLE_CONTRACT_PROGRAM_v0.1.md)).
Research can justify a change proposal; **research does not itself change architecture.**

| Path | Contents |
|---|---|
| [`claim-record.schema.json`](claim-record.schema.json) | Atomic research claim record (§2.4) |
| [`claims/`](claims/) | One YAML file per claim, named `<claim_id>.yaml` — validated by `tools/check.py` |
| [`contradictions/OPEN_QUESTIONS.md`](contradictions/OPEN_QUESTIONS.md) | Contradiction and open-question registry (§2.7) |

## Claim classes (§2.1)

`CANON` · `ARCHITECTURAL_LAW` · `DESIGN_CHOICE` · `EXTERNAL_FACT` · `INFERENCE` · `CANDIDATE` · `OPEN_QUESTION`

Every consequential claim also carries a **maturity** (how stable the source is) and an
**adoption status** (what Concierge actually decided). A true fact is not automatically an adoption.

## Source maturity (§2.2)

| Class | Meaning |
|---|---|
| M0 | Canonical stable standard (RFC, W3C Recommendation, …) |
| M1 | Official stable project specification |
| M2 | Official release documentation |
| M3 | Active standard draft |
| M4 | Official experimental or draft feature |
| M5 | Peer-reviewed research |
| M6 | Preprint or early research — never normative by itself |
| M7 | Community security guidance (OWASP, …) |
| M8 | Secondary source — discovery only, never overrides a primary definition |

Maturity is not a quality ranking; it tells reviewers what kind of confidence a source can support.

## Open work

The research delta in Contract Program §3 (MCP, A2A, OAuth 2.1, Transaction Tokens, SPIFFE, policy
engines, schema evolution, WASI, attestation, transparency receipts, agent-security guidance — as of
2026-09-28) still needs converting into claim records **with re-checked dates**. That is the
remaining Phase 0 deliverable.
