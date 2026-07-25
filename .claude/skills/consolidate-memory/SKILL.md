---
name: consolidate-memory
description: Update the memory layer with session decisions, project state changes, and pattern promotions. Reads current memory files, extracts actionable information from the session, and updates memory with proper categorization and timestamping.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Consolidate Memory — Memory Layer Update

## Trigger Phrases
- "consolidate memory"
- "save to memory"
- "remember this"
- "update memory"
- "store this for later"
- "add this to long-term memory"

## Purpose

Consolidate Memory maintains the three-tier memory system that gives Claude persistent context across sessions. It reads the current memory files, extracts decisions, facts, preferences, and patterns from the current session, updates the appropriate memory tier, and promotes confirmed patterns from recent to long-term memory. This is how JEDS operations knowledge compounds over time.

## Memory Architecture

### Tier 1: Recent Memory (`memory/recent-memory.md`)
- **Scope:** Current session and last 2-3 sessions
- **Content:** Decisions made, tasks completed, context established, questions answered
- **Lifecycle:** Reviewed each consolidation; items either promoted to long-term or archived
- **Format:** Timestamped entries, newest first

### Tier 2: Long-Term Memory (`memory/long-term-memory.md`)
- **Scope:** Persistent knowledge that applies across all sessions
- **Content:** Confirmed patterns, client preferences, standard procedures, tool configurations, regulatory facts
- **Lifecycle:** Permanent unless explicitly invalidated; updated when patterns change
- **Format:** Categorized sections with entries

### Tier 3: Project Memory (`memory/project-memory.md`)
- **Scope:** Per-project state and context
- **Content:** Project status, key decisions, stakeholder contacts, milestone tracking, open issues
- **Lifecycle:** Active for project duration; archived at project closeout
- **Format:** Organized by project name with status tracking

## Execution Phases

### Phase 1: Read Current State

1. **Read all three memory files:**
   - `memory/recent-memory.md` — current recent memory
   - `memory/long-term-memory.md` — current long-term memory
   - `memory/project-memory.md` — current project memory
   - If any file doesn't exist, create it with the standard template (see Templates below)
2. **Read CLAUDE.md** for any relevant context about memory management conventions.
3. **Note the current date** for timestamping entries.

### Phase 2: Extract from Session

Scan the current session for information worth preserving:

#### Decisions
- Any explicit decision made ("we decided to...", "let's go with...", "the approach is...")
- Tool or technology choices
- Process changes
- Client/project direction changes

#### Facts Discovered
- Regulatory requirements learned
- Technical specifications confirmed
- Contact information obtained
- Pricing or cost data gathered
- Site conditions identified

#### Preferences Established
- Formatting preferences
- Communication style preferences
- Tool usage preferences
- Quality standards preferences

#### Patterns Observed
- Workflows that were repeated
- Approaches that worked well
- Approaches that failed
- Sequences of actions that should become skills

#### Project State Changes
- Tasks completed
- Milestones reached
- Issues opened or resolved
- Scope changes
- Schedule changes

### Phase 3: Categorize & Prioritize

For each extracted item, determine:

1. **Which memory tier?**
   - One-time decision or task completion --> Recent Memory
   - Reusable knowledge or confirmed pattern --> Long-Term Memory
   - Project-specific state change --> Project Memory
   - Multiple tiers if applicable (e.g., a decision that also establishes a pattern)

2. **Priority level:**
   - **Critical:** Would cause errors if forgotten (regulatory requirements, client constraints)
   - **Important:** Would reduce efficiency if forgotten (preferences, standard procedures)
   - **Nice-to-have:** Useful context but not essential (background info, minor preferences)

3. **Redundancy check:**
   - Is this already in memory? If yes, does it UPDATE existing info or is it truly redundant?
   - If updating, modify the existing entry rather than adding a duplicate
   - If redundant, skip it

### Phase 4: Update Memory Files

#### Updating Recent Memory

Add new entries at the top of the file with this format:

```markdown
## [Date: YYYY-MM-DD]

### Decisions
- [Decision description] — Context: [why this decision was made]

### Tasks Completed
- [Task description] — Output: [what was produced]

### Context Established
- [Context item] — Source: [where this came from]

### Open Items
- [Item that needs follow-up] — Next step: [what to do]
```

#### Updating Long-Term Memory

Add or update entries in the appropriate category section:

```markdown
### [Category Name]
(e.g., Client Preferences, Regulatory Knowledge, Tool Configuration, Standard Procedures)

- **[Item Name]:** [Description] — Added: [date], Source: [session context]
```

Standard categories for long-term memory:
- **Client Preferences** — How specific clients like things done
- **Regulatory Knowledge** — Verified code requirements, agency procedures
- **Standard Procedures** — Established workflows, checklists, processes
- **Tool Configuration** — Settings, integrations, customizations
- **Quality Standards** — Established quality bars, review criteria
- **Contact Directory** — Key contacts by agency, client, organization
- **Pricing & Costs** — Unit costs, fee structures, budget benchmarks
- **Lessons Learned** — What worked, what didn't, what to do differently

#### Updating Project Memory

Add or update entries under the project heading:

```markdown
## [Project Name]
**Status:** [Active/On Hold/Complete]
**Last Updated:** [date]

### Current Phase
[Where the project stands]

### Key Decisions
- [Date]: [Decision] — [Rationale]

### Open Issues
- [Issue] — Owner: [who], Due: [when]

### Milestones
- [x] [Completed milestone] — [date]
- [ ] [Upcoming milestone] — [target date]
```

### Phase 5: Promote Patterns

Review recent memory for items that have been confirmed through repetition:

1. **Scan recent memory** for items that appear in 2+ sessions.
2. **Identify promotion candidates:**
   - A preference stated and followed multiple times --> promote to Long-Term
   - A workflow executed multiple times --> promote to Long-Term (and suggest creating a skill)
   - A fact verified from multiple sources --> promote to Long-Term
   - A project decision that establishes a precedent --> promote to Long-Term
3. **Execute promotions:**
   - Add the item to long-term memory with proper categorization
   - Mark the item in recent memory as "Promoted to long-term memory"
   - Remove the original recent memory entry after promotion
4. **Archive stale items:**
   - Items older than 5 sessions with no promotion --> archive (remove from recent memory)
   - Before archiving, check: is this still relevant? If yes, promote instead of archiving.

## Templates

### Recent Memory Template
```markdown
# Recent Memory

> Active session context and recent decisions. Items are promoted to long-term memory
> when confirmed through repetition, or archived when stale.

## [Date: YYYY-MM-DD]

### Decisions
- [None yet]

### Tasks Completed
- [None yet]

### Context Established
- [None yet]

### Open Items
- [None yet]
```

### Long-Term Memory Template
```markdown
# Long-Term Memory

> Persistent knowledge that applies across all sessions. Organized by category.
> Items are promoted here from recent memory when confirmed through repetition.

## Client Preferences

## Regulatory Knowledge

## Standard Procedures

## Tool Configuration

## Quality Standards

## Contact Directory

## Pricing & Costs

## Lessons Learned
```

### Project Memory Template
```markdown
# Project Memory

> Per-project state and context. Organized by project name.
> Active projects are listed first, followed by completed/archived projects.

## Active Projects

## Completed Projects
```

## Rules

- **Never delete without archiving.** Information removed from one memory tier should be noted somewhere (even if just a "removed [item] on [date]" log entry).
- **Timestamp everything.** Every entry gets a date.
- **No duplicates.** Check before adding. Update existing entries rather than creating duplicates.
- **Promote, don't copy.** When promoting from recent to long-term, remove from recent after adding to long-term.
- **Be specific.** "Client prefers formal tone" is too vague. "MSD prefers cover letters with project number in subject line and PE signature block" is useful.
- **Preserve source context.** Note where the information came from so it can be verified later.
- **Keep recent memory lean.** It should represent the last 2-3 sessions, not an infinite log.
- **Respect privacy.** Don't store personal information beyond professional contact details.

## Output Format

```
## Memory Consolidation Report

### Items Added
| Tier | Category | Item | Priority |
|------|----------|------|----------|
| [Recent/Long-Term/Project] | [category] | [brief description] | [Critical/Important/Nice-to-have] |

### Items Promoted
| From | To | Item |
|------|----|------|
| Recent | Long-Term | [description] |

### Items Archived
| Tier | Item | Reason |
|------|------|--------|
| Recent | [description] | [stale/superseded/etc.] |

### Memory Health
- Recent Memory: [X] entries ([X] new, [X] promoted, [X] archived)
- Long-Term Memory: [X] entries across [X] categories
- Project Memory: [X] active projects, [X] completed
```
