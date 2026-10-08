# Concierge Foundation — Unbounded Institutional Substrate

**Version:** 0.2  
**Status:** Architectural foundation candidate; research-grounded, not implementation freeze  
**Date:** 2026-09-27  
**Supersedes:** `CONCIERGE_FOUNDATION_ARCHITECTURE(1).md` where this document explicitly changes or generalizes it  
**Subordinate to:** `AI_CONCIERGE_CANONICAL_PRODUCT_CONCEPT(9).md`  
**Scope:** The permanent institutional substrate beneath arbitrarily capable present and future intelligences, including identity, authority, information, causality, work, execution, effects, evidence, security, organizational composition, evolution, federation, recovery, and semantic extensibility.

---

# 0. Why this document exists

The previous Foundation established the correct central direction:

> **Intelligence may remain open-ended. Authority must remain explicit.**

and:

> **Agents are replaceable computation. The institution owns state, authority and effects.**

Those principles remain.

The previous draft also contained a dangerous simplification: it increasingly treated a small set of concepts — `Principal`, `Resource`, `Work`, `Authority`, `Effect`, `Evidence`, `Event` — as though they might form the complete permanent ontology of the institution.

That is too aggressive a collapse.

Those concepts are useful **institutional questions**. They are not necessarily the only semantic dimensions reality will ever require.

Likewise, “keep the Foundation small” is an insufficient objective. The correct objective is:

> **Keep the irreducible trusted enforcement base small; keep the institutional substrate coherent; allow the substrate's expressive dimensionality to expand without predetermined bound.**

The Foundation must not become a sandy island that future capabilities must escape in order to grow.

It must instead become the **physics of an expandable institution**.

---

# 1. Epistemic discipline of this architecture

This project sits in a fast-moving area where current model training is not an adequate source of truth. The document therefore distinguishes design from evidence explicitly.

## 1.1 Claim classes

Every nontrivial assertion should belong to one of these classes:

**CANON** — required by the product concept.  
**ARCHITECTURAL LAW** — a proposed permanent Concierge rule.  
**DESIGN CHOICE** — a current architectural preference that remains replaceable.  
**EXTERNAL FACT** — a factual claim about an external standard, system, protocol, implementation, or research result; must be traceable to a source.  
**INFERENCE** — a conclusion derived from evidence or design constraints, but not directly stated by a source.  
**CANDIDATE** — a technology or mechanism worth evaluating, not adopted as Foundation truth.  
**OPEN QUESTION** — unresolved and deliberately not invented away.

A future architecture process SHOULD preserve these distinctions in ADRs, schemas, comments, and design reviews.

## 1.2 Research snapshot

External facts in this document were checked against primary or project-maintained sources available on **2026-09-27**. A source ledger appears near the end.

The purpose of external research is not to cargo-cult contemporary systems. It is to identify:

- properties already demonstrated in real systems,
- boundaries where standards deliberately stop,
- failure modes known to existing designs,
- useful abstractions that survive technology replacement,
- and areas where no sufficiently general existing answer exists.

## 1.3 No hallucinated closure

When the architecture does not know, it MUST preserve the unknown.

Examples:

- We do not know the dominant agent runtime of 2030.
- We do not know the future semantics of AI-to-AI negotiation.
- We do not know whether a single authorization language will remain suitable across every effect surface.
- We do not know whether future trusted execution will be VM-, capability-hardware-, confidential-compute-, process-, or hardware-partition based.
- We do not know which data-governance model will prove practical for arbitrary derived information.
- We do not know whether all future agent cognition will resemble current LLM agents at all.

The Foundation must encode interfaces, invariants, proof obligations, and replaceability — not fictional certainty.

---

# 2. The architectural objective

The Concierge is a persistent institution capable of hosting increasingly capable intelligence without requiring that intelligence to become the institution itself.

The Foundation must support capabilities that may later include:

- current and future LLMs,
- non-LLM reasoning systems,
- algorithmic planners,
- self-written programs,
- dynamically constructed agent organizations,
- terminal and computer operators,
- human operators,
- remote services,
- autonomous devices and robots,
- confidential execution environments,
- offline workers,
- foreign Concierge compounds,
- new communication protocols,
- new financial protocols,
- new sensor modalities,
- new forms of memory,
- new organizational structures,
- new kinds of scarce resources,
- and capabilities not meaningfully describable using today's concept of an “agent.”

The architecture succeeds if these can be incorporated without bypassing institutional law and without requiring a constitutional rewrite merely because a new dimension appears.

---

# 3. Three strata — never collapse them again

The system has three fundamentally different strata.

## 3.1 Open-ended cognition

This is the space in which intelligence thinks and creates.

It may:

- reason,
- plan,
- hypothesize,
- research,
- write code,
- build tools,
- simulate,
- spawn subordinate cognition,
- invent protocols,
- optimize itself,
- build organizational structures,
- and discover previously unknown methods.

Cognition is not the security boundary.

A prompt telling an agent not to do something is not equivalent to preventing an effect.

## 3.2 Institutional substrate

This is the rich operating system of the institution.

It models and coordinates:

- reality,
- identities,
- representation,
- authority,
- policy,
- information,
- provenance,
- time,
- causality,
- work,
- commitments,
- organization,
- resources,
- execution,
- effects,
- evidence,
- verification,
- security,
- evolution,
- federation,
- recovery,
- and institutional continuity.

This layer MAY be broad and expressive.

Its job is not to be tiny. Its job is to remain internally coherent, composable, evolvable, and independently enforceable where required.

## 3.3 Trusted enforcement substrate / TCB

This is the part whose compromise can invalidate core security claims.

It SHOULD be as small, reviewable, replaceable, isolated, and mechanically testable as practical.

Potential TCB responsibilities include only mechanisms that genuinely must be trusted, such as:

- root institutional identity and key custody,
- issuance and validation of workload identity,
- authoritative grant storage or verification,
- hard policy enforcement boundaries,
- secret release/injection,
- execution isolation control,
- durable-state mutation gates,
- evidence integrity mechanisms,
- revocation/quarantine primitives,
- and cryptographic federation roots.

The full institutional substrate does **not** automatically belong to the TCB.

A planner can be wrong without being able to counterfeit authority.

A context-ranking service can be compromised without being able to mint root credentials.

A department manager can be malicious without owning the user's bank key.

This separation is foundational.

---

# 4. The anti-collapse doctrine

The Foundation MUST actively defend against semantic collapse.

A concept may participate in several institutional dimensions at once. Those dimensions are not therefore the same thing.

## 4.1 Identity is not authority

Knowing *who* something is does not imply what it may do.

## 4.2 Authentication is not trust

Cryptographically proving a foreign compound's identity does not imply believing its claims or granting it local authority.

## 4.3 Trust is not delegation

Believing an entity is reputable does not mean it may act for the user.

## 4.4 Policy is not authority

A policy may constrain or derive authorization decisions. It is not itself necessarily the grant from which delegated power originates.

## 4.5 Credential is not authority

A token, certificate, session, key, or browser cookie is an instrument for exercising or proving some authority. Possession does not define the legitimate scope by itself.

## 4.6 Approval is not authority architecture

User approval can be evidence supporting an authority transition. Repeated approval prompts are not a substitute for a coherent delegation model.

## 4.7 Work is not execution

An objective may exist for months while every worker is dead.

## 4.8 Task is not action

A task is institutional work. An action is an attempt to do something.

## 4.9 Action is not effect

A process may execute an action without altering the world. An effect is a boundary-crossing consequence or attempted consequence.

## 4.10 Effect is not outcome

“Clicked cancel” is not “subscription cancelled.”

## 4.11 Outcome is not evidence

A believed outcome may exist with weak evidence. Evidence is what supports the claim.

## 4.12 Evidence is not truth

Evidence can be forged, stale, ambiguous, incomplete, contradictory, or misinterpreted.

## 4.13 Observation is not belief

An email saying “refund issued” is an observation, not proof of settlement.

## 4.14 Belief is not canon

A reconciled interpretation of the world cannot rewrite constitutional rules.

## 4.15 Event is not state

An event records something that happened or was observed. State is a projection or interpretation across events and other evidence.

## 4.16 Log is not evidence ledger

Telemetry optimized for operations is not automatically sufficient for nonrepudiation, reconstruction, or high-consequence verification.

## 4.17 World entity is not authorization resource

A bank account is a real-world entity. It may also be an authorization target. Those are different projections.

## 4.18 Information is not context

Information may exist without being exposed to a model. Context is a scoped presentation assembled for a particular computation and purpose.

## 4.19 Secret is not information context

A model often needs the capability enabled by a secret, not the secret value itself.

## 4.20 Sandbox is not trust domain

Two workloads may run in the same virtualization technology while belonging to different authority domains.

## 4.21 Trust domain is not tenant

A tenant is a hosting/administrative concept. A cryptographic or institutional sovereignty boundary may cut differently.

## 4.22 Department is not service topology

An organizational unit does not imply a database, cluster, queue, model process, or network segment.

## 4.23 Extension is not plugin

An extension may introduce a semantic type, policy vocabulary, execution provider, device driver, effect adapter, observation source, verifier, or entirely new institutional capability. “Plugin” is too narrow.

## 4.24 Federation is not shared state

Compounds may cooperate without merging world models, secrets, policy roots, or authority graphs.

## 4.25 Resource budget is not authorization

Having €500 available does not imply permission to spend it; being permitted to spend does not imply budget exists.

## 4.26 Security reasoning is not security physics

An AI can detect risk. Enforcement must still occur at a boundary capable of actually preventing or containing the effect.

---

# 5. Stable referents, orthogonal projections

The architecture needs a way to refer to the same thing across multiple institutional dimensions without pretending those dimensions are a universal inheritance tree.

## 5.1 Stable referent

A **Referent** is an institutional identifier for something the system needs to talk about consistently.

A referent does not define what the thing *is* in every semantic system.

Example:

```text
ref:acct:bank:primary-checking
```

may participate simultaneously as:

```text
World projection:
    FinancialAccount

Identity/representation projection:
    Account owned by user

Authority projection:
    Target of bank.read / bank.transfer

Information projection:
    Source of balance and transaction data

Resource/economy projection:
    Monetary inventory

Execution projection:
    External API/browser account

Effect projection:
    Settlement surface

Security projection:
    High-consequence / financial / authentication-sensitive
```

None of these projections owns the meaning of all the others.

## 5.2 A projection is not a copy

Multiple projections SHOULD point to the same referent where they concern the same underlying thing.

The Foundation SHOULD avoid duplicating “bank account as resource,” “bank account as entity,” and “bank account as system” into unrelated records with no shared identity.

## 5.3 A referent is not necessarily an ontology primitive

Referents solve cross-system identity.

