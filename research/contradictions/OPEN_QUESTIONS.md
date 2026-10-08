# Contradictions and open questions

Where two higher-authority artifacts genuinely conflict, the conflict is **build-blocking until
resolved**; code must not choose a winner implicitly. Missing semantics are open questions, not
invitations for implementation code to decide ([Contract Program §1.1](../../program/CONCIERGE_FOUNDATION_EXECUTABLE_CONTRACT_PROGRAM_v0.1.md), rules 9–10).

Add an entry with the next free ID. Do not delete resolved entries; mark them resolved and link the
decision.

## Format

```markdown
### OQ-0001 — <short title>
- **Kind:** contradiction | open question
- **Between:** <document §section> ↔ <document §section>   (contradictions only)
- **Blocks:** <contract family, phase or invariant IDs>
- **Raised:** YYYY-MM-DD
- **Status:** open | resolved by <ADR / change proposal link>
- **Detail:** …
```

## Entries

### OQ-0001 — Document references carry stale filename suffixes
- **Kind:** open question
- **Between:** Contract Program v0.1 header ↔ Foundation v0.2 header
- **Blocks:** nothing (editorial)
- **Raised:** 2026-10-08
- **Status:** open
- **Detail:** The Contract Program names its superiors as `AI_CONCIERGE_CANONICAL_PRODUCT_CONCEPT(10).md`
  and `CONCIERGE_FOUNDATION_UNBOUNDED_INSTITUTIONAL_SUBSTRATE_v0.2(1).md`; Foundation v0.2 names
  `AI_CONCIERGE_CANONICAL_PRODUCT_CONCEPT(9).md`. The repository holds one Canon file without a
  revision suffix. Confirm that the pinned Canon in `PINS.yaml` is the revision both documents
  intend, then fix the references through a change proposal.
