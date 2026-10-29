# Loop contract

Read by the Crucible loop agents (`implement-spec`, `verifier`). Keep it accurate.

- **What this repo is:** the content source for `forge sync`: skills, rules, and workflows. Specimens live on orphan
  branches (`specimen/*`); list them with `python3 scripts/list_specimens.py` after `git fetch --all`.
- **Install:** none.
- **Checks** (before a PR is ready):
  - every `skills/*/SKILL.md` starts with YAML frontmatter that has `name` and `description`;
  - every changed resource still syncs: in a scratch repo, `forge init` against this branch, then `forge sync --dry-run`
    shows the resource for each supported harness without errors;
  - links in changed Markdown files resolve.
- **Commit style:** `v0.x.y: ...` for releases, `docs: ...` otherwise, matching `git log`.
- **Specs:** `specs/NNNN-slug.md`, see `crucibledx/hq` `specs/README.md`.
- **Release:** manual tags. Loop PRs never tag.
