# AI Resources Lifecycle Platform — Monorepo Example

> Team-scoped AI resources in a monorepo layout. Each team owns their canonical `skills/`, `rules/`, `workflows/` under a team folder.

**This is the `example/monorepo` branch.** It demonstrates how to organize AI resources for multiple teams in a single repo, with each team getting their own scoped resources delivered via [Forge CLI](https://github.com/crucibledx/forge-cli).

For the standard single-team setup, see the [`main` branch](https://github.com/crucibledx/forge-skills-starter/tree/main).

---

## Structure

```
shared/                  # Cross-team resources — every team gets these
  skills/                # /detect-stack, /document, /drawio, /review-pr
  rules/                 # code-style, documentation-standards, drawio-conventions
  workflows/             # document-project

frontend/                # Frontend team
  skills/                # /review-frontend, /accessibility
  rules/                 # react-conventions
  workflows/             # component-review

backend/                 # Backend team
  skills/                # /review-api, /database-migration
  rules/                 # api-conventions
  workflows/             # api-review

infra/                   # Infrastructure team
  skills/                # /review-terraform, /incident-runbook
  rules/                 # terraform-conventions
  workflows/             # deploy-review
```

Each team folder contains a full canonical layout (`skills/`, `rules/`, `workflows/`). Forge CLI treats each as an independent source with its own subdirectory.

## Using with Forge CLI

Each team points their Forge source at this repo with a `subdirectory` filter:

```yaml
# .crucible/forge.config.yaml — frontend team project
sources:
  - name: shared
    type: git
    url: https://github.com/your-org/forge-skills-starter.git
    branch: example/monorepo
    subdirectory: shared

  - name: frontend
    type: git
    url: https://github.com/your-org/forge-skills-starter.git
    branch: example/monorepo
    subdirectory: frontend
```

Or use `include`/`exclude` globs for fine-grained control:

```yaml
sources:
  - name: team-skills
    type: git
    url: https://github.com/your-org/forge-skills-starter.git
    branch: example/monorepo
    include:
      - "shared/**"
      - "backend/skills/**"
      - "backend/rules/api-conventions.md"
    exclude:
      - "**/draft-*"
```

## What's Included

### Shared (all teams)

| Resource | Type | Description |
|----------|------|-------------|
| `/detect-stack` | skill | Detect project language, framework, and build tools |
| `/document` | skill | Generate project docs with architecture diagrams |
| `/drawio` | skill | Generate draw.io diagrams with PNG/SVG/PDF export |
| `/review-pr` | skill | Review PR changes for quality and correctness |
| `code-style` | rule | General coding conventions |
| `documentation-standards` | rule | Documentation quality requirements |
| `drawio-conventions` | rule | Standards for clean draw.io diagrams |
| `document-project` | workflow | End-to-end documentation generation |

### Frontend

| Resource | Type | Description |
|----------|------|-------------|
| `/review-frontend` | skill | Review React code for best practices and performance |
| `/accessibility` | skill | Audit for WCAG compliance and accessibility issues |
| `react-conventions` | rule | React component patterns and naming conventions |
| `component-review` | workflow | End-to-end frontend component review |

### Backend

| Resource | Type | Description |
|----------|------|-------------|
| `/review-api` | skill | Review API endpoints for REST conventions and security |
| `/database-migration` | skill | Review DB migrations for safety and reversibility |
| `api-conventions` | rule | REST API design standards |
| `api-review` | workflow | End-to-end API review with migration check |

### Infra

| Resource | Type | Description |
|----------|------|-------------|
| `/review-terraform` | skill | Review IaC changes for security, cost, and blast radius |
| `/incident-runbook` | skill | Generate incident response runbooks |
| `terraform-conventions` | rule | Terraform file structure and naming conventions |
| `deploy-review` | workflow | Infrastructure review before deployment |

## Documentation

| Start here                                                 | Then explore                                           |
|------------------------------------------------------------|--------------------------------------------------------|
| [How to Create a Resource](docs/how-to-create-resource.md) | [Skill Specification](docs/skill-spec.md)              |
| [How to Test a Resource](docs/how-to-test-resource.md)     | [Platform Design](docs/platform-design.md)             |
| [How to Add a Specimen](docs/how-to-add-specimen.md)       | [Meta-Resources Design](docs/meta-resources/design.md) |
|                                                            | [Full Documentation Index](docs/README.md)             |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflow and guidelines.
