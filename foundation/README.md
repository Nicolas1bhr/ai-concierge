# Foundation

The Foundation interprets the [Canon](../canon/) as institutional law: dimensions, invariants and
architectural semantics. It may not silently redefine the Canon.

| Document | Version | Status |
|---|---|---|
| [CONCIERGE_FOUNDATION_UNBOUNDED_INSTITUTIONAL_SUBSTRATE_v0.2.md](CONCIERGE_FOUNDATION_UNBOUNDED_INSTITUTIONAL_SUBSTRATE_v0.2.md) | 0.2 | **Current** — architectural foundation candidate |
| [superseded/CONCIERGE_FOUNDATION_ARCHITECTURE_v0.1.md](superseded/CONCIERGE_FOUNDATION_ARCHITECTURE_v0.1.md) | 0.1 | Superseded where v0.2 explicitly changes or generalizes it |

Both are pinned by hash in [`PINS.yaml`](../PINS.yaml).

## Supersession map v0.1 → v0.2

Source: Foundation v0.2 §36 and Contract Program v0.1 §1.2. This table summarizes; the documents govern.

| v0.1 position | v0.2 outcome |
|---|---|
| Seven "permanent primitives" (Principal, Resource, Work, Authority, Effect, Evidence, Event) as the complete ontology | **Retained as concepts, no longer the complete ontology.** They sit among orthogonal dimensions; new dimensions may be admitted through constitutional evolution. |
| "First express everything through seven primitives" | **Replaced.** Try existing dimensions and projections first without distortion; if a capability does not fit, use the governed new-dimension admission process. |
| "Foundation remains comparatively small" | **Rejected as an objective.** The trusted enforcement base stays small; the substrate's expressive dimensionality may expand without predetermined bound. |
| Physical implementation plan (modular monolith, PostgreSQL, outbox, ExecutionProvider) and build order | **Demoted to an implementation experiment** — a candidate for `profiles/experiments/`, not Foundation law. |
| Subscription-cancellation vertical slice as the scoping slice | **Demoted.** Vertical slices validate; they do not define the semantic horizon. |
| Extension Contract | **Generalized** into the Extension & Capability Protocol (semantics, execution providers, effect adapters, evidence types, verifiers, resources, devices, organizational templates, federation). |
| Institutional Request Channel | **Generalized** into a family of institutional protocol envelopes. A single request socket may be an implementation, not the architecture. |
| Security direction (security reasoning vs. security physics, small TCB, no ambient authority, external control of worker environments, live observation, evidence-backed recovery) | **Preserved and strengthened.** |

Anything in v0.1 not listed above and not contradicted by v0.2 still stands — but where the two
appear to conflict and v0.2 is silent, that is an **open question**, not a choice for code to make
(Contract Program §1.1 rule 9). Record it in [`research/contradictions/OPEN_QUESTIONS.md`](../research/contradictions/OPEN_QUESTIONS.md).