They do not imply that every concept must be materialized as one global object.

Some facts may remain domain-local, ephemeral, computed, or unmaterialized.

## 5.4 Referential ambiguity must be explicit

The system MUST support:

- uncertain identity,
- possible equivalence,
- known aliases,
- merges,
- splits,
- supersession,
- and contested identity.

Two records that may refer to the same person are not automatically merged because a model thinks they look similar.

---

## 5.5 Mapping back to the Canon

This Foundation does **not** delete the Canon's primitives. It prevents them from being mistaken for one closed universal type hierarchy.

A non-exhaustive mapping is:

| Canon concept | Primary dimension(s) | Important non-collapse note |
|---|---|---|
| Entity | World / referential | An entity may also be an authorization target, information source, device, or resource without those becoming the same semantic type. |
| Relationship | World / organization / authority | Social relationships, authorization relationships, and provenance edges are different relation families. |
| Event | Causal / temporal | Not equivalent to observation, evidence, effect, or current state. |
| Observation | World / evidence | Evidence about reality, not automatically reconciled belief. |
| Belief | World | An interpretation with provenance/confidence, not canon. |
| Unknown | World / work / evidence | First-class unresolved state, not null/absence. |
| Commitment | Work / causal / social | Durable obligation, not merely a task. |
| Objective | Work | Desired outcome, not plan or execution. |
| Responsibility | Work / organization | Ongoing delegated management scope, not automatically authority. |
| Jurisdiction | Work / authority | Area of expected proactive management; authority still derives explicitly. |
| Policy | Authority / constitution | Rule material, not identity, credential, or grant. |
| Preference | World/user model | Soft guidance, not hard policy. |
| Task | Work | Concrete work unit, not process or effect. |
| Action | Work/execution | Attempted operation, not guaranteed external effect. |
| Decision | Work/authority | Choice requiring resolution, not automatically approval token. |
| Receipt | Evidence/effect | Evidence of an operation or counterparty response, not guaranteed outcome. |
| Expected state | World/work/effect | Target condition used for verification. |
| Exception | Reconciliation/security/work | Divergence, not one generic error class. |
| Resource | Resource/economy and domain projections | Scarce capacity is distinct from an authorization target that a policy engine may also call a “resource.” |

This mapping is intentionally many-to-many.

The Canon remains product truth. The Foundation supplies the institutional physics that allow those concepts to coexist without semantic flattening.

# 6. The orthogonal institutional dimensions

These are **logical dimensions**, not a microservice diagram.

A deployment MAY combine many dimensions in one process or database. Separation becomes physical only when justified by security, failure containment, performance, scale, or independent lifecycle.

The initial set is intentionally broad but not declared metaphysically complete.

---

## 6A. World / reality dimension

Purpose: represent relevant reality without confusing observations, interpretations, and intentions.

Core concepts include:

- referent,
- entity projection,
- relationship,
- observation,
- belief,
- unknown,
- desired state,
- expected state,
- current-state projection,
- historical state,
- contradiction,
- confidence,
- freshness,
- source lineage.

Laws:

1. Observation MUST NOT silently become belief.
2. Belief MUST NOT silently become fact/canon.
3. Unknown MUST be representable.
4. Conflicting observations MAY coexist until reconciled.
5. Current state SHOULD be reconstructable for consequential domains.
6. Belief updates SHOULD retain why the previous belief changed.

Extensibility:

New entity types and relationship types MAY be introduced through the semantic registry without changing authority or execution semantics.

---

## 6B. Identity / representation dimension

Purpose: answer **who or what is acting, who is represented, and how that claim is established**.

Separate concepts:

- institutional principal,
- human identity,
- compound identity,
- workload identity,
- device identity,
- service identity,
- external principal,
- pseudonymous identity,
- organizational identity,
- credential,
- authenticated session,
- representation mode,
- acting-for relationship,
- delegation subject,
- identity assurance,
- identity provenance.

Representation examples:

```text
as_user
for_user
as_disclosed_assistant
as_concierge
for_organization
as_human_operator_for_concierge
as_foreign_compound
```

Laws:

1. Identity MUST remain distinct from authority.
2. Representation MUST be explicit for consequential external interactions.
3. Authentication strength SHOULD be available to authorization decisions.
4. Long-lived root identity material MUST NOT be exposed to ordinary cognition.
5. Workloads SHOULD receive short-lived identities where feasible.
6. Identity federation authenticates foreign identities; it does not automatically authorize them.

Evidence:

SPIFFE demonstrates portable workload identity, short-lived workload credentials, separate trust domains, and explicit federation across administratively independent domains. This is evidence for the model, not a permanent dependency. `[SRC-01, SRC-02, SRC-03]`

---

## 6C. Intent / work dimension

Purpose: represent **why institutional activity exists** independently of whichever worker happens to execute it.

Do not flatten these:

- objective,
- responsibility,
- jurisdiction,
- commitment,
- decision,
- plan,
- task,
- subtask,
- wait condition,
- dependency,
- attempt,
- escalation,
- completion criterion,
- abandonment/supersession.

A work object SHOULD be durable when its meaning outlives a computation.

Example:

```text
Objective:
    Ensure insurer reimburses €420

Commitment:
    Concierge promised user to follow through

Task:
    Submit reimbursement request

Attempt:
    Browser execution 782

Effect:
    Form submission

Expected state:
    Claim acknowledged

Wait condition:
    Insurer response or 7-day timeout
```

Laws:

1. Worker death MUST NOT imply work death.
2. Work SHOULD retain ownership and authority lineage.
3. Work MAY be re-planned without changing the objective.
4. A plan is advisory state unless explicitly promoted.
5. Completion MUST be tied to objective/commitment criteria, not merely worker self-report.

---

## 6D. Authority / policy dimension

Purpose: determine **what may be done, by whom, for what work, against what target, under which constraints, and with what enforceability**.

The Foundation MUST NOT force all authorization into one paradigm.

Relationship-based, attribute-based, policy-rule, capability/attenuation, discretionary, workflow/approval, risk-based, and cryptographic mechanisms solve overlapping but non-identical problems.

The institutional authority model therefore has a stable request contract with replaceable evaluation mechanisms.

Canonical authorization request conceptually includes:

```text
subject / acting principal
representation
requested operation
referenced targets
work / purpose
parent authority lineage
requested information classes
requested resource consumption
requested environment privilege
current context
assurance posture
consequence description
```

Decision conceptually includes:

```text
allow | deny | require_step_up | require_review | indeterminate
constraints
obligations
required enforcement points
required assurance
expiry / lease
reason codes
policy version(s)
decision evidence reference
```

### Authority grants

A grant is an attributable authorization object, not merely a policy result.

A grant MAY constrain independent dimensions such as:

- operations,
- referents/targets,
- information classes,
- disclosure classes,
- representation modes,
- monetary limits,
- resource limits,
- time windows,
- geographic/device constraints,
- execution environment classes,
- delegation depth,
- audience,
- external counterparties,
- reversibility requirements,
- verification requirements,
- assurance requirements.

### Attenuation law

Delegation MUST NOT increase effective authority without a distinct upstream authority transition.

For every constrained dimension where a partial order exists:

```text
child <= parent
```

If safe subset/attenuation cannot be established mechanically, the system MUST NOT pretend it can. It may require a new grant decision instead.

### Policy engines

Cedar and OPA demonstrate useful contemporary patterns:

- `principal/action/resource/context` structured requests,
- policy validation,
- decoupling policy decision from application enforcement,
- local/distributed policy evaluation,
- signed policy bundles.

These are candidate implementation mechanisms, not Foundation semantics. `[SRC-04, SRC-05, SRC-06, SRC-07]`

### Relationship authorization

Zanzibar/OpenFGA demonstrate that very large authorization graphs can be expressed as relationships, with conditional/contextual extensions in modern implementations. The Foundation SHOULD be capable of using relationship graphs without assuming every authorization question reduces to graph reachability. `[SRC-08, SRC-09, SRC-10]`

### Capability attenuation

Biscuit demonstrates practical cryptographically protected authorization material that can be attenuated through appended blocks. The Foundation SHOULD preserve attenuation as a property even if the initial implementation uses server-authoritative grants. `[SRC-11]`

---

## 6E. Information / provenance dimension

Purpose: control and explain **what information exists, where it came from, what transformations produced it, what may be revealed, and under what purpose**.

Information objects SHOULD be able to carry or derive:

- source,
- producer,
- ownership/custodianship,
- provenance edges,
- freshness,
- confidence,
- trust class,
- sensitivity class,
- subject(s),
- jurisdictional tags,
- permitted disclosure,
- retention,
- expiry,
- transformation lineage,
- integrity evidence,
- redaction state,
- aggregation state,
- declassification authority,
- purpose constraints where enforceable,
- and references to originals.

### Information is not one blob

The model SHOULD distinguish at least:

- raw observation,
- parsed structure,
- assertion,
- derived fact,
- summary,
- embedding/index representation,
- model inference,
- belief,
- secret material,
- public disclosure,
- evidence artifact.

### Derived information

If private data produces a less-sensitive derived result, the result SHOULD retain lineage sufficient to determine whether it can be disclosed.

Example:

```text
Private calendar contents
    ↓ derive
"Nick is available 18:00-20:00"
    ↓ disclose
Foreign concierge receives availability window
```

The availability result is not equivalent to the calendar contents.

### No perfect-IFC fiction

The Foundation MUST NOT claim universal information-flow control where real systems cannot enforce it.

Some restrictions may be:

- cryptographically enforced,
- structurally mediated,
- broker enforced,
- process isolated,
- monitored,
- or advisory.

This enforcement strength must be represented.

### Provenance evidence

W3C PROV provides an established model for entities, activities, agents, derivation, attribution, and provenance-of-provenance; OpenLineage demonstrates a modern extensible “core + namespaced facets” approach to runtime data lineage. The Foundation can borrow properties without adopting either ontology wholesale. `[SRC-12, SRC-13, SRC-14]`

---

## 6F. Causal / temporal dimension

Purpose: preserve **when, in what order, because of what, and under which uncertainty** institutional events occurred.

The system needs more than timestamps.

Possible temporal fields:

- observed wall-clock time,
- source-reported time,
- ingestion time,
- monotonic process time where available,
- validity interval,
- not-before / expires-at,
- deadline,
- temporal uncertainty,
- clock source/assurance.

Possible causal edges:

```text
caused_by
derived_from
authorized_by
triggered_by
supersedes
invalidates
compensates
retries
awaits
satisfies
contradicts
forked_from
merged_from
```

Laws:

1. The architecture MUST NOT assume wall-clock timestamps establish causality.
2. External events MAY arrive late or out of order.
3. Duplicate observations MUST be distinguishable from repeated real-world events.
4. Causal lineage for consequential actions SHOULD survive worker and service restarts.
5. A replayed internal event MUST NOT automatically repeat an external effect.
6. Temporal semantics SHOULD survive disconnected/offline execution through explicit uncertainty and reconciliation.

This dimension is essential for long-horizon autonomy, rollback, replay, forensic reconstruction, and federation.

---

## 6G. Execution / environment dimension

Purpose: host computation while externally controlling the resources and effect surfaces available to it.

An **Execution Cell** is a bounded environment profile, not a specific technology.

A cell may describe:

```text
runtime family
isolation mechanism
workload identity
filesystem view
network/egress policy
secret injection channels
persistent mounts
device access
browser/session access
CPU/memory/time budgets
child-execution policy
observability hooks
attestation state
supply-chain provenance
lifetime/destruction policy
```

Possible providers may include:

- pure model inference,
- language runtimes,
- WebAssembly Components,
- OS processes,
- containers,
- application-kernel sandboxes,
- microVMs,
- full VMs,
- confidential VMs/TEEs,
- remote physical machines,
- mobile devices,
- human-operated environments,
- robots/controllers,
- future execution substrates.

### Execution assurance profile

Isolation must not be represented as a single “secure/not secure” bit.

An assurance profile MAY include dimensions such as:

- host-kernel exposure,
- guest-kernel isolation,
- memory isolation,
- hardware root of trust,
- attestation availability,
- network mediation,
- filesystem mediation,
- process introspection coverage,
- secret exposure mechanism,
- persistence authority,
- child-process authority,
- device authority,
- supply-chain verification,
- runtime integrity monitoring,
- side-channel assumptions.

Authority policy MAY depend on these properties.

### Contemporary evidence

WASI 0.3, ratified in June 2026, demonstrates stable typed component interfaces with native async composition. gVisor demonstrates an application-kernel isolation model distinct from both ordinary containers and VMs. seL4 and CHERI/CHERIoT demonstrate that capability enforcement and compartmentalization can exist much lower in the stack than application policy. None of these is mandated. `[SRC-15, SRC-16, SRC-17, SRC-18]`

---

## 6H. Effect / transaction dimension

Purpose: mediate computation attempting to produce consequences outside its local reasoning state.

The Foundation MUST distinguish:

```text
operation intent
execution mechanism
attempt
effect request
authorization
external interaction
receipt
observed outcome
verified outcome
```

### Effect descriptor

Effects are open-ended but can carry orthogonal semantic descriptors, such as:

```text
OBSERVE
DISCLOSE
COMMUNICATE
PERSIST
MUTATE
SPEND
COMMIT
DELEGATE
ADMINISTER
AUTHENTICATE
SIGN
PUBLISH
DELETE
PHYSICAL
TRANSFER_CUSTODY
CREATE_OBLIGATION
```

New effect classes MAY be registered.

Tags are descriptive inputs to authority, security, auditing, and consequence analysis. They are not sufficient enforcement by themselves.

### Effect lifecycle

Conceptually:

```text
proposed
  ↓
qualified / enriched
  ↓
authority decision
  ↓
prepared
  ↓
attempted
  ↓
receipt(s)
  ↓
reconciled
  ↓
verified | failed | partial | unknown | compensated
```

Not every external system supports a prepare/commit transaction. The Foundation MUST model the truth of the external interface rather than pretend distributed ACID exists where it does not.

### Duplicate-sensitive effects

Payments, bookings, messages, destructive operations, commitments, and other non-idempotent actions MUST treat unknown outcomes as a first-class state.

A timeout after attempted execution is not permission to retry blindly.

### Compensation

Rollback MAY be impossible.

The effect model therefore distinguishes:

- reversible,
- compensatable,
- partially compensatable,
- externally irreversible,
- socially irreversible,
- physically irreversible.

---

## 6I. Evidence / claims / verification dimension

Purpose: support accountable statements about what is believed to have occurred.

These concepts MUST remain separate:

**Claim** — proposition asserted by some principal/system.  
**Evidence** — material supporting or contradicting a claim.  
**Receipt** — evidence produced by an operation or counterparty.  
**Attestation** — signed/verifiable statement about properties or events.  
**Proof** — evidence with a specific verification relationship.  
**Observation** — perceived state.  
**Verification** — process that evaluates whether evidence sufficiently supports an expected state.  
**Belief** — reconciled institutional interpretation.

### Evidence quality

Evidence SHOULD carry dimensions such as:

- issuer/observer,
- integrity protection,
- independence,
- freshness,
- directness,
- scope,
- ambiguity,
- reproducibility,
- collection method,
- trust assumptions,
- retention requirements.

### Independent verification

For high-consequence effects, the executor and verifier SHOULD be separable.

Example:

```text
browser worker claims cancellation
    ≠ sufficient

email confirmation arrives
    + account status checked later
    + no subsequent charge
    → stronger verified state
```

### Transparency and provenance

SLSA/in-toto provide contemporary models for signed software provenance; SCITT RFC 9943 provides a general architecture for signed statements registered into transparency services with receipts and auditable history. These are strong evidence that statements, provenance, and transparency can be modeled independently from the artifacts themselves. `[SRC-19, SRC-20, SRC-21, SRC-22]`

---

## 6J. Resource / economy dimension

Purpose: govern scarce capacity independently from permission.

Resource types MUST be extensible.

Examples today:

- money,
- compute,
- model tokens,
- API quotas,
- storage,
- bandwidth,
- battery,
- phone minutes,
- browser capacity,
- human-operator time,
- latency budget,
- wall-clock deadlines,
- user attention,
- risk budget,
- carbon/energy budget,
- device wear,
- external rate limits.

Future resources may not fit this list.

### Resource semantics

A resource definition MAY expose:

```text
unit
inventory / capacity
reservation semantics
renewability
expiry
cost curve
quota windows
priority rules
transferability
borrowability
hard/soft limit
authoritative meter
```

### Distinct questions

```text
Can this work spend €300?          → authority
Is €300 available?                 → resource state
Should €300 be allocated here?     → planning/economy
Was €300 actually spent?           → effect/evidence
```

These MUST not collapse.

---

## 6K. Organizational dimension

Purpose: compose many intelligences into a coherent institution without equating organization with infrastructure.

Organizational structures MAY include:

- manager,
- worker,
- specialist,
- department,
- committee,
- temporary task force,
- shadow organization,
- adversarial reviewer,
- auditor,
- information custodian,
- security authority,
- human operator,
- external contractor,
- foreign compound collaborator,
- machine collective,
- future structures not yet named.

An organizational role MAY define:

- responsibilities,
- routing rules,
- authority templates,
- context profile,
- allowed delegation patterns,
- reporting paths,
- escalation paths,
- verification requirements,
- resource budgets,
- lifecycle policy.

It MUST NOT automatically grant credentials, OS privileges, or broad information access.

### Dynamic organization

The institution MAY create, reshape, duplicate, isolate, merge, or dissolve organizational structures as work demands.

Organizational change itself is institutional work and remains governed by authority and security.

---

## 6L. Security / assurance dimension

Purpose: prevent, contain, detect, investigate, revoke, and recover from compromise without reducing intelligence to a whitelist of safe thoughts.

Security exists across time:

### Before

- identity establishment,
- authority evaluation,
- supply-chain verification,
- environment selection,
- context minimization,
- secret mediation,
- risk/consequence analysis,
- required independent review.

### During

- process/runtime observation,
- egress monitoring,
- network policy,
- filesystem/device mediation,
- secret-use observation,
- privilege-change detection,
- resource controls,
- behavior anomaly detection,
- effect interception,
- emergency termination.

### After

- evidence preservation,
- reconciliation,
- compromise investigation,
- revocation,
- blast-radius analysis,
- rollback/compensation,
- root-cause analysis,
- operational learning,
- policy/capability repair.

### Enforcement strength

Every consequential restriction SHOULD declare the strongest true enforcement class, e.g.:

```text
HARDWARE_ENFORCED
CRYPTOGRAPHIC
KERNEL/HYPERVISOR_ENFORCED
BROKER_ENFORCED
APPLICATION_ENFORCED
MONITORED
ADVISORY
UNKNOWN
```

The names are not constitutional. The principle is.

The system MUST NEVER describe an advisory model instruction as equivalent to hard enforcement.

### Runtime observation

Operational telemetry standards such as OpenTelemetry demonstrate the value of cross-system semantic conventions, while runtime isolation/monitoring systems demonstrate that security observation can occur outside the agent process. Observability remains evidence/input, not authority. `[SRC-23, SRC-24, SRC-25]`

---

## 6M. Evolution / change dimension

Purpose: make institutional evolution itself a governed capability.

This is the most important addition relative to the previous Foundation.

The Concierge will eventually need to modify itself.

It may:

- replace a model,
- add an execution provider,
- install a capability,
- create a connector,
- add a semantic type,
- add a policy vocabulary,
- introduce a verifier,
- change an organizational structure,
- migrate a schema,
- modify routing,
- deploy code,
- add a device type,
- replace a subsystem,
- change its own Foundation implementation,
- or propose a constitutional change.

Self-change MUST NOT be treated as either:

```text
forbidden forever
```

or:

```text
agent has root, good luck
```

### Change lifecycle

A governed change MAY move through:

```text
proposal
  ↓
classification
  ↓
impact / dependency analysis
  ↓
model / simulation
  ↓
static validation
  ↓
security review proportional to consequence
  ↓
testing
  ↓
staging
  ↓
limited rollout / canary
  ↓
observation
  ↓
promotion | rollback | quarantine
```

Different change classes may skip stages where consequence is low.

### Constitutional change

Changes to constitutional invariants require a distinct path from ordinary deployment.

Such a path SHOULD support:

- explicit human/root authority,
- versioned constitutional text/representation,
- migration plan,
- compatibility analysis,
- affected-state inventory,
- stronger review,
- independent verification,
- signed provenance,
- rollback where semantically possible,
- permanent historical record.

The Foundation must be able to evolve without pretending its own assumptions are infallible.

---

## 6N. Federation / interoperation dimension

Purpose: enable sovereign compounds and external institutions to cooperate without ambient cross-domain authority.

Core laws:

1. Every compound is sovereign by default.
2. Authentication of a foreign identity is not local authorization.
3. Recognition is not trust.
4. Trust is not delegation.
5. Delegation is scoped and attenuated.
6. Foreign statements remain foreign statements unless reconciled locally.
7. Foreign evidence retains origin.
8. Foreign instructions cannot become local canon merely through transport.
9. Shared infrastructure does not imply shared root authority.
10. Compounds SHOULD be able to reveal derived answers without revealing unnecessary source information.

### Federation relationships

A federation relationship MAY describe independently:

- identity trust anchors,
- accepted protocol versions,
- accepted semantic namespaces,
- disclosure policy,
- permitted request classes,
- delegated authority limits,
- evidence requirements,
- rate/resource limits,
- revocation state,
- reputation/risk signals,
- transport mechanisms.

### Contemporary evidence

SPIFFE Federation demonstrates explicit bundle exchange between independent trust domains. A2A 1.0.x demonstrates a contemporary agent-interoperability protocol with capability discovery and explicit protocol versioning. These are evidence for separation and negotiation, not a mandate to use either as the Concierge federation protocol. `[SRC-02, SRC-26]`

---

## 6O. Observability / operations dimension

Purpose: make the institution diagnosable without allowing observability data to become ambient authority or uncontrolled sensitive context.

Signals may include:

- traces,
- metrics,
- logs,
- profiles,
- security events,
- effect telemetry,
- policy decisions,
- resource consumption,
- worker lifecycle,
- federation health,
- state reconciliation anomalies.

OpenTelemetry demonstrates a useful pattern: common semantic conventions across heterogeneous signals. The Concierge SHOULD define its own institutional semantic conventions rather than inventing per-service telemetry vocabulary. `[SRC-23, SRC-24]`

Observability data is itself information and therefore subject to information governance.

Sensitive baggage/context propagation MUST NOT be assumed safe merely because it is “telemetry.” Contemporary OpenTelemetry documentation explicitly warns that baggage can propagate to unintended destinations and lacks built-in integrity checks. `[SRC-27]`

---

## 6P. Recovery / continuity dimension

Purpose: preserve institutional coherence across component loss, corruption, compromise, upgrade, and disaster.

Recovery is broader than backup.

It includes:

- durable work reconstruction,
- current-state projection rebuild,
- key recovery/rotation,
- grant revocation/reconstruction,
- evidence verification,
- compromised-node isolation,
- sandbox destruction,
- provider failover,
- state migration,
- replay with effect suppression,
- reconciliation against external reality,
- disaster recovery,
- and restoring institutional promises.

### Critical property

The institution SHOULD be able to terminate every ordinary cognition process and reconstruct active work, authority, commitments, expected states, and unresolved reality from durable institutional state.

Where this is impossible, the limitation must be explicit.

---

# 7. Semantic type system and institutional registry

Open-ended dimensional growth requires a governed type system.

## 7.1 Namespaced types

Types SHOULD use globally collision-resistant namespaces.

Example:

```text
concierge.core/identity/workload@2
concierge.core/effect/communicate.email@1
com.bankx/resource/credit-line@3
org.robotics/device/manipulator@7
```

Exact syntax is replaceable.

## 7.2 A type declaration cannot create authority

Registering:

```text
com.example/effect/detonate-firework
```

must not make the effect authorized.

The semantic registry describes meaning and contracts. Authority remains separate.

## 7.3 Schema + semantics + obligations

A registered type MAY declare:

- identity/name/version,
- machine-readable schema,
- human semantics,
- compatibility rules,
- validation constraints,
- references to effect tags,
- security-sensitive fields,
- provenance requirements,
- serialization mappings,
- deprecation state,
- migration functions,
- verifier interfaces,
- associated test vectors.

## 7.4 Open world, closed invariants

Unknown extension fields and unknown namespaced facets SHOULD be preserved whenever safe rather than silently discarded.

Protocol Buffers' preservation of unknown binary fields and OpenLineage's namespaced custom facets demonstrate practical compatibility patterns; they also demonstrate that careless representation changes can lose unknown information. `[SRC-28, SRC-13]`

The Foundation therefore distinguishes:

- **unknown but preservable**, and
- **unknown and safety-critical**.

Unknown metadata can often be forwarded.

Unknown authority semantics cannot safely default to “allow.”

## 7.5 Semantic negotiation

Participants MAY negotiate:

- protocol version,
- supported namespaces,
- supported schema versions,
- optional extensions,
- required extensions,
- downgrade policy,
- translation availability.

Silent downgrade that removes safety-relevant semantics SHOULD be forbidden.

## 7.6 Extension maturity

Types/extensions MAY have lifecycle states such as:

```text
EXPERIMENTAL
PROVISIONAL
STABLE
DEPRECATED
RETIRED
QUARANTINED
```

Maturity does not equal trust.

---

## 7.7 Admission of a genuinely new foundational dimension

“Extensible” must not become an excuse to put everything into custom metadata forever.

A new foundational dimension MAY be introduced when an architecture review establishes that the new semantics cannot be represented as an existing projection, extension facet, relationship family, effect descriptor, or domain-local type **without material distortion or invariant loss**.

The proposal should answer:

1. **What independent question does this dimension answer?**
2. **Which existing dimensions were tested and why do they fail?**
3. **What concepts are irreducible rather than convenience wrappers?**
4. **Which existing invariants continue to apply?**
5. **Which new invariants are required?**
6. **How does the dimension reference existing referents without stealing their semantics?**
7. **What information may cross into and out of it?**
8. **What authority can it consume or influence?**
9. **Can it introduce real-world effects directly? If so, through which effect boundary?**
10. **What migration/versioning semantics are required?**
11. **How is old software expected to treat messages/state containing the new dimension?**
12. **What security and recovery obligations does it create?**

Adding a dimension is therefore neither forbidden nor casual.

The architecture is **open-world at the semantic edge and conservative at constitutional boundaries**.

## 7.8 Semantic ownership and non-interference

Each dimension owns the semantics of its own authoritative state.

Other dimensions MAY consume projections or derived facts through explicit contracts; they MUST NOT silently reinterpret another dimension's storage representation as if it were their own truth.

Examples:

- The scheduler may consume an authority decision but must not infer authority from a database role name.
- The authority system may consume an environment-assurance claim but must not infer it from “runs in Kubernetes.”
- The information system may consume a world-model relationship but must not infer disclosure permission from social closeness.
- The work engine may consume a payment verification result but must not equate `HTTP 200` with settlement.
- The organization layer may reference a manager role but must not infer OS privilege from that role.

Cross-dimensional derivations SHOULD be named, attributable, versioned where consequential, and testable.

# 8. Institutional protocol layer

The previous Foundation's “Institutional Request Channel” was directionally correct but too tool-like.

The new design defines a family of **institutional protocol envelopes**.

They are not necessarily one network protocol.

## 8.1 Common envelope properties

A request/event envelope SHOULD be able to identify:

```text
message_id
protocol_family
protocol_version
semantic namespaces
sender identity
acting principal
representation
compound / trust domain
work reference
causal parents
reply correlation
created/observed times
expiry
integrity metadata
optional extensions
```

Sensitive fields MAY be referenced rather than embedded.

## 8.2 Core protocol families

Examples:

```text
ContextRequest / ContextResponse
AuthorityRequest / AuthorityDecision
SecretUseRequest / SecretUseResult
ExecutionRequest / ExecutionState
EffectRequest / EffectReceipt
PersistenceProposal / PersistenceResult
SubworkRequest / SubworkAssignment
ObservationReport
EvidenceSubmission
VerificationRequest / VerificationResult
DecisionEscalation
ResourceReservation
OrganizationChangeProposal
ExtensionRegistrationProposal
ChangeProposal
SecuritySignal / ContainmentCommand
FederationRequest / FederationResponse
```

These names are not constitutional.

The separation of concerns is.

## 8.3 No universal “tool call” abstraction

A tool call is only one execution mechanism.

The institutional protocol sits above:

- API calls,
- browser actions,
- shell commands,
- code execution,
- phone calls,
- human instructions,
- robot commands,
- foreign-agent messages.

## 8.4 Transport independence

The protocol MAY be transported over:

- local IPC,
- HTTP,
- gRPC,
- message streams,
- shared memory,
- signed offline envelopes,
- A2A-like protocols,
- future transports.

Transport authentication and institutional authorization remain distinct.

---

# 9. Authority algebra and delegation

Authority is one of the few areas where ambiguity directly becomes dangerous.

## 9.1 Effective authority is multidimensional

An effective grant can be viewed as a constrained region over dimensions.

Conceptually:

```text
G = {
  subjects,
  representations,
  operations,
  targets,
  purposes/work,
  information,
  disclosure,
  resource budgets,
  time,
  environment assurance,
  delegation,
  counterparties,
  consequence limits,
  required controls
}
```

This is conceptual, not a requirement for one giant tuple.

## 9.2 Delegation lineage

Every delegated authority MUST be traceable to a valid authority origin.

Possible roots include:

- explicit user grant,
- standing policy authorized by user/organization,
- jurisdiction delegation,
- institutional constitutional authority,
- external organization authority where the user legitimately represents it.

## 9.3 Delegation attenuation

A child grant MUST NOT gain power merely because a manager asks for it.

Where dimensions are comparable:

```text
child_scope ⊆ parent_scope
```

Where dimensions are not mechanically comparable, a new decision is required.

## 9.4 Revocation

Authority SHOULD support:

- explicit revocation,
- expiry,
- lease renewal,
- parent invalidation,
- emergency quarantine,
- key compromise response,
- policy supersession,
- compound severance.

Revocation propagation semantics MUST be explicit.

## 9.5 Proof of possession

For powerful bearer-like credentials, the Foundation SHOULD prefer sender-constrained or workload-bound credentials where external protocols support them.

OAuth mTLS and DPoP are contemporary examples of binding access-token use to possession of key material rather than token possession alone. `[SRC-29, SRC-30]`

## 9.6 Offline authority

Offline operation is a separate problem from online centralized grants.

The Foundation SHOULD reserve semantics for:

- time-bounded offline capabilities,
- attenuated delegation,
- revocation freshness limits,
- post-reconnection reconciliation,
- and evidence generated while disconnected.

It MUST NOT claim instantaneous revocation when disconnected operation makes that impossible.

---

# 10. Information physics

The information layer must become powerful enough that capability growth does not force privacy collapse.

## 10.1 Context Broker becomes an Information Mediation Fabric

The broker is not merely a retrieval API.

It may perform:

- source discovery,
- authorization,
- filtering,
- transformation,
- redaction,
- summarization,
- purpose-limited projection,
- freshness checks,
- provenance attachment,
- confidence reporting,
- contradiction reporting,
- and reference issuance.

## 10.2 References over copies

Where practical, workers receive references and mediated operations rather than unrestricted copies.

Examples:

```text
secretref://...
artifactref://...
evidenceref://...
contextref://...
accountref://...
```

Exact schemes are replaceable.

## 10.3 Taint and derived disclosure

The Foundation SHOULD support policy propagation or lineage-aware classification for derived information, but MUST not assume a universal automatic taint system can correctly infer all semantic leakage.

Some transformations can be mechanically recognized.

Others require domain-aware policy or human/AI judgment.

Enforcement strength must remain honest.

