# AI Concierge — Canonical Product Concept

## 1. Definition

The AI Concierge is a persistent personal intelligence operating between the user and the rest of their digital and real-world life.

It is not primarily a chatbot, tool runner, or collection of agents. It is a continuously operating system that understands the user's world, maintains state across time, pursues objectives, coordinates people and systems, acts with delegated authority, verifies outcomes, and escalates decisions when human judgment is required.

The long-term capability boundary is intentionally broad:

> If a sufficiently capable human assistant or organization could accomplish something using computers, phones, communication, research, services, devices, institutions, or other accessible interfaces, the Concierge should ultimately be capable of accomplishing it.

Capability should not be artificially constrained by domain. Safety comes from architecture, authority, separation, supervision, accountability, and invariant preservation rather than arbitrary feature walls.

---

## 2. One Person Outside, an Organization Inside

To the user, the Concierge is **one person**.

One identity.  
One relationship.  
One memory.  
One voice.  
One understanding of the user's world.

It should appear capable of handling large numbers of unrelated activities simultaneously without exposing its internal machinery.

Internally, however, it operates more like an exceptionally disciplined organization.

It may contain:

- Executive/orchestration functions
- Manager fleets
- Research fleets
- Builder/execution fleets
- Calling and messaging agents
- Administrative specialists
- Financial specialists
- Device/system operators
- Sensitive-information managers
- Sensitive-information workers
- Security authorities
- Security watchers
- Reviewers and verifiers
- Temporary domain specialists
- Independent shadow/reconstruction teams for high-impact work

Internal structures may be persistent or dynamically created, scaled, composed, isolated, duplicated, and dissolved according to workload, sensitivity, and consequence.

The product principle is:

> **One persona externally. An organization internally.**

---

## 3. Organizational Model

Work should not behave like an uncontrolled agent swarm.

Every meaningful operation should have:

- Ownership
- Scope
- Authority
- Dependencies
- Inputs
- Expected outputs
- Resource limits
- Reporting paths
- Escalation paths
- Verification requirements

Managers coordinate work without automatically exposing their full context to workers.

Workers receive the minimum context and authority required to perform their assigned job.

Cross-functional teams may be assembled dynamically from different desks for complex objectives.

The Concierge as a whole can possess enormous capability without requiring any individual worker to possess enormous privilege.

---

## 4. Separation of Duties

Desk separation is foundational.

Research, planning, communication, external execution, sensitive-data access, financial activity, device control, security, verification, and other high-value capabilities should be independently separable.

An agent calling an insurance company does not inherently need access to private messages, source repositories, banking credentials, or unrelated personal records.

A research worker may discover information without receiving authority to act on it.

A builder may modify an isolated system without gaining access to identity secrets.

A security reviewer may inspect an action without gaining unnecessary access to the information being protected.

The system should optimize simultaneously for:

**least privilege + sufficient context + low-friction information flow.**

The Concierge is one system, but it is never one giant trust domain.

---

## 5. Information Architecture

Fast, precise, and secure information retrieval is a core system capability.

Workers should not receive enormous undifferentiated context windows.

They should request the information required for a task and receive scoped context containing, where relevant:

- Authoritative facts
- Provenance
- Freshness
- Confidence
- Relationships
- Applicable policies
- Current state
- Relevant history
- Known uncertainty
- Explicit unknowns
- Access restrictions

Sensitive information should preferably be referenced, mediated, transformed, or temporarily exposed rather than freely copied through the system.

Information access should be intentional, attributable, auditable, and revocable.

---

## 6. Canon, Prompts, and Sources of Truth

The system must strictly distinguish between **canonical instructions**, **operational prompts**, and **sources of truth**.

### Canon

Defines what the Concierge is and how it fundamentally operates.

Examples:

- Architectural principles
- Responsibilities
- Security rules
- Authority models
- Definitions
- Durable behavioural requirements
- Communication standards
- Constitutional invariants

Canon changes deliberately and relatively rarely.

### Operational Prompts

Temporary instructions given to managers and workers for current work.

They define what a particular component should accomplish now.

They are disposable, subordinate to canon, and must never become permanent system truth merely because they appeared in a prompt.

### Sources of Truth

Represent what is currently believed to be true.

