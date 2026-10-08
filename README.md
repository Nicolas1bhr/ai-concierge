# AI Concierge

**A persistent personal intelligence — one persona outside, a disciplined organization inside.**

AI Concierge is an open-source project to build a Jarvis-like assistant that is not a chatbot, a
tool runner or a loose swarm of agents. It is a continuously operating system that understands its
owner's world, keeps state across time, pursues objectives, coordinates people and systems, acts
with *delegated* authority, verifies outcomes, and escalates when human judgment is required.

It is designed to ride the AI curve rather than be frozen by it: new models, tools, protocols and
devices are admitted as **extensions and capabilities** through a governed admission path, so the
Concierge can use whatever the landscape produces next — without any new capability silently
granting itself new power.

> If a sufficiently capable human assistant or organization could accomplish something using
> computers, phones, communication, research, services, devices, institutions, or other accessible
> interfaces, the Concierge should ultimately be capable of accomplishing it.
>
> — [Canonical Product Concept](canon/AI_CONCIERGE_CANONICAL_PRODUCT_CONCEPT.md) §1

Safety comes from architecture — authority, separation of duties, supervision, evidence and
invariants — rather than from arbitrary feature walls.

## Status

**Pre-implementation · Phase 0 (source and architecture normalization).** There is no runtime yet,
on purpose. The [Executable Contract Program](program/CONCIERGE_FOUNDATION_EXECUTABLE_CONTRACT_PROGRAM_v0.1.md)
requires the contracts and the conformance harness to exist *before* product code, so the first
codebase cannot become the constitution by momentum. See [ROADMAP.md](ROADMAP.md).

## How the repository is organized

Authority flows downward; change proposals flow upward ([Contract Program §1](program/CONCIERGE_FOUNDATION_EXECUTABLE_CONTRACT_PROGRAM_v0.1.md)).

```text
CANON                    canon/        What the product fundamentally is and must remain
  ▼
FOUNDATION               foundation/   Institutional laws, dimensions, invariants
  ▼
EXECUTABLE CONTRACTS     contracts/    Machine-checkable interpretation of the Foundation
  ▼
IMPLEMENTATION PROFILES  profiles/     Replaceable engineering choices that satisfy contracts
  ▼
RUNTIME / PRODUCT CODE   (not yet)
```

| Path | Contents |
|---|---|
| [`canon/`](canon/) | The Canonical Product Concept — highest authority |
| [`foundation/`](foundation/) | Foundation v0.2 (Unbounded Institutional Substrate); v0.1 kept under `superseded/` |
| [`program/`](program/) | The Executable Contract Program v0.1 — the bootstrap spec for this repository |
| [`contracts/`](contracts/) | Contract families; starts with the machine-readable invariant registry |
| [`formal/`](formal/) | Small formal models (TLA+ first) of authority, effects, work, federation, change |
| [`conformance/`](conformance/) | The judge before the defendant — property, stateful, adversarial and recovery suites |
| [`research/`](research/) | Dated external-claim ledger, source maturity, contradictions and open questions |
| [`adr/`](adr/) | Architecture decision records — may choose implementations, never override a higher layer |
| [`profiles/`](profiles/) | `reference-v0` and experiments — may import contracts, never the reverse |
| [`threat-models/`](threat-models/) | Threat models per boundary |
| [`design/`](design/) | Design projections (spatial / 3D compound) — derived from Canon, not Canon |
| [`PINS.yaml`](PINS.yaml) | SHA-256 pins of every higher-authority document |

## Checks

```bash
python3 -m pip install -r tools/requirements.txt
python3 tools/check.py
```

`tools/check.py` is the first executable piece of the constitution. It verifies that pinned
documents have not drifted from `PINS.yaml`, that the invariant registry validates against its
schema with unique IDs, that no invariant claims stronger enforcement than it has evidence for, and
that nothing under `contracts/` depends on `profiles/`. CI runs it on every push.

## Versioning

The repository follows [Semantic Versioning](https://semver.org). The repository version (in
[`VERSION`](VERSION) and [CHANGELOG.md](CHANGELOG.md)) is separate from each document's own
version: Canon, Foundation v0.2 and Contract Program v0.1 are versioned in their headers and pinned
by hash. Before 1.0.0, a minor bump may change contract shapes.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) first — in particular, the rule that missing semantics are
**open questions**, not invitations for code to make constitutional decisions.

## License

[GNU Affero General Public License v3.0](LICENSE). If you run a modified version as a network
service, you must offer its source to that service's users.

## Credits

Built by [Nicolas Beeckman](https://github.com/Nicolas1bhr).

The repository scaffolding, invariant registry seed and `tools/check.py` were written with Claude
Opus 5.5 (Anthropic), via Claude Code, working from the Canon, Foundation and Contract Program.
