# Scoring Boundary

**Royalty OS v0.3 — Policy-Guided Value Graph Architecture**

---

## 1. Purpose

The Scoring Boundary defines what may and may not be scored in Royalty OS v0.3.

Scoring can help humans and AI systems prioritize review, evaluate evidence, and identify relationships that require attention.

However, scoring can also become dangerous when it is used to determine ownership, rank creators, calculate money, or replace human judgment.

Royalty OS v0.3 therefore allows limited scoring only within a clearly defined boundary.

```text
Royalty OS v0.3 does not decide value automatically.
It structures value relationships so that humans and AI can review them responsibly.
```

The purpose of scoring in v0.3 is **review support**, not final judgment.

---

## 2. Position in the v0.3 Architecture

Royalty OS v0.3 follows this flow:

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

The Scoring Boundary sits between policy recommendation and governance review.

Its role is to prevent scores from becoming automatic authority.

```text
Policy Engine recommends.
Scoring Boundary limits.
Governance Layer reviews.
```

---

## 3. Why a Scoring Boundary Is Necessary

Scores are useful because they can help answer:

```text
Which cases should be reviewed first?
Which evidence is stronger?
Which relationships are uncertain?
Which signals are weak or strong?
Which cases should be escalated?
```

But scores can become harmful if they are used to answer:

```text
Who owns this idea?
How much money is owed?
Who is the most original creator?
Who deserves final credit?
Which creator ranks above another?
```

Royalty OS v0.3 avoids this overreach.

The score is a lantern.
It is not the throne.

---

## 4. Allowed Scoring Fields

Royalty OS v0.3 may allow the following scoring fields:

```text
confidence
review_score
evidence_quality
reference_depth
signal_strength
priority
```

These fields are allowed because they support review, triage, and governance.

They do not directly determine compensation, ownership, or creator rank.

---

## 5. Prohibited Scoring Fields

Royalty OS v0.3 should not include the following scoring fields:

```text
automatic_money_value
final_creator_rank
legal_ownership_score
absolute_originality_score
automatic_compensation_score
final_entitlement_score
```

These fields are excluded because they move beyond review support and into final judgment.

Royalty OS v0.3 is not designed to function as:

```text
- a court
- a bank
- a royalty enforcement machine
- a creator ranking system
- an ownership determination system
```

---

## 6. Allowed vs Prohibited Scoring

| Category    | Allowed in v0.3                    | Not Allowed in v0.3 |
| ----------- | ---------------------------------- | ------------------- |
| Confidence  | relationship confidence            | legal certainty     |
| Evidence    | evidence quality                   | proof of ownership  |
| Review      | review score                       | final verdict       |
| Signal      | signal strength                    | monetary value      |
| Priority    | review priority                    | creator rank        |
| Attribution | attribution recommendation support | forced attribution  |

The distinction is simple:

```text
Allowed scoring = helps review
Prohibited scoring = replaces judgment
```

---

## 7. Confidence

`confidence` indicates how confident the system is about a specific relationship, signal, or evaluation.

Allowed examples:

```yaml
confidence:
  relationship_confidence: 0.82
  evidence_confidence: 0.76
  review_confidence: 0.88
```

Confidence may be used to support review prioritization.

It must not be treated as proof.

Recommended interpretation:

```text
0.00 - 0.30 = low confidence
0.31 - 0.60 = moderate confidence
0.61 - 0.85 = high confidence
0.86 - 1.00 = very high confidence
```

Important boundary:

```text
High confidence does not mean final truth.
Low confidence does not mean no value.
```

---

## 8. Review Score

`review_score` may summarize the result of a review process.

Example:

```yaml
review_score:
  score: 0.78
  reviewed_by: maintainer
  review_status: human_reviewed
  notes: "The relationship appears meaningful, but additional evidence may improve confidence."
```

Allowed use:

```text
- support review triage
- summarize reviewer assessment
- identify cases needing further review
- compare review readiness
```

Prohibited use:

```text
- final ownership judgment
- final originality judgment
- automatic compensation
- creator ranking
```

A review score is a review aid.

It is not a verdict.

---

## 9. Evidence Quality

`evidence_quality` indicates the quality of evidence supporting a value relationship.

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
evidence_quality:
  level: sufficient
  evidence_count: 3
  verified_by: reviewer
```

Interpretation:

```text
none       = no evidence available
weak       = unclear or minimal evidence
partial    = some evidence, but incomplete
sufficient = enough evidence for review
strong     = multiple strong pieces of evidence
verified   = reviewed or confirmed by a responsible verifier
```

Evidence quality may influence policy recommendations.

It must not automatically trigger final attribution or compensation.

---

## 10. Reference Depth

`reference_depth` indicates how deeply a target work or event appears to depend on an origin, trace, concept, or structure.

Recommended values:

```text
surface
minor
moderate
deep
structural
```

Example:

```yaml
reference_depth:
  level: deep
  description: "The target work appears to reuse the conceptual structure of the origin."
