# Policy Engine

**Royalty OS v0.3 — Policy-Guided Value Graph Architecture**

---

## 1. Purpose

The Policy Engine defines how Royalty OS v0.3 applies structured rules to value graph relationships.

The purpose of the Policy Engine is not to execute compensation, determine ownership, or make final value judgments automatically.

Its purpose is to generate reviewable recommendations based on graph relationships, evidence, review status, and defined policy rules.

```text
Royalty OS v0.3 does not decide value automatically.
It structures value relationships so that humans and AI can review them responsibly.
```

The Policy Engine is therefore a judgment-support layer.

It helps answer:

```text
Which value relationships require review?
Which relationships may require attribution?
Which cases should be escalated?
Which cases lack enough evidence?
Which cases should remain unresolved?
```

---

## 2. Position in the v0.3 Architecture

Royalty OS v0.3 has the following core flow:

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

The Policy Engine operates after value events have been transformed into a Value Graph.

It receives structured relationships such as:

```text
Origin → Trace → Reference Event → Value Signal → Evidence → Review
```

Then it applies policy rules to produce reviewable recommendations.

---

## 3. What the Policy Engine Does

The Policy Engine may:

```text
- evaluate value graph relationships
- match relationships against policy rules
- classify cases by review need
- recommend attribution actions
- request additional evidence
- escalate uncertain cases
- mark cases as unresolved
- produce governance tasks
```

The Policy Engine must not:

```text
- execute financial compensation
- assign legal ownership
- determine final originality
- rank creators absolutely
- enforce automatic attribution
- override human review
```

The Policy Engine recommends.
It does not command.

---

## 4. Basic Policy Flow

A basic Policy Engine flow may look like this:

```text
Value Graph
    ↓
Policy Rule Matching
    ↓
Evidence Evaluation
    ↓
Signal Evaluation
    ↓
Review Status Check
    ↓
Recommendation Generation
    ↓
Governance Review
```

In plain terms:

```text
The graph shows relationships.
The policy engine checks rules.
The result is a recommendation.
A human or governance process reviews it.
```

---

## 5. Policy Rule

A `PolicyRule` defines conditions and recommended actions.

A policy rule should be explicit, reviewable, and limited in scope.

A basic policy rule may include:

```yaml
policy_rule:
  id: policy-001
  name: "High Signal Attribution Recommendation"
  description: "Recommend citation and conceptual attribution when a high-value signal is supported by sufficient evidence and approved review."
  conditions:
    signal_strength: high
    evidence_quality: sufficient
    review_status: approved
  recommendations:
    - cite_origin
    - add_linkback
    - add_conceptual_attribution
  enforcement_level: recommendation_only
```

The `enforcement_level` should remain conservative in v0.3.

Recommended values:

```text
recommendation_only
requires_human_review
requires_governance_review
no_automatic_execution
```

---

## 6. Policy Rule Components

A Policy Rule may contain the following components:

```text
id
name
description
scope
conditions
recommendations
required_evidence
review_requirements
governance_requirements
enforcement_level
created_by
created_at
version
```

Example:

```yaml
policy_rule:
  id: policy-002
  name: "Insufficient Evidence Escalation"
  description: "Escalate cases where a value signal exists but evidence quality is insufficient."
  scope:
    applies_to:
      - ValueSignal
      - EvidenceRecord
      - Review
  conditions:
    signal_strength:
      - medium
      - high
    evidence_quality: insufficient
  recommendations:
    - request_more_evidence
    - mark_as_unresolved
  governance_requirements:
    requires_reviewer: true
    allows_external_verifier: true
  enforcement_level: requires_human_review
```

---

## 7. Input Fields

The Policy Engine may evaluate fields from the Value Graph.

Common input fields include:

```text
origin_id
trace_id
reference_event_id
signal_type
signal_strength
confidence
evidence_quality
reference_depth
review_status
review_score
governance_status
dispute_status
```

These fields should be interpreted as review aids.

They must not be treated as automatic proof.

---

## 8. Signal Strength

`signal_strength` indicates the apparent strength of a value signal.

Recommended values:

```text
none
low
medium
high
critical
```

Example:

```yaml
value_signal:
  id: signal-001
  signal_type: conceptual_influence
  signal_strength: high
  confidence: 0.82
```

Interpretation:

```text
none     = no meaningful signal detected
low      = weak or incidental relationship
medium   = possible meaningful relationship
high     = strong relationship requiring review
critical = urgent or high-impact relationship requiring escalation
```

A high signal does not automatically mean attribution is required.

It means the case should be reviewed carefully.

---

## 9. Evidence Quality

`evidence_quality` indicates the quality of supporting evidence.

Recommended values:

```text
none
weak
partial
sufficient
strong
verified
```

Example:

```yaml
evidence_record:
  id: evidence-001
  evidence_type: url
  evidence_quality: sufficient
  summary: "The target work uses a concept closely related to the origin trace."
```

Interpretation:

```text
none       = no evidence available
weak       = weak or unclear support
partial    = some support, but incomplete
sufficient = enough support for review
strong     = strong support from multiple sources
verified   = reviewed or confirmed by a responsible verifier
```

Evidence quality supports review.

It does not replace review.

---

## 10. Review Status

`review_status` indicates the current state of human, AI-assisted, community, or external review.

Recommended values:

```text
not_reviewed
pending_review
ai_assisted_review
human_reviewed
approved
rejected
unresolved
escalated
```

Example:

```yaml
review:
  id: review-001
  reviewer_role: maintainer
  review_status: approved
  notes: "The relationship is sufficiently supported for attribution recommendation."
```

Policy rules should be careful when acting on unreviewed cases.

For example:

```text
If review_status == not_reviewed,
then do not recommend final attribution.
Instead, recommend review.
```

---

## 11. Recommendation Types

The Policy Engine may generate recommendations such as:

```text
cite_origin
add_linkback
add_conceptual_attribution
add_acknowledgment
request_more_evidence
request_human_review
request_governance_review
request_external_verification
mark_as_unresolved
mark_as_low_priority
no_action_required
```

These are recommendations, not automatic actions.

A recommendation should always be connected to:

```text
- the policy rule that generated it
- the evidence that supports it
- the graph relationship it applies to
- the review status of the case
```

---

## 12. Policy Recommendation Object

A `PolicyRecommendation` records the result of policy evaluation.

Example:

```yaml
policy_recommendation:
  id: recommendation-001
  policy_rule_id: policy-001
  value_graph_id: value-graph-001
  applies_to:
    origin_id: origin-001
    trace_id: trace-001
    reference_event_id: ref-001
    value_signal_id: signal-001
  recommendation:
    - cite_origin
    - add_linkback
    - add_conceptual_attribution
  status: pending_human_review
  generated_by: policy_engine
  generated_at: "2026-06-05T00:00:00Z"
```

Recommended status values:

```text
draft
pending_human_review
pending_governance_review
approved
rejected
unresolved
archived
```

---

## 13. Example Policy Rules

### 13.1 High Signal Attribution Rule

```yaml
policy_rule:
  id: policy-high-signal-attribution
  name: "High Signal Attribution Rule"
  description: "Recommend attribution when a high signal is supported by sufficient evidence and approved review."
  conditions:
    signal_strength: high
    evidence_quality:
      - sufficient
      - strong
      - verified
    review_status:
      - approved
      - human_reviewed
  recommendations:
    - cite_origin
    - add_linkback
    - add_conceptual_attribution
  enforcement_level: recommendation_only
```

### 13.2 Medium Signal Review Rule

```yaml
policy_rule:
  id: policy-medium-signal-review
  name: "Medium Signal Review Rule"
  description: "Request human review when a medium value signal exists but no final review has been completed."
  conditions:
    signal_strength: medium
    review_status:
      - not_reviewed
      - pending_review
      - ai_assisted_review
  recommendations:
    - request_human_review
    - mark_as_low_priority
  enforcement_level: requires_human_review
```

### 13.3 Insufficient Evidence Rule

```yaml
policy_rule:
  id: policy-insufficient-evidence
  name: "Insufficient Evidence Rule"
  description: "Request more evidence when the signal exists but evidence quality is insufficient."
  conditions:
    signal_strength:
      - medium
      - high
      - critical
    evidence_quality:
      - none
      - weak
      - partial
  recommendations:
    - request_more_evidence
    - mark_as_unresolved
  enforcement_level: requires_human_review
```

### 13.4 Critical Signal Escalation Rule

