# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] - 2026-04-22

### Added

- **Meta-resources architecture:** orchestrator pattern with `/create-resource` → `/design-resource` → `/develop-resource` → `/test-resource` as Claude Code skills with subagent delegation
- **Design doc:** `docs/meta-resources/design.md` — resource taxonomy, orchestrator phases, test strategies, convention table
- **Architecture diagram:** `docs/meta-resources/architecture.drawio` — orchestrator, phases, resource types
- **How-to guides:** `docs/how-to-create-resource.md`, `docs/how-to-test-resource.md`, `docs/how-to-add-specimen.md`

### Changed

- **Platform flow diagram** upgraded to show full lifecycle: IDEA → DESIGN → DEVELOP → TEST → RELEASE → DELIVER with `/create-resource` orchestrator
- **Convention map diagram** updated with new `.claude/skills/` entries and `docs/meta-resources/`
- **README.md** reframed as "AI resource lifecycle platform" with orchestrator-first quick start
- **CLAUDE.md** updated with new convention table and key commands
- **CONTRIBUTING.md** updated with new workflow and guides section
- **Platform design doc** updated with resource lifecycle, meta-resources reference, convention table

### Removed

- `/develop-skill` meta-skill (replaced by `/create-resource` + `/develop-resource`)
- `/test-skill` meta-skill (replaced by `/test-resource` with type-aware testing)

## [0.5.0] - 2026-04-19

### Added

- **Specimens:** `specimen/python/fastapi` (FastAPI bookmarks API), `specimen/ts/express` (Express notes API)
- **Deltas:** `specimen/python/fastapi-delta-docs` (missing docs), `specimen/ts/express-delta-docs` (missing docs)

## [0.4.0] - 2026-04-19

### Added

- **Diagrams:** `docs/diagrams/platform-flow.drawio.png` (development lifecycle), `docs/diagrams/convention-map.drawio.png` (shared vs platform structure)
- **Scripts:** `scripts/export_diagrams.sh` (batch export all .drawio → .drawio.png)

### Changed

- Diagrams moved to `docs/diagrams/` with source `.drawio` files committed alongside exported PNGs

## [0.3.0] - 2026-04-19

### Added

- **Meta-skills:** `.claude/skills/develop-skill/` (skill development lifecycle, `disable-model-invocation`), `.claude/skills/test-skill/` (specimen-based testing, `disable-model-invocation`)
- **Scripts:** `scripts/list_specimens.py` (list specimen and delta branches)

## [0.2.0] - 2026-04-19

### Added

- **Skills:** `/drawio` (draw.io diagram generation, from jgraph/drawio-mcp), `/detect-stack` (tech stack detection), `/review-pr` (PR review), `/document` (documentation with diagrams)
- **Rules:** `drawio-conventions` (diagram quality standards), `code-style` (coding conventions), `documentation-standards` (documentation requirements)
- **Workflows:** `document-project` (end-to-end documentation workflow)

## [0.1.0] - 2026-04-19

### Added

- **Platform scaffold:** README, CONTRIBUTING, CLAUDE.md, .gitignore
- **Docs:** `docs/platform-design.md` (Convention-over-Configuration architecture), `docs/skill-spec.md` (skill format specification)

[0.6.0]: https://github.com/crucibledx/forge-skills-starter/releases/tag/v0.6.0
[0.5.0]: https://github.com/crucibledx/forge-skills-starter/releases/tag/v0.5.0
[0.4.0]: https://github.com/crucibledx/forge-skills-starter/releases/tag/v0.4.0
[0.3.0]: https://github.com/crucibledx/forge-skills-starter/releases/tag/v0.3.0
[0.2.0]: https://github.com/crucibledx/forge-skills-starter/releases/tag/v0.2.0
[0.1.0]: https://github.com/crucibledx/forge-skills-starter/releases/tag/v0.1.0
