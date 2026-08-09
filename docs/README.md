# Documentation Index

> What to read and when. All paths relative to `docs/`.

---

## Platform

| Document                              | When to read                  | Description                                                                    |
|---------------------------------------|-------------------------------|--------------------------------------------------------------------------------|
| [Platform Design](platform-design.md) | First time contributing       | Architecture (Convention over Configuration), single flow, implementation plan |
| [Skill Specification](skill-spec.md)  | Building or reviewing a skill | Frontmatter fields, step conventions, type system, versioning                  |

## How-To Guides

| Guide                                                 | When to use                            | Description                                                            |
|-------------------------------------------------------|----------------------------------------|------------------------------------------------------------------------|
| [How to Create a Resource](how-to-create-resource.md) | Creating any new resource              | Full lifecycle: `/create-resource` — design → develop → test → release |
| [How to Test a Resource](how-to-test-resource.md)     | Testing any resource against specimens | `/test-resource` workflow, manual testing, test reports                |
| [How to Add a Specimen](how-to-add-specimen.md)       | Need a new test project snapshot       | Orphan branch creation, delta branches, naming conventions             |

## Per-Resource Design Docs

Design artifacts (decision docs, flow/sequence diagrams) live in `docs/<resource-name>/`:

| Folder            | Resource       | Contents                         |
|-------------------|----------------|----------------------------------|
| `meta-resources/` | Meta-resources | Architecture, phase flow, design |

> **Note:** Resource-specific usage docs belong in `skills/<name>/README.md`, not in `docs/`.
> The `docs/<name>/` folders are only for **design artifacts** (architecture decisions, diagrams).

## Scripts

| Document                    | Description                      |
|-----------------------------|----------------------------------|
| `scripts/list_specimens.py` | List specimen and delta branches |
