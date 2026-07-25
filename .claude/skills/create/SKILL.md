---
name: create
description: Auto-detect repeatable workflows and capture them as reusable skills or agents. Converts manual multi-step processes into structured, deployable skill files with proper frontmatter, phases, and validation.
allowed-tools: Read, Write, Grep, Glob, Bash
argument-hint: "[skill-name] [description] — e.g. 'submittal-prep Package agency submittals from plan set'"
---

# Create — Skill & Agent Factory

## Trigger Phrases
- "make a skill"
- "create an agent"
- "automate this"
- "turn this into a skill"
- "save this workflow"
- "make this repeatable"

## Proactive Trigger
This skill also activates **proactively** when:
- A workflow has been executed **twice** in the current session or across recent sessions
- The same sequence of tool calls appears in a repeated pattern
- The user performs a multi-step process that could be parameterized

When proactively triggered, ask: "I've noticed you've done [workflow description] multiple times. Want me to capture this as a reusable skill?"

## Purpose

Create converts ad-hoc workflows into production-grade, reusable Claude Code skills or agent definitions. Every skill it produces follows the directory-format standard (`.claude/skills/[name]/SKILL.md`) with proper frontmatter, execution phases, rules, and output format.

## Execution Phases

### Phase 1: Workflow Capture

1. **Identify the workflow** — either from:
   - The user's explicit description
   - A conversation history pattern (repeated tool sequences)
   - An existing script or checklist being followed manually
2. **Extract the steps** — list every action in order, noting:
   - Which tools are used at each step
   - What inputs are required (parameters, file paths, context)
   - What outputs are produced
   - What decisions/branches exist
   - What validation checks occur
3. **Identify variables** — what changes between executions:
   - Client name, project name, file paths
   - Jurisdiction, standard version
   - Quality tier, output format

### Phase 2: Skill Architecture

1. **Choose the skill type:**
   - **Simple Skill** — linear workflow, <10 steps, single output
   - **Phased Skill** — multi-phase with checkpoints, complex output
   - **Agent Skill** — requires spawning subagents for parallel work
   - **Composite Skill** — orchestrates other existing skills
2. **Define the interface:**
   - `name`: kebab-case, descriptive, 2-3 words max
   - `description`: one sentence, starts with verb, says what it does
   - `allowed-tools`: minimum set needed (principle of least privilege)
   - `argument-hint`: show the user what to pass, with examples
   - Trigger phrases: 3-5 natural language triggers
3. **Map the phases:**
   - Each phase gets a clear name and numbered steps
   - Phases have entry conditions and exit criteria
   - Decision points are explicit with both branches documented

### Phase 3: Skill Construction

Build the SKILL.md file with this structure:

```markdown
---
name: [skill-name]
description: [One-sentence description starting with a verb]
allowed-tools: [Comma-separated tool list]
argument-hint: "[parameter template with examples]"
---

# [Skill Name] — [Subtitle]

## Trigger Phrases
- [3-5 natural language triggers]

## Purpose
[2-3 sentences explaining what this skill does and why]

## Execution Phases

### Phase 1: [Name]
[Numbered steps with tool usage, inputs, outputs]

### Phase 2: [Name]
[Numbered steps]

## Rules
- [Hard constraints, never/always rules]

## Output Format
[Template or structure for the deliverable]
```

### Phase 4: Validation

1. **Completeness check:**
   - Does every step have a clear action?
   - Are all required inputs documented?
   - Is the output format specified?
   - Are error cases handled?
2. **Tool check:**
   - Are all tools in `allowed-tools` actually used?
   - Are any tools used but not listed in `allowed-tools`?
3. **Trigger check:**
   - Are trigger phrases natural and unambiguous?
   - Do they overlap with existing skills? (Grep `.claude/skills/*/SKILL.md` for conflicts)
4. **Dry run:**
   - Mentally walk through the skill with a real example
   - Identify any missing steps or unclear instructions

### Phase 5: Deployment

1. Create the directory: `.claude/skills/[name]/`
2. Write the `SKILL.md` file
3. Verify the file was written correctly
4. Report what was created and how to invoke it

## Rules

- **Every skill MUST have frontmatter** with at minimum: name, description, allowed-tools.
- **Skills must be self-contained.** A skill cannot assume context from a previous conversation turn — it must specify what inputs it needs.
- **Principle of least privilege for tools.** Only list tools the skill actually needs. Never grant Write if the skill only reads.
- **No duplicate triggers.** Check existing skills before assigning trigger phrases.
- **Skills must be idempotent where possible.** Running the same skill twice with the same inputs should produce the same output without side effects.
- **Include error handling.** What happens if a file is not found? If a web search returns nothing? If the input is malformed?
- **Version awareness.** If the skill references external standards or APIs, note which version it targets.

## Naming Conventions

| Pattern | Example | Use When |
|---------|---------|----------|
| `verb-noun` | `check-compliance` | Action-oriented skills |
| `domain` | `stormwater` | Domain-specific lookup/analysis |
| `tool-action` | `civil3d-export` | Tool-specific automation |
| `process-name` | `plan-review` | Multi-step business processes |

## Output Format

When the skill is created, report:

```
## Skill Created: [name]

- **Location:** .claude/skills/[name]/SKILL.md
- **Triggers:** [list of trigger phrases]
- **Tools:** [allowed tools]
- **Phases:** [number] phases, [number] total steps
- **Usage:** Invoke with `/[name]` or say "[trigger phrase]"
```

## Anti-Patterns to Avoid

- **Over-engineering:** If it takes more effort to maintain the skill than to do the task manually, it's too complex. Split it.
- **Magic values:** Don't hardcode file paths, client names, or project-specific data. Use parameters.
- **Missing validation:** Every skill should check its inputs before executing.
- **Monolith skills:** If a skill has more than 5 phases or 30 steps, decompose it into multiple skills.
- **Orphan skills:** Every skill must have trigger phrases. If you can't think of when someone would invoke it, it shouldn't exist.
