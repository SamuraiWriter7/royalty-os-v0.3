# Value Graph Model

**Royalty OS v0.3 — Policy-Guided Value Graph Architecture**

---

## 1. Purpose

The Value Graph Model defines how value event logs are transformed into structured value relationships.

Royalty OS v0.2 records value events.
Royalty OS v0.3 connects those events into a graph.

```text
v0.2 = logs value events
v0.3 = maps value relationships
```

The purpose of the Value Graph is not to prove ownership, rank creators, or calculate automatic compensation.

The purpose is to make value relationships visible, reviewable, and policy-guided.

```text
Royalty OS v0.3 does not decide value automatically.
It structures value relationships so that humans and AI can review them responsibly.
```

---

## 2. What Is a Value Graph?

A Value Graph is a structured network of nodes and edges representing how an origin, trace, reference, review, signal, decision, and return are related.

A simplified model:

```text
Origin
  ├── Trace
  ├── Reference Event
  ├── Review
  ├── Value Signal
  ├── Allocation Decision
  └── Return Record
```

A Value Graph helps answer questions such as:

```text
What was the origin?
What trace was observed?
Where was it referenced?
What kind of value signal emerged?
What evidence supports the relationship?
Which review process was applied?
What policy recommendation was produced?
Was any return or attribution recorded?
```

---

## 3. Relationship to Value Event Logs

Royalty OS v0.2 produces event logs.

Example event log entries may include:

```text
origin_created
trace_recorded
reference_detected
value_signal_emitted
review_submitted
allocation_recommended
return_recorded
```

Royalty OS v0.3 transforms these logs into graph relationships.

```text
Value Event Log
    ↓
Event Normalization
    ↓
Node Extraction
    ↓
Edge Construction
    ↓
Value Graph
    ↓
Policy-Guided Review
```

In simple terms:

```text
v0.2 says: "This happened."
v0.3 asks: "How is this connected?"
```

---

## 4. Core Graph Components

The Value Graph consists of two primary components:

```text
1. Nodes
2. Edges
```

### Nodes

Nodes represent entities, events, records, or review artifacts.

### Edges

Edges represent relationships between nodes.

A graph is not merely a list of events.
It is a structured map of how events relate to one another.

---

## 5. Core Node Types

Royalty OS v0.3 defines the following core node types.

```text
Origin
Trace
ReferenceEvent
Review
ValueSignal
AllocationDecision
ReturnRecord
PolicyRecommendation
GovernanceRecord
EvidenceRecord
```

These node types may be extended in future versions, but v0.3 should remain conservative.

---

## 6. Origin Node

An `Origin` represents the source from which a trace, concept, work, expression, question, idea, dataset, design, or structure may emerge.

Examples:

```text
- article
- essay
- book
- repository
- protocol
- question
- design document
- dataset
- conversation record
- conceptual framework
```

An Origin does not automatically imply legal ownership.

It indicates a possible source of value relationship.

Example fields:

```yaml
origin:
  id: origin-001
  type: article
  title: "Example Essay"
  creator: "Example Creator"
  created_at: "2026-06-05T00:00:00Z"
  uri: "https://example.com/example-essay"
```

---

## 7. Trace Node

A `Trace` represents an identifiable fragment, structure, pattern, idea, reference, or conceptual marker derived from or associated with an Origin.

Examples:

```text
- phrase
- concept
- argument structure
- protocol pattern
- diagram structure
- terminology
- design logic
- citation marker
- transformation pattern
```

A Trace does not automatically prove copying or infringement.

It indicates that something may be recognizable enough to require review.

Example:

```yaml
trace:
  id: trace-001
  origin_id: origin-001
  type: concept
  label: "Policy-guided value graph"
  description: "A conceptual structure for reviewing value relationships through graph and policy layers."
```

---

## 8. Reference Event Node

A `ReferenceEvent` represents a detected or declared use, mention, transformation, citation, inspiration, or dependency involving a Trace or Origin.

Examples:

```text
- direct citation
- linkback
- conceptual influence
- derived implementation
- transformed idea
- summarized concept
- AI-generated reference
- human-authored reference
```

Example:

```yaml
reference_event:
  id: ref-001
  trace_id: trace-001
  target_id: article-002
  reference_type: conceptual_influence
  detected_by: AI assistant
  detected_at: "2026-06-05T01:00:00Z"
```

---

## 9. Value Signal Node

A `ValueSignal` represents an observed indication that a reference relationship may carry value.

Examples:

```text
- high reuse
- conceptual dependency
- repeated citation
- derivative implementation
- audience impact
- review approval
- external verification
- meaningful transformation
```

A Value Signal is not a final judgment.

It is a signal that something may deserve review, attribution, or further policy evaluation.

Example:

```yaml
value_signal:
  id: signal-001
  reference_event_id: ref-001
  signal_type: conceptual_influence
  signal_strength: high
  confidence: 0.82
  evidence_quality: sufficient
```

