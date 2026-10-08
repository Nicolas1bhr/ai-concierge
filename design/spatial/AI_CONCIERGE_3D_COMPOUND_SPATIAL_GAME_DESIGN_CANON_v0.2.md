# AI Concierge 3D Compound — Spatial & Game Design Canon v0.2

> **Status:** Foundational game-design / spatial-architecture specification  
> **Purpose:** Define the durable spatial grammar, campus arrangement, floorplan logic, runtime-to-world mapping, navigation model, and truthfulness rules for a future HTML/3D implementation of the AI Concierge compound.  
> **Source basis:** `AI_CONCIERGE_CANONICAL_PRODUCT_CONCEPT(2).md` plus the design decisions developed in the current conversation.  
> **Important:** This document is a **design projection of the canonical product architecture**, not a replacement for the product canon. Where this document introduces spatial metaphors, they are implementation/design choices derived from the canon rather than new product truth.

---

# 0. Core Thesis

The 3D compound is not a decorative visualization of the AI Concierge.

It is a **spatial operating system and inspectable runtime model** for the AI Concierge.

The world should feel like a believable, game-like company headquarters that a human can understand almost immediately:

- offices look like offices,
- research feels like research,
- execution feels technical and industrial,
- communication spaces feel like communication spaces,
- security looks and behaves like controlled access,
- managers have recognizable workspaces,
- workers visibly own jobs,
- missions visibly move through the institution,
- buildings have believable circulation and relationships,
- ordinary architectural space exists for realism.

At the same time, the world must remain faithful to the actual software:

- a visible active worker corresponds to a real worker instance,
- a mission in a department corresponds to real assigned work,
- a handoff corresponds to a real information/task transfer,
- a door crossing a trust boundary corresponds to an authorization event,
- a temporary fleet expansion can physically expand a workplace,
- a verification state is not shown as complete until the system has appropriate evidence,
- a sensitive-data exchange is represented as mediated access rather than magical omniscience,
- a shadow organization must be genuinely isolated,
- uncertainty remains visible rather than being flattened into fake certainty.

The compound may **dramatize** the Concierge.

It must never **fictionalize its behavior**.

---

# 1. Design Philosophy

## 1.1 Believable first, abstract second

The target is approximately:

> **70% believable place / 30% software-native abstraction**

This is not a hard visual ratio. It is the design instinct.

A human should enter the world and recognize:

- a lobby,
- a research building,
- offices,
- laboratories,
- meeting rooms,
- security checkpoints,
- an archive,
- technical operations areas,
- server rooms,
- call booths,
- loading areas,
- service corridors,
- elevators,
- courtyards,
- stairs,
- lounges,
- ordinary environmental detail.

The abstraction appears where literal architecture would misrepresent the real system.

Examples:

- rooms can expand when fleets scale,
- walls can dissolve into live graphs,
- a mission can appear as a persistent physical object,
- information transfers can become visible packets,
- security overlays can reveal trust boundaries,
- context can appear as mounted packages rather than paper folders,
- consequence graphs can unfold into space,
- uncertainty can be represented as translucency, wireframes, or outlined unknowns,
- a whole remote shadow facility can activate dynamically.

The world should be intuitively understandable **before** the user understands the technical architecture.

---

## 1.2 The world is a projection, not the database

Buildings do not own the underlying data.

Rooms do not become the source of truth.

A file does not exist merely because a player walks to a shelf.

The spatial world is a **projection of canonical software objects and state**.

The same mission can be represented as:

- a physical mission capsule in the world,
- a conventional task graph,
- a command-palette result,
- an objective detail panel,
- an authority graph,
- a raw structured software object.

All views point to the same underlying runtime object.

This distinction must survive every implementation phase.

---

## 1.3 Spatial design encodes meaning

Architecture is not arbitrary.

Use spatial relationships to communicate:

- responsibility,
- collaboration frequency,
- trust separation,
- execution boundaries,
- information flow,
- authority flow,
- permanence,
- sensitivity,
- abstraction level,
- expected workflow.

The player should slowly develop a correct intuition merely by moving through the compound.

---

# 2. Environmental Truth Categories

Every meaningful object or animation should belong to one of three categories.

## Category A — Operationally Literal

What the user sees must correspond directly to live system state.

Examples:

- active agent exists,
- agent is assigned to this task,
- mission belongs to this department,
- fleet scaled from 3 workers to 8,
- tool was leased,
- security authorization succeeded,
- context was transferred,
- message was sent,
- verification is pending,
- task is blocked,
- expected state differs from observed state,
- worker was terminated,
- shadow branch was instantiated.

If the visual says this happened, the underlying system must say it happened.

---

## Category B — Semantically Representative

The visual form is fictional, but the architectural relationship is accurate.

Examples:

- Research Institute,
- manager office,
- archive,
- secure vault,
- elevator between abstraction levels,
- conference room representing temporary coordination,
- mission courier representing a structured handoff,
- loading bay representing environment/tool provisioning.

These metaphors are allowed because they help humans understand the real architecture.

---

## Category C — Environmental Fiction

Pure world-building.

Examples:

- coffee cups,
- plants,
- bathrooms,
- decorative signage,
- weather,
- non-functional furniture,
- ambient lighting,
- casual walking routes,
- architectural detailing,
- background sound,
- cafeteria activity.

These elements may make the world believable without carrying runtime meaning.

They must not accidentally look like high-confidence operational indicators.

---

# 3. The Major Campus Correction: Avoid Hub-and-Spoke Design

A naive layout puts the Concierge Tower in the middle and every facility around it.

That creates an incorrect mental model:

> every department talks only through headquarters.

The real Concierge is not supposed to operate this way.

Research may hand evidence directly to Verification.

Research may provide scoped findings to Execution.

External Relations may send receipts directly to Verification.

Execution may request resources from Resource Control.

Verification may query the World Model.

Security may intervene anywhere.

Sensitive-data infrastructure may broker a capability directly to a worker without the Tower becoming a courier.

Managers coordinate ownership and authority, but they do not need to manually relay every piece of information.

Therefore the campus must behave like a **real multi-building institution with lateral circulation**.

The Tower is important.

It is not the only road.

---

# 4. Campus Planning Principles

## 4.1 Arrange by actual collaboration frequency

Buildings that interact frequently should be physically near one another.

Examples:

- Research ↔ World Model
- Research ↔ External Relations
- Research ↔ Execution
- External Relations ↔ Verification
- Execution ↔ Verification
- Execution ↔ Resource Control
- Verification ↔ World Model
- Security ↔ Vault
- Tower ↔ World Model
- Tower ↔ Resource Control
- Tower ↔ Verification

The player should be able to guess likely workflows from the campus arrangement.

---

## 4.2 Do not encode all security with distance

Distance is useful for suggesting separation, but it is not enough.

Some nearby buildings may still be different trust domains.

Some distant buildings may have fast direct software channels.

Therefore:

- **physical proximity communicates collaboration frequency,**
- **doors/checkpoints communicate authority,**
- **overlays communicate actual trust topology.**

The environment should never imply that “close together” means “fully trusted.”

---

## 4.3 Give the campus multiple circulation systems

A real campus does not have one kind of road.

