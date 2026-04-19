# Contributing to Forge Skills Starter

## Development Workflow

### 1. Create a feature branch

```bash
git checkout main
git pull
git checkout -b feature/my-change
```

### 2. Make your changes

- **Editing a skill?** — modify `skills/<skill-name>/SKILL.md`
- **Adding a rule?** — add `rules/<name>.md`
- **Adding a workflow?** — add `workflows/<name>.md`
- **Adding docs?** — add to `docs/` or update `README.md`

### 3. Test with the agent

Use the `/test-skill` Claude Code command:

```
/test-skill document specimen/python/fastapi
/test-skill review-pr specimen/ts/express
```

This will:

1. Commit your pending changes (if any)
2. Create a test branch from your feature branch
3. Merge the chosen specimen
4. Run the target skill
5. Return you to your feature branch

### 4. Commit and push

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add code review checklist to /review-pr
fix: correct stack detection for monorepos
docs: add how-to-test guide
specimen: add Python FastAPI service
```

### 5. Create a pull request

```bash
git push origin feature/my-change
```

## Working with AI Agents

### Best practices

- **Be specific** — tell the agent exactly which skill to edit, which file, which section
- **Test after every change** — use `/test-skill` to validate before committing
- **Review agent output** — AI-generated skill steps must be reviewed by a human
- **Use capable models** — skills are designed for high-capability reasoning models (Claude Opus 4+, GPT-4o+)

### Things agents should NOT do

- Delete or weaken existing skill steps without explicit permission
- Change specimen branches on `main` (specimens live on orphan branches)
- Modify `.claude/commands/` without asking
- Auto-run destructive git commands (force push, delete branches)

## Repository Structure

```
forge-skills-starter/
├── skills/                     # Skill definitions (SKILL.md + README.md)
├── rules/                      # Shared context rules
├── workflows/                  # Shared workflows
├── docs/                       # Design docs, guides, diagrams
├── scripts/                    # Test automation
├── .claude/commands/           # Claude Code meta-skills (platform-only)
├── CONTRIBUTING.md             # This file
├── CHANGELOG.md
└── README.md
```

> **`.claude/commands/`** contains meta-skills specific to this repository
> (e.g. `/develop-skill`, `/test-skill`). They should **not** be copied to other projects.
> Shared skills live in `skills/` and are delivered by Forge.

### Branch structure

| Branch                               | Purpose                                 |
|--------------------------------------|-----------------------------------------|
| `main`                               | Skills, rules, workflows, docs          |
| `specimen/python/fastapi`            | FastAPI REST API (orphan)               |
| `specimen/python/fastapi-delta-docs` | Missing docs variant                    |
| `specimen/ts/express`                | Express.js TypeScript API (orphan)      |
| `specimen/ts/express-delta-docs`     | Missing docs variant                    |
| `test/*`                             | Disposable test branches (auto-created) |

## Versioning

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** — breaking changes to skill interfaces
- **MINOR** — new skills, specimens, or features
- **PATCH** — bug fixes, doc updates, small improvements

Update `CHANGELOG.md` with every PR. Tag releases on `main`:

```bash
git tag -a v0.2.0 -m "v0.2.0"
git push origin v0.2.0
```

## Delivering Skills to Team Repos

Skills, rules, and workflows from this repo are delivered to team projects using [Forge CLI](https://github.com/crucibledx/forge-cli).

### How it works

Forge reads `skills/`, `rules/`, and `workflows/` from this repo (via git) and maps files to each AI tool's native config path:

| Source path              | Claude Code                      | Windsurf                           | Cursor                           |
|--------------------------|----------------------------------|------------------------------------|----------------------------------|
| `skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` | `.windsurf/skills/<name>/SKILL.md` | `.cursor/skills/<name>/SKILL.md` |
| `rules/<name>.md`        | `.claude/rules/<name>.md`        | `.windsurf/rules/<name>.md`        | `.cursor/rules/<name>.mdc`       |
| `workflows/<name>.md`    | `.claude/commands/<name>.md`     | `.windsurf/workflows/<name>.md`    | `.cursor/commands/<name>.md`     |

Forge handles format transforms automatically (e.g. `.md` → `.mdc` for Cursor rules).

### Setup in a consumer repo

```bash
# Install forge (one-time)
bun add -g @crucibledx/forge-cli

# In the target project
forge init
# → Source type: git
# → URL: <this repo's SSH or HTTPS URL>
# → Branch: main
# → Layout: canonical
# → Select active AI tools

# Sync
forge sync
```

> **Important:** Use `canonical` layout when adding this repo as a source. The repo also contains `.claude/commands/` for platform meta-skills that should not be delivered to consumer repos.

### What gets delivered vs. what stays

| Directory           | Delivered?                 | Reason                   |
|---------------------|----------------------------|--------------------------|
| `skills/`           | Yes                        | Shared skill definitions |
| `rules/`            | Yes                        | Shared context rules     |
| `workflows/`        | Yes                        | Shared workflows         |
| `.claude/commands/` | No (with canonical layout) | Platform meta-skills     |
| `docs/`             | No                         | Design docs, guides      |
| `scripts/`          | No                         | Test automation          |

## Code Style

- **Skills (SKILL.md):** YAML frontmatter + Markdown steps
- **Rules:** Markdown with optional YAML frontmatter for globs/paths
- **Workflows:** Markdown with step-by-step instructions
- **Python scripts:** Python 3.7+ compatible, no external dependencies beyond stdlib
- **Docs:** Markdown with clear headings, tables, and code blocks
