# ADR-0001: Open-source, contracts-first repository under AGPL-3.0

- **Status:** Accepted
- **Date:** 2026-10-08
- **Layer:** repository process

## Context

The Executable Contract Program §5 asks for the Contract Program to "become a versioned repository
rather than one Markdown file" and gives a recommended layout. §25 forbids product runtime work
before Phases 0–3 gates pass. The project is to be developed in the open.

## Decision

1. One public repository, `ai-concierge`, using the §5 layout: `canon/`, `foundation/`, `program/`,
   `contracts/`, `formal/`, `conformance/`, `research/`, `adr/`, `profiles/`, `threat-models/`,
   plus `design/` for design projections that derive from Canon without being Canon.
2. Higher-authority documents are copied in verbatim and pinned by SHA-256 in `PINS.yaml`; CI
   rejects any change to them that does not also update the pin.
3. License: **GNU AGPL v3.0**, so that anyone offering a modified Concierge as a network service
   must offer its source to that service's users.
4. Repository releases use Semantic Versioning, independent of each document's own version.

## Contracts and invariants touched

None directly. `tools/check.py` mechanically supports CF-SEC-001 (honest enforcement) for the
invariant registry itself and the §5 rule that `contracts/` never depends on `profiles/`.

## Consequences

- A contributor can see at a glance which layer a file belongs to and what outranks it.
- Editing Canon or Foundation is deliberately noisy: the pin must change in the same commit.
- AGPL may deter some commercial adopters; that is accepted.

## Alternatives considered

- **Apache-2.0 / MIT** — more adoption-friendly, but permit closed hosted forks.
- **Monorepo with product code from day one** — rejected by Contract Program §25.