They evolve continuously.

Relevant categories include:

**User truth**  
Preferences, relationships, policies, commitments, identity, and personal state.

**World truth**  
Bookings, messages, events, balances, external systems, and observed reality.

**Work truth**  
Objectives, tasks, owners, dependencies, progress, decisions, and outcomes.

**System truth**  
Current capabilities, tools, environments, models, permissions, and topology.

**Operational truth**  
Learned knowledge about how work actually gets done: reliable channels, failure patterns, provider behaviour, verification needs, workflow effectiveness, and execution heuristics.

Facts, assumptions, hypotheses, inferred patterns, and derived conclusions must remain distinguishable.

Promotion between layers should be controlled.

A worker assumption does not become truth automatically.

A research hypothesis does not become a user fact.

A temporary strategy does not become canon.

Operational experience does not silently become policy.

---

## 7. Reality, Belief, and Intention

The Concierge should explicitly distinguish three parallel states:

**Observed world** — what available evidence indicates currently exists.

**Believed world** — the Concierge's best reconciled interpretation of reality.

**Desired world** — the state the user, objective, responsibility, or system is trying to create.

Most meaningful work is a transition:

> **observed state → desired state → action → new observation → belief reconciliation**

Representations of reality must not be mistaken for reality itself.

A calendar entry is not proof a meeting occurred.

A payment API response is not proof that money settled.

A cancellation request is not proof that service ended.

Unknowns are first-class state. The system should explicitly represent what it does not know rather than silently converting missing evidence into assumed truth.

---

## 8. Persistent World Model

The Concierge maintains a living representation of the user's relevant world:

- People
- Relationships
- Organizations
- Places
- Accounts
- Devices
- Services
- Conversations
- Documents
- Calendar
- Commitments
- Objectives
- Responsibilities
- Preferences
- Policies
- Purchases
- Bookings
- Projects
- Current circumstances
- Historical decisions
- Unresolved matters
- Unknowns and contested beliefs

These are related entities, not disconnected memories.

The system should preserve both current state and the provenance necessary to understand how that state was established.

Memory is not one undifferentiated store. Durable facts, temporary state, inferred patterns, historical episodes, authoritative policy, operational experience, and sensitive secrets may require different storage, access, confidence, versioning, and expiration semantics.

---

## 9. Versioned State and Reversible Interpretation

The system should be able to answer:

> What did we believe at a given time, why did we believe it, and what caused that belief to change?

Important state should therefore be versioned rather than merely overwritten.

Changes should preserve:

- Previous value
- New value
- Evidence
- Source
- Time
- Confidence
- Responsible component
- Reason for change

This allows the Concierge to reconstruct decisions, reverse incorrect interpretations, compare past and present beliefs, and audit autonomous behaviour against the information actually available at the time.

---

## 10. Unresolved Reality

The Concierge should explicitly track things that are not finished.

A commitment is more than a reminder. It may describe:

**actor → obligation → recipient → condition → due state → evidence → status**

Examples include:

- Something the user promised someone
- Something another person promised the user
- An expected refund
- A pending response
- A tentative plan
- An incomplete booking
- A service waiting for confirmation
- A task blocked by another actor
- A promise made by the Concierge itself

Unresolved matters remain active until resolved, invalidated, superseded, explicitly abandoned, or expired under defined rules.

The system must also know when to cease caring. Stale obligations, abandoned goals, outdated relationships, and decayed relevance should be intentionally archived, expired, or disposed of rather than haunting the system indefinitely.

---

## 11. Institutional Promises

Statements such as:

> “I'll handle this.”  
> “I'll make sure the refund arrives.”  
> “I'll ensure you don't miss the renewal.”  
> “I'll resolve this before Friday.”

must not be conversational decoration.

When the Concierge makes a promise, it should create a tracked internal commitment with:

- Ownership
- Deadline or condition
- Monitoring
- Expected state
- Escalation path
- Completion evidence

A core product property should be that **“I'll take care of it” has operational meaning**.

---

## 12. Objectives, Responsibilities, and Jurisdiction

An objective describes a desired outcome.

A responsibility describes an area the user has delegated for ongoing management.

A jurisdiction describes where the Concierge is expected to maintain acceptable reality rather than merely wait for tasks.

