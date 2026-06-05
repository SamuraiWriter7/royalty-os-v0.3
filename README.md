# Royalty OS v0.3

**Policy-Guided Value Graph Architecture**

Royalty OS v0.3 is a specification for transforming value event logs into policy-guided value graphs.

It does not automatically decide value, ownership, compensation, or legal entitlement.
Instead, it structures value relationships so that humans and AI systems can review them responsibly.

```text
Royalty OS v0.3 does not decide value automatically.
It structures value relationships so that humans and AI can review them responsibly.
```

---

## Overview

Royalty OS is a progressive architecture for recording, structuring, reviewing, and eventually circulating value derived from traces, references, contributions, and creative influence.

The development path is:

```text
v0.1 = Trace-to-Value Record
v0.2 = Event-Based Value Circulation
v0.3 = Policy-Guided Value Graph Architecture
```

Royalty OS v0.3 builds on v0.2 by converting value event logs into graph structures.

The purpose of this version is not compensation execution.
The purpose is **responsible value review**.

---

## Core Concept

Royalty OS v0.2 introduced event-based value circulation.

Royalty OS v0.3 introduces a graph-and-policy layer.

```text
Value Event Log
    ↓
Value Graph
    ↓
Policy Engine
    ↓
Scoring Boundary
    ↓
Governance Review
```

This allows systems to ask:

```text
Which origin was referenced?
Where did the reference occur?
What kind of value signal was generated?
What evidence supports the signal?
Which policy applies?
Who should review the relationship?
What type of attribution or return may be recommended?
```

---

## Four Pillars

Royalty OS v0.3 is organized around four core pillars.

```text
1. Value Graph
2. Policy Engine
3. Scoring Boundary
4. Governance Layer
```

---

## 1. Value Graph

The Value Graph represents relationships between origins, traces, references, reviews, value signals, allocation decisions, and return records.

A simplified structure:

```text
Origin
  ├── Trace
  ├── Reference Event
  ├── Review
  ├── Value Signal
  ├── Allocation Decision
  └── Return Record
```

The Value Graph makes it possible to examine how an origin is connected to later usage, interpretation, transformation, or value generation.

It is designed for visibility, not automatic judgment.

---

## 2. Policy Engine

The Policy Engine applies structured rules to value signals.

A policy rule may recommend actions such as:

```text
- citation
- linkback
- conceptual attribution
- review escalation
- evidence request
- manual governance review
```

Example rule logic:

```text
if signal_strength == high
and review_status == approved
then recommend:
  - citation
  - linkback
  - conceptual_attribution
```

The Policy Engine does not execute compensation.
It only provides reviewable recommendations.

---

## 3. Scoring Boundary

Royalty OS v0.3 allows limited scoring, but only within carefully defined boundaries.

Allowed scoring fields may include:

```text
confidence
review_score
evidence_quality
reference_depth
signal_strength
priority
```

Fields intentionally excluded from v0.3 include:

```text
automatic_money_value
final_creator_rank
legal_ownership_score
absolute_originality_score
```

This boundary is important.

Scoring can support review, but it must not replace human judgment.

---

## 4. Governance Layer

The Governance Layer defines who may review, approve, challenge, or verify value relationships.

Possible governance roles include:

```text
originator
maintainer
reviewer
AI assistant
community reviewer
external verifier
```

Royalty OS v0.3 assumes a human-reviewed and AI-assisted process.

```text
Human-Reviewed
AI-Assisted
Policy-Guided
```

This balance prevents both extremes:

```text
Too much automation = unsafe value judgment
No automation = weak value infrastructure
```

---

## Validation Package

Royalty OS v0.3 includes a validation package for checking example YAML files against JSON Schema definitions.

The validation package includes:

```text
schemas/
examples/
scripts/validate_examples.py
.github/workflows/validate-royalty-os-v0.3.yml
```

This allows the repository to verify that its examples conform to the intended v0.3 structure.

---

## Schemas

The `schemas/` directory defines machine-readable validation rules.

```text
schemas/value-graph.schema.json
schemas/policy-rule.schema.json
schemas/scoring-boundary.schema.json
schemas/governance-record.schema.json
schemas/royalty-os-v0.3-record.schema.json
```

### `schemas/value-graph.schema.json`

Defines the structure of a Value Graph, including origins, traces, reference events, value signals, evidence records, reviews, recommendations, governance records, allocation decisions, return records, and graph edges.

### `schemas/policy-rule.schema.json`

Defines policy rules used by the Policy Engine to generate reviewable recommendations.

### `schemas/scoring-boundary.schema.json`

Defines allowed and prohibited scoring fields and prevents scores from becoming automatic authority.

### `schemas/governance-record.schema.json`

Defines governance records for responsibility, review, approval, rejection, escalation, dispute handling, and auditability.

### `schemas/royalty-os-v0.3-record.schema.json`

Defines an integrated v0.3 record that connects Value Graph, Policy Evaluation, Scoring Boundary Check, Governance, Public Action Boundary, and Return Record.

---

## Examples

The `examples/` directory contains YAML examples that are validated against the schemas.

```text
examples/value-graph.example.yaml
examples/policy-rule.example.yaml
examples/scoring-boundary.example.yaml
examples/governance-record.example.yaml
examples/royalty-os-v0.3-record.example.yaml
```

### `examples/value-graph.example.yaml`

