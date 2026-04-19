# Forge Skills Starter

This is a reference AI skills repository — a development and testing platform for AI agent skills, rules, and workflows, powered by [Forge CLI](https://github.com/crucibledx/forge-cli).

## Architecture

**Convention over Configuration** — the directory structure IS the API.

| What       | Convention                                 | Auto-discovered by                         |
|------------|--------------------------------------------|--------------------------------------------|
| Skill      | `skills/<name>/SKILL.md`                   | `/develop-skill`, `/test-skill`, Forge     |
| Skill docs | `skills/<name>/README.md`                  | Developers browsing the repo               |
| Rule       | `rules/<name>.md`                          | Forge delivery                             |
| Workflow   | `workflows/<name>.md`                      | Forge delivery                             |
| Specimen   | orphan branch `specimen/<lang>/<fw>`       | `/test-skill`, `scripts/list_specimens.py` |
| Delta      | branch `specimen/<lang>/<fw>-delta-<name>` | `/test-skill`                              |

Put a file in the right place → the platform discovers it.

## Shared vs Platform

- **Shared** (`skills/`, `rules/`, `workflows/`) — delivered to consumer repos via Forge
- **Platform** (`.claude/skills/`, `docs/`, `scripts/`) — stays in this repo, powers development & testing

## Key commands

- `/develop-skill` — scaffold and build a new skill
- `/test-skill` — test a skill against a specimen branch

## Skill format

Every `SKILL.md` uses YAML frontmatter:

```yaml
---
description: What the skill does
version: 1.0.0
type: orchestrator | sub-skill | utility
---
```

See `docs/skill-spec.md` for full specification.
