# Configuration Versions

Ledger of the files that steer Claude sessions. Older revisions stay recoverable (git history for repo files; a local `_versions/` copy for the global file). Never edit a past row; add a new one.

| Config | Rev | Date | Lines | Bytes | SHA-256 | Recover from |
|--------|-----|------|-------|-------|---------|--------------|
| Global `~/.claude/CLAUDE.md` | rev0 (superseded) | 2026-11-25 | 56 | 8,866 | `93ab3210930f381e159674c5a4d6322243550d1bcb50bd64e3049224caee29f0` | `~/.claude/_versions/CLAUDE.md.rev0` |
| Global `~/.claude/CLAUDE.md` | rev1 | 2026-11-25 | 43 | 8,249 | `342a4c5d54c4ee20ca35b22dda382087d169070e0ecef1c25b6563d6e41dd99d` | `~/.claude/_versions/CLAUDE.md.rev1` |
| Repo `CLAUDE.md` | rev0 (superseded) | 2026-11-25 | 1,229 | 56,345 | `df00c70b86d971b522a14054db30c95be4bdf3087826cc33cd1888304e6fb4eb` | `git show 3a63013:CLAUDE.md` |
| Repo `CLAUDE.md` | rev1 | 2026-11-25 | 63 | see `SHA256SUMS` | see `SHA256SUMS` | this repository |

## Install the global file

Keep the backup first, then install and compare the hash to the rev1 row:

```bash
mkdir -p ~/.claude/_versions && cp ~/.claude/CLAUDE.md ~/.claude/_versions/CLAUDE.md.rev0
cp CLAUDE.global.rev1.md ~/.claude/CLAUDE.md && sha256sum ~/.claude/CLAUDE.md
```

The claude.ai preferences block (used by Cowork and chat) should carry the same text as the global file. Paste rev1 there too, and compare it to the global file whenever either changes.

## Check for drift

```bash
cd references/setup && sha256sum -c SHA256SUMS
sha256sum ~/.claude/CLAUDE.md
```

The first command verifies the repo files listed in `SHA256SUMS`. The second prints the global file's hash, to compare with the latest row above. After any intended change, regenerate `SHA256SUMS` (command at the top of that file) and add a ledger row.