---

## 10. Review Node

A `Review` represents a human, AI-assisted, community, or external review process.

Review may include:

```text
- evidence inspection
- attribution check
- confidence assessment
- dispute review
- policy matching
- approval or rejection
- unresolved-case marking
```

Example:

```yaml
review:
  id: review-001
  reviewer_role: maintainer
  review_status: approved
  reviewed_at: "2026-06-05T02:00:00Z"
  notes: "The conceptual relationship is sufficiently supported for attribution recommendation."
```

---

## 11. Policy Recommendation Node

A `PolicyRecommendation` represents a recommendation generated by applying a policy rule to a value relationship.

Possible recommendations:

```text
- cite_origin
- add_linkback
- add_conceptual_attribution
- request_more_evidence
- escalate_to_governance_review
- mark_as_unresolved
- no_action_required
```

Example:

```yaml
policy_recommendation:
  id: recommendation-001
  policy_rule_id: policy-001
  recommendation:
    - cite_origin
    - add_linkback
    - add_conceptual_attribution
  status: pending_human_review
```

The recommendation is not automatic execution.

It is a reviewable output.

---

## 12. Allocation Decision Node

An `AllocationDecision` represents a reviewed decision about what kind of non-financial or procedural return may be appropriate.

In v0.3, this should remain limited.

Allowed examples:

```text
- attribution recommended
- citation recommended
- linkback recommended
- governance review required
- unresolved
- no return required
```

Avoid in v0.3:

```text
- automatic payment
- automatic royalty allocation
- legal ownership assignment
- final creator ranking
```

Example:

```yaml
allocation_decision:
  id: allocation-001
  decision_type: attribution_recommended
  decided_by: maintainer
  decision_status: approved
```

---

## 13. Return Record Node

A `ReturnRecord` represents a recorded return action.

In v0.3, return actions should generally be non-financial or documentation-based.

Examples:

```text
- citation added
- linkback added
- conceptual attribution added
- acknowledgment recorded
- unresolved status recorded
- governance escalation recorded
```

Example:

```yaml
return_record:
  id: return-001
  return_type: conceptual_attribution
  target_id: article-002
  origin_id: origin-001
  recorded_at: "2026-06-05T03:00:00Z"
```

---

## 14. Governance Record Node

A `GovernanceRecord` represents responsibility, review authority, dispute handling, and accountability.

Examples:

```text
- reviewer assignment
- escalation record
- dispute record
- external verification
- community review
- final review status
```

Example:

```yaml
governance_record:
  id: governance-001
  role: maintainer
  action: approved_policy_recommendation
  related_recommendation_id: recommendation-001
  timestamp: "2026-06-05T04:00:00Z"
```

---

## 15. Evidence Record Node

An `EvidenceRecord` represents supporting material for a relationship.

Examples:

```text
- URL
- quote excerpt
- commit hash
- timestamp
- similarity report
- human review note
- AI analysis summary
- external verification note
```

Evidence must support review, but it must not be treated as automatic proof.

Example:

```yaml
evidence_record:
  id: evidence-001
  evidence_type: url
  uri: "https://example.com/reference"
  summary: "The target article uses a concept similar to the origin trace."
  evidence_quality: sufficient
```

---

## 16. Core Edge Types

Edges define relationships between nodes.

Royalty OS v0.3 may use the following core edge types:

```text
originates_from
contains_trace
references
generates_signal
supported_by
reviewed_by
evaluated_under
recommends
decided_by
returns_to
escalated_to
```

Example relationship chain:

```text
Origin
  └── contains_trace → Trace
Trace
  └── referenced_by → ReferenceEvent
ReferenceEvent
  └── generates_signal → ValueSignal
ValueSignal
  └── supported_by → EvidenceRecord
ValueSignal
  └── reviewed_by → Review
Review
  └── evaluated_under → PolicyRule
PolicyRule
  └── recommends → PolicyRecommendation
PolicyRecommendation
  └── decided_by → AllocationDecision
AllocationDecision
  └── recorded_as → ReturnRecord
```

---

## 17. Directionality

Edges should be directional.

Directionality helps clarify the flow of value relationships.

Example:

```text
Trace → ReferenceEvent
```

means:

```text
The trace was referenced in the event.
```

It does not mean:

```text
The reference event created the original trace.
```

Directional edges reduce ambiguity and support responsible review.

---

## 18. Graph Status

A Value Graph may have a status.

Recommended status values:

```text
draft
pending_review
reviewed
approved
rejected
unresolved
escalated
archived
```

Example:

```yaml
graph_status: pending_review
```

Status should describe the review state of the graph, not the absolute truth of the value relationship.

---

## 19. Relationship Confidence

Value Graphs may include confidence indicators, but these must remain bounded.

Allowed confidence use:

```text
- relationship confidence
- evidence confidence
- review confidence
- signal confidence
```

