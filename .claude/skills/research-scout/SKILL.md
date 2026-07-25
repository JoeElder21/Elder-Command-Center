---
name: research-scout
description: Scan for industry news, regulatory changes, tool updates, and market trends relevant to JEDS Engineering Solutions. Cross-references against existing knowledge and stores new findings in long-term memory.
allowed-tools: Read, Grep, Glob, Bash, WebSearch, WebFetch
argument-hint: "[topic-area] — e.g. 'Kentucky zoning changes', 'Civil 3D 2026 features', 'Claude Code updates', 'stormwater regulations'"
---

# Research Scout — Industry Intelligence Scanner

## Trigger Phrases
- "scout for updates"
- "what's new in"
- "research scout"
- "scan for changes"
- "industry update"
- "check for regulatory changes"

## Purpose

Research Scout proactively scans for news, regulatory changes, tool updates, and market trends that affect JEDS operations. It searches across defined topic areas, cross-references findings against existing knowledge in CLAUDE.md and long-term memory, discards redundant information, and stages genuinely new and actionable findings for memory storage. This is how JEDS stays current without manual monitoring.

## Scan Topics

### 1. Kentucky Planning & Zoning Changes
**Search targets:**
- Louisville Metro Planning Commission updates
- Jefferson County zoning amendments
- Kentucky General Assembly bills affecting land development
- Louisville Metro Land Development Code (LDC) revisions
- KRS changes relevant to civil engineering and land development

**Search queries:**
- `Louisville Metro planning commission agenda OR minutes [current year]`
- `Kentucky zoning ordinance amendment [current year]`
- `Louisville land development code update`
- `Kentucky General Assembly land development OR subdivision OR zoning`
- `Jefferson County Louisville planning zoning change`

### 2. AutoCAD Civil 3D Updates
**Search targets:**
- New Civil 3D releases and feature updates
- Autodesk product roadmap for infrastructure
- Civil 3D API changes
- Plugin and extension updates
- Known issues and workarounds

**Search queries:**
- `AutoCAD Civil 3D [current year] update new features`
- `Autodesk Civil 3D release notes [current year]`
- `Civil 3D API changes [current year]`
- `Autodesk infrastructure product roadmap`

### 3. Claude Code Updates
**Search targets:**
- New Claude Code releases and features
- Claude API changes (models, pricing, capabilities)
- MCP protocol updates
- New skills, tools, or agent patterns
- Best practices and workflow improvements

**Search queries:**
- `Claude Code update release notes [current year]`
- `Anthropic Claude API changes [current year]`
- `Model Context Protocol MCP update`
- `Claude Code new features agent`

### 4. Land Development Market Trends
**Search targets:**
- Louisville/Kentucky development activity
- Construction cost trends
- Material pricing changes
- Labor market conditions
- Development pipeline and permit activity

**Search queries:**
- `Louisville Kentucky development activity [current year]`
- `Kentucky construction cost index trend`
- `Louisville building permits issued [current year]`
- `civil engineering market outlook Kentucky`

### 5. Stormwater Regulation Updates
**Search targets:**
- MSD (Louisville Metropolitan Sewer District) regulation changes
- Kentucky DOW (Division of Water) updates
- EPA stormwater rule changes
- MS4 permit modifications
- BMP technology advances

**Search queries:**
- `Louisville MSD stormwater regulation update [current year]`
- `Kentucky Division of Water stormwater [current year]`
- `EPA stormwater rule change [current year]`
- `MS4 permit Kentucky update`
- `stormwater BMP new technology [current year]`

## Execution Phases

### Phase 1: Load Existing Knowledge

Before searching, know what we already know:

1. **Read CLAUDE.md** — extract current tool versions, standards referenced, procedures documented.
2. **Read `memory/long-term-memory.md`** — extract regulatory knowledge, tool configurations, market intelligence.
3. **Read `memory/recent-memory.md`** — check for recently scouted topics (avoid re-scouting within 7 days).
4. **Build a knowledge inventory:** List the key facts, versions, dates, and standards currently stored.

### Phase 2: Execute Scans

For each topic area (or the specific topic requested):

1. **Run 2-3 WebSearch queries** per topic.
2. **Fetch the top 3-5 results** per search using WebFetch.
3. **Extract key findings:**
   - What changed? (regulation, feature, price, etc.)
   - When did it change? (effective date, release date)
   - Who is affected? (JEDS directly? Clients? Projects?)
   - What action is needed? (update process, notify client, change tool config)
