# Configuration Versions

Ledger of the files that steer Claude sessions. Repo revisions stay recoverable through git history. The retired global rev0 is intentionally not retained. Never edit a past row; add a new one.

| Config | Rev | Date | Lines | Bytes | SHA-256 | Recover from |
|--------|-----|------|-------|-------|---------|--------------|
| Global `~/.claude/CLAUDE.md` | rev0 (superseded) | 2026-11-25 | 56 | 8,866 | `93ab3210930f381e159674c5a4d6322243550d1bcb50bd64e3049224caee29f0` | not retained (it held the prior-employer lines you asked to remove) |
| Global `~/.claude/CLAUDE.md` | rev1 | 2026-11-25 | 43 | 8,492 | `8f3be920d8692bc68f2c7cc10fe9eb71368a50a5509f801c6dcec3e592e0cadb` | `CLAUDE.global.rev1.md` (session attachment; kept out of this repo because it holds Drive folder IDs) |
| Repo `CLAUDE.md` | rev0 (superseded) | 2026-11-25 | 1,229 | 56,345 | `df00c70b86d971b522a14054db30c95be4bdf3087826cc33cd1888304e6fb4eb` | `git show 3a63013:CLAUDE.md` |
| Repo `CLAUDE.md` | rev1 | 2026-11-25 | 65 | see `SHA256SUMS` | see `SHA256SUMS` | this repository |

## Install the global file

The global file lives on your own computer, so install it there. Rev1 is delivered as a session attachment named `CLAUDE.global.rev1.md` (hash in the table above). Save it in the folder where you run these commands.

Windows (PowerShell):

```powershell
Copy-Item .\CLAUDE.global.rev1.md "$env:USERPROFILE\.claude\CLAUDE.md"
Get-FileHash "$env:USERPROFILE\.claude\CLAUDE.md" -Algorithm SHA256
```

PowerShell prints the hash in upper case; compare it with the rev1 row.

macOS or Linux:

```bash
cp CLAUDE.global.rev1.md ~/.claude/CLAUDE.md && sha256sum ~/.claude/CLAUDE.md
```

The claude.ai preferences block (used by Cowork and chat) should carry the same text. Rev0 is not retained here because it contained the prior-employer lines you asked to remove. If you want a rollback copy, save your current file somewhere private before replacing it.

## Lean plugin profile

```bash
python tools/claude_profile.py plan            # usage ranking from your own transcripts, and the hook groups the lean set keeps
python tools/claude_profile.py lean --apply    # disable all, enable your top 15
python tools/claude_profile.py full --apply    # everything back
python tools/claude_profile.py enable NAME --apply
```

Run these on the computer whose sessions you want measured. Plugin hooks stop when their plugin is disabled, so the lean profile also cuts hooks.

## Check for drift

```bash
cd references/setup && sha256sum -c SHA256SUMS
sha256sum ~/.claude/CLAUDE.md
```

The first command verifies the repo files listed in `SHA256SUMS`. The second prints the global file's hash, to compare with the latest row above. After any intended change, regenerate `SHA256SUMS` (command at the top of that file) and add a ledger row.
