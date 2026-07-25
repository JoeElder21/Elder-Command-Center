---
name: system-design
description: Map business and project delivery systems into buildable architectures with cost analysis and ROI justification. Optimized for JEDS civil engineering and land development operations.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
argument-hint: "[system-type] [project-or-client-name] — e.g. 'project delivery pipeline JEDS', 'submittal tracking Louisville Metro', 'estimating pipeline'"
---

# System Design — Business Architecture Mapper

## Trigger Phrases
- "system design"
- "map this system"
- "architect this"
- "lay out the pipeline"
- "design the workflow"
- "build the system for"
- "how should we structure"

## Purpose

System Design translates business processes, project delivery workflows, and operational needs into structured, buildable system architectures. It documents the current state, designs the target state, identifies the build steps, and provides cost analysis with ROI justification. Every system it designs is grounded in real operational needs — not abstract architecture for its own sake.

## Execution Phases

### Phase 1: Discovery

Understand the current state before designing anything.

1. **Identify the system scope:**
   - What business process or workflow is being systematized?
   - Who are the users/stakeholders?
   - What are the inputs and outputs?
   - What are the current pain points?
2. **Map the current state:**
   - Search the repo for existing documentation, workflows, templates
   - Check memory files for prior decisions or context
   - Interview questions for the user (if needed):
     - "What does the current process look like step by step?"
     - "Where does it break down?"
     - "What takes the most time?"
     - "What gets missed most often?"
3. **Identify constraints:**
   - Budget (one-time build + ongoing maintenance)
   - Timeline (when does this need to be operational?)
   - Technical skills available (who will maintain this?)
   - Tools already in use (what must we integrate with?)
   - Regulatory requirements (what must the system comply with?)

### Phase 2: Architecture Design

Design the target system.

1. **Define system boundaries:**
   - What is IN scope vs. OUT of scope?
   - What interfaces with external systems?
   - What is automated vs. manual?
2. **Design the components:**
   - For each component, define:
     - **Purpose:** What it does
     - **Inputs:** What it receives
     - **Outputs:** What it produces
     - **Logic:** How it transforms inputs to outputs
     - **Storage:** What data it persists
     - **Triggers:** What initiates it (manual, scheduled, event-driven)
3. **Design the data flow:**
   - How does information move through the system?
   - Where is the single source of truth for each data type?
   - What are the handoff points between components?
4. **Design error handling:**
   - What happens when a component fails?
   - How are exceptions routed for human review?
   - What monitoring and alerting is needed?

### Phase 3: JEDS Pattern Matching

Check against known JEDS system patterns for reusable architecture.

#### Pattern: Project Delivery Pipeline
**Scope:** End-to-end project lifecycle from proposal to closeout.

```
Proposal → Contract → Kickoff → Design (30/60/90%) → Internal QC
→ Client Review → Agency Submittal → Permit → Construction Support → Closeout
```

Key components:
- Project intake form (standardized data capture)
- Milestone tracker (stage gates with checklists)
- Document management (plan sets, reports, calculations)
- Time/budget tracking (hours vs. fee, % complete)
- Communication log (client, agency, sub-consultant)

#### Pattern: Client Acquisition System
**Scope:** Lead identification through proposal win.

```
Lead Source → Qualification → Pursuit Decision → Proposal Prep
→ Interview/Presentation → Selection → Contract Negotiation → Kickoff
```

Key components:
- Lead tracking (source, value, probability)
- Go/No-Go scoring matrix
- Proposal template library
- Win/loss tracking with lessons learned
- Client relationship history

#### Pattern: Submittal Tracking
**Scope:** Agency plan review and permit acquisition.

```
Pre-Submittal Meeting → Prepare Package → Submit → Agency Review
→ Comments Received → Revise & Respond → Resubmit → Approval → Permit
```

Key components:
- Submittal checklist by agency (MSD, Louisville Metro, KYTC, etc.)
- Review comment tracker (comment, response, status)
- Deadline management (review period tracking)
- Fee tracking (application fees, review fees, permit fees)
- Agency contact directory

#### Pattern: Field Operations
**Scope:** Construction observation, staking, and field data collection.

