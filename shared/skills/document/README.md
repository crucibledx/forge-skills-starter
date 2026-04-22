# /document — Project Documentation Generator

## Overview

An orchestrator skill that generates comprehensive project documentation including architecture diagrams. Analyzes the project structure, identifies the architecture pattern, creates visual diagrams using `/drawio`, and produces structured Markdown documentation.

## Input / Output

**Input:** A project directory to document (defaults to current working directory).

**Output:**

- `docs/architecture.drawio.png` — architecture diagram with embedded XML
- `docs/api-routes.drawio.png` — API route map (if applicable)
- `docs/README.md` or `docs/ARCHITECTURE.md` — structured documentation

## Dependencies

- `/detect-stack` — for project classification
- `/drawio` — for diagram generation
- `drawio-conventions` rule — for consistent diagram styling
- `documentation-standards` rule — for documentation quality

## Features

- Auto-detects architecture patterns (layered, clean, modular, microservices)
- Generates draw.io diagrams with proper styling and layout
- Produces structured Markdown with tables, code blocks, and embedded images
- Human-in-the-loop review before finalizing

## Design Decisions

- **Diagram-first approach** — visual architecture overview before detailed text
- **Convention-based styling** — follows `drawio-conventions` rule for consistent diagrams across projects
- **Non-destructive** — generates docs in `docs/` directory, never modifies source code
- **Iterative** — presents output for review, iterates on feedback