## 10.4 Retrieval is not truth

Search/ranking systems may surface candidates.

Only reconciliation can promote claims into stronger institutional belief/truth classes.

## 10.5 Embeddings are derived sensitive artifacts

Embeddings, indexes, caches, summaries, and model-generated metadata SHOULD inherit information-governance treatment appropriate to the source and leakage risk.

They are not “safe” merely because they are not plaintext.

---

# 11. Temporal and causal substrate

Long-term autonomous operation requires a durable partial-order history.

## 11.1 Institutional event identity

Consequential events SHOULD have globally unique IDs within their intended federation scope.

## 11.2 Event classes

Different event families may include:

- world observation,
- belief transition,
- work transition,
- authority transition,
- policy transition,
- execution lifecycle,
- effect lifecycle,
- evidence registration,
- verification transition,
- resource allocation,
- security event,
- organizational change,
- extension/change lifecycle,
- federation event.

## 11.3 Hybrid state model

The Foundation SHOULD retain both:

- current projections for efficient operational queries,
- immutable or tamper-evident records for consequential transitions.

This does not require religious full event sourcing.

## 11.4 Replay safety

Replaying institutional history for recovery MUST distinguish:

- rebuilding state projections,
- rerunning deterministic internal computations,
- and reissuing external effects.

External effects MUST NOT occur merely because an internal event was replayed.

---

# 12. Durable work and continuous responsibility

The Concierge is not a request/response chatbot.

## 12.1 Durable work state

Work may be in states such as:

```text
DRAFT
PLANNING
READY
RUNNING
WAITING_EXTERNAL
WAITING_DEPENDENCY
WAITING_DECISION
BLOCKED
VERIFYING
COMPLETED
FAILED
SUPERSEDED
ABANDONED
EXPIRED
```

The exact state machine can vary by work type.

## 12.2 Wake conditions

A work item MAY reactivate due to:

- time,
- event arrival,
- external state change,
- resource availability,
- dependency completion,
- authority availability,
- user decision,
- security restoration,
- newly discovered information.

## 12.3 Responsibilities and jurisdictions

Ongoing delegated domains should support policy-defined acceptable-state conditions and monitoring strategies.

They MUST NOT imply unlimited authority.

## 12.4 Institutional promises

When the Concierge promises to handle something, the promise SHOULD create durable tracked work with expected outcome and escalation semantics.

---

# 13. Execution substrate

## 13.1 Execution providers are replaceable

The Foundation contracts with providers through capabilities and assurance properties.

A provider may expose:

```text
create_cell(profile)
attach_identity(...)
mount_scoped_workspace(...)
configure_egress(...)
inject_secret_capability(...)
attach_device(...)
stream_security_events(...)
snapshot(...)
terminate(...)
destroy(...)
attest(...)
```

These are illustrative semantics, not a frozen API.

## 13.2 Nested cognition

A worker may spawn child computation inside its execution boundary.

That child does not automatically receive additional institutional identity or authority.

If the child needs institutional standing, it must obtain a workload identity / delegated authority through institutional mechanisms.

## 13.3 Escape versus effect

The architecture assumes a compromised worker may attempt to bypass institutional channels.

Therefore:

- network,
- credentials,
- filesystem persistence,
- devices,
- privileged APIs,
- internal control plane,
- and production systems

must be controlled outside ordinary worker code to the degree claimed by the assurance profile.

## 13.4 Environment selection

Isolation strength SHOULD scale with:

- hostile input exposure,
- generated/native code execution,
- secret sensitivity,
- effect consequence,
- cross-tenant risk,
- persistence authority,
- exploit surface,
- and required assurance.

Security is asymmetric; harmless work should not always pay the strongest isolation cost.

---

# 14. Universal Effect Fabric

## 14.1 Every consequential path must terminate at an enforceable boundary

For structured systems:

```text
cognition
  → effect proposal
  → semantic qualification
  → authority/security decision
  → enforcement point
  → external adapter
  → receipt/evidence
  → reconciliation
```

For GUI/voice/physical systems, exact interception may be weaker.

The Foundation must report that honestly.

## 14.2 Effect adapters

An adapter declares:

- operations it can attempt,
- targets it can address,
- semantic effect descriptors,
- consequence metadata it can calculate,
- idempotency properties,
- authentication mechanisms,
- enforcement strength,
- receipts available,
- verification options,
- compensation mechanisms,
- observability coverage.

An adapter declaration is not automatically trusted. It is supply-chain material plus runtime evidence.

## 14.3 Consequence graph

An effect may create:

- obligations,
- deadlines,
- dependencies,
- new work,
- financial exposure,
- social commitments,
- security state,
- physical state,
- or future effects.

The Foundation SHOULD allow consequence models to be attached and learned.

They may remain probabilistic/incomplete.

---

# 15. Evidence fabric

## 15.1 Evidence graph

Evidence should be graph-addressable:

```text
claim
  supported_by → evidence
  contradicted_by → evidence
  produced_by → principal/process
  observed_at → time/source
  derived_from → other evidence
  verifies → expected state
```

## 15.2 Evidence immutability and tamper evidence

Not every piece of evidence needs a blockchain or global transparency log.

Consequential evidence SHOULD however support integrity protection appropriate to its use.

Possible mechanisms include:

- cryptographic digests,
- signed receipts,
- append-only storage,
- hash chains/trees,
- external transparency services,
- timestamping,
- replicated independent observations.

## 15.3 Evidence retention classes

Retention may vary by:

- legal requirement,
- user preference,
- sensitivity,
- forensic value,
- reversibility,
- cost,
- dispute horizon.

Evidence governance is separate from ordinary operational logs.

---

# 16. Security architecture

## 16.1 Threat assumption

Assume eventually:

- agents are prompt-injected,
- websites and documents are adversarial,
- model outputs hallucinate authority,
- connectors are compromised,
- packages are malicious,
- credentials leak,
- browsers are exploited,
- external providers lie,
- humans make privileged mistakes,
- policy bugs ship,
- security detectors miss attacks,
- foreign compounds are compromised,
- an isolation technology has a vulnerability,
- a model becomes unexpectedly more capable than assumed.

The objective is not perfect prevention.

It is prevention where possible, containment where prevention fails, detection while compromise occurs, rapid revocation, evidence preservation, recovery, and bounded blast radius.

## 16.2 Security policy is consequence-aware

Security controls SHOULD depend on consequence and assurance, not only operation names.

## 16.3 Emergency controls

The Foundation SHOULD provide mechanisms for:

- revoke grant,
- revoke workload identity,
- terminate execution,
- sever egress,
- disable connector,
- quarantine extension,
- lock secret capability,
- suspend a jurisdiction,
- isolate compound federation,
- require global step-up,
- freeze constitutional changes.

Emergency controls themselves require strong authorization and auditability.

## 16.4 Policy distribution integrity

If distributed policy evaluators are used, policy material SHOULD be versioned and integrity-checked. OPA's signed bundle mechanism is contemporary evidence for this pattern. `[SRC-06]`

## 16.5 Runtime and sandbox diversity

The architecture SHOULD permit heterogeneous isolation mechanisms rather than assuming one sandbox is optimal for all threats.

## 16.6 Formal assurance where it buys real properties

High-value small components may justify stronger formal methods than ordinary application code.

seL4 demonstrates that code-level formal verification of a general-purpose capability-based microkernel is possible. This does not mean the Concierge should use seL4 everywhere; it demonstrates that the bottom of a high-assurance stack can be substantially more rigorous than prompt-level safeguards. `[SRC-17]`

---

# 17. Resource economy and scheduling

## 17.1 Resource reservation

Long-running work may need reservations rather than immediate consumption.

## 17.2 Competing objectives

The scheduler may optimize across:

- urgency,
- deadline,
- value,
- user attention,
- monetary cost,
- compute cost,
- risk,
- opportunity cost,
- fairness,
- jurisdiction priority.

The optimization strategy is replaceable.

## 17.3 Budgets are attributable

Consumption SHOULD be attributable to work, organizational owners, and delegated budgets.

## 17.4 Runaway control

Budgets SHOULD exist outside ordinary agent self-discipline where enforcement is possible.

Examples:

- CPU/memory quotas,
- token/API budgets,
- monetary limits,
- recursive spawn limits,
- wall-clock leases,
- network rate limits.

---

# 18. Organizational substrate

## 18.1 Organization is data + authority + routing + relationships

A department need not be a daemon.

A manager need not be an always-running LLM.

An organization can be instantiated when work exists and reconstructed later.

## 18.2 Organizational templates

Templates MAY define reusable structures, but they MUST remain overrideable and evolvable.

## 18.3 Shadow organizations

High-impact work MAY create isolated independent branches that receive approved evidence but do not inherit the primary branch's hidden reasoning.

They can independently reconstruct and challenge the problem.

## 18.4 Human operators

Humans are first-class principals and execution providers.

The Foundation must record:

- what they were asked,
- under what authority,
- what information was disclosed,
- what action they reported,
- what independent evidence exists.

Human involvement must not become an unlogged escape hatch from institutional governance.

---

# 19. Evolution engine

## 19.1 Change is work

Every meaningful self-modification is represented as institutional work with authority, evidence, expected state, and rollback/containment semantics.

## 19.2 Change classes

Examples:

```text
CONTENT_CHANGE
PROMPT_CHANGE
MODEL_CHANGE
WORKFLOW_CHANGE
POLICY_CHANGE
SCHEMA_CHANGE
EXTENSION_INSTALL
EXECUTION_PROVIDER_CHANGE
SECRET/KEY_CHANGE
INFRASTRUCTURE_CHANGE
SECURITY_CONTROL_CHANGE
FEDERATION_CHANGE
FOUNDATION_CHANGE
CONSTITUTIONAL_CHANGE
```

Risk is not determined solely by class; context and consequence matter.

## 19.3 Compatibility analysis

A change SHOULD identify:

- producers,
- consumers,
- stored state,
- protocol peers,
- policies,
- migrations,
- downgrade behavior,
- unknown extension handling,
- rollback semantics.

## 19.4 Automated builders remain untrusted

An AI may generate the migration, policy, runtime, connector, or extension.

Its output still passes through the change pipeline.

## 19.5 Self-improvement without self-authorization

A system may improve its ability to solve tasks without being able to silently broaden its own authority.

This is a constitutional invariant.

---

# 20. Extension & Capability Protocol

The old Extension Contract becomes a broader institutional protocol.

## 20.1 An extension may introduce any subset of:

- semantic types,
- schemas,
- observation sources,
- execution providers,
- effect adapters,
- evidence types,
- verifiers,
- policy functions/vocabulary,
- resource types,
- organizational templates,
- UI surfaces,
- device interfaces,
- federation capabilities,
- translation layers,
- simulation models.

