# Changelog

All notable changes to this repository are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html). Document versions (Canon, Foundation,
Contract Program) are tracked in their own headers and pinned in `PINS.yaml`.

## [Unreleased]

### Added
- Orchestration standard for delegated and multi-agent work (`docs/ORCHESTRATION-STANDARD.md`) and a `CLAUDE.md`
  naming this project's gate, protected surfaces and record.

## [0.1.0] - 2026-10-08

### Added
- Canon (Canonical Product Concept), Foundation v0.2, superseded Foundation v0.1, Executable
  Contract Program v0.1 and the 3D compound spatial design projection, pinned by SHA-256 in `PINS.yaml`.
- Repository layout from Contract Program §5.
- Supersession map v0.1 → v0.2 (`foundation/README.md`).
- Invariant record schema and a registry seeded with all 22 Foundation v0.2 §28 invariants, each at
  enforceability `UNKNOWN`.
- Research claim record schema with claim classes and M0–M8 source maturity.
- Open-question registry, ADR template, ADR-0001 (license and layout), ADR-0002 (naming, proposed).
- `tools/check.py`: pin drift, schema validation, duplicate IDs, honest-enforcement and layering checks; run in CI.
- Tag-driven release workflow: a release is published only if the constitutional checks pass and `VERSION` matches the tag.

[Unreleased]: https://github.com/Nicolas1bhr/ai-concierge/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Nicolas1bhr/ai-concierge/releases/tag/v0.1.0
