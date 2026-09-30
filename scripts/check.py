#!/usr/bin/env python3
"""The repository's gate: every schema is a valid JSON Schema, every fixture parses and
validates against the input schema of its capability.

    python3 scripts/check.py        # exit 0 green, 1 on any finding, 2 when jsonschema is missing

A fixture `<name>-input.json` belongs to `schemas/<name>-input.schema.json` when that schema
exists, and otherwise to `estate.survey`'s `schemas/capability-input.schema.json` (the three
survey probes: admission, degradation, name-inference — probes/assertions.md).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    try:
        import jsonschema
    except ImportError:
        print("NOT_RUN: python3 -m pip install jsonschema")
        return 2
    findings: list[str] = []
    schemas = sorted((ROOT / "schemas").glob("*.schema.json"))
    fixtures = sorted((ROOT / "fixtures").glob("*-input.json"))
    if not schemas or not fixtures:
        findings.append("schemas/ or fixtures/ is empty")
    loaded: dict[str, dict] = {}
    for path in schemas:
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
            jsonschema.validators.validator_for(doc).check_schema(doc)
            loaded[path.name] = doc
        except ValueError as exc:
            findings.append(f"{path.relative_to(ROOT)}: not JSON: {exc}")
        except jsonschema.SchemaError as exc:
            findings.append(f"{path.relative_to(ROOT)}: not a valid JSON Schema: {exc.message}")
    for path in fixtures:
        own = path.name.replace("-input.json", "-input.schema.json")
        schema_name = own if (ROOT / "schemas" / own).exists() else "capability-input.schema.json"
        schema = loaded.get(schema_name)
        if schema is None:
            findings.append(f"{path.relative_to(ROOT)}: its schema {schema_name} did not load")
            continue
        try:
            instance = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as exc:
            findings.append(f"{path.relative_to(ROOT)}: not JSON: {exc}")
            continue
        for err in jsonschema.validators.validator_for(schema)(schema).iter_errors(instance):
            findings.append(f"{path.relative_to(ROOT)} against {schema_name}: {err.message}")
    for f in findings:
        print(f"FINDING {f}")
    print(f"{len(schemas)} schemas, {len(fixtures)} fixtures, {len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
