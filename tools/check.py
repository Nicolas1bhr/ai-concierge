#!/usr/bin/env python3
"""Phase 0 constitutional checks for the AI Concierge repository.

Runs in CI on every push. Exits non-zero on any violation.

  python3 tools/check.py               # verify everything
  python3 tools/check.py --write-pins  # re-hash the documents already listed in PINS.yaml

--write-pins exists for accepted change proposals only (see CONTRIBUTING.md). It never adds or
removes a pinned document; edit PINS.yaml by hand for that.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
PINS = ROOT / "PINS.yaml"
INVARIANTS = ROOT / "contracts" / "constitution" / "invariants.yaml"
INVARIANT_SCHEMA = ROOT / "contracts" / "constitution" / "invariant-record.schema.json"
CLAIMS_DIR = ROOT / "research" / "claims"
CLAIM_SCHEMA = ROOT / "research" / "claim-record.schema.json"

# Contract Program §6.2: anything stronger than DETECTIVE is a prevention claim and needs evidence.
PREVENTION_LEVELS = {"CRYPTOGRAPHIC", "HARD_PLATFORM", "HARD_BROKERED", "MEDIATED"}


class Report:
    def __init__(self):
        self.errors = []
        self.notes = []

    def error(self, msg):
        self.errors.append(msg)

    def note(self, msg):
        self.notes.append(msg)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_yaml(path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_pins(report, write):
    pins = load_yaml(PINS)
    entries = pins.get("documents", [])
    if not entries:
        report.error("PINS.yaml lists no documents")
    for entry in entries:
        path = ROOT / entry["path"]
        if not path.is_file():
            report.error(f"pinned document missing: {entry['path']}")
            continue
        actual = sha256(path)
        if write:
            entry["sha256"] = actual
        elif actual != entry.get("sha256"):
            report.error(
                f"pin drift: {entry['path']} changed without a pin update "
                f"(expected {entry.get('sha256', '<none>')[:12]}…, got {actual[:12]}…)"
            )
    if write:
        with PINS.open("w", encoding="utf-8") as f:
            f.write("# SHA-256 pins of every higher-authority document. Regenerate only for an accepted\n")
            f.write("# change proposal: python3 tools/check.py --write-pins\n")
            yaml.safe_dump(pins, f, sort_keys=False, width=100)
        report.note(f"rewrote {len(entries)} pins")
    return {Path(e["path"]).stem for e in entries}


def check_invariants(report, pinned_stems):
    validator = Draft202012Validator(json.loads(INVARIANT_SCHEMA.read_text(encoding="utf-8")))
    records = (load_yaml(INVARIANTS) or {}).get("invariants", [])
    seen_ids, seen_sources = set(), set()
    without_tests = []
    for i, rec in enumerate(records):
        label = rec.get("id", f"record #{i + 1}") if isinstance(rec, dict) else f"record #{i + 1}"
        for err in validator.iter_errors(rec):
            where = "/".join(str(p) for p in err.absolute_path) or "<root>"
            report.error(f"{label}: {where}: {err.message}")
        if not isinstance(rec, dict):
            continue
        rid = rec.get("id")
        if rid in seen_ids:
            report.error(f"{rid}: duplicate invariant id")
        seen_ids.add(rid)

        src = rec.get("source", {})
        if src.get("document") not in pinned_stems:
            report.error(f"{label}: source document {src.get('document')!r} is not pinned in PINS.yaml")
        key = (src.get("document"), src.get("section"), src.get("item"))
        if src.get("item") is not None and key in seen_sources:
            report.error(f"{label}: another record already transcribes {key}")
        seen_sources.add(key)

        enf = rec.get("enforceability", {})
        if enf.get("current") in PREVENTION_LEVELS and not enf.get("evidence"):
            report.error(
                f"{label}: claims {enf['current']} enforcement without evidence "
                "(unknown or advisory enforcement must never be represented as hard prevention)"
            )
        if not rec.get("test_obligations"):
            without_tests.append(rid)
    report.note(f"{len(records)} invariants registered")
    if without_tests:
        report.note(f"{len(without_tests)} invariants have no test obligations yet (Gate P1 blocker)")


def check_claims(report):
    validator = Draft202012Validator(
        json.loads(CLAIM_SCHEMA.read_text(encoding="utf-8")), format_checker=FormatChecker()
    )
    seen = set()
    files = sorted(CLAIMS_DIR.glob("*.yaml")) if CLAIMS_DIR.is_dir() else []
    for path in files:
        rec = load_yaml(path)
        for err in validator.iter_errors(rec):
            where = "/".join(str(p) for p in err.absolute_path) or "<root>"
            report.error(f"{path.relative_to(ROOT)}: {where}: {err.message}")
        cid = rec.get("claim_id") if isinstance(rec, dict) else None
        if cid in seen:
            report.error(f"{path.relative_to(ROOT)}: duplicate claim_id {cid}")
        seen.add(cid)
    report.note(f"{len(files)} research claims recorded")


def check_layering(report):
    """Contract Program §5: /profiles may import contracts; /contracts MUST NOT import profiles.

    Prose (*.md) may explain the rule; every other contract artifact may not reference profiles/.
    """
    for path in (ROOT / "contracts").rglob("*"):
        if not path.is_file() or path.suffix == ".md":
            continue
        if "profiles/" in path.read_text(encoding="utf-8", errors="replace"):
            report.error(f"{path.relative_to(ROOT)}: contracts must not reference profiles/")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--write-pins", action="store_true", help="re-hash documents listed in PINS.yaml")
    args = parser.parse_args()

    report = Report()
    pinned = check_pins(report, args.write_pins)
    check_invariants(report, pinned)
    check_claims(report)
    check_layering(report)

    for note in report.notes:
        print(f"  · {note}")
    if report.errors:
        print(f"\n{len(report.errors)} violation(s):", file=sys.stderr)
        for err in report.errors:
            print(f"  ✗ {err}", file=sys.stderr)
        return 1
    print("\nAll constitutional checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
