---
name: swarm
description: Decompose complex tasks into parallel subagents that execute concurrently, then synthesize results. Optimized for JEDS civil engineering and land development workflows.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
argument-hint: "[task-description] or [swarm-pattern-name] [project-name] — e.g. 'full plan review Shakes Run Phase 3', 'parcel feasibility 1234 Old Henry Rd'"
---

# Swarm — Parallel Agent Orchestrator

## Trigger Phrases
- "spin up a swarm"
- "parallel agents"
- "swarm this"
- "full plan review"
- "run agents in parallel"
- "decompose this task"

## Purpose

Swarm takes a complex, multi-faceted task and breaks it into independent work units that can execute as parallel subagents. Each agent gets a focused brief, executes independently, and returns structured results. The orchestrator then synthesizes all agent outputs into a unified deliverable. This is how JEDS handles tasks that would take hours sequentially — by running them concurrently.

## Execution Phases

### Phase 1: Context Capture

Before decomposition, gather everything the agents will need:

1. **Read the task description** — what is the user asking for? What is the final deliverable?
2. **Identify the project** — search for project files, prior work, relevant memory entries:
   - Grep for project name in `**/memory/*.md`, `**/*.md`
   - Check for project folders, plan sets, existing deliverables
3. **Identify constraints:**
   - Deadline or urgency level
   - Quality tier (draft, internal review, client-ready, agency submittal)
   - Dependencies between subtasks (what MUST be sequential?)
4. **Gather shared context** — information ALL agents will need:
   - Project location, jurisdiction, zoning
   - Client name and preferences
   - Applicable standards and codes
   - File paths to reference materials

### Phase 2: Decomposition

Break the task into independent work units:

1. **List all subtasks** needed to complete the deliverable.
2. **Identify dependencies** — draw a dependency graph:
   - Which tasks can run in parallel? (no shared inputs/outputs)
   - Which tasks must be sequential? (output of one feeds into another)
   - Which tasks are optional? (nice-to-have but not blocking)
3. **Group into waves:**
   - **Wave 1:** All tasks with no dependencies (run first, in parallel)
   - **Wave 2:** Tasks that depend on Wave 1 outputs (run after Wave 1)
   - **Wave N:** Continue until all tasks are assigned
4. **Size each task:** Estimate complexity (small/medium/large). If any task is "large," decompose it further.

### Phase 3: Agent Design

For each subtask, design an agent brief:

1. **Agent Name:** Short, descriptive (e.g., "civil-review-agent", "zoning-check-agent")
2. **Objective:** One sentence — what this agent must deliver.
3. **Context Packet:** The shared context from Phase 1, plus any task-specific context.
4. **Specific Instructions:** Step-by-step what to do.
5. **Output Format:** Exactly how to structure the result (template provided).
6. **Success Criteria:** How to know the agent completed its work.
7. **Failure Protocol:** What to do if the agent cannot complete (flag for human review, provide partial results).

### Phase 4: Execution Plan

Present the plan before executing:

```
## Swarm Plan: [Task Name]

### Wave 1 (Parallel)
| Agent | Objective | Est. Complexity |
|-------|-----------|-----------------|
| [name] | [one-line objective] | [S/M/L] |

### Wave 2 (After Wave 1)
| Agent | Depends On | Objective |
|-------|------------|-----------|

### Synthesis
[How agent outputs will be combined into the final deliverable]
```

Wait for user approval before executing, unless the task is urgent or the user has said "just do it."

### Phase 5: Execution

1. **Launch Wave 1 agents** — all in a single message with multiple Agent tool calls so they run concurrently.
2. **Collect results** as agents complete.
3. **Launch Wave 2 agents** once their dependencies are satisfied, passing relevant Wave 1 outputs.
4. **Continue** through all waves.

### Phase 6: Synthesis

1. **Merge all agent outputs** into a unified result.
2. **Resolve conflicts** — if agents produced contradictory findings, flag them.
3. **Fill gaps** — if any agent failed or returned incomplete results, note what's missing.
4. **Quality check** — does the synthesized result meet the original task requirements?
5. **Deliver** the final result in the format the user requested.

## JEDS-Specific Swarm Patterns

### Pattern: Full Plan Review

Trigger: "full plan review [project name]"

Launches 4 parallel review agents:

| Agent | Focus | Checks |
|-------|-------|--------|
| **Civil Review** | Grading, drainage, utilities, road design | Slopes, pipe sizing, utility conflicts, ADA compliance |
| **Landscape Review** | Planting, screening, buffer yards, tree preservation | LDC landscape requirements, plant spacing, species selection |
| **Zoning Review** | Setbacks, density, use permissions, parking | LDC zoning district standards, conditional use conditions |
| **Stormwater Review** | Detention, water quality, BMP sizing, MSD compliance | MSD Design Manual, post-construction requirements, SWPPP |

Synthesis: Combined review comment letter organized by sheet number, with severity ratings (Critical / Major / Minor / Note).

### Pattern: Parcel Feasibility

Trigger: "parcel feasibility [address or PVA ID]"

Launches 4 research agents:

| Agent | Research Area |
|-------|--------------|
| **Zoning Agent** | Current zoning, permitted uses, dimensional standards, overlay districts |
| **Utilities Agent** | Water, sewer, gas, electric availability and capacity |
| **Environmental Agent** | Floodplain, wetlands, sinkholes, environmental constraints |
| **Access Agent** | Road frontage, curb cuts, traffic study requirements, KYTC involvement |

Synthesis: One-page feasibility summary with Go/No-Go recommendation and risk matrix.

### Pattern: Agency Submittal

Trigger: "agency submittal [project name] [agency]"

Launches 2 parallel agents:

| Agent | Focus |
|-------|-------|
| **Compliance Agent** | Check all plan sheets against agency submittal checklist |
| **Jurisdiction Agent** | Verify jurisdiction-specific requirements (MSD, KYTC, Louisville Metro, etc.) |

Synthesis: Submittal-ready checklist with pass/fail for each item, list of missing items, and cover letter draft.

### Pattern: Project Startup

Trigger: "project startup [project name]"

Launches 3 research agents + 1 synthesis agent:

| Agent | Task |
|-------|------|
| **Site Research** | Pull PVA data, zoning, utilities, environmental constraints |
| **Regulatory Research** | Identify all required permits, approvals, agency reviews |
| **Precedent Research** | Find similar completed projects for reference |
| **Briefing Agent** (Wave 2) | Synthesize into project brief document |

Synthesis: Project brief with site summary, regulatory roadmap, timeline estimate, and risk register.

## Rules

- **Never launch more than 8 agents simultaneously.** Diminishing returns and context management issues beyond this.
- **Every agent gets the shared context packet.** No agent should have to re-discover project basics.
- **Agents must be independent within a wave.** If two agents in the same wave need each other's output, they belong in different waves.
- **Always present the plan before executing** unless the user explicitly says to skip review.
- **Flag conflicts, don't resolve silently.** If two agents disagree, present both findings and let the user decide.
- **Track agent completion.** Report which agents finished, which are pending, and which failed.
- **Each agent prompt must be self-contained.** Brief it like a colleague who just walked in — full context, clear objective, specific deliverable format.

## Output Format

### Swarm Execution Report

```
## Swarm Complete: [Task Name]

### Agents Executed
| Agent | Status | Key Findings |
|-------|--------|-------------|
| [name] | Complete/Partial/Failed | [1-2 sentence summary] |

### Synthesized Result
[The combined deliverable]

### Conflicts & Gaps
- [Any disagreements between agents]
- [Any missing information]

### Recommended Next Steps
- [What to do with the results]
```