```
Field Request → Schedule → Mobilize → Observe/Stake → Document
→ Report → File → Invoice
```

Key components:
- Field request intake
- Scheduling and dispatch
- Field report templates (observation, staking, material testing)
- Photo documentation with location tagging
- Issue tracking (RFI, non-compliance, change order)

#### Pattern: Estimating Pipeline
**Scope:** Cost estimation from concept through bid-ready.

```
Scope Definition → Quantity Takeoff → Unit Pricing → Estimate Assembly
→ Contingency Analysis → Internal Review → Client Presentation
```

Key components:
- Quantity takeoff templates by work type
- Unit cost database (updated annually)
- Estimate templates (conceptual, preliminary, detailed, bid)
- Contingency guidelines by project phase
- Historical cost data from completed projects

### Phase 4: Build Plan

Create a phased implementation plan.

1. **Prioritize by impact:**
   - What delivers the most value fastest?
   - What are the quick wins vs. long-term investments?
   - What is the minimum viable system?
2. **Phase the build:**
   - **Phase 1 (MVP):** Core functionality, manual where acceptable
   - **Phase 2 (Automation):** Automate repetitive steps, add integrations
   - **Phase 3 (Optimization):** Analytics, reporting, continuous improvement
3. **Define deliverables per phase:**
   - What gets built?
   - What gets documented?
   - What gets trained?
   - What is the acceptance criteria?

### Phase 5: Cost Analysis & ROI

Justify the investment.

1. **Cost estimation:**
   - Build cost (hours to design and implement each component)
   - Tool/platform costs (subscriptions, licenses)
   - Ongoing maintenance (hours/month to operate and update)
   - Training cost (hours to train team members)
2. **Value estimation:**
   - Time saved per occurrence (hours)
   - Frequency of occurrence (per week/month/year)
   - Error reduction (fewer rework cycles, missed deadlines, lost items)
   - Revenue impact (faster delivery, more capacity, fewer lost opportunities)
3. **ROI calculation:**
   ```
   Annual Value = (Hours Saved x Hourly Rate) + (Errors Avoided x Cost per Error)
   Payback Period = Total Build Cost / Annual Value
   3-Year ROI = ((Annual Value x 3) - Total Build Cost) / Total Build Cost x 100%
   ```
4. **Risk assessment:**
   - What if adoption is slower than expected?
   - What if requirements change mid-build?
   - What is the cost of NOT building this system?

## Rules

- **Start with the problem, not the solution.** Understand what's broken before proposing a fix.
- **Design for the team you have.** Don't design systems that require skills or tools the team doesn't have.
- **Prefer boring technology.** Spreadsheets, templates, and checklists beat custom software when the process is straightforward.
- **Every component must have a clear owner.** If nobody will maintain it, don't build it.
- **Document decisions, not just designs.** Record WHY you chose this architecture, not just WHAT it is.
- **Plan for day 2.** How will this system be maintained, updated, and evolved? If the answer is "it won't," reconsider.
- **Quantify everything possible.** "It will save time" is not sufficient. "It will save 4 hours per submittal, with 3 submittals per month" is.

## Output Format

```
## System Design: [System Name]

### Problem Statement
[What problem does this system solve? Who is affected? What is the cost of the status quo?]

### Current State
[How things work today — process map, pain points, metrics]

### Target State Architecture

#### System Overview
[High-level diagram or description of the target system]

#### Components
| Component | Purpose | Input | Output | Owner |
|-----------|---------|-------|--------|-------|

#### Data Flow
[How information moves through the system]

### Build Plan

#### Phase 1: MVP ([timeline])
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

#### Phase 2: Automation ([timeline])
- [ ] [Deliverable 3]

### Cost Analysis
| Item | One-Time | Monthly | Annual |
|------|----------|---------|--------|
| Build | $X | — | — |
| Tools | — | $X | $X |
| Maintenance | — | $X | $X |
| **Total** | **$X** | **$X** | **$X** |

### ROI Justification
- **Annual value:** $X
- **Payback period:** X months
- **3-year ROI:** X%

### Risks & Mitigations
| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|

### Decision Log
| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|
```
