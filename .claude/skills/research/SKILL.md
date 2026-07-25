---
name: research
description: Deep multi-source parallel research with cross-referencing and synthesis. Decomposes questions into sub-questions, runs parallel discovery, validates across sources, and delivers cited findings.
allowed-tools: Read, Grep, Glob, Bash, WebSearch, WebFetch
argument-hint: "[question or topic] — e.g. 'compare bioretention vs permeable pavement for MSD compliance', 'Kentucky SB 123 impact on subdivision regs'"
---

# Research — Deep Multi-Source Investigation

## Trigger Phrases
- "research this"
- "look into"
- "compare options for"
- "find out about"
- "what are the pros and cons of"
- "deep dive on"
- "investigate"

## Purpose

Research conducts thorough, multi-source investigations that go far beyond a single search query. It decomposes complex questions, runs parallel discovery across local files and web sources, cross-references findings for accuracy, and synthesizes everything into an actionable, cited deliverable. It never summarizes from a single source.

## Execution Phases

### Phase 1: Decompose the Question

Break the user's question into 3-5 independent sub-questions that, when answered together, fully address the topic.

**Process:**
1. Restate the user's question in precise terms.
2. Identify what you need to know to answer it completely:
   - **Factual sub-questions:** What are the hard facts? (costs, dimensions, regulations)
   - **Comparative sub-questions:** How do options differ? (performance, cost, risk)
   - **Contextual sub-questions:** What's the local/project-specific context? (jurisdiction, site conditions)
   - **Temporal sub-questions:** Has anything changed recently? (new regulations, updated standards)
   - **Practical sub-questions:** What does implementation look like? (timeline, resources, process)
3. List the sub-questions in priority order.
4. Identify which sub-questions can be researched in parallel vs. sequentially.

**Example Decomposition:**
> User: "Should we use bioretention or permeable pavement for the Shakes Run project?"
>
> Sub-questions:
> 1. What are MSD's current requirements for post-construction water quality BMPs?
> 2. What are the site-specific constraints at Shakes Run (soils, slope, space)?
> 3. What are the cost, maintenance, and performance differences between bioretention and permeable pavement?
> 4. Has MSD expressed a preference or issued guidance favoring either approach?
> 5. What have similar Louisville-area projects used successfully?

### Phase 2: Parallel Discovery

For each sub-question, conduct targeted research using multiple sources:

1. **Local sources first:**
   - Grep the repository for relevant terms, project files, memory entries
   - Read any matching files for detailed context
   - Check `long-term-memory.md` and `project-memory.md` for prior research
2. **Web sources second:**
   - WebSearch with 2-3 different query formulations per sub-question
   - WebFetch the top 2-3 results per search
   - Target authoritative sources: .gov, .edu, professional organizations, official agency sites
3. **Source documentation:**
   - For every finding, record: source name, URL or file path, date, author/agency
   - Rate source reliability: Official/Authoritative/Professional/General/Unverified
   - Note any paywall or access limitations

**Search Strategy by Domain:**

| Domain | Search Approach |
|--------|----------------|
| Regulatory/Code | Official agency sites, state legislature, code repositories |
| Technical/Engineering | ASCE, AASHTO, NCHRP, manufacturer tech docs |
| Cost/Market | RSMeans, recent bid tabs, industry publications |
| Local/Jurisdictional | Louisville Metro, MSD, KYTC, PVA, county records |
| Precedent/Case Study | Project databases, conference proceedings, trade publications |

### Phase 3: Cross-Reference

Validate findings across sources:

1. **Fact verification:** Does each key finding appear in at least 2 independent sources?
   - If yes: mark as **Verified**
   - If only 1 source: mark as **Unverified** and note the limitation
   - If sources conflict: mark as **Disputed** and document both positions
2. **Currency check:** Is the information current?
   - Check publication dates
   - Look for superseding documents or updates
   - For regulations, verify the cited version is still in effect
3. **Applicability check:** Does the information apply to this specific situation?
   - Correct jurisdiction?
   - Correct project type/scale?
   - Correct time frame?
4. **Bias check:** Is any source potentially biased?
   - Manufacturer data about their own products
   - Advocacy organizations with a stated position
   - Outdated sources that predate current best practices

### Phase 4: Synthesize

Combine all findings into a unified, actionable deliverable:

1. **Lead with the answer.** State the conclusion or recommendation first, then support it.
2. **Organize by theme, not by source.** Group findings logically, not "Source A says... Source B says..."
3. **Quantify where possible.** Prefer numbers over adjectives (e.g., "$12/SF" not "expensive").
4. **Acknowledge uncertainty.** If the answer is unclear, say so and explain what additional information would resolve it.
5. **Include actionable next steps.** What should the user do with this information?

## Rules

- **NEVER summarize from a single source.** Every key finding must be cross-referenced. If only one source exists, explicitly state that limitation.
- **ALWAYS cite sources.** Every factual claim gets a source attribution.
- **Distinguish facts from opinions.** Label interpretive statements as such.
- **Prefer primary sources over secondary.** A regulation's actual text over a blog post about it.
- **Date everything.** Include publication/access dates for all sources.
- **Flag stale information.** Anything older than 2 years in a fast-changing domain gets a staleness warning.
- **No hallucinated citations.** If you cannot find a source for something, do not fabricate one. Say "I could not verify this claim."
- **Respect scope.** Answer the question asked. Note related findings in a separate section, don't let them dilute the core answer.

## Output Format

```
## Research Report: [Topic]

### Executive Summary
[2-3 sentence answer to the original question with recommendation if applicable]

### Key Findings

#### [Theme 1]
[Findings organized by theme, not by source]
- [Finding with source citation]
- [Finding with source citation]

#### [Theme 2]
[...]

### Comparison Matrix
(Include when comparing options)

| Criterion | Option A | Option B | Notes |
|-----------|----------|----------|-------|
| [criterion] | [value] | [value] | [context] |

### Sources

| # | Source | Type | Date | Reliability |
|---|--------|------|------|-------------|
| 1 | [Name + URL/path] | [Official/Professional/General] | [Date] | [Verified/Unverified] |

### Confidence Assessment
- **Overall confidence:** [High/Medium/Low]
- **Key uncertainties:** [What we don't know]
- **What would increase confidence:** [Additional research or verification needed]

### Recommended Next Steps
1. [Specific action items]
```

## Research Quality Standards

| Criterion | Minimum Standard |
|-----------|-----------------|
| Sources per finding | 2+ independent sources |
| Source diversity | At least 2 different source types (e.g., government + professional) |
| Currency | Primary sources from within 3 years |
| Local applicability | At least 1 jurisdiction-specific source |
| Completeness | All sub-questions addressed or gaps explicitly noted |
