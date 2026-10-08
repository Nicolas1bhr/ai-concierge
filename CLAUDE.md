# Working on AI Concierge

Contracts before code. Read `CONTRIBUTING.md` (authority flows down; missing semantics are open questions, not choices for code)
and `ROADMAP.md` (the current phase and its gate) before planning anything.

## Orchestration

Before any delegated or multi-agent work — one agent or a fleet — read
[`docs/ORCHESTRATION-STANDARD.md`](docs/ORCHESTRATION-STANDARD.md), the shared standard (version 2026-10-08,
synced from TradeAgent). Every brief tells its agent to read it and this file first. The project facts it relies on:

- **Gate:** `python3 tools/check.py` (after `python3 -m pip install -r tools/requirements.txt`).
- **Protected surfaces** (red-first test + one watched mutant): the pinned higher-authority documents (`PINS.yaml`); the invariant registry's honest enforceability; `contracts/` never depending on `profiles/`.
- **Record:** `CHANGELOG.md` and `ROADMAP.md`.
