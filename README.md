# Forge Skills Starter

> A reference AI skills repository — develop, test, and deliver AI agent skills to your team

A **development and testing platform** for AI agent skills, rules, and workflows. Build skills here. Test them against real specimens. Deliver to team repos via [Forge CLI](https://github.com/crucibledx/forge-cli).

## How It Works

Two commands, one flow:

![Platform Flow](docs/platform-flow.drawio.png)

| What | Convention | Discovered by |
|------|------------|---------------|
| Skill | `skills/<name>/SKILL.md` | `/develop-skill`, `/test-skill`, Forge |
| Skill docs | `skills/<name>/README.md` | Developers browsing the repo |
| Rule | `rules/<name>.md` | Forge delivery tools |
| Workflow | `workflows/<name>.md` | Forge delivery tools |
| Specimen | orphan branch `specimen/<lang>/<fw>` | `/test-skill`, `list_specimens.py` |
| Delta | branch `specimen/<lang>/<fw>-delta-<name>` | `/test-skill` |

Put a file in the right place → the platform discovers it. No config, no registration.

> **Architecture:** Convention over Configuration. See [Platform Design](docs/platform-design.md) for details.

## Quick Start

### For skill developers (this repo)

```bash
# 1. Develop a new skill
/develop-skill "A skill that does X"

# 2. Test it against a specimen
/test-skill <skill-name> <specimen>
```

### For skill consumers (team repos)

#### Using Forge CLI

[Forge](https://github.com/crucibledx/forge-cli) syncs skills, rules, and workflows from this repo into your project's AI tool paths automatically.

```bash
# 1. Install forge
bun add -g @crucibledx/forge-cli

# 2. In your project repo, initialize forge
forge init
# → Select "git" source type
# → Enter this repo's URL
# → Select which AI tools you use (Claude Code, Windsurf, Cursor, etc.)

# 3. Sync skills and rules to your project
forge sync
```

Forge auto-detects the canonical layout in this repo, maps each skill/rule/workflow to the right path for each AI tool, and handles format transforms (e.g. `.md` → `.mdc` for Cursor).

> **Layout note:** This repo uses **canonical** layout (`skills/`, `rules/`, `workflows/`). When adding this as a Forge source, use layout override `canonical` to avoid syncing platform meta-skills from `.claude/commands/`. The meta-skills (`/develop-skill`, `/test-skill`) are for this repo's own development, not for delivery.
>
> ```bash
> forge source add
> # → Layout: canonical (not auto)
> ```
>
> If you use `pre-structured` layout, Forge would also sync the `.claude/commands/` directory, which contains this repo's development tools — not the shared skills.

To keep skills up to date:

```bash
forge sync              # pull latest manually
forge scheduler install # or set up auto-sync
```

#### Manual copy (alternative)

If you prefer not to use Forge, copy skill files directly:

```bash
# For Claude Code
cp skills/drawio/SKILL.md /path/to/your-project/.claude/skills/drawio/SKILL.md

# For Windsurf
cp skills/drawio/SKILL.md /path/to/your-project/.windsurf/skills/drawio/SKILL.md
```

## Repository Structure

```
forge-skills-starter/
├── skills/                         # Shared skills (delivered to team repos)
│   ├── drawio/                     # Draw.io diagram generation
│   ├── detect-stack/               # Project tech stack detection
│   ├── review-pr/                  # Generic PR review
│   └── document/                   # Project documentation generator
├── rules/                          # Shared rules (delivered to team repos)
│   ├── drawio-conventions.md       # Diagram quality standards
│   ├── code-style.md              # Coding conventions
│   └── documentation-standards.md  # Documentation requirements
├── workflows/                      # Shared workflows (delivered to team repos)
│   └── document-project.md        # Full documentation workflow
├── docs/                           # Platform docs (NOT delivered)
│   ├── platform-design.md         # Architecture & conventions
│   ├── skill-spec.md             # Skill format specification
│   └── *.drawio.png              # Platform diagrams
├── scripts/                        # Test automation (NOT delivered)
│   └── list_specimens.py
├── .claude/                        # Claude Code meta-skills (NOT delivered)
│   └── commands/
│       ├── develop-skill.md       # Skill development lifecycle
│       └── test-skill.md          # Skill testing against specimens
├── CLAUDE.md                       # Project instructions
├── CHANGELOG.md
└── CONTRIBUTING.md
```

**Shared** (`skills/`, `rules/`, `workflows/`) → delivered to consumer repos via Forge.
**Platform** (everything else) → stays in this repo, powers development & testing.

## Skills

| Skill | Version | Type | Description |
|-------|---------|------|-------------|
| `/drawio` | 1.0.0 | utility | Generate draw.io diagrams as native files with PNG/SVG/PDF export |
| `/detect-stack` | 1.0.0 | utility | Classify project type, language, framework, and build tools |
| `/review-pr` | 1.0.0 | orchestrator | Review pull request changes for quality, style, and correctness |
| `/document` | 1.0.0 | orchestrator | Generate project documentation with architecture diagrams |

## Rules

| Rule | Purpose |
|------|---------|
| `drawio-conventions` | Standards for clean, readable draw.io diagrams |
| `code-style` | General coding conventions and best practices |
| `documentation-standards` | Documentation quality and completeness requirements |

## Workflows

| Workflow | Purpose |
|----------|---------|
| `document-project` | End-to-end project documentation using `/document` skill and drawio |

## Testing

### Specimens

Specimens are **real project snapshots** on orphan branches. Any skill that operates on source code can use them.

| Specimen | Description |
|----------|-------------|
| `specimen/python/fastapi` | FastAPI REST API service |
| `specimen/ts/express` | Express.js TypeScript REST API |

Delta branches (e.g. `specimen/python/fastapi-delta-docs`) add small changes with intentional findings.

### Running tests

```bash
# Agent-assisted (recommended)
/test-skill document specimen/python/fastapi

# Manual
python3 scripts/list_specimens.py   # list specimens and deltas
```

### Guides

- [Skill Specification](docs/skill-spec.md) — frontmatter fields, step conventions, versioning
- [Platform Design](docs/platform-design.md) — architecture and conventions

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflow and agent usage guidelines.
