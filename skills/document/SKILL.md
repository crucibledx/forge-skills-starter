---
description: Generate comprehensive project documentation with architecture diagrams using draw.io
version: 1.0.0
type: orchestrator
language: "*"
requires:
  - /detect-stack
  - /drawio
test:
  specimens:
    - specimen/python/fastapi
    - specimen/ts/express
---

# Document Project

Generate comprehensive project documentation including architecture diagrams. Uses `/detect-stack` for project analysis and `/drawio` for diagram generation. Follows `documentation-standards` and `drawio-conventions` rules.

## Step 1 — Detect project stack

Call `/detect-stack` to classify the project. Record:

- Language and framework
- Project structure (single module, multi-module, monorepo)
- Entry points
- Key directories

## Step 2 — Analyze project structure

Read the project's directory tree and key files:

```bash
find . -type f -not -path '*/node_modules/*' -not -path '*/.git/*' -not -path '*/venv/*' -not -path '*/__pycache__/*' | head -100
```

Identify:

- Source directories and their purpose
- Configuration files
- Test directories
- Build/deployment files
- Existing documentation

## Step 3 — Map the architecture

Based on the analysis, identify the architecture pattern:

| Pattern              | Indicators                                                          |
|----------------------|---------------------------------------------------------------------|
| Layered (MVC/3-tier) | `controllers/`, `services/`, `models/` or `routes/`, `handlers/`    |
| Clean/Hexagonal      | `domain/`, `application/`, `infrastructure/`, `ports/`, `adapters/` |
| Modular              | Feature folders with self-contained logic                           |
| Monolith             | Single app entry, shared database                                   |
| Microservices        | Multiple services, API gateway, message queues                      |

## Step 4 — Generate architecture diagram

Use the `/drawio` skill to create an architecture diagram:

- Show major components/layers and their relationships
- Use containers for logical groupings
- Show external dependencies (databases, APIs, queues)
- Follow `drawio-conventions` rule for consistent styling
- Export as PNG with embedded XML: `docs/architecture.drawio.png`

### Diagram requirements

- Clear labels on all components
- No overlapping elements
- Consistent arrow direction (top-to-bottom or left-to-right for data flow)
- Color coding for different layer types
- Border padding of at least 10px

## Step 5 — Generate API/endpoint diagram (if applicable)

If the project exposes an API:

- List all endpoints/routes with methods
- Group by resource/module
- Create a route map diagram using `/drawio`
- Export as: `docs/api-routes.drawio.png`

## Step 6 — Write README documentation

Generate or update the project's `docs/README.md` (or `docs/ARCHITECTURE.md`):

```markdown
# <Project Name> — Architecture

## Overview

Brief description of what the project does.

## Tech Stack

- Language: <detected>
- Framework: <detected>
- Build: <detected>

## Architecture

![Architecture](architecture.drawio.png)

<Description of the architecture pattern and key components>

## Directory Structure

<Annotated tree of key directories>

## API Routes (if applicable)

![API Routes](api-routes.drawio.png)

<Table of endpoints>

## Getting Started

<How to run the project locally>

## Testing

<How to run tests>
```

## Step 7 — Review with user

> "Here's the generated documentation and diagrams. Would you like me to adjust anything?"

Present:

1. The architecture diagram (open the PNG)
2. The generated documentation
3. Any additional diagrams created

Iterate based on feedback.
