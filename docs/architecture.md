# Architecture

**Royalty OS v0.3 — Policy-Guided Value Graph Architecture**

---

## 1. Purpose

Royalty OS v0.3 defines an architecture for transforming value event logs into policy-guided value graphs.

The purpose of this architecture is not to execute compensation automatically.
The purpose is to make value relationships visible, reviewable, and governable.

```text
Royalty OS v0.3 does not decide value automatically.
It structures value relationships so that humans and AI can review them responsibly.
```

Royalty OS v0.3 is therefore a **judgment-support architecture**, not an autonomous compensation system.

---

## 2. Position in the Royalty OS Roadmap

Royalty OS evolves through three major stages:

```text
v0.1 = Trace-to-Value Record
v0.2 = Event-Based Value Circulation
v0.3 = Policy-Guided Value Graph Architecture
```

### v0.1: Record

Royalty OS v0.1 focuses on static trace records.

It asks:

```text
What trace exists?
What value may be associated with it?
How can it be recorded?
```

### v0.2: Event

Royalty OS v0.2 introduces event-based value circulation.

It asks:

```text
What happened?
Who or what was referenced?
What value event occurred?
How was it logged?
```

### v0.3: Graph + Policy

Royalty OS v0.3 transforms event logs into structured graphs and applies policy-guided review.

It asks:

```text
How are value events connected?
Which origins influenced which outcomes?
What evidence supports each relationship?
Which policy should guide review?
Who is responsible for judgment?
```

---

## 3. Architectural Summary

Royalty OS v0.3 consists of five architectural layers.

```text
Input Layer
  ↓
Value Graph Layer
  ↓
Policy Engine Layer
  ↓
Scoring Boundary Layer
  ↓
Governance Layer
```

Each layer has a distinct responsibility.

```text
Input Layer              = receives value event logs
Value Graph Layer        = structures relationships
Policy Engine Layer      = recommends review actions
Scoring Boundary Layer   = limits and defines scoring
Governance Layer         = assigns review responsibility
```

---

## 4. Core Flow

The standard flow of Royalty OS v0.3 is:

```text
Value Event Log
    ↓
Graph Transformation
    ↓
Value Graph
    ↓
Policy Evaluation
    ↓
Review Recommendation
    ↓
Governance Review
    ↓
Optional Return Record
```

This flow allows value relationships to be traced without prematurely converting them into money, rank, or legal ownership.

---

## 5. Input Layer

The Input Layer receives records from Royalty OS v0.2 or compatible event-based systems.

Possible inputs include:

```text
- origin records
- trace records
- reference events
- review events
- value signal events
- allocation events
- return records
```

The Input Layer does not judge the value of these records.

Its role is to normalize and prepare them for graph transformation.

---

## 6. Value Graph Layer

The Value Graph Layer converts event logs into graph structures.

A basic graph structure may look like this:

```text
Origin
  ├── Trace
  ├── Reference Event
  ├── Review
  ├── Value Signal
  ├── Allocation Decision
  └── Return Record
```

The Value Graph is designed to show relationships such as:

```text
Origin → Trace
Trace → Reference Event
Reference Event → Value Signal
Value Signal → Review
Review → Policy Recommendation
Policy Recommendation → Governance Decision
Governance Decision → Return Record
```

The graph does not prove ownership.
It shows relationships that may require review.

---

## 7. Policy Engine Layer

The Policy Engine Layer evaluates value graph relationships using explicit rules.

A policy rule may define:

```text
- required evidence
- review conditions
- recommendation criteria
- escalation thresholds
- attribution requirements
- governance responsibilities
```

Example:

```text
if signal_strength == high
and evidence_quality >= sufficient
and review_status == approved
then recommend:
  - citation
  - linkback
  - conceptual_attribution
```

The Policy Engine does not execute final judgment.

It provides reviewable recommendations.

---

## 8. Scoring Boundary Layer

The Scoring Boundary Layer defines what may be scored and what must not be scored in v0.3.

Allowed scoring fields include:

```text
confidence
review_score
evidence_quality
reference_depth
signal_strength
priority
```

These scores may support review, triage, and prioritization.

However, v0.3 intentionally excludes scores such as:

```text
automatic_money_value
final_creator_rank
legal_ownership_score
absolute_originality_score
```

