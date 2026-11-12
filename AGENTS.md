# Forge Skills Starter — Agent Context

> AI resource lifecycle platform — design, develop, test, and deliver AI agent skills, rules, and workflows, powered by
> [Forge CLI](https://github.com/crucibledx/forge-cli). This is the canonical agent doc; `CLAUDE.md` points here.

## Identity

- **Repo:** `crucibledx/forge-skills-starter` · template repository (fork and customize)
- **Version:** see `CHANGELOG.md` and git tags (`main` may contain commits after the latest tag)
- **Tooling:** Markdown content plus one Python helper script. No `package.json`, no CI workflows.

## What It Does

The content platform of the Crucible ecosystem. Teams fork it, build AI resources with a structured lifecycle, and
deliver them to team repos via Forge CLI (`forge init` → `forge sync`).

## Convention over Configuration

The directory structure is the API: put a file in the right place and the platform discovers it.

| What       | Convention                                 | Discovered by                                 |
|------------|--------------------------------------------|-----------------------------------------------|
| Skill      | `skills/<name>/SKILL.md`                   | `/create-resource`, `/test-resource`, Forge   |
| Skill docs | `skills/<name>/README.md` (every skill)    | Developers browsing the repo                  |
| Design     | `docs/<name>/design.md`                    | `/design-resource`, `/develop-resource`       |
| Diagrams   | `docs/<name>/*.drawio`                     | `/design-resource`, draw.io CLI               |
| Rule       | `rules/<name>.md`                          | `/create-resource`, Forge                     |
| Workflow   | `workflows/<name>.md`                      | `/create-resource`, Forge                     |
| Specimen   | orphan branch `specimen/<lang>/<fw>`       | `/test-resource`, `scripts/list_specimens.py` |
| Delta      | branch `specimen/<lang>/<fw>-delta-<name>` | `/test-resource`                              |

- **Shared** (`skills/`, `rules/`, `workflows/`) — delivered to consumer repos via Forge.
- **Platform** (`.claude/skills/`, `docs/`, `scripts/`) — stays here and powers development and testing.

## Structure

```
├── skills/              ← detect-stack, document, drawio, review-pr (each SKILL.md + README.md)
├── rules/               ← code-style, documentation-standards, drawio-conventions
├── workflows/           ← document-project
├── docs/                ← platform docs, skill spec, meta-resources/design.md
├── scripts/list_specimens.py
└── .claude/skills/      ← meta-skills: create-, design-, develop-, test-resource
```

## Meta-Skills (Lifecycle)

| Skill | Purpose |
|-------|---------|
| `/create-resource` | Orchestrator: idea → design → develop → test → release |
| `/design-resource` | Phase 1: clarify, classify, `design.md` + diagrams |
| `/develop-resource` | Phase 2: scaffold, implement step by step, human review |
| `/test-resource` | Phase 3: auto-detect type, merge specimen, run and validate |

Each phase works standalone or as a subagent of the orchestrator.

## Skill Frontmatter

```yaml
---
description: What the skill does
version: 1.0.0
type: orchestrator | sub-skill | utility
language: "*"            # or "python", "typescript", ...
requires:                # optional: skills this one delegates to
  - /detect-stack
test:
  specimens:
    - specimen/python/fastapi
    - specimen/ts/express
---
```

Full spec (including `test.needs-pr`, `test.needs-delta`, `test.needs-study`): `docs/skill-spec.md`.

## Testing with Specimens

Specimens are real project snapshots on orphan branches:

| Branch | Description |
|--------|-------------|
| `specimen/python/fastapi` | FastAPI REST API service |
| `specimen/ts/express` | Express.js TypeScript REST API |
| `specimen/python/fastapi-delta-docs` | Delta with intentional documentation issues |
| `specimen/ts/express-delta-docs` | Delta with intentional documentation issues |

`example/monorepo` shows multi-team resource organization.

```bash
git fetch --all
python3 scripts/list_specimens.py    # lists origin/specimen/* branches, specimens and deltas
```

## Git Datetime Rule

When creating commits, tags, and branches in this repo, base git datetimes on the latest existing commit's datetime plus
a small offset (minutes or seconds), not the current system time. Use the git identity already configured in the
environment; do not override author or committer.

## Commits and Releases

Release commits use `v0.x.y: description`, with a `CHANGELOG.md` entry and an annotated tag. Non-release commits use
`docs: ...` style.

## Docs

| Doc | Purpose |
|-----|---------|
| `docs/README.md` | Documentation index |
| `docs/how-to-create-resource.md` | End-to-end resource creation |
| `docs/how-to-test-resource.md` | Testing with specimens |
| `docs/how-to-add-specimen.md` | Adding specimens |
| `docs/skill-spec.md` | Skill file specification |
| `docs/platform-design.md` | Platform architecture |
| `docs/meta-resources/design.md` | Meta-skills / orchestrator design |
