# Relationship to Royalty OS v0.2

**Royalty OS v0.3 — Policy-Guided Value Graph Architecture**

---

## 1. Purpose

This document explains how Royalty OS v0.3 relates to Royalty OS v0.2.

Royalty OS v0.2 introduced **Event-Based Value Circulation**.

Royalty OS v0.3 extends that model by transforming value event logs into **Policy-Guided Value Graphs**.

```text
v0.2 = Event-Based Value Circulation
v0.3 = Policy-Guided Value Graph Architecture
```

The purpose of v0.3 is not to replace v0.2.

The purpose is to build a reviewable graph and policy layer on top of v0.2 event records.

---

## 2. Version Progression

Royalty OS develops through a staged architecture.

```text
v0.1 = Trace-to-Value Record
v0.2 = Event-Based Value Circulation
v0.3 = Policy-Guided Value Graph Architecture
```

Each version adds a new structural capability.

```text
v0.1 records traces.
v0.2 records value events.
v0.3 connects events into reviewable value graphs.
```

In this progression, v0.3 depends conceptually on v0.2.

Without event logs, there is no reliable input for a value graph.

---

## 3. What v0.2 Provides

Royalty OS v0.2 provides the event layer.

It records value-related events such as:

```text
- origin creation
- trace recording
- reference detection
- value signal emission
- review submission
- allocation recommendation
- return recording
```

These events describe what happened.

Example:

```yaml
value_event:
  id: event-001
  event_type: reference_detected
  origin_id: origin-001
  trace_id: trace-001
  target_id: article-002
  timestamp: "2026-06-05T00:00:00Z"
```

v0.2 answers:

```text
What happened?
When did it happen?
Which origin or trace was involved?
What type of value event occurred?
```

---

## 4. What v0.3 Adds

Royalty OS v0.3 adds graph structure, policy guidance, scoring boundaries, and governance review.

It asks:

```text
How are these events connected?
Which relationships require review?
Which policy rules apply?
Which scores may assist review?
Who is responsible for governance?
```

v0.3 transforms event logs into structured relationships.

```text
Value Event Log
    ↓
Value Graph
    ↓
Policy Engine
    ↓
Scoring Boundary
    ↓
Governance Layer
```

This creates a reviewable path from event recording to responsible value review.

---

## 5. Key Difference

The key difference between v0.2 and v0.3 is this:

```text
v0.2 records events.
v0.3 maps relationships between events.
```

v0.2 says:

```text
A reference event occurred.
```

v0.3 asks:

```text
What origin was referenced?
What trace was involved?
What value signal emerged?
What evidence supports the relationship?
Which policy applies?
Who should review the case?
```

This is the shift from event logging to graph-based judgment support.

---

## 6. Event Log to Value Graph

A v0.2 event log may contain multiple separate records.

Example:

```text
origin_created
trace_recorded
reference_detected
value_signal_emitted
review_submitted
return_recorded
```

v0.3 connects these records into a graph.

```text
Origin
  ↓
Trace
  ↓
Reference Event
  ↓
Value Signal
  ↓
Evidence
  ↓
Review
  ↓
Policy Recommendation
  ↓
Governance Record
  ↓
Return Record
```

The graph allows the system to inspect how a value relationship evolved over time.

---

## 7. Conceptual Mapping

The following table shows how v0.2 concepts map into v0.3 concepts.

| Royalty OS v0.2    | Royalty OS v0.3                 |
| ------------------ | ------------------------------- |
| Value Event Log    | Value Graph input               |
| Origin Event       | Origin Node                     |
| Trace Event        | Trace Node                      |
| Reference Event    | ReferenceEvent Node             |
| Value Signal Event | ValueSignal Node                |
| Review Event       | Review Node                     |
| Allocation Event   | AllocationDecision Node         |
| Return Event       | ReturnRecord Node               |
| Event sequence     | Directed graph path             |
| Event metadata     | Evidence and governance context |

This mapping allows v0.3 to preserve v0.2 event data while giving it relational structure.

---

## 8. Why v0.3 Does Not Replace v0.2

v0.2 remains necessary because it provides the chronological event record.

v0.3 does not remove that record.

Instead, it builds on it.

```text
v0.2 = chronological record
v0.3 = relational interpretation layer
```

Both are needed.

