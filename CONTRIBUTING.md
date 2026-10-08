# Contributing to AI Concierge

Thank you for helping. This project is unusual: **it is building the judge before the defendant.**
Contracts, formal models and conformance tests come before product code, so that the first
implementation can be demonstrably wrong instead of quietly becoming the architecture.

## The rules that matter most

These come from the [Executable Contract Program §1.1](program/CONCIERGE_FOUNDATION_EXECUTABLE_CONTRACT_PROGRAM_v0.1.md).

1. **Authority flows down.** Canon > Foundation > Contracts > Implementation profiles > Runtime.
   A lower layer never rewrites a higher one by convention, convenience or accumulated code.
2. **Missing semantics are open questions.** If the Foundation does not say, do not decide it in
   code — add an entry to [`research/contradictions/OPEN_QUESTIONS.md`](research/contradictions/OPEN_QUESTIONS.md).
3. **A framework's vocabulary is not institutional semantics.** Its data model, permission names,
   workflow states or transport do not become law because they are convenient.
4. **Never overstate enforcement.** Unknown or advisory controls are never labeled hard prevention.
   `tools/check.py` rejects an invariant that claims prevention without evidence.
5. **`contracts/` never depends on `profiles/`.** Profiles may import contracts, not the reverse.
6. **A bare URL is not evidence.** External facts go into `research/claims/` as dated records with
   source maturity (see [`research/README.md`](research/README.md)).

## Kinds of change

| You want to… | Do this |
|---|---|
| Fix a typo or link in a README | Open a PR. |
| Add or change a contract, schema or invariant record | Open a PR; reference the Foundation section it operationalizes. |
| Choose an implementation approach | Write an ADR in [`adr/`](adr/) from the template. ADRs choose; they cannot override a higher layer. |
| Change Canon, Foundation or the Contract Program | Open a **change proposal** issue first. If accepted, the PR updates the document **and** its pin (`python3 tools/check.py --write-pins`) in the same commit. |
| Record an external fact (standard, release, paper) | Add a claim record under `research/claims/`. |

Changes flow upward only through explicit proposals:
implementation finding → ADR / evidence → contract change → Foundation change → Canon change.

## Before you open a PR

```bash
python3 -m pip install -r tools/requirements.txt
python3 tools/check.py
```

CI runs the same command. Update [CHANGELOG.md](CHANGELOG.md) under `Unreleased`.

## Licensing of contributions

By contributing you agree that your contribution is licensed under the
[GNU AGPL v3.0](LICENSE), the license of this repository.

## Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md).