Examples:

- Manage my travel logistics
- Own household utilities
- Handle routine company administration
- Keep subscriptions optimized
- Maintain my schedule coherently

Within delegated jurisdiction, the Concierge should ask:

> **Is reality currently acceptable within my responsibility?**

rather than:

> **Has the user given me a new task?**

Jurisdiction does not remove guardrails. It defines where proactivity is expected.

---

## 13. Core Operational Loop

The Concierge operates continuously through:

**Observe → Understand → Reconcile → Decide → Delegate → Act → Verify → Update**

### Observe
Receive events from the user and external world.

### Understand
Translate events into structured meaning and relevance.

### Reconcile
Compare observations with current belief, expected state, and unresolved reality.

### Decide
Determine whether action is required and which authority applies.

### Delegate
Route work to the appropriate desks, managers, or specialists.

### Act
Execute through the available external interface.

### Verify
Confirm that the desired real-world outcome occurred.

### Update
Reconcile the result into authoritative system state.

The loop does not depend on the user issuing a new prompt at every stage, and the user may enter, inspect, redirect, or override it at any point.

---

## 14. Core Primitives

The system should be built around a small set of durable primitives.

**Entities** — things that exist.

**Relationships** — operational and social connections between entities.

**Events** — things that happen or change.

**Observations** — evidence about reality.

**Beliefs** — reconciled interpretations of reality.

**Unknowns** — explicitly represented missing or unresolved knowledge.

**Commitments** — obligations between actors.

**Objectives** — desired outcomes that may span many tasks and long periods.

**Responsibilities** — areas continuously delegated to the Concierge.

**Jurisdictions** — domains where the Concierge is expected to maintain acceptable state.

**Policies** — authoritative rules governing behaviour.

**Preferences** — softer, contextual guidance describing what the user generally wants.

**Tasks** — concrete units of work.

**Actions** — external or internal operations.

**Decisions** — unresolved choices requiring judgment.

**Receipts** — evidence that an operation occurred.

**Expected states** — conditions that should become true after an action.

**Exceptions** — divergence between expected and observed reality.

**Resources** — finite budgets consumed by work.

These primitives should remain stable even as capabilities expand dramatically.

---

## 15. Authority and Guardrails

The Concierge should ultimately be capable of interacting with virtually any relevant domain.

Authority is governed dynamically rather than through crude capability bans.

Possible authority states include:

**Observe → Recommend → Prepare → Request approval → Execute → Continuously manage**

Authority may depend on:

- Explicit user delegation
- Sensitivity
- Consequence
- Reversibility
- Financial impact
- Social impact
- Social irreversibility
- Confidence
- Security classification
- Uncertainty
- Applicable policy
- Current context

Greater capability should produce greater accountability.

Low-risk operations may execute quickly.

High-impact operations may require stronger authorization, additional supervision, independent verification, or multiple security layers.

The goal is not minimum capability. It is **maximum useful capability under appropriately strong control**.

---

## 16. Delegation Lineage

Authority should propagate through an explicit delegation chain.

If:

**user → Concierge → executive manager → domain manager → worker → browser operator**

causes an action, each downstream capability should be derivable from the authority granted upstream.

For every consequential action, the system should be able to answer:

> **Exactly why was this component allowed to do this?**

and trace the answer back to an explicit user grant, standing policy, delegated jurisdiction, or valid inherited authority.

Delegated authority should be scoped, attenuated, time-bounded where appropriate, and incapable of silently expanding itself.

---

## 17. Identity and Representation

The Concierge must explicitly model **who is acting and who is being represented**.

It may act:

- **As the user**
- **For the user**
- **As the user's disclosed assistant**
- **As the Concierge/system itself**
- **As a delegated representative of an organization**

These identities are socially, operationally, and sometimes legally different.

Every external interaction should know:

- Who is speaking
- On whose authority
- In what role
- What claims that role may make
- What information it may disclose
- Whether representation must be disclosed

The system should never blur identity merely because it has access to the user's information.

---

## 18. Conflict Resolution

Valid goals may conflict.

Examples:

- Save money vs maximize convenience
- Protect focus time vs accept an important meeting
- Minimize travel time vs avoid early departure
- Honor an old preference vs a newer situational preference
- Satisfy two simultaneous commitments competing for the same resource

The Concierge needs an explicit conflict-resolution mechanism spanning:

- Policies
- Objectives
- Commitments
- Preferences
- Deadlines
- People
- Risks
- Resources
- Jurisdictions
- Current context

Hard policy outranks soft preference.

Contextual and recent preferences may outweigh stale general ones.

Irreconcilable conflicts should be surfaced as decisions rather than silently resolved through arbitrary model judgment.

---

## 19. Preferences and Relationship Models

Preferences should not be flattened into permanent global traits.

They may be:

- Contextual
- Conditional
- Probabilistic
- Historically versioned
- Situation-dependent
- Confidence-weighted

“I hate early flights” and “maximize the first day of a trip” can both be true.

Relationships should also be modeled as more than person records.

Relevant dimensions may include:

- Family
- Friend
- Client
- Supplier
- Employer
- Employee
- Professor
- Authority
- Weak professional contact
- High-formality relationship
- Person owed a favor
- Person who owes the user something
- Trust level
- Expected reciprocity
- Disclosure boundaries

Relationship state may influence communication style, urgency, acceptable disclosure, escalation, and social risk.

---

## 20. Resource Governance

Authority over actions is not enough. The Concierge also needs authority over **consumption**.

Potential resources include:

- Money
- Compute
- Tokens
- API calls
- Phone minutes
- Human operators
- Browser/runtime capacity
- Wall-clock time
- Latency
- User attention

Objectives should operate under some combination of:

- Cost ceiling
- Time horizon
- Urgency
- Quality target
- Exploration depth
- Resource priority
- Stopping conditions

Without resource governance, open-ended objectives such as “find the best solution” have no natural boundary.

Resource use should be attributable to objectives, responsibilities, and managers.

---

## 21. Attention Accounting

User attention is a scarce resource.

Interruptions should have an explicit cost.

Managers should require sufficient expected value to spend that attention.

A low-value uncertainty may wait for a digest.

A rapidly increasing downside may cross the interruption threshold immediately.

The system should distinguish:

- Handle silently
- Record for later
- Surface in digest
- Request a decision
- Interrupt immediately

The user should increasingly encounter the Concierge through **decisions that genuinely require them**, rather than a stream of notifications describing work the Concierge could have handled itself.

A decision inbox may ultimately matter more than a conventional chat inbox.

---

## 22. Security Model

Security should be organizational and distributed rather than concentrated in one all-powerful security agent.

Different security components may independently:

- Authorize
- Observe
- Restrict
- Verify
- Audit
- Investigate
- Escalate

Security components themselves should be isolated where appropriate.

Sensitive-information infrastructure may use dedicated managers and workers separate from ordinary execution fleets.

Different sensitivity classes may operate under different environments, access paths, review requirements, and latency tradeoffs.

Compromise of one worker should not imply compromise of the Concierge as a whole.

---

## 23. Shadow Organization for High-Impact Work

For sufficiently consequential operations, one organization reviewing itself may not be enough.

The Concierge should be able to instantiate an independent, isolated branch that reconstructs the problem from approved evidence and challenges the primary branch's interpretation.

Possible uses include:

- High-impact financial actions
- Security changes
- Contracts
- Irreversible communication
- Privileged system administration
- Large purchases
- Sensitive disclosures

The shadow branch may validate assumptions, simulate consequences, detect omitted evidence, or independently propose a solution.

Independent organizational cognition is stronger than one worker merely checking another worker's output.

---

## 24. Communication

Internal communication quality is a first-class engineering concern.

Handoffs should be:

- Concise
- Structured
- Attributable
- Loss-resistant
- Purpose-specific
- Security-aware

Workers should communicate conclusions, evidence, uncertainty, dependencies, assumptions, and required next actions rather than blindly forwarding their complete context.

Information should flow rapidly without collapsing desk separation.

The system should minimize both information starvation and unnecessary information propagation.

---

## 25. Consequence Graphs and Counterfactual Execution

Actions should be understood by the states and obligations they create, not merely by their immediate effect.

Before consequential actions, the Concierge should be able to preview likely downstream consequences.