Without v0.2, v0.3 would lack traceable event data.

Without v0.3, v0.2 would remain a list of events without deeper relationship mapping.

---

## 9. Transformation Flow

The transformation from v0.2 to v0.3 may follow this process:

```text
1. Collect v0.2 value event logs
2. Normalize event records
3. Extract nodes
4. Construct edges
5. Build Value Graph
6. Apply Policy Engine
7. Apply Scoring Boundary
8. Create Governance Tasks
9. Record review outcomes
```

Example:

```text
v0.2 event:
  reference_detected

v0.3 graph:
  Trace → ReferenceEvent → ValueSignal → Review → PolicyRecommendation
```

The same event becomes part of a larger reviewable structure.

---

## 10. Example Mapping

### v0.2 Event

```yaml
value_event:
  id: event-001
  event_type: reference_detected
  origin_id: origin-001
  trace_id: trace-001
  target_id: article-002
  reference_type: conceptual_influence
  timestamp: "2026-06-05T00:00:00Z"
```

### v0.3 Graph Nodes

```yaml
nodes:
  origins:
    - id: origin-001
      type: article
      title: "Example Essay"

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
```

### v0.3 Graph Edges

```yaml
edges:
  - from: origin-001
    to: trace-001
    type: contains_trace

  - from: trace-001
    to: ref-001
    type: referenced_by
```

This shows how a v0.2 event becomes part of a v0.3 graph.

---

## 11. From Circulation to Review

Royalty OS v0.2 focuses on value circulation.

Royalty OS v0.3 focuses on reviewable structure.

```text
v0.2 = value moved or appeared as an event
v0.3 = the relationship behind that movement can be reviewed
```

This means v0.3 slows the system down before compensation or final attribution.

That slowness is intentional.

Royalty OS v0.3 prioritizes:

```text
- review before automation
- evidence before scoring
- policy before execution
- governance before public action
```

---

## 12. v0.2 Input Categories

v0.3 may receive the following v0.2 input categories:

```text
OriginRecord
TraceRecord
ValueEvent
ReferenceEvent
ValueSignal
ReviewRecord
AllocationRecord
ReturnRecord
```

These may be transformed into v0.3 objects:

```text
Origin
Trace
ReferenceEvent
ValueSignal
Review
PolicyRecommendation
AllocationDecision
ReturnRecord
GovernanceRecord
EvidenceRecord
```

The transformation should preserve source identifiers whenever possible.

---

## 13. Identifier Continuity

v0.3 should preserve v0.2 identifiers where possible.

Example:

```yaml
source_event:
  version: "0.2"
  event_id: event-001

value_graph_node:
  version: "0.3.0-draft"
  node_id: ref-001
  source_event_id: event-001
```

This creates continuity between the event log and the graph.

Recommended fields:

```text
source_version
source_event_id
source_record_id
source_timestamp
source_uri
transformed_at
transformed_by
```

Identifier continuity improves traceability.

---

## 14. Backward Compatibility

Royalty OS v0.3 should remain conceptually compatible with v0.2.

Compatibility principles:

```text
1. v0.3 should not discard v0.2 event records.
2. v0.3 should preserve event timestamps where possible.
3. v0.3 should preserve origin and trace identifiers where possible.
4. v0.3 should record transformation provenance.
5. v0.3 should treat v0.2 events as inputs, not obsolete artifacts.
```

This ensures that v0.2 remains a valid foundation.

---

## 15. Transformation Provenance

When v0.2 events are transformed into v0.3 graph structures, the transformation should be recorded.

Example:

```yaml
transformation_record:
  id: transform-001
  source_version: "0.2"
  target_version: "0.3.0-draft"
  source_event_ids:
    - event-001
    - event-002
    - event-003
  target_value_graph_id: value-graph-001
  transformed_by: "AI assistant"
  reviewed_by: "maintainer"
  transformed_at: "2026-06-05T00:00:00Z"
```

This makes the graph auditable.

A graph should not appear from nowhere.

---

## 16. Policy Layer Added in v0.3

Royalty OS v0.2 may record that a value event occurred.

Royalty OS v0.3 applies policy rules to the graph created from those events.

Example:

```text
v0.2:
  value_signal_emitted

v0.3:
  if signal_strength == high
  and evidence_quality == sufficient
  and review_status == approved
  then recommend:
    - cite_origin
    - add_linkback
    - add_conceptual_attribution
```

This is the main expansion from v0.2 to v0.3.

v0.3 turns raw event records into policy-guided review paths.

---

## 17. Scoring Boundary Added in v0.3

Royalty OS v0.2 may record signals.

Royalty OS v0.3 may evaluate those signals with bounded scoring.

Allowed scoring:

```text
confidence
review_score
evidence_quality
reference_depth
signal_strength
priority
```

Prohibited scoring:

```text
automatic_money_value
final_creator_rank
legal_ownership_score
absolute_originality_score
```

This boundary is essential.

v0.3 allows scoring only as a review aid.

It does not allow scoring to become final judgment.

---

## 18. Governance Layer Added in v0.3

Royalty OS v0.2 records events.

Royalty OS v0.3 defines who reviews and takes responsibility for the interpretation of those events.

Governance roles may include:

```text
originator
maintainer
reviewer
AI assistant
community reviewer
external verifier
governance steward
dispute reviewer
observer
```

Governance ensures that v0.3 remains:

```text
Human-Reviewed
AI-Assisted
Policy-Guided
```

This is one of the most important differences from v0.2.

---

## 19. What v0.3 Still Does Not Do

Even though v0.3 adds graph, policy, scoring, and governance layers, it still does not perform final compensation.

Royalty OS v0.3 does not provide:

```text
- automatic royalty payment
- final legal ownership determination
- automatic compensation allocation
- creator ranking
- absolute originality scoring
- autonomous dispute resolution
```

v0.3 prepares the review structure.

It does not become the court, bank, or throne.

---

## 20. Why Compensation Is Still Deferred

Compensation should remain outside v0.3 because compensation requires additional layers.

Examples:

```text
- legal review
- payment infrastructure
- consent management
- jurisdictional policy
- financial auditing
- dispute resolution
- creator agreement models
```

Royalty OS v0.3 builds the map needed before such systems can be responsibly explored.

```text
First map the relationship.
Then review the relationship.
Only later consider compensation.
```

This prevents premature automation.

---

## 21. Recommended Integration Model

A recommended integration model is:

```text
Royalty OS v0.2
  ↓ exports event logs

Royalty OS v0.3
  ↓ imports event logs
  ↓ builds value graphs
  ↓ applies policy rules
  ↓ applies scoring boundaries
  ↓ creates governance tasks
  ↓ records review outcomes
```

This preserves the role of both systems.

v0.2 remains the event source.

v0.3 becomes the review architecture.

---

## 22. Example End-to-End Flow

```text
1. v0.2 records a reference event.
2. v0.2 records a value signal.
3. v0.3 imports both records.
4. v0.3 creates Origin, Trace, ReferenceEvent, and ValueSignal nodes.
5. v0.3 connects them with directed edges.
6. v0.3 evaluates the relationship using policy rules.
7. v0.3 applies scoring boundaries.
8. v0.3 creates a governance task.
9. A reviewer approves, rejects, or marks the case unresolved.
10. A return record may be created if appropriate.
```

This flow shows how event circulation becomes responsible review.

---

## 23. Design Principles for the Transition

The transition from v0.2 to v0.3 follows these principles:

```text
1. Preserve event history.
2. Transform logs into graphs.
3. Keep uncertainty visible.
4. Apply policy before action.
5. Bound all scoring.
6. Require governance for public outcomes.
7. Defer compensation.
8. Preserve human responsibility.
```

These principles prevent v0.3 from becoming unsafe automation.

---

## 24. Summary

Royalty OS v0.2 and v0.3 are complementary.

```text
v0.2 records value events.
v0.3 maps those events into policy-guided value graphs.
```

v0.2 answers:

```text
What happened?
```

v0.3 answers:

```text
How are these events related, and how should they be reviewed?
```

The transition is:

```text
Event Log
  ↓
Value Graph
  ↓
Policy Engine
  ↓
Scoring Boundary
  ↓
Governance Review
```

Royalty OS v0.3 does not replace v0.2.

It gives v0.2 event records a structure that can be responsibly reviewed by humans and assisted by AI.

```text
v0.1 placed the stone.
v0.2 let the water flow.
v0.3 maps the waterways.
```