```yaml
policy_rule:
  id: policy-critical-signal-escalation
  name: "Critical Signal Escalation Rule"
  description: "Escalate critical value signals to governance review."
  conditions:
    signal_strength: critical
    evidence_quality:
      - sufficient
      - strong
      - verified
  recommendations:
    - request_governance_review
    - request_external_verification
  enforcement_level: requires_governance_review
```

### 13.5 No Action Rule

```yaml
policy_rule:
  id: policy-no-action
  name: "No Action Rule"
  description: "Recommend no action when signal strength is low and evidence quality is weak."
  conditions:
    signal_strength:
      - none
      - low
    evidence_quality:
      - none
      - weak
  recommendations:
    - no_action_required
  enforcement_level: recommendation_only
```

---

## 14. Decision Boundary

The Policy Engine must preserve a clear boundary between recommendation and execution.

Allowed outputs:

```text
- recommendation
- review request
- evidence request
- escalation request
- unresolved flag
- attribution suggestion
```

Disallowed outputs in v0.3:

```text
- automatic payment execution
- automatic royalty allocation
- final legal ownership decision
- final originality score
- forced attribution
- irreversible enforcement
```

This boundary protects Royalty OS v0.3 from becoming an unsafe automated judgment system.

---

## 15. Human Review Requirement

Any recommendation that affects attribution, governance, or future return records should require human review.

Recommended rule:

```text
If a recommendation affects public attribution, formal record, or governance status,
then human review is required before execution.
```

Example:

```yaml
review_requirement:
  required_for:
    - add_conceptual_attribution
    - add_linkback
    - request_governance_review
    - approve_return_record
  required_reviewer_role:
    - maintainer
    - reviewer
    - external_verifier
```

This ensures that AI assistance remains bounded.

---

## 16. AI-Assisted Evaluation

AI systems may assist the Policy Engine by:

```text
- detecting possible relationships
- summarizing evidence
- estimating signal strength
- suggesting applicable policy rules
- identifying unresolved cases
- preparing review notes
```

AI systems must not:

```text
- finalize ownership
- enforce compensation
- assign legal status
- override governance review
- erase unresolved uncertainty
```

AI may carry the lantern.

It must not declare itself the judge.

---

## 17. Governance Connection

The Policy Engine should connect directly to the Governance Layer.

When a case requires review, escalation, or verification, the Policy Engine should generate a governance task.

Example:

```yaml
governance_task:
  id: governance-task-001
  source_recommendation_id: recommendation-001
  task_type: human_review_required
  assigned_role: maintainer
  status: pending
```

Possible governance task types:

```text
human_review_required
external_verification_required
dispute_review_required
evidence_review_required
policy_exception_review
unresolved_case_review
```

The Policy Engine should not resolve governance tasks by itself.

---

## 18. Relationship to Scoring Boundary

The Policy Engine may use scores, but only within the Scoring Boundary.

Allowed scoring inputs may include:

```text
confidence
review_score
evidence_quality
reference_depth
signal_strength
priority
```

The Policy Engine must not use or generate:

```text
automatic_money_value
final_creator_rank
legal_ownership_score
absolute_originality_score
```

Example:

```yaml
policy_evaluation:
  confidence: 0.82
  evidence_quality: sufficient
  signal_strength: high
  priority: medium
```

This may help triage review.

It must not become final value judgment.

---

## 19. Unresolved Cases

Unresolved cases must be preserved.

The Policy Engine should not delete uncertain relationships merely because they are difficult to classify.

Recommended handling:

```text
If evidence is insufficient,
or review is incomplete,
or policy rules conflict,
then mark the case as unresolved.
```

Example:

```yaml
policy_recommendation:
  id: recommendation-002
  recommendation:
    - mark_as_unresolved
    - request_more_evidence
  status: pending_human_review
```

Unresolved does not mean worthless.

It means the relationship requires more care.

---

## 20. Policy Conflict Handling

Policy rules may conflict.

For example:

```text
One rule may recommend attribution.
Another rule may request more evidence.
```

In such cases, the Policy Engine should prefer the safer path.

Recommended priority order:

```text
1. governance_review
2. human_review
3. request_more_evidence
4. mark_as_unresolved
5. attribution_recommendation
6. no_action_required
```

This prevents premature attribution or compensation.

Example:

```yaml
policy_conflict:
  id: conflict-001
  conflicting_rules:
    - policy-high-signal-attribution
    - policy-insufficient-evidence
  resolution:
    recommended_action:
      - request_more_evidence
      - mark_as_unresolved
    reason: "Evidence quality is not sufficient for attribution recommendation."
```

When in doubt, the Policy Engine should slow down.

A cautious engine is better than a reckless oracle.

---

## 21. Policy Evaluation Record

A `PolicyEvaluationRecord` may record how a recommendation was produced.

Example:

```yaml
policy_evaluation_record:
  id: evaluation-001
  value_graph_id: value-graph-001
  evaluated_at: "2026-06-05T00:00:00Z"
  evaluated_by: policy_engine
  applied_rules:
    - policy-high-signal-attribution
  input_summary:
    signal_strength: high
    evidence_quality: sufficient
    review_status: approved
  output_recommendation_id: recommendation-001
  notes: "Attribution is recommended, but execution requires human review."
```

This improves transparency and auditability.

---

## 22. Minimal Policy Engine Example

```yaml
policy_engine:
  id: royalty-os-v0.3-policy-engine
  version: "0.3.0-draft"
  mode: policy_guided_review
  execution_boundary: no_automatic_execution

  inputs:
    - value_graph
    - value_signal
    - evidence_record
    - review
    - governance_record

  allowed_recommendations:
    - cite_origin
    - add_linkback
    - add_conceptual_attribution
    - request_more_evidence
    - request_human_review
    - request_governance_review
    - mark_as_unresolved
    - no_action_required

  prohibited_actions:
    - automatic_payment
    - automatic_royalty_allocation
    - legal_ownership_assignment
    - final_creator_ranking
    - absolute_originality_scoring
```

---

## 23. Full Evaluation Example

```yaml
policy_evaluation_record:
  id: evaluation-001
  value_graph_id: value-graph-001
  evaluated_by: policy_engine
  evaluated_at: "2026-06-05T00:00:00Z"

  input:
    origin_id: origin-001
    trace_id: trace-001
    reference_event_id: ref-001
    value_signal_id: signal-001
    signal_strength: high
    evidence_quality: sufficient
    review_status: approved
    confidence: 0.82

  applied_policy_rules:
    - policy-high-signal-attribution

  recommendation:
    id: recommendation-001
    actions:
      - cite_origin
      - add_linkback
      - add_conceptual_attribution
    status: pending_human_review

  boundary_notice:
    automatic_compensation: false
    automatic_legal_judgment: false
    requires_human_review: true
```

---

## 24. Security and Misuse Considerations

The Policy Engine may be misused if it is treated as an authority instead of a review-support tool.

Risks include:

```text
- false attribution
- premature ownership claims
- automated creator ranking
- evidence laundering
- AI-generated authority illusion
- hidden scoring systems
- compensation overreach
```

Mitigations:

```text
- preserve human review
- require evidence records
- record policy evaluation history
- maintain scoring boundaries
- expose unresolved cases
- separate recommendation from execution
- connect high-impact decisions to governance
```

The Policy Engine should remain transparent enough to be challenged.

---

## 25. Design Principles

The Policy Engine follows these principles:

```text
1. Recommendation before execution
2. Review before attribution
3. Evidence before recommendation
4. Governance before escalation
5. Uncertainty before false certainty
6. Human responsibility before AI authority
```

These principles keep Royalty OS v0.3 within its proper boundary.

---

## 26. Non-Goals

The Policy Engine does not provide:

```text
- final compensation logic
- payment execution
- legal ownership determination
- creator ranking
- originality scoring
- autonomous enforcement
- dispute resolution by itself
```

These belong to future systems or external governance processes.

Royalty OS v0.3 prepares structured review.

It does not replace law, ethics, or human responsibility.

---

## 27. Summary

The Policy Engine is the review-guidance layer of Royalty OS v0.3.

It receives a Value Graph, evaluates relationships using explicit policy rules, and generates reviewable recommendations.

It may recommend:

```text
- attribution
- linkback
- citation
- more evidence
- human review
- governance review
- unresolved status
```

It must not automatically decide:

```text
- ownership
- money
- rank
- legality
- originality
```

The Policy Engine is the compass of v0.3.

The Value Graph maps the waterways.
The Policy Engine helps decide where careful review should flow next.