The Concierge compound should have at least four.

### A. Human / pedestrian circulation

For intuitive traversal.

Examples:

- public paths,
- courtyards,
- internal streets,
- bridges,
- normal doors,
- elevators.

### B. Operational circulation

For high-frequency work exchange.

Examples:

- internal service corridors,
- controlled staff bridges,
- mission dispatch routes,
- interdepartmental transit.

### C. Secure circulation

For privileged movement.

Examples:

- secure tunnels,
- badge-gated bridges,
- one-way airlocks,
- capability transfer hatches.

### D. Infrastructure circulation

Not necessarily walkable.

Examples:

- event buses,
- encrypted context channels,
- secret-broker links,
- runtime provisioning,
- queue traffic,
- high-volume evidence streams.

These can become visible in X-ray mode without being literal hallways.

---

# 5. Recommended Macro Campus Arrangement

The compound should be structured as a **connected institutional block**, not a star.

A useful initial graybox:

```text
                         NORTH / KNOWLEDGE + EXTERNAL EDGE

 ┌──────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
 │                  │===│                      │===│                      │
 │ RESEARCH         │   │ WORLD MODEL          │   │ EXTERNAL RELATIONS   │
 │ INSTITUTE        │   │ + ARCHIVE            │   │                      │
 │                  │   │                      │   │                      │
 └───────┬──────────┘   └──────────┬───────────┘   └──────────┬───────────┘
         │                         │                          │
         │                  ┌──────┴───────┐                  │
         │                  │ SECURE COURT │                  │
         │                  │ VAULT +      │                  │
         │                  │ SECURITY     │                  │
         │                  └──────┬───────┘                  │
         │                         │                          │
 ┌───────┴──────────┐   ┌──────────┴───────────┐   ┌──────────┴───────────┐
 │                  │===│                      │===│                      │
 │ EXECUTION        │   │ RESOURCE CONTROL     │   │ VERIFICATION +       │
 │ WORKS            │   │                      │   │ RECONCILIATION       │
 │                  │   │                      │   │                      │
 └─────────┬────────┘   └──────────┬───────────┘   └──────────┬───────────┘
           │                       │                          │
           └──────────────┐        │        ┌─────────────────┘
                          │        │        │
                    ┌─────┴────────┴────────┴─────┐
                    │                            │
                    │ CONCIERGE TOWER            │
                    │ + CENTRAL PLAZA            │
                    │                            │
                    └────────────────────────────┘

                         SOUTH / USER-FACING CORE

                                      ↓
                        REMOTE SHADOW COMPOUND
                   (no ordinary campus circulation)
```

This is not the final art direction.

It is the **functional adjacency model**.

---

# 6. Why This Arrangement Works

## 6.1 Research Institute — north-west

Research belongs beside:

- the World Model,
- External Relations,
- Execution.

It frequently needs:

- authoritative user/world context,
- external sources,
- specialist environments,
- evidence handoffs.

Research should not need to walk through the Tower every time it retrieves evidence or hands findings to another desk.

Direct routes:

- Research ↔ World Model
- Research ↔ External Relations
- Research ↔ Execution
- Research ↔ Tower

---

## 6.2 World Model + Archive — north-central

This is one of the most connected facilities.

It is positioned centrally among:

- Research,
- Tower,
- Verification,
- External Relations,
- the secure Vault.

It should feel like an institutional library/records facility on the outside and become increasingly impossible/data-native inside.

Direct relationships:

- Archive ↔ Research
- Archive ↔ Tower
- Archive ↔ Verification
- Archive ↔ External Relations for controlled retrieval
- Archive ↔ Vault through secure brokering
- Archive ↔ Security for audit/provenance cases

This is not a public shared memory room.

Most workers interact through scoped context services.

---

## 6.3 External Relations — north-east

This facility sits near a campus edge because it interfaces with the outside world.

It contains:

- browser operators,
- telephone workers,
- email agents,
- messaging agents,
- form interaction,
- external identity/representation controls.

It belongs near:

- Research, because external interaction often depends on fresh investigation,
- Verification, because outbound actions generate receipts and expected-state checks,
- World Model, because representation may require scoped user facts,
- Tower, because high-impact external communication may require escalation.

It should have both:

- internal campus access,
- a distinct external-facing perimeter.

---

## 6.4 Execution Works — south-west / operations edge

Execution is more industrial.

It benefits from proximity to:

- Research,
- Resource Control,
- Verification.

It can also sit near a service perimeter for believable:

- equipment delivery,
- runtime infrastructure,
- device labs,
- isolated environments,
- maintenance access.

Direct routes:

- Execution ↔ Research
- Execution ↔ Resource Control
- Execution ↔ Verification
- Execution ↔ Tower
- secure capability links to Vault
- embedded Security enforcement

---

## 6.5 Resource Control — south-central

Resource Control acts as a bridge between:

- Tower-level objective budgeting,
- Execution-level consumption,
- system-level capacity.

It tracks:

- money,
- compute,
- tokens,
- API calls,
- browser capacity,
- phone minutes,
- latency,
- wall-clock time,
- user attention,
- human operator capacity.

Direct routes:

- Resource ↔ Tower
- Resource ↔ Execution
- Resource ↔ Verification for cost/accounting evidence
- Resource ↔ system infrastructure
- Resource ↔ Security where policy caps or abuse controls apply

It should not look like a bank.

Think:

operations control + utilities + capacity management.

---

## 6.6 Verification + Reconciliation — south-east

Verification should sit between:

- External Relations,
- Execution,
- World Model,
- Tower.

That reflects its real role.

It receives:

- action receipts,
- external confirmations,
- expected states,
- observations,
- contradictions,
- partial outcomes.

It asks:

> did reality actually become what the mission intended?

Direct routes:

- Verification ↔ External Relations
- Verification ↔ Execution
- Verification ↔ World Model
- Verification ↔ Tower
- Verification ↔ Resource Control
- Verification ↔ Security for consequential or suspicious outcomes

This building should be one of the most connected on the campus.

---

## 6.7 Security + Vault — secure inner court

Security and sensitive-information infrastructure need proximity, but they must not collapse into one trust domain.

The area can contain two distinct facilities:

### Security Directorate

Responsible for:

- authorization systems,
- policy enforcement oversight,
- investigations,
- security review,
- incidents,
- watchers,
- escalation.

### Identity + Secret Vault

Responsible for:

- credentials,
- identity secrets,
- sensitive records,
- protected information,
- temporary secret disclosure,
- signed capabilities,
- token brokering.

The secure court should have:

- restricted vehicle/service access,
- controlled pedestrian access,
- no casual cut-through,
- dedicated secure infrastructure links.

Most ordinary agents should not physically enter the Vault.

---

## 6.8 Concierge Tower — south-central, not absolute center

The Tower remains:

- the most recognizable building,
- the user's institutional home,
- the center of objectives,
- the home of executive management,
- the primary decision interface.

But moving it slightly away from geometric center prevents the entire campus from visually becoming a monarchy around headquarters.

The Tower is **institutionally central**.

It does not need to be **geometrically dominant over every workflow**.

---

## 6.9 Shadow Compound — remote

The Shadow Compound must not share ordinary campus circulation.

