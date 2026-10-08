# ADR-0002: Contract naming and versioning rules

- **Status:** Proposed — needs the maintainer's acceptance to close the Phase 0 deliverable
- **Date:** 2026-10-08
- **Layer:** contract tooling

## Context

Phase 0 requires "contract naming/versioning rules" (Contract Program §25). Gate P1 requires every
Foundation invariant to have a stable ID. The Contract Program's only example ID is `CF-AUTH-001`
(§6.1) and its claim example is `EXT-AUTH-0042` (§2.4).

## Decision (proposed)

**Invariant IDs** — `CF-<DIMENSION>-<NNN>`.

| Code | Dimension | Code | Dimension |
|---|---|---|---|
| AUTH | authority | FED | federation |
| IDEN | identity & representation | ORG | organization |
| INFO | information & disclosure | RES | resources |
| EFF | effects | SIM | simulation |
| EVID | evidence & verification | SEC | security enforcement |
| EXT | extension & capability | TCB | trusted computing base |
| WORK | durable work & continuity | CHG | change & evolution |

New dimension codes are added by amending this ADR. IDs are **never reused or renumbered**; a
retired invariant keeps its ID with a superseded status.

**Claim IDs** — `EXT-<AREA>-<NNNN>`, one file per claim at `research/claims/<claim_id>.yaml`.

**Contract families** — one directory per family under `contracts/`, using the names in Contract
Program §5 (`constitution`, `semantics`, `referents`, `protocol`, `identity`, `authority`,
`information`, `work`, `execution`, `effects`, `evidence`, `resources`, `organization`,
`extension`, `federation`, `simulation`, `change`). A directory is created when its first contract
lands, not before.

**Versioning** — each schema carries an `$id`. A change that can reject a previously valid record,
or that changes a field's meaning, is breaking: it gets a new schema file with a version suffix
(`…-v2.schema.json`) and the old one stays until every record migrates. Additive optional fields are
non-breaking. Compatibility is multidimensional (§8.6); this rule covers only syntactic validation.

## Contracts and invariants touched

The 22 seed records in `contracts/constitution/invariants.yaml` use these codes. Accepting this ADR
makes those IDs stable.

## Consequences

IDs carry their dimension, which makes the registry readable but means an invariant that later
proves cross-dimensional keeps a single-dimension prefix. That is accepted: the ID is a name, not a
classification — `applies_to` carries the real scope.

## Alternatives considered

- **Flat numbering (`CF-001` … `CF-022`) following Foundation §28 order** — simplest, but the
  Contract Program's own example already uses a dimension prefix.