## 20.2 Extension manifest

A manifest is a **claim** about the extension.

It MAY declare:

```yaml
identity:
  namespace: com.example.future
  version: 4.2.0
  artifact_digest: ...

semantics:
  types: [...]
  schemas: [...]
  extensions: [...]

runtime:
  supported_execution_profiles: [...]
  required_interfaces: [...]

requested_capabilities:
  network: ...
  devices: ...
  secret_classes: ...
  persistent_storage: ...

institutional_interfaces:
  effects: [...]
  observations: [...]
  evidence: [...]
  verifiers: [...]

assurance_claims:
  provenance: ...
  signatures: ...
  attestability: ...

compatibility:
  protocol_versions: [...]
  migration: ...
```

The manifest does not grant any of these capabilities.

## 20.3 Unknown capability path

When cognition invents something new:

```text
Can it remain internal computation?
    → run within execution boundary.

Does it need information?
    → information mediation.

Does it need a secret-derived capability?
    → secret broker / delegated capability.

Does it need persistence?
    → persistence proposal.

Does it need external consequences?
    → register/use effect adapter.

Does it need novel semantics?
    → semantic extension proposal.

Does it need additional authority?
    → authority request.

Does it need another institution?
    → federation.
```

The institution can absorb novelty without granting ambient power.

## 20.4 Capability discovery

Capabilities SHOULD be discoverable by semantics and contracts, not merely by hard-coded tool names.

## 20.5 Capability reputation and health

Operational learning MAY track reliability, cost, security history, verification quality, and performance of extensions/providers.

This is operational truth, not immutable policy.

---

# 21. Federation architecture

## 21.1 Sovereignty

A compound owns its own:

- root identity,
- keys,
- authority,
- policy,
- secrets,
- world state,
- user truth,
- work,
- evidence,
- extensions,
- security decisions.

## 21.2 Federation envelope

A federation exchange SHOULD be able to carry:

```text
sender compound identity
sender principal
recipient compound
protocol version
semantic namespaces
request/response type
representation claim
work/purpose claim
requested disclosure/effect
delegation evidence if any
attached evidence references
integrity/signature
expiry/replay protection
```

## 21.3 Local reauthorization

A foreign request is input to local policy.

The foreign compound cannot authorize itself locally.

## 21.4 Delegated cross-compound work

Explicit cross-compound delegation MAY issue scoped authority that the foreign compound can exercise under agreed semantics.

Where possible, delegation SHOULD be attenuable, time-bounded, revocable, and purpose-bound.

## 21.5 Information minimization

Federation SHOULD favor derived disclosures and proofs over raw private data when sufficient.

## 21.6 Protocol agility

A transport/protocol such as A2A, HTTP, gRPC, or a future agent protocol may be used without becoming the federation trust model.

---

# 22. Simulation and counterfactual branches

The institution needs a native way to explore futures without accidentally producing reality.

## 22.1 Branchable institutional state

A simulation branch MAY fork selected state:

- world beliefs,
- work,
- resource assumptions,
- organization,
- policy candidate,
- extension candidate,
- infrastructure state.

## 22.2 Effects default to simulated

Effect adapters in a simulation MUST be simulation adapters unless explicitly elevated through authority.

## 22.3 Counterfactual evaluation

Branches may evaluate:

- plans,
- budgets,
- consequences,
- migrations,
- organization designs,
- policy changes,
- security attacks,
- recovery procedures.

## 22.4 Branch provenance

A simulated result MUST remain distinguishable from observed reality.

No simulation output silently becomes world truth.

---

# 23. Persistence and state boundaries

## 23.1 Institutional mutation is privileged

Agent filesystem mutation is not institutional mutation.

Durable writes to:

- canon,
- authority,
- world truth,
- policies,
- commitments,
- official documents,
- production code,
- evidence,
- secrets,
- extension registry

cross explicit boundaries.

## 23.2 Domain-specific stores are allowed

The architecture MUST NOT require one universal database or graph.

Different dimensions may use different physical representations when justified.

What matters is referential coherence, explicit contracts, transaction semantics, and reconstructability.

## 23.3 No universal event-store mandate

Some domains may be event-sourced, some relational, some content-addressed, some graph-based, some external.

The Foundation requires consequential transition history where needed, not a single storage religion.

---

# 24. Interoperability and schema evolution

## 24.1 Compatibility is explicit

Each protocol/schema family SHOULD define:

- backward compatibility,
- forward compatibility,
- unknown-field behavior,
- removed-field behavior,
- required-extension behavior,
- downgrade behavior,
- migration rules.

## 24.2 Silent semantic loss is dangerous

A decoder that accepts a message while discarding a new safety-critical field can be worse than rejecting it.

Unknown-field preservation is useful only when the receiver can safely remain ignorant of the field's semantics.

## 24.3 Version negotiation

OpenAPI 3.2.1 (published 2026-09-10) and A2A 1.0.x illustrate that interface standards themselves evolve and require explicit version semantics. `[SRC-26, SRC-31]`

The Foundation therefore treats protocol evolution as ordinary institutional reality.

---

# 25. Verification and formalization strategy

“Hallucination-proof” architecture is not achieved by writing confident prose.

It requires executable checks.

## 25.1 Property tests

Examples:

- delegated authority never exceeds parent where attenuation is defined,
- revoked authority cannot authorize new effects,
- expired workload identities cannot exercise grants,
- unknown duplicate-sensitive effect outcomes are never auto-retried without reconciliation,
- simulated effects never reach live adapters by default,
- foreign authentication never implies local authorization,
- extension registration never grants authority,
- work survives worker termination,
- claimed completion requires configured evidence,
- replay rebuilds state without repeating external effects.

## 25.2 State-machine model checking

High-value state machines SHOULD be specified in a machine-checkable formalism or model checker where practical.

Candidates include authority delegation, effect lifecycle, revocation, change lifecycle, and federation handshakes.

The Foundation does not mandate a specific formal language.

## 25.3 Differential authorization testing

If multiple policy implementations or compiled forms exist, test equivalent decisions across them.

## 25.4 Schema compatibility tests

Every evolution should test old producer/new consumer, new producer/old consumer, unknown extension preservation, and semantic downgrade.

## 25.5 Fault injection

Inject:

- crashes,
- timeouts,
- duplicated messages,
- reordered events,
- lost acknowledgements,
- stale caches,
- policy service loss,
- credential expiry,
- storage failover,
- partial network partitions,
- external contradictory states.

## 25.6 Security adversarial tests

Test:

- prompt injection,
- tool poisoning,
- malicious extensions,
- dependency compromise,
- credential theft,
- confused deputy,
- authority laundering,
- cross-compound impersonation,
- sandbox escape attempts,
- exfiltration,
- memory poisoning,
- evidence forgery,
- policy rollback attacks,
- malicious migration.

## 25.7 Recovery drills

A recovery plan not exercised is a hypothesis.

The institution SHOULD periodically prove it can reconstruct selected critical domains from durable state and verified evidence.

---

# 26. Candidate implementation mapping — explicitly non-constitutional

This section demonstrates that the architecture is implementable with contemporary systems. It is **not** a mandate.

| Foundation need | Contemporary candidates / evidence | Architectural status |
|---|---|---|
| Workload identity | SPIFFE/SPIRE | Candidate |
| Policy evaluation | Cedar, OPA | Candidate |
| Relationship authorization | Zanzibar-like model, OpenFGA | Candidate |
| Attenuable credentials | Biscuit / capability-token approaches | Candidate |
| Sender-constrained OAuth | DPoP, mTLS-bound tokens | Candidate where protocols support |
| Typed portable components | WebAssembly Component Model / WASI 0.3 | Candidate execution provider |
| Process/container isolation | gVisor | Candidate assurance tier |
| Strong VM isolation | microVM/full VM technologies | Candidate assurance tier |
| High-assurance capability kernel | seL4 | Research/high-assurance candidate |
| Capability hardware | CHERI/CHERIoT | Future/embedded candidate |
| Remote attestation architecture | IETF RATS | Candidate conceptual mapping |
| Software provenance | SLSA, in-toto | Candidate evidence schemas |
| Transparency receipts | SCITT | Candidate evidence/transparency service |
| Observability semantics | OpenTelemetry | Candidate telemetry baseline |
| Data lineage semantics | W3C PROV, OpenLineage | Candidate/inspiration |
| HTTP API description | OpenAPI | Adapter/interface description only |
| Event API description | AsyncAPI | Adapter/interface description only |
| Agent interoperability | A2A | Federation/adapter candidate only |

The Foundation SHOULD permit replacing every row without redesigning the institution.

---

# 27. Architecture stress battery

Before freezing a Foundation version, architects MUST try to express scenarios that were not used to design it.

The following battery exists specifically to detect hidden narrowness.

## 27.1 Future cognition

1. A reasoning system has no natural-language prompt and exposes only a typed planning API.
2. An agent writes a new agent runtime and executes it inside its cell.
3. A worker spawns 1,000 internal subagents unknown to Concierge.
4. A planner uses a future algorithm that does not fit token-based cost accounting.

Required result: no constitutional redesign merely because cognition changed.

## 27.2 New execution dimensions

5. Household robot with cameras, arms, locks, and physical geofence.
6. Offline laptop worker disconnected for one month.
7. Confidential-compute worker with verifiable attestation.
8. Human contractor executing a physical errand.
9. AR glasses streaming ambient world observations.

Required result: execution/environment and effect semantics can express them without pretending they have identical assurance.

## 27.3 New authority shapes

10. User delegates “manage travel under €2,000/month but never book overnight layovers.”
11. Company grants user authority that the user's personal Concierge may exercise only when representing the company.
12. Two humans jointly control an asset requiring threshold approval.
13. Foreign Concierge receives temporary authority to schedule only within disclosed availability windows.

Required result: identity, representation, authority, resource, and information dimensions remain separate.

## 27.4 New information shapes

14. Medical record yields a derived yes/no eligibility fact without disclosing diagnosis.
15. A model produces an inference from three confidential sources with different retention policies.
16. A foreign compound submits evidence whose raw artifact cannot be shared locally.
17. An embedding cache leaks more information than its application expected.

Required result: provenance and disclosure can be modeled without calling everything “context.”

## 27.5 New organizational dimensions

18. Concierge creates a temporary company to execute a project.
19. A security incident spawns an isolated incident organization with authority to quarantine but not read unrelated personal data.
20. Two departments create an independent shadow team to reconstruct a financial decision.
21. A human law firm becomes an external specialist organization.

Required result: organization does not equal process topology.

## 27.6 New economic dimensions

22. Work is constrained by battery degradation rather than money.
23. User attention budget is exhausted while monetary budget remains.
24. A scarce third-party API quota must be reserved across objectives.

