# Contracts

Machine-checkable interpretations of Foundation obligations. Contracts operationalize the Foundation
but **cannot invent new constitutional meaning**, and **must not depend on `profiles/`**
(`tools/check.py` enforces the latter).

| Family | State |
|---|---|
| [`constitution/`](constitution/) | Invariant record schema + registry seeded with Foundation v0.2 §28 (22 invariants) |

The remaining families from Contract Program §5 — `semantics`, `referents`, `protocol`, `identity`,
`authority`, `information`, `work`, `execution`, `effects`, `evidence`, `resources`,
`organization`, `extension`, `federation`, `simulation`, `change` — get a directory when their first
contract lands ([ADR-0002](../adr/0002-contract-naming-and-versioning.md)).