Shows how an origin, trace, reference event, value signal, evidence, review, recommendation, governance record, allocation decision, and return record are connected.

### `examples/policy-rule.example.yaml`

Shows a policy rule for high-signal attribution recommendation.

### `examples/scoring-boundary.example.yaml`

Shows allowed and prohibited scoring categories and the boundary rules that keep scoring limited to review support.

### `examples/governance-record.example.yaml`

Shows a governance record that approves non-financial attribution while explicitly rejecting automatic compensation, legal ownership decisions, and creator ranking.

### `examples/royalty-os-v0.3-record.example.yaml`

Shows an integrated Royalty OS v0.3 record connecting Value Graph, Policy Evaluation, Scoring Boundary Check, Governance, Public Action Boundary, and Return Record.

---

## Validation Script

The repository includes a Python validation script:

```text
scripts/validate_examples.py
```

It validates each example YAML file against its corresponding JSON Schema.

Validation targets:

```text
Value Graph Example
Policy Rule Example
Scoring Boundary Example
Governance Record Example
Royalty OS v0.3 Integrated Record Example
```

---

## Running Validation Locally

Install dependencies:

```bash
pip install pyyaml jsonschema
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected successful output:

```text
All examples passed validation.
```

---

## GitHub Actions

This repository includes a GitHub Actions workflow:

```text
.github/workflows/validate-royalty-os-v0.3.yml
```

The workflow runs validation automatically on:

```text
push
pull_request
workflow_dispatch
```

It checks that all example YAML files conform to their schemas.

---

## Non-Goals

Royalty OS v0.3 does not attempt to provide:

```text
- automatic financial compensation
- legal ownership determination
- final originality judgment
- creator ranking
- automated royalty enforcement
- fully autonomous allocation
```

These may be explored in later versions, but v0.3 focuses on structuring value relationships before any compensation layer is introduced.

---

## Repository Structure

```text
.
├── docs/
│   ├── architecture.md
│   ├── value-graph-model.md
│   ├── policy-engine.md
│   ├── scoring-boundary.md
│   ├── governance-layer.md
│   └── relationship-to-v0.2.md
├── spec/
│   └── royalty-os-v0.3.yaml
├── schemas/
│   ├── value-graph.schema.json
│   ├── policy-rule.schema.json
│   ├── scoring-boundary.schema.json
│   ├── governance-record.schema.json
│   └── royalty-os-v0.3-record.schema.json
├── examples/
│   ├── value-graph.example.yaml
│   ├── policy-rule.example.yaml
│   ├── scoring-boundary.example.yaml
│   ├── governance-record.example.yaml
│   └── royalty-os-v0.3-record.example.yaml
├── scripts/
│   └── validate_examples.py
├── .github/
│   └── workflows/
│       └── validate-royalty-os-v0.3.yml
├── README.md
├── CHANGELOG.md
├── CITATION.cff
└── LICENSE
```

---

## Key Documents

### `docs/architecture.md`

Defines the overall architecture of Royalty OS v0.3.

### `docs/value-graph-model.md`

Explains how value event logs are transformed into value graph structures.

### `docs/policy-engine.md`

Defines policy-guided recommendation logic.

### `docs/scoring-boundary.md`

Clarifies what may and may not be scored in v0.3.

### `docs/governance-layer.md`

Defines governance roles, review flows, and responsibility boundaries.

### `docs/relationship-to-v0.2.md`

Explains how v0.3 extends Royalty OS v0.2.

### `spec/royalty-os-v0.3.yaml`

Provides the machine-readable core specification for Royalty OS v0.3.

---

## Recommended Reading Order

```text
1. README.md
2. docs/architecture.md
3. docs/relationship-to-v0.2.md
4. docs/value-graph-model.md
5. docs/policy-engine.md
6. docs/scoring-boundary.md
7. docs/governance-layer.md
8. spec/royalty-os-v0.3.yaml
9. schemas/
10. examples/
11. scripts/validate_examples.py
```

---

## Design Principles

Royalty OS v0.3 follows these principles:

```text
1. Structure before compensation
2. Review before automation
3. Evidence before scoring
4. Policy before execution
5. Human responsibility before AI recommendation
```

---

## Relationship to Previous Versions

### Royalty OS v0.1

v0.1 defines a static Trace-to-Value Record.

```text
Trace
↓
Value Record
```

### Royalty OS v0.2

v0.2 introduces Event-Based Value Circulation.

```text
Origin
↓
Value Event
↓
Circulation Record
```

### Royalty OS v0.3

v0.3 converts event logs into policy-guided value graphs.

```text
Value Event Log
↓
Value Graph
↓
Policy-Guided Review
```

---

## Status

```text
Version: v0.3.0-draft
Status: Draft Specification
Stage: Architecture, schema, example, and validation design
```

This repository is an early-stage specification and may change as the model develops.

---

## License

This project is released under the MIT License.

---

## Citation

If you use or reference this specification, please cite this repository.

A `CITATION.cff` file will be provided for structured citation metadata.

---

## Summary

Royalty OS v0.3 is the stage where value events become value graphs.

It does not decide value automatically.
It does not execute compensation.
It does not replace human review.

It creates a structure where value relationships can be responsibly examined by humans and assisted by AI.

```text
v0.1 placed the stone.
v0.2 let the water flow.
v0.3 maps the waterways.
```