4. **Record source metadata:**
   - Source name and URL
   - Publication date
   - Author/agency
   - Reliability assessment

### Phase 3: Cross-Reference & Filter

Compare findings against existing knowledge:

1. **Redundancy check:**
   - Is this finding already in long-term memory? --> DISCARD (note as "already known")
   - Is this finding already in CLAUDE.md? --> DISCARD
   - Was this topic scouted in recent memory within 7 days? --> DISCARD unless the finding is genuinely new
2. **Relevance check:**
   - Does this affect JEDS operations directly? --> KEEP
   - Does this affect JEDS clients or projects? --> KEEP
   - Is this general industry noise with no actionable impact? --> DISCARD
3. **Urgency assessment:**
   - **Urgent:** Regulation effective immediately, tool breaking change, client-impacting
   - **Important:** Regulation effective within 6 months, notable tool update, market shift
   - **Informational:** Background trend, future roadmap item, nice-to-know
4. **Confidence assessment:**
   - Verified by 2+ sources --> High confidence
   - Single authoritative source --> Medium confidence
   - Single non-authoritative source --> Low confidence (flag for verification)

### Phase 4: Stage Findings

Prepare new findings for memory storage:

1. **Format each finding** using the staging template:

```markdown
### [Finding Title]
- **Topic Area:** [1-5 from scan topics]
- **Date Discovered:** [today's date]
- **Source:** [name + URL]
- **Confidence:** [High/Medium/Low]
- **Urgency:** [Urgent/Important/Informational]
- **Summary:** [2-3 sentence description of what changed]
- **Impact on JEDS:** [How this affects operations, projects, or clients]
- **Action Required:** [What JEDS should do about this, if anything]
- **Memory Target:** [Which memory category this belongs in]
```

2. **Write staged findings** to the long-term memory staging section.
3. **If urgent findings exist**, flag them prominently in the output.

### Phase 5: Report

Deliver the scouting report:

```
## Research Scout Report: [Date]

### Scan Summary
| Topic Area | Queries Run | Results Reviewed | New Findings | Discarded |
|------------|------------|-----------------|-------------|-----------|
| [topic] | [#] | [#] | [#] | [#] |

### New Findings

#### Urgent
[Any findings requiring immediate attention]

#### Important
[Notable findings worth acting on soon]

#### Informational
[Background trends and future items]

### Already Known (Confirmed Current)
[Items found that match existing memory — confirms our knowledge is up to date]

### Staged for Memory
[List of items written to long-term memory staging]

### Recommended Actions
1. [Specific action items based on findings]

### Next Scout
- **Recommended in:** [X days/weeks based on findings volatility]
- **Focus areas:** [Topics that showed the most change]
```

## Rules

- **Never store redundant information.** The entire point of cross-referencing is to avoid bloating memory with things we already know.
- **Always cite sources.** Every finding must have a traceable source.
- **Date everything.** Findings without dates are useless for tracking changes over time.
- **Urgency must be justified.** Don't cry wolf — only mark "Urgent" if there's a real operational impact.
- **Respect the 7-day cooldown.** Don't re-scout the same topic within 7 days unless explicitly asked.
- **Discard more than you keep.** A good scout run discards 80% of what it finds. Only genuinely new, relevant, actionable information gets staged.
- **Confidence levels matter.** Don't present a single blog post's claim with the same confidence as an official agency announcement.
- **Suggest actions, don't just report.** Every finding should connect to "so what?" — what does JEDS do about this?
- **Track what was scanned.** Record the scan date and topics in recent memory so we know when to scout again.

## Automated Scout Schedule (Recommended)

| Topic Area | Frequency | Rationale |
|------------|-----------|-----------|
| Kentucky Planning & Zoning | Bi-weekly | Commission meetings are typically monthly; bi-weekly catches agendas and minutes |
| Civil 3D Updates | Monthly | Software updates are periodic; monthly is sufficient |
| Claude Code Updates | Weekly | Rapidly evolving; weekly catches meaningful changes |
| Market Trends | Monthly | Trends move slowly; monthly is sufficient |
| Stormwater Regulations | Monthly | Regulatory changes are infrequent but high-impact |
