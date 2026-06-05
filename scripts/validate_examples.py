#!/usr/bin/env python3
"""
Validate Royalty OS v0.3 example YAML files against JSON Schema files.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    print("Missing dependency: PyYAML")
    print("Install with: pip install pyyaml")
    raise SystemExit(1) from exc

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError, ValidationError
except ImportError as exc:
    print("Missing dependency: jsonschema")
    print("Install with: pip install jsonschema")
    raise SystemExit(1) from exc

REPO_ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Value Graph Example",
        "schema": REPO_ROOT / "schemas" / "value-graph.schema.json",
        "example": REPO_ROOT / "examples" / "value-graph.example.yaml",
    },
    {
        "name": "Policy Rule Example",
        "schema": REPO_ROOT / "schemas" / "policy-rule.schema.json",
        "example": REPO_ROOT / "examples" / "policy-rule.example.yaml",
    },
    {
        "name": "Scoring Boundary Example",
        "schema": REPO_ROOT / "schemas" / "scoring-boundary.schema.json",
        "example": REPO_ROOT / "examples" / "scoring-boundary.example.yaml",
    },
    {
        "name": "Governance Record Example",
        "schema": REPO_ROOT / "schemas" / "governance-record.schema.json",
        "example": REPO_ROOT / "examples" / "governance-record.example.yaml",
    },
    {
        "name": "Royalty OS v0.3 Integrated Record Example",
        "schema": REPO_ROOT / "schemas" / "royalty-os-v0.3-record.schema.json",
        "example": REPO_ROOT / "examples" / "royalty-os-v0.3-record.example.yaml",
    },
]

def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise SystemExit(f"File not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc

def load_yaml(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        raise SystemExit(f"File not found: {path}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"Invalid YAML in {path}: {exc}") from exc

    if data is None:
        raise SystemExit(f"YAML file is empty: {path}")

    return data

def format_json_path(error: ValidationError) -> str:
    if not error.absolute_path:
        return "$"

    path = "$"
    for part in error.absolute_path:
        if isinstance(part, int):
            path += f"[{part}]"
        else:
            path += f".{part}"

    return path

def format_error_context(error: ValidationError) -> str:
    if not error.context:
        return ""

    lines = ["Nested validation errors:"]
    for sub_error in sorted(error.context, key=lambda item: list(item.absolute_path)):
        lines.append(f"  - Path: {format_json_path(sub_error)}")
        lines.append(f"    Message: {sub_error.message}")

    return "\n".join(lines)

def validate_example(name: str, schema_path: Path, example_path: Path) -> None:
    print(f"Validating target: {name}")
    print(f"Using schema: {schema_path.relative_to(REPO_ROOT)}")
    print(f"Using example: {example_path.relative_to(REPO_ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        print()
        print("Schema validation failed.")
        print(f"Target: {name}")
        print(f"Schema: {schema_path}")
        print(f"Error: {exc.message}")
        raise SystemExit(1) from exc

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(example), key=lambda item: list(item.absolute_path))

    if errors:
        print()
        print("Example validation failed.")
        print(f"Target: {name}")
        print(f"Example: {example_path}")
        print()

        for index, error in enumerate(errors, start=1):
            print(f"[{index}] Path: {format_json_path(error)}")
            print(f"    Message: {error.message}")
            context = format_error_context(error)
            if context:
                print(context)
            print()

        raise SystemExit(1)

    print("Validation passed.")
    print()

def main() -> int:
    print("Royalty OS v0.3 example validation")
    print("=" * 40)
    print()

    for target in VALIDATION_TARGETS:
        validate_example(
            name=target["name"],
            schema_path=target["schema"],
            example_path=target["example"],
        )

    print("All examples passed validation.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

