# Formal models

"Prove small things that matter" (Contract Program §22). Priority models, starting in Phase 2:
authority (no cross-grant union, bounded revocation), effects (commit-before-dispatch, ambiguous
outcomes, no replayed effects), work ownership and continuity, federation, and change.

TLA+/TLC first (§22.2). Every model is versioned and states which contract revision it models —
proving the wrong model is a known failure mode (§22.4).
