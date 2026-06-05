# Changelog

All notable changes to this project will be documented in this file.

This project follows a draft-based specification process.

---

## [0.3.0-draft] - 2026-06-06

### Added

* Added initial Royalty OS v0.3 repository structure.
* Added `README.md` for the v0.3 project overview.
* Added `docs/architecture.md`.
* Added `docs/value-graph-model.md`.
* Added `docs/policy-engine.md`.
* Added `docs/scoring-boundary.md`.
* Added `docs/governance-layer.md`.
* Added `docs/relationship-to-v0.2.md`.
* Added `spec/royalty-os-v0.3.yaml`.

### Added: Schema Validation Package

* Added `schemas/value-graph.schema.json`.
* Added `schemas/policy-rule.schema.json`.
* Added `schemas/scoring-boundary.schema.json`.
* Added `schemas/governance-record.schema.json`.
* Added `schemas/royalty-os-v0.3-record.schema.json`.

These schemas define the machine-readable structure for:

```text
Value Graph
Policy Rule
Scoring Boundary
Governance Record
Royalty OS v0.3 Integrated Record
```

### Added: Examples

* Added `examples/value-graph.example.yaml`.
* Added `examples/policy-rule.example.yaml`.
* Added `examples/scoring-boundary.example.yaml`.
* Added `examples/governance-record.example.yaml`.
* Added `examples/royalty-os-v0.3-record.example.yaml`.

These examples demonstrate how Royalty OS v0.3 connects:

```text
Value Event Log
↓
Value Graph
↓
Policy Evaluation
↓
Scoring Boundary Check
↓
Governance Review
↓
Non-financial Return Record
```

### Added: Validator

* Added `scripts/validate_examples.py`.
* The validator checks all example YAML files against their corresponding JSON Schema files.
* The validator uses:

  * `PyYAML`
  * `jsonschema`
  * JSON Schema Draft 2020-12

Validation targets:

```text
Value Graph Example
Policy Rule Example
Scoring Boundary Example
Governance Record Example
Royalty OS v0.3 Integrated Record Example
```

### Added: GitHub Actions

* Added `.github/workflows/validate-royalty-os-v0.3.yml`.
* The workflow validates examples automatically on:

  * `push`
  * `pull_request`
  * `workflow_dispatch`

### Changed

* Updated `README.md` to include:

  * schema list
  * example list
  * validation script instructions
  * GitHub Actions workflow
  * updated repository structure
  * updated reading order
  * updated project status

### Fixed

* Fixed `examples/policy-rule.example.yaml` indentation so that all fields are correctly nested under `policy_rule`.
* Fixed `examples/governance-record.example.yaml` so that `change_log` is correctly nested under `audit`.
* Fixed `examples/royalty-os-v0.3-record.example.yaml` so that governance actions use valid governance action values.

### Validation

* Confirmed that the following examples pass validation:

```text
examples/value-graph.example.yaml
examples/policy-rule.example.yaml
examples/scoring-boundary.example.yaml
examples/governance-record.example.yaml
examples/royalty-os-v0.3-record.example.yaml
```

### Notes

Royalty OS v0.3 remains a review-support architecture.

It does not provide:

```text
automatic financial compensation
automatic royalty allocation
legal ownership determination
creator ranking
absolute originality scoring
autonomous dispute resolution
```

The central principle remains:

```text
Royalty OS v0.3 does not decide value automatically.
It structures value relationships so that humans and AI can review them responsibly.
```
