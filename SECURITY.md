# Security policy

AI Concierge is pre-implementation: there is no runtime to attack yet. Security reports are still
welcome — especially flaws in the **contracts, invariants, threat models or formal models**, since a
hole designed in now is a hole built in later.

## Reporting

Use GitHub's private reporting: **Security → Report a vulnerability** on this repository. Please do
not open a public issue for anything exploitable. You should get an acknowledgement within 7 days.

## Scope

- Contract or invariant gaps that would let authority, information or effects escape their boundary.
- `tools/check.py` or CI weaknesses that would let a higher-authority document change unpinned.
- Anything in a future `profiles/` implementation.