```

Interpretation:

```text
surface    = casual mention or shallow reference
minor      = small reference or limited influence
moderate   = meaningful reference
deep       = strong conceptual or structural dependency
structural = core structure depends on the origin
```

Boundary:

```text
Reference depth may support review.
It must not automatically determine ownership.
```

---

## 11. Signal Strength

`signal_strength` indicates how strong a value signal appears to be.

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
signal_strength:
  level: high
  confidence: 0.82
  signal_type: conceptual_influence
```

Interpretation:

```text
none     = no meaningful signal detected
low      = weak or incidental signal
medium   = possible meaningful relationship
high     = strong relationship requiring review
critical = high-impact relationship requiring escalation
```

A critical signal does not mean automatic action.

It means the case should move toward governance review.

---

## 12. Priority

`priority` indicates how urgently a case should be reviewed.

Recommended values:

```text
low
medium
high
urgent
```

Example:

```yaml
priority:
  level: high
  reason: "High signal strength with sufficient evidence and unresolved attribution."
```

Allowed use:

```text
- review queue ordering
- governance task prioritization
- escalation management
- unresolved case tracking
```

Prohibited use:

```text
- creator ranking
- value ranking
- automatic compensation
- public status labeling without review
```

Priority is about workflow.

It is not about worth.

---

## 13. Scoring Object

A basic scoring object may look like this:

```yaml
scoring:
  confidence:
    relationship_confidence: 0.82
    evidence_confidence: 0.76
    review_confidence: 0.88

  evidence_quality:
    level: sufficient

  reference_depth:
    level: deep

  signal_strength:
    level: high

  priority:
    level: high
    reason: "High signal strength with sufficient evidence."
```

This object may support policy evaluation and governance review.

It must not generate final outcomes by itself.

---

## 14. Scoring Boundary Object

A `ScoringBoundary` defines allowed and prohibited scoring categories.

Example:

```yaml
scoring_boundary:
  id: scoring-boundary-001
  version: "0.3.0-draft"

  allowed_fields:
    - confidence
    - review_score
    - evidence_quality
    - reference_depth
    - signal_strength
    - priority

  prohibited_fields:
    - automatic_money_value
    - final_creator_rank
    - legal_ownership_score
    - absolute_originality_score
    - automatic_compensation_score
    - final_entitlement_score

  boundary_rule:
    scoring_purpose: review_support_only
    automatic_execution: false
    requires_human_review_for_public_action: true
```

---

## 15. Boundary Rules

Royalty OS v0.3 should follow these scoring boundary rules:

```text
1. Scores may support review, but must not replace review.
2. Scores may prioritize cases, but must not determine final value.
3. Scores may describe confidence, but must not declare legal truth.
4. Scores may summarize evidence, but must not prove ownership.
5. Scores may support attribution recommendations, but must not enforce attribution.
6. Scores may inform governance, but must not override governance.
```

These rules keep scoring within its proper role.

---

## 16. Relationship to the Policy Engine

The Policy Engine may use scores as inputs.

Example:

```yaml
policy_input:
  signal_strength: high
  evidence_quality: sufficient
  relationship_confidence: 0.82
  review_status: approved
```

The Policy Engine may then produce a recommendation:

```yaml
policy_recommendation:
  recommendation:
    - cite_origin
    - add_linkback
    - add_conceptual_attribution
  status: pending_human_review
```

However, the Scoring Boundary must ensure that this does not become automatic execution.

```text
Score → Policy Recommendation → Human Review → Governance Decision
```

Not:

```text
Score → Automatic Decision
```

---

## 17. Relationship to Governance

The Governance Layer should review any score that affects:

```text
- attribution
- public records
- return records
- unresolved-case status
- escalation
- external verification
```

Governance should be able to:

```text
- approve scores
- challenge scores
- revise scores
- reject scores
- request more evidence
- mark the case as unresolved
```

Scores must remain contestable.

A score that cannot be challenged becomes hidden authority.

---

## 18. Human Review Requirement

Any score used to support public attribution, return records, or governance status should require human review.

Recommended rule:

```text
If a score affects public action,
then human review is required before execution.
```

Example:

```yaml
human_review_requirement:
  applies_when:
    - recommendation_affects_public_attribution
    - recommendation_affects_return_record
    - recommendation_affects_governance_status
  required: true
```

---

## 19. AI-Assisted Scoring

AI may assist scoring by:

```text
- estimating confidence
- summarizing evidence
- detecting weak signals
- comparing reference depth
- identifying unresolved cases
- suggesting review priority
```

AI must not:

```text
- finalize compensation
- determine legal ownership
- rank creators
- declare absolute originality
- erase uncertainty
- override human review
```

AI may help weigh the stone.

It must not declare the mountain.

---

## 20. Uncertainty Handling

Uncertainty should be preserved, not hidden.

When a score is uncertain, the system should mark it clearly.

Example:

```yaml
uncertainty:
  status: unresolved
  reason:
    - insufficient_evidence
    - conflicting_reviews
    - ambiguous_reference_depth
```

Recommended uncertainty states:

```text
clear
uncertain
conflicting
unresolved
requires_review
requires_external_verification
```

Uncertainty is not failure.

In Royalty OS v0.3, uncertainty is a valid state of the graph.

---

## 21. Score Provenance

Scores should include provenance.

Score provenance records where the score came from and how it was produced.

Example:

```yaml
score_provenance:
  score_id: score-001
  generated_by: AI assistant
  reviewed_by: maintainer
  generated_at: "2026-06-05T00:00:00Z"
  method: "AI-assisted evidence summary with human review"
  related_evidence:
    - evidence-001
    - evidence-002
```

A score without provenance should be treated as weak.

---

## 22. Score Review Status

Scores should have review status.

Recommended values:

```text
draft
ai_generated
pending_human_review
human_reviewed
approved
rejected
unresolved
archived
```

Example:

```yaml
score_review_status:
  status: pending_human_review
  reviewer_role: maintainer
```

Scores should not silently move from AI-generated to approved.

There must be a visible review transition.

---

## 23. Misuse Risks

Scoring may be misused in several ways.

Risks include:

```text
- treating confidence as truth
- treating evidence quality as legal proof
- treating signal strength as entitlement
- treating priority as value rank
- treating AI-generated scores as objective authority
- creating hidden creator ranking systems
- converting review scores into automatic payment scores
```

These risks are why the Scoring Boundary exists.

---

## 24. Mitigations

Royalty OS v0.3 should mitigate scoring misuse through:

```text
- explicit prohibited fields
- human review requirements
- score provenance
- review status tracking
- governance oversight
- unresolved-case preservation
- separation of recommendation and execution
- prohibition of automatic financial calculation
```

A safe score is visible, bounded, and challengeable.

---

## 25. Minimal Scoring Boundary Example

```yaml
scoring_boundary:
  id: scoring-boundary-001
  version: "0.3.0-draft"
  purpose: review_support_only

  allowed_scoring:
    confidence:
      allowed: true
      use: "Relationship and evidence review support"

    review_score:
      allowed: true
      use: "Reviewer assessment summary"

    evidence_quality:
      allowed: true
      use: "Evidence sufficiency assessment"

    reference_depth:
      allowed: true
      use: "Depth of reference relationship"

    signal_strength:
      allowed: true
      use: "Strength of value signal"

    priority:
      allowed: true
      use: "Review queue ordering"

  prohibited_scoring:
    automatic_money_value:
      allowed: false
      reason: "v0.3 does not calculate compensation"

    final_creator_rank:
      allowed: false
      reason: "v0.3 does not rank creators"

    legal_ownership_score:
      allowed: false
      reason: "v0.3 does not determine legal ownership"

    absolute_originality_score:
      allowed: false
      reason: "v0.3 does not determine absolute originality"

  execution_boundary:
    automatic_execution: false
    requires_human_review: true
    requires_governance_for_high_impact_cases: true
```

---

## 26. Design Principles

The Scoring Boundary follows these principles:

```text
1. Scores support review.
2. Scores do not replace judgment.
3. Confidence is not truth.
4. Evidence quality is not legal proof.
5. Signal strength is not entitlement.
6. Priority is not creator rank.
7. AI scoring must remain reviewable.
8. Uncertainty must remain visible.
```

These principles prevent scoring from becoming an invisible authority layer.

---

## 27. Non-Goals

The Scoring Boundary does not define:

```text
- compensation calculation
- payment allocation
- legal ownership scoring
- final originality scoring
- creator ranking
- automatic royalty distribution
- autonomous enforcement
```

These are outside the scope of Royalty OS v0.3.

---

## 28. Summary

The Scoring Boundary is the safety layer of Royalty OS v0.3.

It allows limited scoring for:

```text
confidence
review_score
evidence_quality
reference_depth
signal_strength
priority
```

It prohibits scoring for:

```text
automatic_money_value
final_creator_rank
legal_ownership_score
absolute_originality_score
```

The purpose of scoring is to support responsible review.

It must not become automatic judgment.

```text
The score may guide the reviewer.
The score must not become the judge.
```