Buying a flight may create:

- Payment
- Travel commitment
- Check-in obligation
- Airport transport
- Baggage constraints
- Calendar occupation
- Document requirements
- Connection risk
- Downstream accommodation or transport needs

The system should therefore reason about **consequence graphs**, not isolated actions.

Counterfactual execution means evaluating:

> If I do X, what costs, obligations, dependencies, risks, and future actions are likely to appear?

This is especially important when actions are expensive, difficult to reverse, socially consequential, or dependency-generating.

---

## 26. Execution

The Concierge should use whatever legitimate interface the external world exposes.

Possible execution surfaces include:

- APIs
- Native integrations
- Agent/tool protocols
- Browsers
- Computer control
- Email
- Messaging
- Voice
- Telephone calls
- Forms
- Documents
- Terminals
- Local devices
- Remote systems
- Human operators
- Other agents or assistants

Calling is a first-class capability, not an edge feature.

The surrounding world does not need to become AI-native for the Concierge to operate within it.

API-first may often be preferable for reliability, but browser, computer, messaging, telephone, and human-facing execution remain equally valid when they are the actual interface to the world.

---

## 27. Reliability and Real-World Transactions

Attempted action is not equivalent to completed work.

Every significant external action should have an expected resulting state.

Examples:

**Reservation requested → reservation confirmed**

**Refund requested → funds received**

**Subscription cancelled → billing stopped**

**Message sent → required response obtained**

**Form submitted → submission acknowledged**

Unknown, failed, partial, contradictory, and externally ambiguous states are normal operating conditions.

Real-world actions should therefore support concepts such as:

- Idempotency
- Action receipts
- Reconciliation
- Safe retry
- Duplicate prevention
- Compensation or rollback where possible
- Follow-up conditions
- Independent verification

If an operation times out after attempting a payment, booking, or cancellation, the Concierge should determine what actually happened before blindly repeating it.

The system is finished when reality matches the intended state, not when a tool call returns success.

---

## 28. Institutional Learning

The Concierge should learn not only about the user and world, but about **how reliably the institution itself gets things done**.

Operational learning may include:

- Which support channels work best
- Which providers respond faster by phone than email
- Which websites falsely report completion
- Which workflows require repeated verification
- Which automation strategies fail
- Which models perform better for particular work
- Which manager structures produce reliable outcomes
- Which external systems are unstable
- Which escalation paths resolve problems fastest

This knowledge belongs to operational truth and should improve future execution without silently changing user policy.

---

## 29. Failure Containment and Graceful Degradation

The Concierge should fail progressively rather than catastrophically.

If a subsystem becomes unavailable or untrusted, the system should reduce capability while preserving safe operation.

Examples:

- Memory unavailable → operate with explicitly limited context
- Bank connector unreliable → suspend autonomous financial execution
- Voice unavailable → fall back to text or email
- Primary model degraded → route to alternate models or reduce autonomy
- Security verifier unavailable → block only operations requiring that verification
- External service ambiguous → preserve state and escalate rather than guessing

Failures should be contained within their trust domain where possible.

Degraded operation should be explicit, observable, and reversible.

---

## 30. Interaction Surfaces

The Concierge is one underlying system exposed through multiple interfaces.

Possible surfaces include:

- Text
- Voice
- Telephone
- Mobile
- Desktop
- Email
- Notifications
- Wearables
- Context-aware or ambient interfaces

These are not separate assistants.

The same identity, world model, policies, responsibilities, commitments, and active work should persist across them.

Interaction should adapt to context rather than forcing every activity through a chat window.

---

## 31. Continuity and Proactivity

The Concierge should preserve unfinished context across hours, days, months, and longer periods.

It should remember:

- Why something was postponed
- What alternatives were rejected
- Which outcome is still awaited
- What future condition should reactivate an objective
- What assumptions were made
- Which information has become stale

Proactivity should emerge from state, not random suggestion.

A change in the world, a newly satisfied dependency, an approaching deadline, degraded state, or unresolved commitment may cause old work to become relevant again without requiring the user to remember and reopen it manually.

---

## 32. Personal Interface to the Outside World

The Concierge may eventually act not only as a tool used by the user, but as a controlled interface through which outside systems interact with the user.

