---
name: consolidate-memory
description: >
  Review recent session activity, extract key decisions, preferences, and facts,
  update the memory files accordingly, and promote important patterns from
  recent-memory to long-term-memory. Trigger when: "consolidate memory",
  "save this to memory", "update memory", "remember this", or at session end.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Consolidate Memory

Review recent session activity, extract key decisions, preferences, and facts,
update the memory files accordingly, and promote important patterns from
recent-memory to long-term-memory.

## When to Use

- End of a working session
- After major project decisions are made
- When the user says "remember this" or "save to memory"
- After completing a complex deliverable

## Phase 1: Read Current State

Read all three memory files:
- `memory/recent-memory.md` (rolling 48-hour context)
- `memory/long-term-memory.md` (distilled facts and patterns)
- `memory/project-memory.md` (active project state)

## Phase 2: Extract from Session

Scan recent conversation context for:
- Decisions made (project direction, design choices, client agreements)
- New facts learned (agency requirements, jurisdiction details, contact info)
- Preferences confirmed or changed
- Project status changes (phase transitions, blocking issues resolved)
- Workflow patterns (tools used, approaches that worked)

## Phase 3: Update Recent Memory

Update `memory/recent-memory.md`:
- Add new entries with timestamp, topic, decision/finding, context, and status
- Mark entries older than 48 hours as candidates for promotion or removal

## Phase 4: Update Project Memory

Update `memory/project-memory.md`:
- Update "Last Worked" dates for any projects touched this session
- Update current phase, blocking issues, next actions, and open questions
- Add new projects if they appeared in conversation

## Phase 5: Promote to Long-Term

Move to `memory/long-term-memory.md`:
- Entries that represent confirmed patterns (appeared 2+ times)
- Verified jurisdiction/agency learnings
- Confirmed preferences that supplement CLAUDE.md
- Clear promoted entries from recent-memory.md

## Phase 6: Report

```
## Memory Consolidation Report — [Date]

### Added to Recent Memory
- [entry summaries]

### Updated in Project Memory
- [project: what changed]

### Promoted to Long-Term Memory
- [entry: why promoted]

### Cleared from Recent Memory
- [entry: reason — promoted / stale / resolved]

### Needs Verification
- [entry: why verification needed]
```

## Rules

- Never delete memory entries without promoting or explicitly marking stale
- Always preserve the full history in long-term-memory — append, don't overwrite
- Flag any contradictions between new information and existing memory
- Cross-reference CLAUDE.md Section 2.7 (Confirmed vs. Inferred Information)