It should feel genuinely independent.

Possible placement:

- distant hill,
- separate valley,
- offshore platform,
- detached second campus,
- physically remote secure complex.

The exact visual treatment can come later.

Functional rule:

> evidence may cross under controlled rules; ordinary internal assumptions and privileged context do not flow freely.

---

# 7. Campus Circulation Network

## 7.1 North Knowledge Promenade

Connects:

**Research ↔ World Model ↔ External Relations**

This is one of the most heavily trafficked pedestrian and mission routes.

Typical flows:

- research worker requests authoritative facts,
- research findings move toward external communication,
- external observations become source evidence,
- World Model provides scoped user/world context.

---

## 7.2 West Operations Lane

Connects:

**Research ↔ Execution**

Useful when:

- research produces an actionable technical plan,
- a builder needs investigation,
- a device/operator worker needs domain evidence,
- a research experiment requires an execution environment.

This route should be internal staff circulation, not public.

---

## 7.3 East Outcome Lane

Connects:

**External Relations ↔ Verification**

Extremely important.

A call, message, booking, form submission, or browser action should not visually return to the Tower just to be checked.

It can move directly into Verification.

Examples:

- airline booking confirmation,
- support case number,
- cancellation email,
- signed document,
- response from a human,
- payment receipt.

---

## 7.4 South Operational Spine

Connects:

**Execution ↔ Resource Control ↔ Verification**

This is the heavy operational side of the campus.

Typical flows:

- environment allocation,
- resource consumption,
- evidence and receipts,
- runtime capacity,
- completion verification.

This can visually feel more like a service/technical road than a landscaped pedestrian promenade.

---

## 7.5 Inner Institutional Crossings

Important cross-campus direct paths include:

- Archive ↔ Verification
- Archive ↔ Tower
- Tower ↔ Resource Control
- Tower ↔ Verification
- Tower ↔ Research
- Tower ↔ External Relations

These routes preserve executive coordination without forcing executive mediation.

---

## 7.6 Secure Court Routes

The secure court should expose:

- Security Directorate access,
- Vault broker access,
- secure archive link,
- secure Tower link,
- infrastructure-only Execution link.

Not every one of these should be represented as a normal walkable hallway.

Some should only become visible in:

- security overlay,
- infrastructure overlay,
- authority overlay.

---

# 8. Direct Adjacency Matrix

Legend:

- **H** = high-frequency direct relationship
- **M** = meaningful regular relationship
- **L** = occasional controlled relationship
- **S** = secure/brokered relationship
- **—** = no reason for ordinary direct circulation

| From / To | Tower | Archive | Research | External | Execution | Verification | Resource | Security | Vault |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Tower** | — | H | H | M | M | H | H | M | S |
| **Archive** | H | — | H | M | M | H | M | M | S |
| **Research** | H | H | — | H | H | M | L | L | S |
| **External** | M | M | H | — | L | H | L | M | S |
| **Execution** | M | M | H | L | — | H | H | M | S |
| **Verification** | H | H | M | H | H | — | M | M | S |
| **Resource** | H | M | L | L | H | M | — | M | S |
| **Security** | M | M | L | M | M | M | M | — | H |
| **Vault** | S | S | S | S | S | S | S | H | — |

Important:

The table describes **relationship strength**, not unrestricted data access.

---

# 9. Concierge Tower: Vertical Logic

The Tower represents the portion of the institution where vertical hierarchy is genuinely useful.

The spatial rule:

> **Higher floors = broader abstraction and institutional responsibility.**  
> **Lower floors = closer to runtime substrate and implementation detail.**

This is not social class.

It is abstraction depth.

---

# 10. Roof — Institutional Overview

The roof / observatory is the ultimate high-level operational view.

It may show:

- delegated jurisdictions,
- current responsibilities,
- active objectives,
- unresolved commitments,
- long-lived blockers,
- system health,
- major incidents,
- resource pressure,
- fleet density,
- degraded capabilities.

Possible spaces:

### Institution Map

A live overview of the whole Concierge organization.

### Jurisdiction Observatory

Shows areas the Concierge is expected to actively maintain.

### Health Deck

System-level model, connector, queue, capacity, and incident state.

### User Presence Terrace

A calm human-facing view of the institution.

Important rule:

> visibility does not equal authority.

Standing on the roof does not give the user/avatar or a worker magical access to every secret or operation.

---

# 11. F5 — Consequence + Strategy

One of the visually richest floors.

Think:

- war room,
- scenario studio,
- architectural planning theater,
- simulation center.

This is where the system asks:

> What happens if we actually do this?

Core spaces:

## Consequence Theater

Shows downstream state created by a contemplated action.

Example:

**Buy replacement flight**

could unfold into:

- financial transaction,
- new travel commitment,
- check-in requirement,
- airport transport,
- baggage constraints,
- calendar occupation,
- passport/document requirements,
- hotel implications,
- original-flight refund dependency,
- arrival logistics.

## Counterfactual Lab

Used for:

- comparing alternative actions,
- simulating branches,
- keeping hypothetical state visually distinct from committed state.

## Conflict Chamber

For irreconcilable conflicts among:

- hard policy,
- objectives,
- commitments,
- preferences,
- deadlines,
- people,
- risk,
- resources,
- jurisdiction,
- context.

## High-Impact Review

A preparatory environment for actions that may require:

- stronger authorization,
- independent verification,
- shadow review,
- extra security control.

---

# 12. F4 — Responsibilities + Jurisdictions

This floor should feel more like a ministry or long-lived institutional administration floor.

A responsibility is not a task.

A jurisdiction remains represented even when idle.

Example offices:

- Travel
- Company Administration
- Household
- Schedule Management
- Subscription Management
- Personal Infrastructure
- dynamically created user responsibilities

A Travel Office could show, while no mission is active:

- upcoming journeys,
- passport expiry,
- pending refunds,
- current travel commitments,
- known travel preferences,
- unresolved travel issues,
- jurisdiction health.

The floor answers:

> Is reality acceptable inside each delegated responsibility?

---

# 13. F3 — Domain Managers

This is the real organizational coordination floor.

Managers can be visibly represented as people/agents with offices.

But their workspaces must reflect actual manager scope.

A manager can see:

- owned objectives,
- task topology,
- worker assignments,
- summarized evidence,
- dependencies,
- deadlines,
- budgets,
- blockers,
- escalation state.

A manager does **not** automatically possess every worker's complete context.

Core spaces:

## Manager Atrium

Live population of managers and current ownership.

## Mission Briefing Rooms

Temporary cross-functional coordination spaces.

## Dependency Control

Cross-team blockers and dependencies.

## Escalation Gallery

Issues requiring:

- higher authority,
- clarification,
- human judgment,
- policy interpretation.

## Delegation Registry

Visualizes:

> user → Concierge → executive manager → domain manager → worker → tool

and answers:

> why exactly is this component allowed to do this?

---

# 14. F2 — Executive Operations

This is the institutional operations heart.

Core spaces:

## Mission Control

Active objectives and decomposition.

## Decision Hall

Only decisions that truly require judgment should accumulate here.

## Commitments Desk

Tracks unresolved reality:

