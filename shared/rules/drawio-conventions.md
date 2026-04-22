---
description: Standards for creating clean, readable draw.io diagrams
globs:
  - "**/*.drawio"
  - "**/*.drawio.png"
  - "**/*.drawio.svg"
---

# Draw.io Diagram Conventions

Follow these conventions when creating or editing draw.io diagrams.

## Layout

- **Direction:** Top-to-bottom for hierarchies, left-to-right for flows/sequences
- **Alignment:** Align elements to grid (gridSize=10). Use snap-to-grid.
- **Spacing:** Minimum 40px between elements. 60px between groups/containers.
- **Border:** Always export with `-b 10` (10px border padding)
- **Page:** Use `page="0"` (infinite canvas) unless the diagram fits a standard page

## Elements

- **No overlapping elements** — every shape must have clear boundaries
- **Consistent sizing** — same-type elements should be the same width/height
- **Labels inside shapes** — never floating text next to an unlabeled shape
- **Readable font size** — minimum 10px for labels, 12px for titles

## Edges (Arrows)

- **No arrow spaghetti** — if arrows cross, rearrange elements to minimize crossings
- **Orthogonal routing** — use `edgeStyle=orthogonalEdgeStyle` for clean right-angle paths
- **Label important edges** — add labels to edges that represent non-obvious relationships
- **Consistent stroke width** — use 1-2px for normal edges, 2-3px for emphasis

## Color Coding

Use consistent colors for element types:

| Purpose                | Fill      | Stroke    |
|------------------------|-----------|-----------|
| Primary component      | `#dae8fc` | `#6c8ebf` |
| Agent/AI work          | `#e1d5e7` | `#9673a6` |
| User interaction       | `#f8cecc` | `#b85450` |
| Success/test           | `#d5e8d4` | `#82b366` |
| Artifact/output        | `#fff2cc` | `#d6b656` |
| Neutral/infrastructure | `#f5f5f5` | `#666666` |
| Release/deploy         | `#ECEFF1` | `#607D8B` |

## Containers

- **Use containers** to group related elements (layers, services, modules)
- **Label containers** with bold text at the top (`verticalAlign=top;spacingTop=5`)
- **Container stroke** should be 2px with a distinct color from children

## Export

- **Always embed XML** — use `--embed-diagram` flag so the exported file remains editable
- **Double extensions** — `name.drawio.png`, not `name.png`
- **Delete intermediate .drawio** — after successful export, the PNG/SVG contains the diagram
- **Scale for readability** — if the diagram has small text, use `--scale 2` or `--width` flag

## Anti-patterns

- Arrows crossing multiple times (rearrange elements instead)
- Tiny text that's unreadable when exported
- Inconsistent colors for same-type elements
- Floating labels not connected to any shape
- Missing arrow labels on ambiguous relationships
