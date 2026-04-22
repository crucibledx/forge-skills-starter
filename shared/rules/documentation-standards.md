---
description: Documentation quality and completeness requirements
globs:
  - "**/*.md"
  - "**/README*"
  - "**/docs/**"
---

# Documentation Standards

Follow these standards when writing or generating documentation.

## Every Project Must Have

- **README.md** — project overview, quick start, and key commands
- **Architecture section** — either in README or a separate `docs/ARCHITECTURE.md`
- **Setup instructions** — how to install dependencies and run locally
- **API documentation** — if the project exposes an API (endpoints, request/response formats)

## README Structure

```
# Project Name

Brief one-line description.

## Overview
What this project does and why it exists (2-3 sentences).

## Quick Start
Numbered steps to get running locally.

## Architecture
High-level diagram + description.

## API (if applicable)
Endpoint table or link to API docs.

## Testing
How to run tests.

## Contributing
Link to CONTRIBUTING.md or inline guidelines.
```

## Writing Style

- **Concise** — say it in fewer words. No filler.
- **Scannable** — use headings, tables, and code blocks. Avoid walls of text.
- **Actionable** — tell the reader what to do, not just what exists
- **Code examples** — show, don't just describe. Include runnable examples.
- **Keep up to date** — outdated docs are worse than no docs

## Diagrams

- **Architecture diagrams are required** for any project with more than 3 components
- Use draw.io format (`.drawio.png` with embedded XML)
- Follow the `drawio-conventions` rule for styling
- Place diagrams in `docs/` directory
- Reference diagrams in Markdown with relative paths: `![Architecture](docs/architecture.drawio.png)`

## Tables Over Lists

Prefer tables for structured information:

```markdown
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/users` | GET | List all users |
| `/users/:id` | GET | Get user by ID |
```

## Code Blocks

- Always specify the language for syntax highlighting
- Show complete, runnable examples when possible
- Include expected output for CLI commands