- expected refunds,
- pending responses,
- promises made to the user,
- promises made by third parties,
- incomplete bookings,
- blocked tasks,
- future conditions.

## Attention Office

Routes events into:

- handle silently,
- record for later,
- digest,
- request decision,
- interrupt immediately.

## Resource Desk

Objective-level resource governance.

The user should increasingly encounter the Concierge through **real decisions**, not notifications describing autonomous work it could have handled itself.

---

# 15. F1 — User Interface + Concierge Identity

This floor physically expresses:

> **One person outside. Organization inside.**

Core spaces:

## Concierge Hall

The singular persistent identity the user interacts with.

## Conversation Lounge

Text/voice interactions become structured institutional events.

## Decision Inbox

Human-required decisions.

## Objective Intake

New desired outcomes enter and become structured objectives.

## Override Desk

The user may:

- correct,
- redirect,
- teach,
- amend,
- stop,
- override interpretation.

## Continuity Desk

Reopens:

- deferred objectives,
- awaiting conditions,
- historical context,
- unresolved work,
- reactivated responsibilities.

---

# 16. Ground Floor — Public Lobby + Transit

This should be intentionally simple.

The user should enter and immediately understand the place.

Possible first view:

> **Everything is operating normally**  
> 3 active objectives  
> 1 awaiting external response  
> 0 decisions needed  
> 12 autonomous actions today  
> Security healthy

Spaces:

## Reception

Search, status, teleport.

## Mission Directory

Browse:

- objectives,
- departments,
- responsibilities.

## Transit Core

Elevators / fast travel.

## Visitor Briefing

Explains:

- what is literal,
- what is metaphor,
- how to reveal real software objects.

## Incident Entrance

Fast route to:

- exceptions,
- failures,
- blocked urgent work.

## Campus Exit

Leads toward specialized facilities.

---

# 17. B1 — Runtime Fabric

The first basement is where the world becomes less office-like.

Think:

- datacenter,
- transit interchange,
- logistics center,
- execution scheduler.

This is where the operational loop becomes visible:

**Observe → Understand → Reconcile → Decide → Delegate → Act → Verify → Update**

Core spaces:

## Event Exchange

Incoming world/user events.

## Task Scheduler

Runnable work and worker allocation.

## Runtime Pool

Available:

- model workers,
- browser environments,
- execution environments.

## Capability Broker

Leases approved tools to workers.

## Retry + Idempotency Control

Prevents dangerous duplicate external actions.

## Degraded Operations

Fallbacks and reduced-capability operation.

This is infrastructure.

It should feel active and logistical.

---

# 18. B2 — Infrastructure + System Truth

Closer to raw software reality.

Spaces:

## Model Routing

Current model pools and routing policy.

## Connector Registry

APIs and native integrations.

## Environment Registry

Browsers, terminals, sandboxes, devices.

## Topology Room

Services and trust-domain structure.

## System Truth Store

Current:

- capabilities,
- versions,
- permissions,
- health.

## Operational Learning Link

Institutional knowledge about:

- what channels work,
- what workflows fail,
- which providers misreport completion,
- which models are reliable,
- which escalation paths work.

Operational learning must not silently rewrite user policy.

---

# 19. Canonical Department Interior

The same organizational grammar should repeat in:

- Research,
- Travel,
- Finance,
- Administration,
- Communication,
- Build,
- other domain departments.

The décor changes.

The logic should remain learnable.

---

## 19.1 Open Work Floor

Visible active workers.

Important rule:

> desk population corresponds to actual worker population.

If there are five live workers:

- five workstations are active.

If the fleet scales to twenty:

- the physical workplace expands,
- temporary desks or a modular wing appears.

If the fleet dissolves:

- temporary workers leave,
- their evidence remains.

---

## 19.2 Manager Office

Contains:

- objective ownership,
- worker assignments,
- budgets,
- deadline state,
- dependencies,
- escalations.

Not unrestricted raw context.

---

## 19.3 Context Counter

Think:

> reference desk + secure retrieval terminal

Workers request scoped information here.

Returned context should expose:

- authoritative facts,
- provenance,
- freshness,
- confidence,
- relevant relationships,
- applicable policy,
- current state,
- relevant history,
- uncertainty,
- explicit unknowns,
- access restrictions.

Workers do not share a magical omniscient memory cloud.

---

## 19.4 Mission Room

Temporary cross-functional room.

Created only when a real objective needs coordination.

A mission room may contain:

- manager,
- research worker,
- execution specialist,
- reviewer.

But it represents a real coordination context.

No decorative fake meetings.

---

## 19.5 Evidence Dock

Work exits as:

- conclusion,
- evidence,
- sources,
- uncertainty,
- dependencies,
- receipts,
- next required action.

Not the complete hidden internal context of every participant.

---

## 19.6 Tool Room

Shows currently leaseable or leased capabilities:

- browser,
- terminal,
- connector,
- telephone,
- device,
- specialist model,
- execution environment.

Tools are leased.

Workers do not automatically own them forever.

---

## 19.7 Escalation Room

Blocked work appears here instead of being silently guessed through.

Examples:

- ambiguous user intent,
- policy conflict,
- missing authority,
- contradictory evidence,
- insufficient confidence,
- external failure.

---

## 19.8 Restricted Doors

A real trust-domain boundary.

A denied worker should be able to expose:

- which policy blocked access,
- what authority is missing,
- whether escalation is possible,
- whether a mediated alternative exists.

---

# 20. Workstations as Debuggers

A workstation is not just visual decoration.

At close inspection it becomes a system-debugging surface.

A worker workstation should expose:

- worker ID,
- role,
- owning manager,
- objective,
- task contract,
- model/runtime,
- prompt/instructions,
- current context mounts,
- known facts,
- explicit unknowns,
- leased tools,
- authority scope,
- delegation lineage,
- cost/resource budget,
- dependencies,
- current activity,
- current uncertainty,
- latest output,
- expected deliverable,
- escalation route.

This is where the game becomes genuinely useful for operating the software.

---

# 21. Agents at Three Distances

## Across the room

Only show:

- role,
- team,
- activity state.

Example:

> Research worker — working

---

## Standing nearby

Show:

- worker name/ID,
- task,
- manager,
- execution state,
- authority category.

Example:

> Travel Research Worker #48  
> Task: Find same-day alternatives  
> Manager: Travel Manager #2  
> State: Waiting for search results  
> Authority: External read-only research

---

## Inspect workstation

Reveal full runtime detail.

This level-of-detail system prevents visual overload.

---

# 22. Agent Animation Rules

Agents may:

- walk,
- type,
- brief one another,
- enter rooms,
- use equipment,
- wait,
- leave.

But meaningful animation must follow live state.

Examples:

- a waiting worker should visibly wait,
- a blocked worker should not fake progress,
- a worker using a browser can move toward a browser workstation,
- a mission handoff can physically travel,
- a temporary worker disappears after termination,
- a manager entering a mission room corresponds to real coordination.

Ambient humanizing animations are allowed as environmental fiction.

Operational animations must remain truthful.

---

# 23. The Mission Object

Every active objective should have a persistent physical representation.

Working concept:

> **Mission Capsule**

Alternatives:

- dossier,
- briefcase,
- document wallet,
- project container,
- mission token.