Avoid confidence use for:

```text
- legal ownership certainty
- final originality certainty
- monetary entitlement certainty
- absolute creator ranking
```

Example:

```yaml
confidence:
  relationship_confidence: 0.82
  evidence_confidence: 0.76
  review_confidence: 0.88
```

Confidence is a review aid.
It is not a verdict.

---

## 20. Graph Integrity Rules

A valid Value Graph should follow these integrity rules:

```text
1. Every Trace should be linked to an Origin.
2. Every ReferenceEvent should identify a target.
3. Every ValueSignal should be linked to a ReferenceEvent or Trace.
4. Every Review should identify a reviewer role.
5. Every PolicyRecommendation should identify the applied policy rule.
6. Every AllocationDecision should remain non-final unless explicitly reviewed.
7. Every ReturnRecord should identify what was returned and to which origin.
8. Every graph should preserve unresolved cases instead of deleting them.
```

Unresolved relationships are part of the graph.

They should not be erased merely because they are uncertain.

---

## 21. Minimal Value Graph Example

A minimal Value Graph may look like this:

```yaml
value_graph:
  id: value-graph-001
  version: "0.3.0-draft"
  graph_status: pending_review

  nodes:
    origins:
      - id: origin-001
        type: article
        title: "Example Essay"
        creator: "Example Creator"

    traces:
      - id: trace-001
        origin_id: origin-001
        type: concept
        label: "Policy-guided value graph"

    reference_events:
      - id: ref-001
        trace_id: trace-001
        target_id: article-002
        reference_type: conceptual_influence

    value_signals:
      - id: signal-001
        reference_event_id: ref-001
        signal_type: conceptual_influence
        signal_strength: high
        confidence: 0.82

    reviews:
      - id: review-001
        reviewer_role: maintainer
        review_status: approved

    policy_recommendations:
      - id: recommendation-001
        policy_rule_id: policy-001
        recommendation:
          - cite_origin
          - add_linkback
          - add_conceptual_attribution
        status: pending_human_review

  edges:
    - from: origin-001
      to: trace-001
      type: contains_trace

    - from: trace-001
      to: ref-001
      type: referenced_by

    - from: ref-001
      to: signal-001
      type: generates_signal

    - from: signal-001
      to: review-001
      type: reviewed_by

    - from: review-001
      to: recommendation-001
      type: recommends
```

This example does not determine compensation.

It only structures the relationship for review.

---

## 22. Expanded Conceptual Flow

A more complete flow may look like this:

```text
Origin
  ↓ contains_trace
Trace
  ↓ referenced_by
ReferenceEvent
  ↓ generates_signal
ValueSignal
  ↓ supported_by
EvidenceRecord
  ↓ reviewed_by
Review
  ↓ evaluated_under
PolicyRule
  ↓ recommends
PolicyRecommendation
  ↓ decided_by
AllocationDecision
  ↓ recorded_as
ReturnRecord
```

This chain creates a reviewable path from origin to possible return.

---

## 23. Value Graph and Policy Engine

The Value Graph does not act alone.

It provides structured input for the Policy Engine.

```text
Value Graph
    ↓
Policy Engine
    ↓
Policy Recommendation
```

For example:

```text
If a ValueSignal is high,
and EvidenceRecord is sufficient,
and Review is approved,
then Policy Engine may recommend attribution.
```

The Policy Engine does not replace the graph.

The graph provides structure.
The policy provides guidance.

---

## 24. Value Graph and Governance

The Value Graph must remain connected to governance.

Without governance, the graph becomes a hidden scoring system.

With governance, the graph becomes a reviewable public or semi-public record.

Governance should answer:

```text
Who reviewed this relationship?
Who approved the recommendation?
Who can challenge it?
Who can verify the evidence?
Who is responsible for unresolved cases?
```

A Value Graph without governance is incomplete.

---

## 25. Non-Goals

The Value Graph Model does not provide:

```text
- automatic legal proof
- automatic royalty payment
- final originality judgment
- creator ranking
- ownership scoring
- fully autonomous attribution enforcement
```

The graph is a map.

It is not a court, bank, or throne.

---

## 26. Design Principles

The Value Graph Model follows these principles:

```text
1. Relationship before reward
2. Evidence before scoring
3. Structure before judgment
4. Review before decision
5. Transparency before automation
6. Governance before execution
```

These principles preserve the safety boundary of Royalty OS v0.3.

---

## 27. Summary

The Value Graph Model is the core structural layer of Royalty OS v0.3.

It transforms value event logs into reviewable relationships.

It connects:

```text
Origin
Trace
Reference Event
Value Signal
Evidence
Review
Policy Recommendation
Governance
Return Record
```

Its purpose is not to automatically decide value.

Its purpose is to make value relationships visible enough for responsible human and AI-assisted review.

```text
v0.1 placed the stone.
v0.2 let the water flow.
v0.3 maps the waterways.
```
