# Implementation profiles

Replaceable engineering choices that satisfy contracts. Profiles **may import contracts; contracts
never import profiles.**

- `reference-v0/` — the first reference implementation (Phase 4 onward; not started).
- `experiments/` — candidates such as the Foundation v0.1 plan (modular monolith, PostgreSQL,
  outbox, ExecutionProvider, subscription-cancellation slice), which Contract Program §1.2 demotes
  from Foundation law to a reference experiment.