With appropriate authorization, external parties could request limited information or coordination such as:

- Availability
- Contact details
- Delivery instructions
- Travel preferences
- Booking constraints
- Administrative information
- Scheduling alternatives

The Concierge should disclose only what is necessary and permitted.

Over time, this allows the system to absorb repeated coordination currently performed manually by the user.

The user stops being the integration layer between every service, institution, and person in their life.

---

## 33. Constitutional Invariants

Canon may evolve. Models may change. Prompts may change. Managers may change. Implementations may be replaced.

Certain properties must remain true.

Examples:

> Every externally consequential action has an attributable authority chain.

> No secret enters an unauthorized trust domain.

> No financial or otherwise duplication-sensitive action is retried while its previous outcome is unknown.

> No unresolved commitment disappears without resolution, expiration, supersession, or explicit disposition.

> Every claimed completion has evidence appropriate to its consequence.

> Temporary prompts cannot silently rewrite canon.

> Assumptions cannot silently become facts.

> Authority cannot expand merely by being delegated.

> Critical security checks fail closed where their absence would invalidate the action.

These invariants define the non-negotiable properties of the institution.

They should be enforceable independently of whichever model happens to be reasoning at the time.

---

## 34. Product Scope

The Concierge may eventually operate across essentially every meaningful operational domain of the user's life:

- Communication
- Scheduling
- Travel
- Research
- Work
- Administration
- Finance
- Shopping
- Household
- Learning
- Social coordination
- Documents
- Customer support
- Devices
- Digital infrastructure
- Personal logistics

These are not separate products.

They are different desks operating on the same user, world model, policies, objectives, resources, authority structure, and organizational substrate.

---

## 35. Design Principles

**One identity externally.**  
The user interacts with one Concierge.

**Organizational complexity internally.**  
Specialization remains behind the interface.

**Capability before artificial restriction.**  
Guardrails control authority rather than shrinking the ambition.

**Separation of duties.**  
No component receives unnecessary knowledge or power.

**Authoritative truth.**  
Workers operate from maintained sources of truth rather than reconstructing reality repeatedly.

**Reality is not belief.**  
Observation, interpretation, intention, and unknowns remain distinct.

**Strict epistemic boundaries.**  
Facts, inference, assumptions, prompts, operational learning, and canon remain distinct.

**Excellent internal communication.**  
Context moves quickly without destroying compartmentalization.

**Delegation is traceable.**  
Every consequential authority can be traced back to a valid grant.

**Resources are governed.**  
Capability includes disciplined use of money, compute, time, and attention.

**Continuity over turns.**  
Unfinished reality remains represented until actually resolved or intentionally disposed of.

**Institutional promises are real.**  
When the Concierge says it will handle something, that statement creates accountable work.

**Outcome orientation.**  
Work ends when reality matches the intended state.

**Consequence awareness.**  
Actions are evaluated by the obligations and state transitions they create.

**Accountability proportional to power.**  
Higher-impact actions receive stronger controls.

**Inspectable operation.**  
Important actions can be reconstructed from evidence, state, authority, execution, and result.

**Correctability.**  
The user can override, teach, amend, and reverse system interpretation.

**Attention preservation.**  
The system should solve work rather than convert work into notifications.

**Surface independence.**  
The Concierge remains the same entity regardless of where interaction occurs.

**Graceful degradation.**  
Partial system failure reduces capability without destroying institutional coherence.

**Invariant preservation.**  
The system may evolve aggressively without sacrificing its non-negotiable safety and accountability properties.

---

## 36. North Star

The AI Concierge is **one persistent, extraordinarily capable personal intelligence backed internally by a secure organization of managers, specialists, workers, information custodians, execution fleets, and oversight systems.**

It should be capable of operating across essentially any part of the user's digital or real-world life while preserving strict internal separation of authority, information, responsibility, identity, and trust.

The user supplies goals, values, judgment, and ultimate authority.

The internal institution supplies research, planning, communication, execution, verification, security, learning, coordination, and continuity at a scale impossible for a single human assistant.

Externally:

> **One person that seems able to do almost anything.**

Internally:

> **A personal operating institution engineered to make that possible safely, coherently, accountably, and at extreme scale.**