This boundary prevents the system from overreaching.

Royalty OS v0.3 may assist judgment.
It must not replace judgment.

---

## 9. Governance Layer

The Governance Layer defines who may review, approve, reject, challenge, or verify value relationships.

Possible roles include:

```text
originator
maintainer
reviewer
AI assistant
community reviewer
external verifier
```

The Governance Layer is responsible for:

```text
- assigning review responsibility
- recording review outcomes
- managing disputes
- identifying unresolved cases
- preventing premature automation
- preserving accountability
```

This layer ensures that Royalty OS v0.3 remains human-reviewed, AI-assisted, and policy-guided.

---

## 10. Architectural Principles

Royalty OS v0.3 follows five major principles.

```text
1. Structure before compensation
2. Review before automation
3. Evidence before scoring
4. Policy before execution
5. Human responsibility before AI recommendation
```

These principles define the safety boundary of the architecture.

---

## 11. Human-Reviewed / AI-Assisted / Policy-Guided

Royalty OS v0.3 is built around three operating modes.

```text
Human-Reviewed
AI-Assisted
Policy-Guided
```

### Human-Reviewed

Humans remain responsible for final interpretation, approval, and governance decisions.

### AI-Assisted

AI may help identify patterns, summarize evidence, recommend review actions, and detect possible relationships.

### Policy-Guided

All AI assistance should be constrained by explicit policies, review rules, and scoring boundaries.

This creates a balanced architecture:

```text
Too much automation = unsafe value judgment
No automation = weak value infrastructure
Balanced assistance = responsible value review
```

---

## 12. Non-Automatic Value Judgment

Royalty OS v0.3 must not automatically determine:

```text
- legal ownership
- final compensation
- originality rank
- absolute value
- creator hierarchy
- monetary entitlement
```

Instead, it may generate:

```text
- review candidates
- attribution recommendations
- evidence summaries
- confidence indicators
- governance tasks
- unresolved-case flags
```

This distinction is essential.

The system may support decision-making.
It must not become the decision-maker.

---

## 13. Recommended Data Objects

Royalty OS v0.3 may use the following data objects.

```text
ValueGraph
PolicyRule
ScoringBoundary
GovernanceRecord
ReviewRecord
ValueSignal
ReturnRecord
RoyaltyOSv03Record
```

These objects will be defined more formally in the `schemas/` directory.

---

## 14. Example Architecture

A simplified example:

```text
Origin: Essay A
  ↓
Trace: Concept X
  ↓
Reference Event: Used in Article B
  ↓
Value Signal: High conceptual influence
  ↓
Policy Rule: Attribution required if evidence is sufficient
  ↓
Review: Approved by maintainer
  ↓
Recommendation:
      - cite Essay A
      - include linkback
      - record conceptual attribution
```

This does not mean Essay A automatically receives money.

It means the relationship between Essay A and Article B has been structured, reviewed, and made visible.

---

## 15. Relationship to Compensation

Royalty OS v0.3 is intentionally positioned before compensation.

```text
v0.1 = record the trace
v0.2 = log the event
v0.3 = map the value relationship
future versions = explore compensation or circulation mechanisms
```

This separation is important.

Compensation requires additional layers such as:

```text
- legal review
- payment policy
- jurisdictional rules
- consent management
- dispute resolution
- financial infrastructure
```

Royalty OS v0.3 prepares the ground, but does not cross into automatic compensation.

---

## 16. Architecture Boundary

Royalty OS v0.3 belongs to the following domain:

```text
Value relationship mapping
Policy-guided review
Evidence-based attribution support
Governance-aware recommendation
```

It does not belong to the following domain:

```text
Automatic legal judgment
Automatic royalty enforcement
Automatic payment allocation
Creator ranking systems
Ownership scoring systems
```

This boundary should be preserved throughout the specification.

---

## 17. Summary

Royalty OS v0.3 transforms value event logs into policy-guided value graphs.

It creates a structure where origins, traces, references, reviews, signals, and returns can be connected and examined.

Its role is not to decide value automatically.

Its role is to make value relationships visible enough for responsible human and AI-assisted review.

```text
v0.1 placed the stone.
v0.2 let the water flow.
v0.3 maps the waterways.
```
