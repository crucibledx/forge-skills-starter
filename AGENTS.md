# Forge Skills Starter: agent guide

How to work in this repo and where to find things. The linked documents are canonical; this file does not repeat them.

## Where to find information

| Need                                                  | Read                                                                                                                         |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| What this repo is, conventions, delivery via Forge    | [`README.md`](README.md)                                                                                                     |
| Workflow, structure, branches, versioning, code style | [`CONTRIBUTING.md`](CONTRIBUTING.md)                                                                                         |
| Which doc to read when                                | [`docs/README.md`](docs/README.md)                                                                                           |
| Skill format (frontmatter, steps, versioning)         | [`docs/skill-spec.md`](docs/skill-spec.md)                                                                                   |
| Testing against specimens, adding specimens           | [`docs/how-to-test-resource.md`](docs/how-to-test-resource.md), [`docs/how-to-add-specimen.md`](docs/how-to-add-specimen.md) |
| PR checks, commit style, release                      | [`.factory/loop-contract.md`](.factory/loop-contract.md)                                                                     |
| Org context, delivery loop, approval boundaries       | `crucibledx/hq` `AGENTS.md`                                                                                                  |
| Org engineering standards                             | `engineering-standards` skill (`crucibledx/factory-loop` `plugins/crucible-loop/skills/engineering-standards/`)              |
| Specs                                                 | [`specs/`](specs/)                                                                                                           |

## How to work

There is nothing to install or build. Run the checks in the loop contract before a PR is ready. To see the specimens:

```bash
git fetch --all
python3 scripts/list_specimens.py
```

- `skills/`, `rules/` and `workflows/` ship to consumer repos through `forge sync`. A change there is a change for
  every team that syncs this repo.
- `.claude/skills/` holds this repo's own meta-skills (`/create-resource` and the phase skills). Do not change them
  unless the task asks for it.
- Every skill folder has both `SKILL.md` and `README.md`; keep them in step.
- Specimens live on orphan `specimen/*` branches. Never merge one into `main`, and never push the disposable `test/*`
  branches that `/test-resource` creates.
- Do not delete or weaken existing skill steps without explicit permission.
- Python scripts use the standard library only.

## Where the docs disagree

The loop contract asks for `name` in every `skills/*/SKILL.md` frontmatter. `docs/skill-spec.md` says the folder name
is the skill name, and no skill on `main` has a `name` field. Until that is settled, follow `docs/skill-spec.md` and
do not add `name` to existing skills as a side effect.

## Boundaries

- Never push to `main`, force push or merge. Nazar's code-owner approval is the merge gate.
- No version tags or release commits in agent PRs; releases are manual.