Required result: arbitrary resource types can be introduced without confusing budget with authority.

## 27.7 New federation dimensions

25. 10,000 compounds exchange threat intelligence but no private user data.
26. Two compounds cooperate while their clocks disagree and one was offline.
27. A foreign compound is cryptographically authentic but compromised.
28. A federation transport changes from A2A to a future protocol.

Required result: transport and authentication do not become trust/authority.

## 27.8 Self-evolution

29. Concierge discovers its current policy engine cannot express a needed constraint and proposes a replacement.
30. An extension introduces a novel effect class not known at Foundation v0.2.
31. A schema migration changes how relationships are represented.
32. A new hardware isolation mechanism becomes available.
33. The institution proposes changing a constitutional invariant.

Required result: evolution occurs through governed change rather than escape from the architecture.

## 27.9 Failure and compromise

34. Worker is compromised after obtaining legitimate context but before effect execution.
35. Policy engine serves a stale policy version.
36. Connector returns success although external state did not change.
37. Control-plane database restores from a backup older than external actions.
38. Root key rotation occurs while foreign compounds are disconnected.
39. Evidence store is partially corrupted.
40. Model provider becomes malicious.

Required result: compromise does not automatically collapse every institutional domain.

---

# 28. Constitutional invariants v0.2

These are candidate non-negotiable properties.

1. **Cognition does not own institutional authority merely by being capable.**
2. **Identity, authentication, trust, authority, representation, and credential possession remain distinguishable.**
3. **Delegation cannot silently increase authority.**
4. **No semantic extension grants itself authority by defining new vocabulary.**
5. **No worker assumption silently becomes user truth, world truth, policy, or canon.**
6. **No untrusted external content becomes institutional instruction merely because cognition consumed it.**
7. **No secret is placed in model-readable context when the needed capability can be safely mediated without doing so, subject to practical enforceability.**
8. **No duplicate-sensitive effect is automatically retried while the prior outcome remains materially unknown.**
9. **Effect attempt, receipt, observed outcome, and verified outcome remain distinct.**
10. **Every claimed high-consequence completion has evidence appropriate to the consequence.**
11. **Replay/recovery does not repeat external effects merely because internal history is replayed.**
12. **Foreign authentication never implies local authorization.**
13. **Shared infrastructure never implies shared compound root authority.**
14. **Organization does not automatically imply infrastructure privilege.**
15. **Resource availability does not imply authority; authority does not imply resource availability.**
16. **Simulation state never silently becomes observed reality.**
17. **Security enforcement strength is represented honestly; advisory controls are never labeled hard enforcement.**
18. **Ordinary agents, models, generated code, web content, third-party tools, and foreign compounds are outside the root TCB by default.**
19. **Institutional state needed for continuity survives ordinary worker death.**
20. **Self-improvement cannot silently self-authorize broader real-world power.**
21. **Constitutional changes follow a distinct, attributable, strongly authorized change path.**
22. **Unknown future dimensions may extend semantics, but cannot bypass existing authority, information, evidence, security, and effect boundaries merely because they are novel.**

---

# 29. What is deliberately *not* frozen

The Foundation does not freeze:

- model vendor,
- model architecture,
- agent framework,
- orchestration framework,
- programming language,
- database,
- graph database,
- event broker,
- workflow engine,
- policy language,
- workload identity implementation,
- sandbox technology,
- VM technology,
- container runtime,
- WebAssembly runtime,
- RPC framework,
- federation transport,
- A2A,
- MCP,
- browser agent,
- secret-management vendor,
- cloud provider,
- telemetry backend,
- vector database,
- schema serialization,
- UI framework,
- organizational chart,
- or one universal ontology.

Implementations may standardize temporarily for engineering efficiency.

Temporary standardization MUST remain distinguishable from constitutional dependency.

---

# 30. What *is* intended to remain durable

The following properties are intended to survive implementation replacement:

- open-ended cognition separated from authority,
- institutional continuity outside ordinary agents,
- stable cross-domain referents,
- orthogonal semantic projections,
- explicit identity and representation,
- traceable authority and delegation,
- mediated information access,
- durable work and unresolved reality,
- explicit causal/temporal history,
- isolated/qualified execution environments,
- mediated effects,
- evidence-backed verification,
- resource governance independent of permission,
- dynamic organizational composition,
- independent security enforcement/observation,
- governed self-evolution,
- sovereign federation,
- recoverability,
- semantic/version extensibility,
- and constitutional invariants enforced outside ordinary model preference.

---

# 31. Development doctrine from here

## 31.1 Architecture before implementation — but executable architecture

The next phase should not be a narrow MVP.

It should turn this Foundation into **machine-testable contracts** without prematurely collapsing implementation choice.

Required artifacts should eventually include:

1. semantic registry specification,
2. referent and projection model,
3. authority/delegation formal model,
4. information lineage and disclosure model,
5. causal/event envelope model,
6. work/commitment state machines,
7. execution-provider contract,
8. assurance-profile model,
9. effect lifecycle and adapter contract,
10. evidence/claim model,
11. resource type contract,
12. extension/change protocol,
13. federation envelope and local-reauthorization model,
14. simulation branch semantics,
15. constitutional change protocol,
16. executable invariant/property test suite.

These should be developed together enough to detect cross-domain contradictions.

## 31.2 No subsystem may define another dimension accidentally

Examples:

- Policy schema cannot become world ontology.
- Event schema cannot become authorization semantics.
- Extension manifest cannot become execution authority.
- Workflow engine state cannot become institutional truth by default.
- Sandbox profile cannot become organization structure.
- Database schema cannot become the Constitution.

## 31.3 Every abstraction earns its permanence

For each proposed permanent concept ask:

```text
Is this truly universal?
Is it a semantic dimension or just today's implementation?
Does it collapse unrelated concerns?
Can future systems extend it without escape hatches?
Can we state its invariants mechanically?
Can we preserve unknown future semantics safely?
What happens when this assumption is false?
```

## 31.4 Architectural red team is mandatory

Before marking a Foundation version stable, an independent architecture branch should attempt to:

- find hidden ambient authority,
- find semantic conflation,
- find TCB creep,
- find non-recoverable state,
- find protocol lock-in,
- find schema lock-in,
- find unversioned semantics,
- find impossible offline assumptions,
- find unenforceable “security” claims,
- find domains that cannot express a future stress scenario.

---

# 32. Research source ledger

The following sources support factual claims and provide design evidence. They do **not** become Concierge constitutional dependencies.

## Identity, zero trust, authorization

**[SRC-01] SPIFFE Standard — latest specification set**  
https://spiffe.io/docs/latest/spiffe-specs/  
Checked 2026-09-27. Demonstrates workload identities, SVIDs, Workload API, trust domains and federation as separable standards.

**[SRC-02] SPIFFE Federation**  
https://spiffe.io/docs/latest/spiffe-specs/spiffe_federation/  
Stable specification. Demonstrates authentication across administratively independent trust domains by exchanging/verifying trust bundles.

**[SRC-03] SPIFFE Workload API / Trust Domain and Bundle**  
https://spiffe.io/docs/latest/spiffe-specs/spiffe_workload_api/  
https://spiffe.io/docs/latest/spiffe-specs/spiffe_trust_domain_and_bundle/  
Evidence for runtime workload identity and separate trust-domain roots.

**[SRC-04] NIST SP 800-207 — Zero Trust Architecture**  
https://csrc.nist.gov/pubs/sp/800/207/final  
Evidence for no implicit trust based solely on network location and separation of policy decision/enforcement roles.

**[SRC-05] Cedar Policy Language Reference**  
https://docs.cedarpolicy.com/  
Current documentation checked 2026-09-27. Evidence for structured principal/action/resource/context authorization and policy/schema validation.

**[SRC-06] Open Policy Agent — architecture, deployment, signed bundles**  
https://www.openpolicyagent.org/docs/deploy  
https://www.openpolicyagent.org/docs/management-bundles  
Evidence for decoupled policy decision/enforcement, local PDP deployment, and integrity-checked policy distribution.

**[SRC-07] NIST SP 800-207A**  
https://csrc.nist.gov/pubs/sp/800/207/a/final  
Evidence for granular application/service identity policies in cloud-native/multi-cloud environments.

**[SRC-08] Zanzibar: Google's Consistent, Global Authorization System**  
https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/  
Evidence for relationship-based authorization at very large scale and causal consistency considerations.

**[SRC-09] OpenFGA Concepts / Modeling**  
https://openfga.dev/docs/concepts  
Evidence for relationship tuple models.

**[SRC-10] OpenFGA Conditions**  
https://openfga.dev/docs/modeling/conditions  
Evidence for combining relationships with contextual/attribute conditions.

**[SRC-11] Biscuit Specifications**  
https://doc.biscuitsec.org/reference/specifications  
Evidence for cryptographically protected authorization material with block-based attenuation and scoped trust origins.

## Provenance, lineage, transparency

**[SRC-12] W3C PROV Overview**  
https://www.w3.org/TR/prov-overview/  
Established provenance model family covering entities, activities, agents, derivation, attribution, versioning, and provenance of provenance.

**[SRC-13] OpenLineage Facets & Extensibility**  
https://openlineage.io/docs/spec/facets/  
Version observed: 1.53.0. Evidence for small core entities plus namespaced, schema-versioned extensible facets.

**[SRC-14] OpenLineage Lineage Facets**  
https://openlineage.io/docs/spec/facets/job-facets/lineage/  
https://openlineage.io/docs/spec/facets/dataset-facets/lineage/  
Evidence for explicit entity- and field-level lineage without inferring false all-to-all dependencies.

## Execution and assurance

**[SRC-15] WASI 0.3 Launch / Roadmap**  
https://bytecodealliance.org/articles/WASI-0.3  
https://wasi.dev/roadmap  
WASI 0.3.0 ratified 2026-06-11; 0.3.1 shipped 2026-08-11. Evidence for stable typed component interfaces and native async composition.

**[SRC-16] gVisor Architecture / Security Model**  
https://gvisor.dev/docs/architecture_guide/intro/  
https://gvisor.dev/docs/architecture_guide/security/  
Evidence for an application-kernel isolation model and honest documentation of threat boundaries/limitations.

**[SRC-17] seL4 White Paper / FAQ**  
https://sel4.systems/About/whitepaper.html  
https://sel4.systems/About/FAQ.html  
Evidence that capability-based resource access and deep formal verification can be implemented at kernel level.

**[SRC-18] CHERIoT Platform**  
https://cheriot.org/  
Evidence for hardware-supported capabilities, compartmentalization, bounded pointers, and scoped delegation in embedded systems.

