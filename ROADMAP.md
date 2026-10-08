# Roadmap

The build program is defined in [Contract Program §25](program/CONCIERGE_FOUNDATION_EXECUTABLE_CONTRACT_PROGRAM_v0.1.md).
Each phase ends in a **hard gate**. A phase is not "mostly done": its gate passes or it does not.
This file tracks status only; the program document defines the phases.

| Phase | Name | Status |
|---|---|---|
| **0** | Source and architecture normalization | **In progress** |
| 1 | Constitutional registry and semantic substrate | Not started (registry seeded) |
| 2 | Power, effect, and continuity formal skeleton | Not started |
| 3 | Conformance harness before product runtime | Not started |
| 4 | Minimal Trusted Enforcement Skeleton | Not started |
| 5 | Durable state, information mediation, evidence, recovery | Not started |
| 6 | Execution providers and effect adapters | Not started |
| 7 | First adversarial real vertical slice | Not started |
| 8 | Contrasting vertical slices | Not started |

## Phase 0 — deliverables

| Deliverable | State | Where |
|---|---|---|
| Pinned Canon/Foundation source references | Done | [`PINS.yaml`](PINS.yaml), checked by `tools/check.py` |
| Explicit supersession map v0.1 → v0.2 | Done | [`foundation/README.md`](foundation/README.md) |
| Research claim registry format | Done | [`research/claim-record.schema.json`](research/claim-record.schema.json) |
| Source maturity taxonomy | Done (M0–M8, encoded in the claim schema) | [`research/README.md`](research/README.md) |
| Contradiction / open-question registry | Started | [`research/contradictions/OPEN_QUESTIONS.md`](research/contradictions/OPEN_QUESTIONS.md) |
| Initial research ledger with checked dates | **Open** — Contract Program §3 claims still need converting into dated records | [`research/claims/`](research/claims/) |
| ADR template | Done | [`adr/0000-template.md`](adr/0000-template.md) |
| Contract naming / versioning rules | **Proposed**, awaiting acceptance | [`adr/0002-contract-naming-and-versioning.md`](adr/0002-contract-naming-and-versioning.md) |

### Gate P0 — PASS only if

- [ ] the higher-layer authority hierarchy is unambiguous;
- [ ] no known conflicting Foundation interpretation is silently resolved;
- [ ] every current external fact used by architecture has source/maturity metadata;
- [ ] v0.1 implementation choices are visibly demoted to profile/experiment status.

**DO NOT PROCEED if** a developer or agent can still reasonably confuse "current implementation
choice" with "Foundation law."

## Phase 1 — head start

The machine-readable invariant registry ([`contracts/constitution/invariants.yaml`](contracts/constitution/invariants.yaml))
already holds all 22 Foundation v0.2 §28 invariants with stable IDs, every one at enforceability
`UNKNOWN`. Gate P1 needs each to carry test obligations; `tools/check.py` reports how many still do not.
