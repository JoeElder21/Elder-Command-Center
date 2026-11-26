# CLAUDE.md — Elder Command Center

AI operating standard for **Elder Land Design** (JEDS, Joe Elder Design Studios) and Savage Investments. This file is context, not enforcement: hard stops belong in hooks and settings. The global `~/.claude/CLAUDE.md` governs identity, approvals and the Brains, and wins on any conflict.

## 1. Identity and titles (read first)

- Joe Elder is Founder & Principal of Elder Land Design (JEDS), a land-development design studio working across site and civil design, landscape design, and the overlap between them.
- Joe is not a licensed PE or PLA. Never give him PE, PLA, "engineer", "landscape architect", "licensed" or "engineer of record". Signature: `Joe Elder / Founder & Principal / Elder Land Design`.
- Work that needs a seal or licensure belongs to the licensed professional of record. Wherever a prompt or template says "PE/PLA of record", that is the licensed professional engaged on the project, never Joe. Flag it; never imply it.
- Brand: `references/brand/jeds.md` (JEDS) and `references/brand/savage.md` (Savage Investments, owned by the Apex Brain).
- Project rosters, client contacts and Brain data live in the Apex Brain (Google Drive), never in this repository.

## 2. Rules for every output

1. Accuracy over speed. Never guess setbacks, pipe sizes, soils or code sections. Cite document, section and edition, or write VERIFY.
2. Never invent contacts, citations, project facts, survey or geotechnical data, bids, minutes or correspondence. Name the source that is needed.
3. Label every site condition Existing (E), Demolition (D) or Proposed (P).
4. Label confidence HIGH, MEDIUM or LOW. Mark [Inferred] and [Assumed] items. AI output is never field-verified data.
5. Quote regulatory language in agency documents; do not paraphrase it.
6. Be jurisdiction-specific. Never carry one jurisdiction's standard to another.
7. When requirements conflict: life safety, then regulatory compliance, then constructability, then design intent, then cost.

## 3. Output

- Answer first. Use tables for structured data. Quick questions: answer, support, next step.
- Formal deliverables only: Context, Analysis, Findings, Recommendations, Next Steps, plus Assumptions, Risk Flags and a revision log (Rev 0 is the initial draft; see `references/deliverables.md`).
- Real decisions only: one line each for baseline, top-1% move and missing move. Otherwise skip them.
- Everything outbound is a DRAFT headed "DRAFT — approval required before sending". Nothing is sent, filed or posted without Joe's approval.
- Voice: professional, direct, specific, action-oriented. No filler.

## 4. Where things live (open on demand)

| Need | Open |
|------|------|
| Task prompts | `prompts/<task>.md` |
| Report and letter templates | `templates/` |
| Communication drafts (client, contractor, agency) | `references/communication-standards.md` |
| Checklists: civil, stormwater, landscape, zoning, construction documents, QA/QC | `references/checklists/` |
| Standards, details, zoning by jurisdiction, agencies | `references/standards/`, `references/details/`, `references/zoning/` |
| Deliverable catalog, phase matrix, revision log | `references/deliverables.md` |
| Output modes and daily planning format | `references/output-modes.md` |
| Worked workflows and samples (fictional data) | `examples/` |
| Brand system | `references/brand/` |
| Setup, versions, checksums | `references/setup/` |

Numbers, names and contacts in `examples/` are invented. Never reuse them as requirements or facts.

## 5. Commands

| Command | Purpose |
|---------|---------|
| `python tools/run_tests.py` | Run lint, template and naming checks before committing |
| `python tools/generate_pdf.py [--batch]` | Markdown to PDF |
| `python tools/lint.py`, `format.py`, `generate_toc.py` | Content tools |
| `python tools/plugin_usage.py` | Rank plugins by real use and count their hooks (run on your own machine) |
| `python tools/claude_profile.py` plan, lean, full, enable | Load only your most-used plugins by default; bring any or all back (run on your own machine) |

Python 3.10+, Ruff, 120 columns, type hints and Google-style docstrings.

## 6. Git and files

- Commits: `type(scope): message`, imperative (feat, fix, docs, style, refactor, test, chore).
- Claude cloud sessions work on `claude/*` branches and open draft PRs. Human branches: `feature/`, `fix/`, `docs/`, `refactor/`.
- Markdown: ATX headings, pipe tables, fenced code with a language. File names are lowercase-hyphen, except `CLAUDE.md`, `SKILL.md` and `SHA256SUMS`.
- Integrity: `cd references/setup && sha256sum -c SHA256SUMS`. Version history: `references/setup/config-versions.md`.
