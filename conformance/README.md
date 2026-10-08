# Conformance harness

**Build the judge before the defendant** (Contract Program §23). The harness exists before any
product runtime (Phase 3) so that implementations can be shown to be wrong.

Planned suites (§5, §23.2): `invariants/`, `property/`, `stateful/`, `schema-compatibility/`,
`differential/`, `fault-injection/`, `adversarial/`, `recovery/`, and `stress-battery/` (scenarios
001–056, §24). Every invariant's `test_obligations` in
[`contracts/constitution/invariants.yaml`](../contracts/constitution/invariants.yaml) must be met here.
