---
name: context7
description: Live documentation lookup for libraries, zoning codes, design standards, and KYTC manuals. Searches local knowledge base, web sources, and regulatory databases to return authoritative, cited answers.
allowed-tools: Read, Grep, Glob, Bash, WebSearch, WebFetch
argument-hint: "[topic or question] — e.g. 'KYTC drainage manual section 4', 'Louisville setback requirements R-4', 'Civil 3D pipe network API'"
---

# Context7 — Live Documentation Lookup

## Trigger Phrases
- "check the docs for ..."
- "look up the ordinance ..."
- "context7"
- "what does the code say about ..."
- "find the standard for ..."
- "KYTC manual section ..."
- "zoning code for ..."

## Purpose

Context7 retrieves authoritative, citable documentation from multiple sources — local project files, regulatory databases, design manuals, and web references. It replaces guessing from memory with verified, source-linked answers.

## Execution Phases

### Phase 1: Parse the Query

1. Identify the **domain**: zoning, design standard, KYTC manual, library/API docs, building code, stormwater regulation, or general reference.
2. Identify the **specificity level**: broad topic, specific section/article, or exact clause.
3. Identify the **jurisdiction** if applicable: Louisville/Jefferson County, Kentucky state, federal, or project-specific.
4. Extract **key terms** for search (e.g., "setback", "R-4 zone", "pipe network", "culvert sizing").

### Phase 2: Local Knowledge Search

Search the local repository first — fastest and most project-relevant.

1. **Glob** for relevant files:
   - `**/*zoning*`, `**/*ordinance*`, `**/*standard*`, `**/*manual*`
   - `**/*KYTC*`, `**/*specification*`, `**/*regulation*`
   - `**/memory/*.md`, `**/references/**`
2. **Grep** for key terms across the repo.
3. **Read** any matching files for full context.
4. Check `long-term-memory.md` and `project-memory.md` for previously stored references.

### Phase 3: Web Source Search

If local sources are insufficient or verification is needed:

1. **WebSearch** with targeted queries:
   - For zoning: `"Louisville Metro" OR "Jefferson County" [topic] zoning ordinance`
   - For KYTC: `KYTC "drainage manual" OR "highway design guide" [section]`
   - For design standards: `[standard name] [version] [section]`
   - For libraries: `[library name] [version] documentation [topic]`
2. **WebFetch** the top 2-3 results to extract relevant sections.
3. Cross-reference multiple sources when possible.

### Phase 4: Assemble the Answer

Structure the response with:

1. **Direct Answer** — the specific information requested, stated plainly.
2. **Source Citation** — exact document name, section number, URL, or file path.
3. **Relevant Context** — surrounding rules, exceptions, or related provisions that affect interpretation.
4. **Applicability Notes** — any caveats about jurisdiction, version, effective date, or project-specific overrides.
5. **Related References** — other sections or documents the user should also check.

## Source Priority Order

1. Project-local files (highest trust — already vetted for this project)
2. Official government/agency websites (.gov, .ky.us)
3. Published standards bodies (AASHTO, ACI, ASTM)
4. KYTC official manuals and guidance documents
5. Professional reference materials (textbooks, guides)
6. General web sources (lowest trust — flag as unverified)

## Rules

- **NEVER guess a code section number or regulatory requirement.** If you cannot find the exact reference, say so and suggest where to look.
- **ALWAYS include the source** — file path, URL, document name and section, or "not found."
- **Flag outdated information.** If a source has a publication date older than 2 years, note it.
- **Distinguish between jurisdictions.** Louisville Metro, Jefferson County, Kentucky state, and federal requirements are different. Never conflate them.
- **Quote directly** when the exact wording matters (legal/regulatory text). Paraphrase only for explanatory context.
- **Note effective dates** for any regulation or standard that has been recently updated or is pending update.

## Output Format

```
## Context7 Lookup: [Topic]

### Answer
[Direct answer to the question]

### Source
- **Document:** [Name, section, page]
- **Location:** [URL or file path]
- **Effective Date:** [If applicable]

### Context
[Surrounding rules, exceptions, related provisions]

### Applicability Notes
[Caveats, jurisdiction notes, version info]

### Related References
- [Other documents/sections to check]
```

## Common Lookup Domains

| Domain | Primary Sources |
|--------|----------------|
| Louisville Zoning | Louisville Metro Land Development Code (LDC) |
| Kentucky Transportation | KYTC Highway Design Guide, Drainage Manual, Standard Drawings |
| Stormwater | MSD Design Manual, Kentucky BMP Manual |
| Building Code | Kentucky Building Code (KBC), IBC |
| ADA/Accessibility | PROWAG, ADA Standards for Accessible Design |
| Civil 3D | Autodesk Knowledge Network, Civil 3D API docs |
| Surveying | Kentucky KRS Chapter 322, 201 KAR standards |
| Environmental | USACE Section 404, KY DOW regulations |
