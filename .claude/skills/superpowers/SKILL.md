---
name: superpowers
description: 5-phase structured execution framework (Plan, Build, Review, Refine, Ship) for all client, agency, and contractor deliverables. Enforces quality scoring and QA/QC checklists.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
argument-hint: "[deliverable-type] [project-name] — e.g. 'cover letter Shakes Run MSD submittal', 'cost estimate Old Henry Road widening'"
---

# Superpowers — Structured Execution Framework

## Trigger Phrases
- Auto-activates on all client/agency/contractor deliverables
- "superpowers"
- "structured execution"
- "full process"
- "plan build review"

## Auto-Activation Conditions

This skill activates automatically when the task involves producing a deliverable for:
- **Client:** proposals, reports, cost estimates, presentations, letters
- **Agency:** submittal packages, permit applications, response letters, compliance reports
- **Contractor:** bid documents, construction drawings, specifications, RFI responses
- **Internal:** QC review reports, project briefs, meeting summaries

If the output is a deliverable that leaves JEDS (goes to a client, agency, or contractor), Superpowers is mandatory.

## The 5 Phases

### Phase 1: PLAN

Before writing a single word, answer every question in this checklist:

| Question | Answer Required |
|----------|----------------|
| **What is the deliverable?** | Specific document type (letter, report, estimate, plan set, etc.) |
| **Who is the audience?** | Name, role, organization, technical level, preferences |
| **Is there a template?** | Search repo for templates: `**/*template*`, `**/*boilerplate*` |
| **Is there an example?** | Search for prior similar deliverables: same client, same type, same agency |
| **What are the inputs?** | List every source document, dataset, reference, and context needed |
| **Where does the output go?** | File path, email, submittal portal, print |
| **What is the quality tier?** | See tier definitions below |

**Quality Tiers:**

| Tier | Name | Use Case | Review Level |
|------|------|----------|-------------|
| 1 | Draft | Internal working document, not shared externally | Self-review only |
| 2 | Internal Review | Shared within JEDS team for feedback | Peer review |
| 3 | Client-Ready | Goes to client for review or information | PM review + peer review |
| 4 | Agency Submittal | Goes to regulatory agency for formal review | Full QC per CLAUDE.md Section 10 |
| 5 | Record Document | Legal or contractual significance, permanent record | Full QC + principal review |

**Plan Output:**
```
## Execution Plan
- **Deliverable:** [type]
- **Audience:** [who]
- **Template:** [path or "none found"]
- **Example:** [path or "none found"]
- **Inputs:** [list]
- **Output Location:** [path]
- **Quality Tier:** [1-5]
- **Estimated Effort:** [time]
```

### Phase 2: BUILD

Execute the plan. Create the deliverable following these principles:

1. **Start from a template** if one exists. Never build from scratch when a template is available.
2. **Follow the audience's conventions:**
   - Agency deliverables: formal tone, complete sentences, standard formatting
   - Client deliverables: professional but accessible, tailored to their technical level
   - Contractor deliverables: precise, unambiguous, standard industry terminology
3. **Reference inputs explicitly.** Cite source documents, calculations, or standards by name.
4. **Structure for scanning.** Use headings, bullets, tables. Assume the reader will scan before reading.
5. **Include all required components.** Check the template or prior examples for standard sections.
6. **Leave nothing implied.** If a decision was made, state it. If an assumption was required, document it.

### Phase 3: REVIEW

Run the QA/QC checklist. Score each criterion 1-5.

**Quality Scoring Rubric:**

| Score | Meaning |
|-------|---------|
| 5 | Excellent — exceeds expectations, no improvements needed |
| 4 | Good — meets expectations, minor improvements possible |
| 3 | Acceptable — meets minimum requirements, notable improvements possible |
| 2 | Below Standard — missing important elements, requires revision |
| 1 | Unacceptable — fundamentally flawed, requires major rework |

**QA/QC Checklist:**

