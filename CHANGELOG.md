# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[0.3.0]: https://github.com/crucibledx/forge-skills-starter/releases/tag/v0.3.0
[0.2.0]: https://github.com/crucibledx/forge-skills-starter/releases/tag/v0.2.0
[0.1.0]: https://github.com/crucibledx/forge-skills-starter/releases/tag/v0.1.0