**[SRC-32] IETF RATS Architecture — RFC 9334**  
https://www.rfc-editor.org/rfc/rfc9334.html  
Evidence for explicit Attester / Verifier / Relying Party separation and policy-based appraisal of attestation evidence.

## Supply-chain evidence and transparency

**[SRC-19] SLSA Specification v1.2**  
https://slsa.dev/spec/v1.2/  
Current observed version: 1.2. Evidence for source/build provenance and verification properties.

**[SRC-20] SLSA Provenance**  
https://slsa.dev/spec/v1.2/provenance  
Evidence for verifiable information describing where, when, and how artifacts were produced.

**[SRC-21] in-toto Specifications**  
https://in-toto.io/docs/specs/  
Stable in-toto specification and stable Attestation Framework v1.0 observed.

**[SRC-22] SCITT — RFC 9943**  
https://www.rfc-editor.org/rfc/rfc9943/  
Published June 2026. Defines an extensible transparency architecture for signed statements and receipts backed by verifiable data structures.

## Observability

**[SRC-23] OpenTelemetry Semantic Conventions**  
https://opentelemetry.io/docs/specs/semconv/  
Observed semantic conventions 1.44.0. Evidence for cross-platform common semantics over telemetry signals/resources.

**[SRC-24] OpenTelemetry Signals**  
https://opentelemetry.io/docs/concepts/signals/  
Evidence for distinct traces, metrics, logs, baggage and profiles rather than one universal log format.

**[SRC-25] OpenTelemetry General Semantic Conventions**  
https://opentelemetry.io/docs/specs/semconv/general/  
Evidence for convention evolution and shared attribute semantics.

**[SRC-27] OpenTelemetry Baggage security considerations**  
https://opentelemetry.io/docs/concepts/signals/baggage/  
Explicitly warns that baggage can propagate to unintended resources and lacks built-in integrity checks.

## Protocol evolution and interoperability

**[SRC-26] Agent2Agent (A2A) Protocol**  
https://github.com/a2aproject/A2A/blob/main/docs/specification.md  
Latest released line observed: 1.0.x; explicit protocol-version negotiation and extension mechanisms. Used only as evidence that agent interop protocols evolve rapidly.

**[SRC-31] OpenAPI 3.2.1**  
https://spec.openapis.org/oas/v3.2.1.html  
Published 2026-09-10. Evidence for explicit API specification versioning and evolving interface description standards.

**[SRC-33] AsyncAPI concepts/specification**  
https://www.asyncapi.com/docs/concepts  
Evidence for protocol-independent event-driven API description. Candidate for adapter documentation, not institutional semantics.

## Schema evolution

**[SRC-28] Protocol Buffers — Updating a Message Type / Unknown Fields**  
https://protobuf.dev/programming-guides/proto3/  
Evidence that unknown-field preservation can support forward compatibility while some representation changes (notably JSON transformations) can lose unknown data.

## Sender-constrained authorization

**[SRC-29] OAuth 2.0 DPoP — RFC 9449**  
https://www.rfc-editor.org/rfc/rfc9449/  
Application-level proof-of-possession mechanism for sender-constrained OAuth tokens.

**[SRC-30] OAuth 2.0 mTLS — RFC 8705**  
https://www.rfc-editor.org/rfc/rfc8705/  
Certificate-bound OAuth tokens and mutual-TLS client authentication.

---

# 33. Explicit non-adoptions

Research does not imply adoption.

At Foundation v0.2:

- SPIFFE is **not** the permanent Concierge identity model.
- OPA is **not** the permanent policy engine.
- Cedar is **not** the permanent policy language.
- OpenFGA/Zanzibar is **not** the complete authority model.
- Biscuit is **not** mandated as the grant format.
- WASI is **not** the universal execution runtime.
- gVisor is **not** the universal sandbox.
- seL4 is **not** mandated as the host kernel.
- CHERI/CHERIoT is **not** assumed available.
- SLSA/in-toto is **not** the complete evidence ontology.
- SCITT is **not** the Concierge evidence ledger.
- OpenTelemetry is **not** the security plane.
- W3C PROV/OpenLineage is **not** the complete information model.
- A2A is **not** the Concierge federation protocol.
- OpenAPI/AsyncAPI is **not** the institutional type system.
- Protocol Buffers is **not** the required wire format.

Each is evidence that particular properties are achievable or that particular pitfalls are real.

---

# 34. Deep architectural equation

The previous Foundation equation was useful but incomplete.

A more accurate expression is:

```text
OPEN-ENDED COGNITION
+
STABLE REFERENTS
+
ORTHOGONAL SEMANTIC DIMENSIONS
+
EXPLICIT IDENTITY & REPRESENTATION
+
TRACEABLE, ATTENUABLE AUTHORITY
+
MEDIATED INFORMATION & PROVENANCE
+
DURABLE INTENT / WORK / COMMITMENTS
+
CAUSAL & TEMPORAL CONTINUITY
+
QUALIFIED EXECUTION ENVIRONMENTS
+
MEDIATED REAL-WORLD EFFECTS
+
EVIDENCE & INDEPENDENT VERIFICATION
+
RESOURCE / ATTENTION ECONOMY
+
DYNAMIC ORGANIZATIONAL COMPOSITION
+
CONTINUOUS SECURITY & CONTAINMENT
+
GOVERNED SELF-EVOLUTION
+
SOVEREIGN FEDERATION
+
RECOVERY & RECONCILIATION
+
A SMALLER TRUSTED ENFORCEMENT BASE
=
UNBOUNDED INSTITUTIONAL AUTONOMY
```

No single term is sufficient.

No contemporary product should be mistaken for a term.

---

# 35. Final architectural statement

The Concierge must not be a giant privileged agent, and it must not be a tiny kernel surrounded by capability-specific islands.

It should be a **persistent sovereign institution with a richly expressive but compositionally disciplined substrate, capable of absorbing dimensions of intelligence, execution, information, organization, and real-world interaction that were not known when the Foundation was designed.**

The institution must permit cognition to become radically more capable without equating capability with privilege.

It must permit its own organization to grow without equating departments with infrastructure.

It must permit new semantics without allowing a type declaration to manufacture authority.

It must permit new execution technologies without making one sandbox the Constitution.

It must permit new protocols without making transport into trust.

It must permit new evidence forms without confusing evidence with truth.

It must permit derived information without collapsing provenance into context.

It must permit self-improvement without self-authorization.

It must permit federation without surrendering sovereignty.

It must permit constitutional evolution without pretending constitutional rules are ordinary configuration.

The Foundation therefore does not try to predict every future capability.

It establishes the institutional laws by which future capabilities can **enter, identify themselves, obtain scoped information, request or inherit legitimate authority, consume resources, execute in qualified environments, affect reality, produce evidence, be verified, be contained, be replaced, cooperate with other institutions, and change the institution itself — without needing to escape the institution to do so.**

That is the floor.

Everything above it may evolve aggressively.

Everything below it should be as small, rigorous, and independently enforceable as practical.

And when a future capability arrives that does not fit, the first assumption must not be that the future capability is wrong.

The first question must be:

> **Did we discover a genuinely new institutional dimension, or did we accidentally make an old abstraction too narrow?**

If it is genuinely new, the Foundation must have a governed way to grow.

That property — **the ability to expand without escaping its own laws** — is the deepest requirement of the Concierge Foundation.

---

# 36. Supersession notes relative to Foundation v0.1

This document deliberately changes several conclusions of the previous draft.

## 36.1 Previous “permanent primitives”

`Principal / Resource / Work / Authority / Effect / Evidence / Event` are retained as highly useful concepts, but **are no longer declared to be the complete permanent ontology**. They live inside a larger set of orthogonal dimensions and may be supplemented by genuinely new dimensions through constitutional evolution.

## 36.2 Previous design rule: “first express everything through seven primitives”

Replaced with:

> **First attempt to express a new capability through existing dimensions and projections without distortion. If it does not fit, do not force it. Use the governed new-dimension admission process.**

The defense against architectural entropy is not refusing new dimensions. It is requiring new dimensions to prove semantic independence.

## 36.3 Previous “Foundation remains comparatively small”

Rejected as an architectural objective.

The corrected rule is:

> **The trusted enforcement base remains deliberately small. The institutional substrate remains conceptually coherent while its expressive dimensionality may expand without predetermined bound.**

## 36.4 Previous v0.1 physical implementation and build order

Demoted from Foundation-level direction to one possible implementation experiment.

The core engine should not be scoped around the minimum set required for one subscription-cancellation vertical slice. Vertical slices remain valuable for validation, but they do not define the semantic horizon of the floor.

Implementation should begin only after enough cross-dimensional contracts exist to prevent the first codebase from silently becoming the Constitution.

## 36.5 Previous Extension Contract

Generalized into the **Extension & Capability Protocol**, which can add semantics, execution providers, effect adapters, evidence types, verifiers, resources, devices, organizational templates, and federation capabilities without equating extension with a plugin.

## 36.6 Previous Institutional Request Channel

Generalized into a family of institutional protocol envelopes. A single “request socket” may still be an implementation, but it is not the architecture.

## 36.7 Previous security direction

Preserved and strengthened.

The separation of security reasoning from security physics, reduction of the TCB, no ambient authority, external control of worker environments, live observation, and evidence-backed recovery remain central.

---

# 37. Foundation acceptance criteria

A future revision SHOULD NOT be called a stable Foundation merely because the prose is comprehensive. It should satisfy evidence-backed quality gates.

At minimum:

1. **Semantic separation:** major concepts have explicit anti-collapse tests/reviews.
2. **Cross-dimensional contracts:** data and authority crossing dimensions are declared rather than inferred from storage internals.
3. **Authority model:** delegation, revocation, representation, environment constraints, and foreign reauthorization have machine-testable semantics.
4. **Unknown handling:** each protocol family specifies safe behavior for unknown versions/extensions.
5. **Effect safety:** duplicate-sensitive unknown outcomes and replay semantics are testable.
6. **Recovery:** ordinary cognition can be terminated and critical institutional work reconstructed.
7. **Evolution:** an extension can add genuinely new semantics without obtaining authority by definition.
8. **Constitutional evolution:** the architecture contains a path to change itself without treating such change as ordinary configuration.
9. **Federation sovereignty:** foreign identity/authentication cannot bypass local authority.
10. **Honest enforcement:** every important security property can state where and how strongly it is enforced.
11. **Reference independence:** no contemporary vendor/project is required for the semantics to remain meaningful.
12. **Stress battery:** the Foundation survives the scenario battery or explicitly records the architectural gap.
13. **Research traceability:** external factual claims have dated primary sources or are marked as unverified/open.
14. **Implementation non-capture:** schemas/frameworks chosen for the first build are mapped to Foundation contracts rather than redefining them.

Only after these are materially satisfied should implementation choices be allowed to harden around the floor.