| # | Criterion | Score (1-5) | Notes |
|---|-----------|-------------|-------|
| 1 | **Completeness** — All required sections present? All questions answered? No placeholders or TBDs remaining? | | |
| 2 | **Accuracy** — Facts correct? Numbers verified? Standards cited correctly? Calculations checked? | | |
| 3 | **Audience Fit** — Tone appropriate? Technical level matched? Jargon explained where needed? Client/agency preferences followed? | | |
| 4 | **Structure** — Logical flow? Easy to scan? Headings and sections organized well? Tables used where appropriate? | | |
| 5 | **Actionability** — Clear next steps? Recommendations specific? Deadlines stated? Responsibilities assigned? | | |

**Scoring Rules:**
- **Target: 4.5+ average** across all 5 criteria
- If any single criterion scores below 3: proceed to Phase 4 (Refine) before shipping
- If average is below 4.0: proceed to Phase 4 (Refine) before shipping
- If average is 4.5+: proceed directly to Phase 5 (Ship)

**Additional checks for Tier 4-5 deliverables:**

| # | Check | Pass/Fail |
|---|-------|-----------|
| 6 | All applicable code/standard references verified | |
| 7 | All calculations independently checked | |
| 8 | Professional engineer stamp/signature block included where required | |
| 9 | Document control (revision number, date, author) present | |
| 10 | Distribution list identified | |

### Phase 4: REFINE

Address every deficiency identified in the Review phase:

1. **Fix all items scoring below 4** — revise the specific content.
2. **Re-score after fixes** — verify the fix actually improved the score.
3. **Iterate until target met:**
   - Tier 1-2: Average 3.5+ acceptable
   - Tier 3: Average 4.0+ required
   - Tier 4-5: Average 4.5+ required, no single item below 3
4. **Document what changed** — list the revisions made in this phase.

If after 2 refinement iterations the target is not met, flag for human review with specific items that need attention.

### Phase 5: SHIP

Deliver the final product:

1. **Write the file** to the specified output location.
2. **Generate the delivery summary:**

```
## Delivery Summary

### Deliverable
- **Type:** [document type]
- **File:** [output path]
- **Quality Tier:** [1-5]
- **Audience:** [who receives this]

### Quality Scores
| Criterion | Score |
|-----------|-------|
| Completeness | [X]/5 |
| Accuracy | [X]/5 |
| Audience Fit | [X]/5 |
| Structure | [X]/5 |
| Actionability | [X]/5 |
| **Average** | **[X.X]/5** |

### Revisions Made
- [List of changes from Refine phase, if any]

### Notes for Reviewer
- [Any caveats, assumptions, or items flagged for human review]

### Next Steps
- [What happens after delivery — review cycle, submittal, etc.]
```

3. **If Tier 3+**, recommend who should review before external distribution.
4. **If Tier 4-5**, generate a transmittal letter or cover sheet if not already included.

## Rules

- **Never skip phases.** Even for "quick" deliverables, run all 5 phases. The plan and review phases can be abbreviated for Tier 1-2, but they cannot be skipped.
- **Never ship below target.** If the quality score is below target after 2 refinement iterations, do not ship. Flag for human review.
- **Always document the quality score.** Every deliverable gets a scorecard, even Tier 1 drafts.
- **Templates first, always.** Search for existing templates before building from scratch. If no template exists and this deliverable type will recur, suggest creating one (invoke the Create skill).
- **The audience is always right.** Match their conventions, preferences, and expectations — not your own.
- **Assumptions are documented, not hidden.** If you had to assume something to complete the deliverable, state it explicitly.
- **Track refinement iterations.** If refinement is taking more than 2 passes, the problem is likely in the Plan phase — revisit inputs and requirements.

## Output Format

Every Superpowers execution produces:
1. **The deliverable itself** (written to the output location)
2. **The Execution Plan** (from Phase 1)
3. **The Quality Scorecard** (from Phase 3/4)
4. **The Delivery Summary** (from Phase 5)