The visual form can change later.

The important property is continuity.

Agents come and go.

The objective persists.

---

## 23.1 Example Mission

User says:

> “Sort out my cancelled flight.”

Mission Capsule:

**Objective**  
Get user home tonight.

**Desired state**  
Confirmed viable journey home.

**Observed current state**  
Original flight cancelled.

**Owner**  
Travel Manager.

**Budget**  
≤ €450 additional spend.

**Authority**  
- research automatically,
- prepare alternatives automatically,
- purchase replacement ≤ €250 automatically,
- above €250 request approval.

**Dependencies**
- current booking,
- identity details,
- document validity,
- available transport.

The player can follow this single object through the institution.

---

# 24. Mission Lifecycle Through the Campus

A typical mission might travel:

1. Concierge Hall  
2. Executive Operations  
3. World Model  
4. Research  
5. Domain Manager  
6. External Relations or Execution  
7. Verification  
8. World Model update  
9. Tower completion  
10. temporary fleet dissolution

This is not mandatory choreography.

Different work takes different paths.

Examples:

### Pure research objective

Tower → World Model → Research → Tower

### Technical fix

Tower → Research → Execution → Verification → Tower

### Customer-support problem

Tower → World Model → Research → External Relations → Verification → Tower

### High-impact financial action

Tower → Strategy → Research → Resource Control → Shadow Compound → Execution → Verification → Tower

### Secret-mediated external transaction

External Relations ↔ Vault broker ↔ Verification

The campus must therefore support lateral routes.

---

# 25. Information Handoffs

A handoff may be represented physically as:

- a mission packet,
- evidence container,
- secure capsule,
- context bundle.

Click it to inspect:

- sender,
- destination,
- purpose,
- task,
- information scope,
- provenance,
- authority basis,
- sensitivity,
- expiry,
- allowed retention,
- redactions.

A transfer should not simply show a giant context dump.

The system values:

> concise, structured, attributable, loss-resistant, purpose-specific, security-aware communication.

The visual world should teach that.

---

# 26. World Model + Archive

This building should eventually become one of the project's signature environments.

Outside:

- library,
- archive,
- records institution,
- knowledge center.

Inside:

the geometry becomes increasingly impossible.

The building should visibly distinguish different epistemic and authoritative layers.

---

## 26.1 Canon Chamber

Feels:

- permanent,
- quiet,
- heavy,
- deliberate.

Contains:

- architectural principles,
- security rules,
- constitutional invariants,
- authority models,
- definitions,
- durable behavioral requirements.

Canon changes should visually feel consequential.

---

## 26.2 Operational Prompt Area

Temporary and disposable.

The architecture should communicate that prompts are **current instructions**, not permanent truth.

Possibly:

- mission brief stations,
- active instruction boards,
- ephemeral rooms.

---

## 26.3 User Truth Wing

Contains user-related authoritative state:

- preferences,
- relationships,
- commitments,
- identity information,
- policies,
- personal state.

Sensitive data may not be directly visible without authorization.

---

## 26.4 World Truth Wing

Contains:

- bookings,
- messages,
- events,
- balances,
- external system state,
- observed reality.

---

## 26.5 Work Truth Wing

Contains:

- objectives,
- tasks,
- owners,
- dependencies,
- progress,
- decisions,
- outcomes.

---

## 26.6 System Truth Wing

Contains:

- models,
- capabilities,
- tools,
- environments,
- permissions,
- topology.

---

## 26.7 Operational Truth Wing

Contains learned institutional knowledge about:

- which support channels work,
- which providers respond,
- failure patterns,
- workflow effectiveness,
- verification requirements,
- model suitability.

Operational learning does not silently become user policy.

---

## 26.8 Relationship / World Graph Hall

A person, organization, project, device, account, booking, or commitment is not a disconnected memory.

The hall becomes a living graph.

Walk toward a person.

Related regions appear.

Open a company.

See:

- people,
- documents,
- projects,
- accounts,
- obligations,
- communication,
- decisions.

This is where the “library” metaphor deliberately breaks into graph-native visualization.

---

# 27. Versioned State Gallery

The system must be able to answer:

> what did we believe at time X, why, and what caused that belief to change?

Therefore important objects have time depth.

A current fact can be pulled backward.

Example:

```text
Sep 18 — believed flight 21:15
Sep 20 — external schedule changed
Sep 22 — new booking evidence received
Current — believed departure 20:45
```

Each change can expose:

- previous value,
- new value,
- evidence,
- source,
- time,
- confidence,
- responsible component,
- reason.

This is a visual debugger for institutional belief.

---

# 28. Uncertainty as a First-Class Visual Language

Unknowns must not disappear.

Potential visual grammar:

- **solid** = observed / verified
- **semi-transparent** = inferred / belief
- **wireframe** = hypothesis / candidate state
- **outlined empty slot** = explicit unknown
- **flickering conflict marker** = contradictory evidence
- **ghosted historical form** = previous belief
- **dashed future geometry** = desired or expected state

Do not rely solely on color.

Use:

- material,
- shape,
- line style,
- iconography,
- label,
- interaction detail.

---

# 29. Observed vs Believed vs Desired Reality

A powerful overlay should let the player inspect all three.

Example:

### Observed

Airline website says cancelled.

### Believed

Flight is cancelled.

### Desired

Confirmed replacement travel.

### Expected next state

Replacement booked.

### Unknown

Refund status.

The environment can render these as overlapping spatial states.

This is one of the concepts that justifies 3D rather than ordinary tables.

---

# 30. Execution Works

This facility should feel more industrial than corporate.

Think:

- software engineering campus,
- robotics lab,
- test facility,
- operations center,
- factory.

Core bays:

---

## 30.1 Browser Bay

Shows:

- browser sessions,
- target site,
- active operator,
- authentication scope,
- network state,
- current task.

---

## 30.2 Terminal Bay

Shows:

- repository,
- branch,
- environment,
- process,
- shell authority,
- execution history.

---

## 30.3 Device Lab

Represents:

- user computers,
- phones,
- servers,
- remote systems,
- other controlled devices.

---

## 30.4 API Bay

Less literal.

Can look like a high-throughput machine hall.

Represents:

- API execution,
- connector actions,
- structured machine-to-machine work.

---

## 30.5 Builder Hangars

Temporary and scalable.

If a task needs 15 workers:

- capacity visibly expands.

When complete:

- fleet dissolves,
- temporary rooms disappear,
- evidence and outputs remain.

The architecture itself may change because the organization itself is dynamic.

---

# 31. External Relations

External Relations represents the boundary between the Concierge and human/external systems.

Core areas:

- Voice Wing
- Browser Wing
- Messaging Wing
- Email Wing
- Forms / Administrative Desk
- Identity Checkpoint
- Representation Control

---

## 31.1 Identity Checkpoint

Every external interaction knows:

- who is speaking,
- on whose authority,
- in which role,
- what claims are allowed,
- what information may be disclosed,
- whether representation must be disclosed.

Before a call booth:

```text
REPRESENTATION

Acting as:
User's disclosed assistant

Authority:
Travel support

Allowed disclosure:
Booking reference
Passenger name

Denied:
Unrelated messages
Financial records
```

