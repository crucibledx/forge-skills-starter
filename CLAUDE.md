# AI Resource Lifecycle Platform

A development lifecycle platform for AI resources (skills, rules, workflows), powered by [Forge CLI](https://github.com/crucibledx/forge-cli).

## Architecture

**Convention over Configuration** — the directory structure IS the API.

| What       | Convention                                 | Auto-discovered by                            |
|------------|--------------------------------------------|-----------------------------------------------|
| Skill      | `skills/<name>/SKILL.md`                   | `/create-resource`, `/test-resource`, Forge   |
| Skill docs | `skills/<name>/README.md`                  | Developers browsing the repo                  |
| Design     | `docs/<name>/design.md`                    | `/design-resource`, `/develop-resource`       |
| Diagrams   | `docs/<name>/*.drawio`                     | `/design-resource`, draw.io CLI               |
| Rule       | `rules/<name>.md`                          | `/create-resource`, Forge                     |
| Workflow   | `workflows/<name>.md`                      | `/create-resource`, Forge                     |
| Specimen   | orphan branch `specimen/<lang>/<fw>`       | `/test-resource`, `scripts/list_specimens.py` |
| Delta      | branch `specimen/<lang>/<fw>-delta-<name>` | `/test-resource`                              |

Put a file in the right place → the platform discovers it.

## Shared vs Platform

- **Shared** (`skills/`, `rules/`, `workflows/`) — delivered to consumer repos via Forge
- **Platform** (`.claude/skills/`, `docs/`, `scripts/`) — stays in this repo, powers development & testing

## Key commands

- `/create-resource` — orchestrator: idea → design → develop → test → release
- `/design-resource` — Phase 1: clarify, classify, design.md + diagrams
- `/develop-resource` — Phase 2: scaffold, implement step-by-step
- `/test-resource` — Phase 3: auto-detect type, run test strategy

Each phase works standalone or as a subagent of the orchestrator.

## Skill format

Every `SKILL.md` uses YAML frontmatter:

```yaml
---
description: What the skill does
version: 1.0.0
type: orchestrator | sub-skill | utility
---
```

See `docs/skill-spec.md` for full specification. See `docs/meta-resources/design.md` for the orchestrator architecture.
