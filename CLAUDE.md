# Forge Skills Starter

Read `AGENTS.md` in this folder: it is the canonical agent context (conventions, frontmatter, specimens, git rules).

Essentials for Claude Code:

- Lifecycle meta-skills live in `.claude/skills/`: `/create-resource` (orchestrator), `/design-resource`,
  `/develop-resource`, `/test-resource`.
- Skills are `skills/<name>/SKILL.md` + `README.md`; spec in `docs/skill-spec.md`.
- Git datetimes: latest commit's datetime plus a small offset, never current system time. Do not override git identity.