The worker then enters.

This turns identity policy into intuitive spatial behavior.

---

# 32. Identity + Secret Vault

The Vault must not behave like a normal video-game locked room.

The design should teach:

> sensitive information is usually mediated, not copied.

Most workers should never physically enter.

Instead:

1. worker requests capability,
2. policy evaluates request,
3. Vault returns a narrowly scoped capability,
4. capability expires.

Example:

```text
PAYMENT AUTHORITY

Merchant:
Wizz Air

Maximum:
€350

Expires:
08:43

Raw card details exposed:
NO
```

This may physically arrive as a secure capsule.

The worker receives power to perform the operation without necessarily receiving the underlying secret.

---

# 33. Verification + Reconciliation

This may be one of the most important facilities in the entire compound.

The world must distinguish:

> attempted action

from:

> verified outcome.

Example:

### Desired

Hotel cancelled.

### Tool response

“Cancellation successful.”

### Observation

No confirmation received.

### Belief

Likely cancelled.

### State

Pending verification.

The mission remains visibly incomplete.

Later:

- cancellation email arrives,
- no future charge exists,
- expected state is confirmed.

Only then:

- mission is completed,
- evidence is recorded,
- World Model updates,
- Tower receives completion.

This makes outcome-oriented reliability physically understandable.

---

# 34. Security Model

Security is both:

- a facility,
- and an architectural property of the entire campus.

The Security Directorate houses:

- investigations,
- incident response,
- security operations,
- access reviews,
- watchers.

But real enforcement exists everywhere.

Visible mechanisms:

- badge checkpoints,
- one-way information hatches,
- quarantine doors,
- approval terminals,
- audit sensors,
- tool guards,
- credential brokers,
- secure environment boundaries,
- restricted elevators,
- privileged service tunnels.

Security is ambient infrastructure.

---

# 35. Security Overlays

A dedicated X-ray mode can reveal actual trust topology.

Possible conventions:

- **solid connection** — persistent authorized channel
- **dashed connection** — temporary delegated capability
- **arrow-only connection** — one-way information flow
- **locked edge** — explicit approval needed
- **dark zone** — viewer lacks authority to inspect content
- **bright sensor node** — independent watcher/auditor
- **isolated shell** — sandbox / quarantined environment

The physical world remains readable.

The overlay reveals the software truth.

---

# 36. Shadow Compound

The Shadow Compound must feel independent.

It should not be a wing of Security.

It should not be a room in the Tower.

For high-impact work:

1. primary organization develops interpretation/action,
2. approved evidence bundle is created,
3. bundle crosses a controlled transfer,
4. remote shadow organization reconstructs problem independently,
5. shadow branch challenges assumptions or proposes alternative,
6. result returns for comparison.

Possible use:

- financial action,
- security changes,
- contracts,
- irreversible communication,
- privileged administration,
- large purchases,
- sensitive disclosure.

The point is independent organizational cognition.

---

# 37. Resource Control

Resource governance must be visible.

Potential resources:

- money,
- compute,
- tokens,
- API calls,
- browser capacity,
- phone minutes,
- human operators,
- wall-clock time,
- latency,
- user attention.

An objective could have a physical resource panel:

```text
OBJECTIVE RESOURCE ENVELOPE

Money:
€450 / €600

Compute:
31%

Token budget:
48%

Deadline:
2h 15m

User attention:
0 interruptions spent

Exploration depth:
High

Stopping condition:
Confirmed viable return trip
```

Resource use should be attributable to:

- objective,
- responsibility,
- manager.

---

# 38. Attention as a Resource

User attention deserves its own visual concept.

Managers should not interrupt the user merely because they are uncertain.

Possible routing:

- silent,
- record,
- digest,
- decision request,
- immediate interruption.

The game can expose why something crossed the threshold.

Example:

```text
INTERRUPTION JUSTIFICATION

Potential downside:
€1,280

Time sensitivity:
21 minutes

Autonomous authority:
Insufficient

Confidence:
0.71

Decision required:
YES
```

---

# 39. Runtime Overlays

The world should support switchable global overlays.

---

## Work Overlay

Shows:

- objectives,
- tasks,
- owners,
- dependencies,
- blockers,
- queues,
- execution state.

---

## Information Overlay

Shows:

- context packets,
- provenance,
- freshness,
- uncertainty,
- current mounted information,
- information movement.

---

## Authority Overlay

Shows:

> user → Concierge → manager → worker → tool

including:

- scope,
- expiry,
- restrictions.

---

## Security Overlay

Shows:

- trust domains,
- access gates,
- watchers,
- secret boundaries,
- isolated environments.

---

## Reality Overlay

Shows:

- observed,
- believed,
- desired,
- expected,
- unknown.

---

## Resource Overlay

Shows:

- money,
- compute,
- tokens,
- time,
- API usage,
- phone usage,
- attention budget.

---

## Evidence Overlay

Shows:

- receipts,
- proof,
- citations,
- completion claims,
- unverified outcomes.

---

## Consequence Overlay

Shows downstream:

- obligations,
- costs,
- dependencies,
- risks,
- follow-up.

---

## Failure Overlay

Shows:

- degraded systems,
- quarantined services,
- unavailable capabilities,
- fallback routes,
- blocked fail-closed actions.

---

# 40. Navigation Model

The world needs four forms of navigation.

The game world must never make serious operation slower than a traditional interface.

---

## 40.1 Physical Navigation

- walk,
- stairs,
- doors,
- elevators,
- campus paths.

Best for:

- exploration,
- learning,
- watching work.

---

## 40.2 Fast Travel

Click:

- building,
- floor,
- room,
- objective,
- worker.

Teleport immediately.

---

## 40.3 Semantic Navigation

Command palette examples:

```text
refund
Travel Manager
Wizz Air
show blocked tasks
show agents with payment authority
why did we call this company?
pending commitments
```

The system resolves the object and takes the player there.

---

## 40.4 Graph Navigation

One key changes representation entirely.

Possible graph modes:

- objective graph,
- authority graph,
- information graph,
- relationship graph,
- consequence graph,
- dependency graph.

Exit graph mode.

Return to same physical location.

The world is never a prison.

---

# 41. HUD / Game UX

The interface should feel closer to a polished strategy/management game than enterprise software.

Core HUD:

## Objective Tracker

Like a quest tracker.

Shows:

- active objectives,
- waiting conditions,
- deadlines,
- blockers,
- decisions.

## Minimap

Buildings light up by:

- activity,
- incident,
- blocked work,
- user-required action.

## Command Palette

Universal navigation and action surface.

## Interaction Reticle

Look at:

- person,
- workstation,
- mission,
- door,
- screen,
- package.

One obvious primary interaction.

## Layer Wheel

Possible layers:

- Normal
- Work
- Information
- Authority
- Security
- Resources
- Reality

## Breadcrumb

Example:

```text
Cancelled Flight
› Travel Manager
› Airline Research
› Worker 12
› Lufthansa source
```

---

# 42. Realism and Ordinary Space

The compound should include boring spaces.

This matters.

Include:

- bathrooms,
- cafeterias,
- break rooms,
- lounges,
- hallways,
- maintenance corridors,
- stairs,
- courtyards,
- windows,
- service doors,
- loading areas,
- parking/service access,
- plants,
- ordinary furniture.

