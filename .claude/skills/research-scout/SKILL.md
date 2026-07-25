---
name: research-scout
description: >
  Find new information that challenges or updates existing knowledge. Search the
  web for new strategies, tools, announcements, and workflow changes relevant to
  Joe Elder's professional context. Trigger when: "scout for updates",
  "what's new in", "research scout", "check for changes", or on scheduled runs.
allowed-tools: Read, Grep, Glob, Bash, WebSearch, WebFetch
---

# Research Scout

Find new information that challenges or updates existing knowledge. Search the web
for new strategies, tools, announcements, and workflow changes relevant to
Joe Elder's professional context and current documentation.

## When to Use

- Scheduled runs (3x per week recommended)
- When the user asks "what's new in [topic]"
- Before starting a project in a jurisdiction not recently researched
- When checking for regulatory or tool updates

## Phase 1: Define Search Scope

Based on Joe's professional context:
- Civil engineering tools and workflows (AutoCAD Civil 3D updates, BIM trends)
- Landscape architecture industry news
- Kentucky planning and zoning regulatory changes
- Land development market trends (Kentucky and Southeast US)
- AI tools for engineering and design workflows
- Claude Code and AI coding assistant updates
- Construction technology and project management tools
- Stormwater management regulation updates

## Phase 2: Execute Searches

Default search queries:
- "Kentucky planning zoning regulation changes [current year]"
- "AutoCAD Civil 3D new features [current year]"
- "Claude Code updates new features"
- "land development market trends Kentucky"
- "stormwater management regulation updates"
- "AI tools civil engineering design"
- "landscape architecture technology trends"

## Phase 3: Cross-Reference

For each finding:
- Read CLAUDE.md to check if the finding contradicts or updates current knowledge
- Read relevant prompt files if the finding relates to a specific deliverable type
- Check `memory/long-term-memory.md` for duplicate entries
- Discard anything redundant

## Phase 4: Store Findings

Store validated findings in `memory/long-term-memory.md` under "New Learnings (Staging)":

```
### [Category] — [Topic]
- **Date Added**: YYYY-MM-DD
- **Source**: [URL]
- **Finding**: One-line description
- **Impact**: How it affects current workflows
```

## Phase 5: Report

```
## Research Scout Report — [Date]

### New Findings
| # | Category | Finding | Source | Impact | Action |
|---|----------|---------|--------|--------|--------|
| 1 | | | URL | | Update CLAUDE.md / Note / No action |

### Contradictions Found
- [What existing knowledge is challenged and by what source]

### Staged in Long-Term Memory
- [Entries added to New Learnings staging]

### No Action Needed
- [Searches that returned nothing new]
```

## Rules

- Never present training data as current — always verify with live sources
- Discard redundant information ruthlessly
- Flag anything requiring immediate action (regulatory deadlines, security updates)
- Prioritize findings that affect active projects