Do not assign a metaphor to everything.

Not every coffee machine should represent token budgets.

Ordinary reality gives contrast to the parts that actually carry software meaning.

---

# 43. The Core Human Questions the World Must Answer

Without documentation, the player should be able to discover:

- Who owns this work?
- Where is it currently happening?
- Which manager is responsible?
- What information does the worker have?
- Where did that information come from?
- What remains unknown?
- Who is allowed to act?
- Why are they allowed?
- What tools are available?
- What is blocked?
- What has actually happened?
- What is merely believed?
- What outcome is desired?
- What evidence exists?
- What does the user need to decide?
- What happens next?

If the world answers these intuitively, the 3D layer is doing real product work.

---

# 44. Core Game Loop

The player loop should not be:

> walk around the office.

It should be:

> **notice → inspect → follow → understand → intervene if wanted**

Example:

1. enter lobby,
2. see 3 missions active / 1 blocked,
3. select blocked mission,
4. teleport or physically follow it,
5. arrive in Research,
6. see worker waiting,
7. inspect dependency,
8. jump to required identity record,
9. resolve ambiguity,
10. mission automatically resumes.

This is effectively a:

> **first-person debugger for autonomous institutional software**

---

# 45. Example Full Mission Walkthrough

Objective:

> “Fix my cancelled flight and get me home tonight.”

---

## Step 1 — Concierge Hall

Mission Capsule appears.

The user sees:

- desired state,
- current state,
- authority,
- budget,
- deadline.

---

## Step 2 — Executive Operations

Travel responsibility owns the mission.

Travel Manager instantiated/activated.

Mission decomposed into:

- booking state,
- replacement research,
- refund status,
- user constraints,
- external communication.

---

## Step 3 — World Model

Scoped context retrieved:

- booking,
- identity,
- travel preferences,
- calendar,
- location,
- commitments.

---

## Step 4 — Research Institute

Multiple workers may spawn.

Examples:

- alternative flights,
- rail alternatives,
- airline policy,
- refund rights.

Temporary desks appear.

---

## Step 5 — Domain Manager

Travel Manager receives structured results.

Not raw unlimited worker context.

Dependencies reconciled.

---

## Step 6 — Strategy Floor

Candidate plans compared.

Consequence graph created.

Example:

Option A:
- €190
- late arrival
- no hotel impact

Option B:
- €340
- earlier arrival
- taxi needed

---

## Step 7 — Authority Check

If action fits delegation:

continue automatically.

If not:

Decision Hall surfaces one decision.

---

## Step 8 — External Relations

Booking worker enters browser/phone environment.

Identity checkpoint verifies representation.

Payment capability may be requested from Vault.

---

## Step 9 — Vault

Temporary payment authority issued.

Raw secret not copied.

---

## Step 10 — External Action

Booking attempted.

Receipt created.

But mission is not complete.

---

## Step 11 — Verification

Checks:

- booking confirmed,
- payment settled,
- ticket exists,
- itinerary valid.

If ambiguous:

mission remains pending.

---

## Step 12 — World Model Update

New travel state becomes authoritative.

Consequences create:

- check-in commitment,
- calendar update,
- transport dependency.

---

## Step 13 — Tower

Mission reaches desired state.

Completion evidence available.

Temporary workers dissolve.

Institution retains:

- evidence,
- history,
- operational learning,
- unresolved follow-up.

---

# 46. Failure / Degradation as Spatial Behavior

Partial system failure should reduce capability visibly.

Examples:

### Memory unavailable

World Model area shows degraded state.

Workers operate with explicit context limitation.

### Bank connector unreliable

Financial execution bays close.

Research and recommendation remain available.

### Voice unavailable

Voice Wing darkens.

Messaging/email routes remain.

### Primary model degraded

Runtime Fabric reroutes workers.

### Security verifier unavailable

Only operations requiring that verifier become blocked.

The whole compound should not enter fake catastrophic failure.

Failures remain bounded to trust/capability domains where possible.

---

# 47. Building Relationships Must Be More Important Than Buildings Themselves

Do not over-focus on architecture.

The campus succeeds if the player develops an intuition for:

- which teams cooperate,
- which work can flow laterally,
- which boundaries are difficult to cross,
- where evidence goes,
- where execution happens,
- where sensitive information lives,
- where authority originates,
- where work is verified.

The physical buildings are a teaching mechanism for the organization.

---

# 48. HTML / Web Prototype Translation

This document is intended to become the basis for a future HTML/3D prototype.

The implementation should keep spatial data separated from rendering.

Do not hard-code semantics into meshes.

---

## 48.1 Core Data Objects

Suggested conceptual objects:

```text
Campus
Building
Floor
Room
Route
TrustDomain
Objective
Mission
Task
Worker
Manager
ContextPacket
EvidencePacket
CapabilityLease
AuthorityGrant
Observation
Belief
Unknown
ExpectedState
Receipt
Exception
ResourceEnvelope
SecurityEvent
```

---

## 48.2 Building Object

Conceptual shape:

```json
{
  "id": "verification",
  "name": "Verification + Reconciliation",
  "position": [0, 0, 0],
  "trustDomain": "verification",
  "purpose": "Confirm real-world outcomes",
  "adjacentBuildings": [
    "external-relations",
    "execution",
    "world-model",
    "resource-control",
    "concierge-tower"
  ],
  "floors": [],
  "runtimeState": {
    "activeWorkers": 7,
    "pendingMissions": 4,
    "exceptions": 1
  }
}
```

The renderer consumes the state.

The building does not become the state store.

---

## 48.3 Route Object

```json
{
  "id": "external-verification-east-lane",
  "from": "external-relations",
  "to": "verification",
  "routeType": "operational",
  "walkable": true,
  "authorityBoundary": true,
  "trustCrossing": true,
  "visualMode": "staff-bridge"
}
```

---

## 48.4 Room Object

```json
{
  "id": "travel-research-workfloor",
  "building": "research",
  "floor": "travel",
  "roomType": "work-floor",
  "ownedBy": "travel-research-manager",
  "trustDomain": "research",
  "populationSource": "runtime.workers.travelResearch",
  "capacityBehavior": "dynamic-expand"
}
```

---

## 48.5 Worker Object

```json
{
  "id": "worker-48",
  "role": "travel-research-worker",
  "manager": "travel-manager-2",
  "objective": "objective-flight-recovery",
  "task": "find-same-day-alternatives",
  "state": "waiting",
  "location": "research.travel.workfloor",
  "contextMounts": [],
  "capabilityLeases": [],
  "authorityGrant": "grant-932",
  "resources": {},
  "uncertainty": {}
}
```

---

# 49. Rendering Principle for HTML / 3D

The rendering hierarchy should be something like:

```text
canonical state
    ↓
runtime projection model
    ↓
spatial state
    ↓
3D scene
    ↓
HUD / overlays
```

Never:

```text
3D scene
    ↓
invent state
```

The scene reflects the system.

It does not fabricate it.

---

# 50. Recommended Initial HTML Prototype Scope

Do not begin with final 3D art.

First prove the spatial model.

Phase 1:

- top-down campus,
- buildings,
- direct routes,
- selectable nodes,
- active mission object,
- worker counts,
- trust overlay,
- task overlay.

Phase 2:

- tower floor navigation,
- department interiors,
- worker desks,
- mission movement,
- context/evidence packets.

Phase 3:

- first-person/third-person navigation,
- building interiors,
- level streaming,
- environmental art.

Phase 4:

- live runtime integration,
- real agent state,
- real execution state,
- real security state.

Phase 5:

- advanced overlays,
- consequence theater,
- World Model graph hall,
- Shadow Compound.

---

# 51. Graybox Order

Recommended order for game design.

## Graybox 1 — Campus circulation

Build only:

- terrain,
- building masses,
- main paths,
- operational routes,
- secure court,
- Tower,
- remote shadow marker.

Question:

> Can I understand why each building is where it is?

---

## Graybox 2 — One mission journey

Use one synthetic mission.

Example:

> cancelled flight recovery

Make it travel through the campus.

Question:

> Does work move naturally without always returning to headquarters?

---

## Graybox 3 — One department

Build Research or Travel.

Include:

- manager,
- work floor,
- context counter,
- mission room,
- evidence dock,
- tool room.

Question:

> Can I understand manager/worker/context/tool separation by looking?

---

## Graybox 4 — One security crossing

Create a worker who needs sensitive capability.

Question:

> Does the player understand that authority and secrets are mediated?

---

## Graybox 5 — Verification

Attempt an external action.

Make the result ambiguous.

Question:

> Can the world visually communicate “tool succeeded, reality not yet proven”?

---

## Graybox 6 — Overlays

Add:

- Work
- Authority
- Security
- Reality

Question:

> Can the player peel the metaphor away and see the real system?

---

# 52. What Should Be Stable Before Art Production

Freeze:

- campus adjacency,
- major routes,
- Tower abstraction floors,
- facility responsibilities,
- trust-domain logic,
- mission lifecycle,
- truthfulness categories,
- overlay semantics,
- workstation semantics.

Do **not** freeze yet:

- façade style,
- architectural era,
- materials,
- exact building dimensions,
- brand color,
- NPC visual identity,
- camera style,
- final mission-object appearance,
- landscaping,
- interior decoration.

Those should come after functional grayboxing.

---

# 53. Spatial Rules to Treat as Canonical for the Visualization

1. **The Tower is institutionally central but not the only route.**
2. **Departments may communicate laterally when architecture permits it.**
3. **High-frequency collaboration should create physical adjacency.**
4. **Trust boundaries remain explicit even between nearby buildings.**
5. **Sensitive information is normally mediated rather than copied.**
6. **Worker population corresponds to real runtime population.**
7. **Mission movement corresponds to real work movement.**
8. **Important handoffs correspond to real context/evidence transfer.**
9. **Verification is separate from execution.**
10. **The system never displays attempted work as confirmed reality without evidence.**
11. **Authority crossings are inspectable.**
12. **Unknowns remain first-class state.**
13. **Temporary organizational structures may physically appear and disappear.**
14. **Shadow work is genuinely isolated.**
15. **Physical navigation is optional; semantic navigation is always available.**
16. **Every metaphor can reveal its underlying software object.**
17. **Environmental realism is allowed without assigning software meaning to everything.**
18. **The world may dramatize the system but must not fictionalize operational behavior.**

---

# 54. North-Star Experience

A user should eventually be able to:

walk into the compound,

see the organization alive,

notice that Research is unusually busy,

follow a mission packet from Research to External Relations,

see it cross an identity checkpoint,

watch an external action occur,

follow the resulting receipt directly to Verification,

see Verification hold the mission because reality is still ambiguous,

switch on the Reality overlay,

see:

- observed,
- believed,
- desired,
- unknown,

open the Authority overlay,

trace:

> user → Concierge → Travel Manager → External Worker → browser capability,

jump to the World Model,

inspect why the system believes what it believes,

correct one assumption,

watch the mission resume,

and eventually see the verified objective close.

At no point should the user need to understand agent architecture first.

The architecture teaches itself through the world.

---

# 55. Product-Level Purpose of the 3D Compound

The compound is simultaneously:

### A human interface

A way to understand and control a system that may otherwise become too complex to reason about.

### An observability environment

A live view of the organization, workers, objectives, dependencies, failures, and resources.

### A security interface

A way to inspect trust domains, authority, data movement, sensitive access, and security intervention.

### A debugging environment

A way to inspect:

- workers,
- context,
- tool access,
- state,
- evidence,
- beliefs,
- unknowns.

### A management interface

A way to see:

- responsibilities,
- missions,
- budgets,
- managers,
- queues,
- commitments.

### A game-like representation

A world that is enjoyable and intuitive enough that users actually want to explore it.

The strongest version of the idea is not:

> “a game showing agents.”

It is:

> **a navigable spatial operating institution whose game-like world happens to expose the exact inner workings of the AI Concierge.**

---

# 56. Canonical Product Grounding

This spatial design is primarily derived from the following concepts in the AI Concierge Canonical Product Concept:

- §2 — One Person Outside, an Organization Inside
- §3 — Organizational Model
- §4 — Separation of Duties
- §5 — Information Architecture
- §6 — Canon, Prompts, and Sources of Truth
- §7 — Reality, Belief, and Intention
- §8 — Persistent World Model
- §9 — Versioned State and Reversible Interpretation
- §10 — Unresolved Reality
- §11 — Institutional Promises
- §12 — Objectives, Responsibilities, and Jurisdiction
- §13 — Core Operational Loop
- §14 — Core Primitives
- §15 — Authority and Guardrails
- §16 — Delegation Lineage
- §17 — Identity and Representation
- §18 — Conflict Resolution
- §20 — Resource Governance
- §21 — Attention Accounting
- §22 — Security Model
- §23 — Shadow Organization for High-Impact Work
- §24 — Communication
- §25 — Consequence Graphs and Counterfactual Execution
- §26 — Execution
- §27 — Reliability and Real-World Transactions
- §28 — Institutional Learning
- §29 — Failure Containment and Graceful Degradation
- §31 — Continuity and Proactivity
- §33 — Constitutional Invariants
- §35 — Design Principles
- §36 — North Star

The spatial design should continue to evolve **downstream of that canon**.

If a future visual idea conflicts with the core architectural model, the visual idea loses.

---

# 57. Immediate Next Design Work

The next detailed design exercise should be:

> **One complete grayboxed mission from objective creation to verified real-world completion, using the campus circulation defined here.**

That mission should explicitly demonstrate:

- a Tower-originated objective,
- World Model retrieval,
- Research work,
- direct Research ↔ External or Research ↔ Execution movement,
- a lateral inter-building handoff that does **not** return through the Tower,
- an authority check,
- a mediated sensitive capability,
- an external action,
- Verification,
- an ambiguous intermediate state,
- eventual confirmation,
- World Model update,
- mission closure,
- temporary fleet dissolution.

If that sequence feels intuitive in the graybox, the architecture is working.

If it feels like the player is walking arbitrary distances because “the building is over there,” the circulation network must be corrected before visual production.

---

## End of Spatial & Game Design Canon v0.2
