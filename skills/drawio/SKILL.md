---
description: Always use when user asks to create, generate, draw, or design a diagram, flowchart, architecture diagram, ER diagram, sequence diagram, class diagram, network diagram, mockup, wireframe, or UI sketch, or mentions draw.io, drawio, .drawio files, or diagram export to PNG/SVG/PDF.
version: 1.0.0
type: utility
language: "*"
test:
  specimens:
    - specimen/python/fastapi
    - specimen/ts/express
---

# Draw.io Diagram Skill

Generate draw.io diagrams as native `.drawio` files. Optionally export to PNG, SVG, or PDF with the diagram XML embedded (so the exported file remains editable in draw.io).

## How to create a diagram

1. **Generate draw.io XML** in mxGraphModel format for the requested diagram
2. **Write the XML** to a `.drawio` file in the current working directory using the Write tool
3. **If the user requested an export format** (png, svg, pdf), locate the draw.io CLI (see below), export with `--embed-diagram`, then delete the source `.drawio` file. If the CLI is not found, keep the `.drawio` file and tell the user they can install the draw.io desktop app to enable export, or
   open the `.drawio` file directly
4. **Open the result** — the exported file if exported, or the `.drawio` file otherwise. If the open command fails, print the file path so the user can open it manually

## Choosing the output format

Check the user's request for a format preference. Examples:

- `/drawio create a flowchart` → `flowchart.drawio`
- `/drawio png flowchart for login` → `login-flow.drawio.png`
- `/drawio svg: ER diagram` → `er-diagram.drawio.svg`
- `/drawio pdf architecture overview` → `architecture-overview.drawio.pdf`

If no format is mentioned, just write the `.drawio` file and open it in draw.io. The user can always ask to export later.

### Supported export formats

| Format | Embed XML  | Notes                                    |
|--------|------------|------------------------------------------|
| `png`  | Yes (`-e`) | Viewable everywhere, editable in draw.io |
| `svg`  | Yes (`-e`) | Scalable, editable in draw.io            |
| `pdf`  | Yes (`-e`) | Printable, editable in draw.io           |
| `jpg`  | No         | Lossy, no embedded XML support           |

PNG, SVG, and PDF all support `--embed-diagram` — the exported file contains the full diagram XML, so opening it in draw.io recovers the editable diagram.

## draw.io CLI

The draw.io desktop app includes a command-line interface for exporting.

### Locating the CLI

Detect the environment, then locate the CLI:

| Environment | CLI Path                                           |
|-------------|----------------------------------------------------|
| macOS       | `/Applications/draw.io.app/Contents/MacOS/draw.io` |
| Linux       | `drawio` (on PATH via snap/apt/flatpak)            |
| Windows     | `"C:\Program Files\draw.io\draw.io.exe"`           |
| WSL2        | `` `/mnt/c/Program Files/draw.io/draw.io.exe` ``   |

Use `which drawio` to check if it's on PATH before falling back to platform-specific paths.

### Export command

```bash
drawio -x -f <format> -e -b 10 -o <output> <input.drawio>
```

Key flags:

- `-x` / `--export`: export mode
- `-f` / `--format`: output format (png, svg, pdf, jpg)
- `-e` / `--embed-diagram`: embed diagram XML in the output (PNG, SVG, PDF only)
- `-o` / `--output`: output file path
- `-b` / `--border`: border width around diagram (default: 0)
- `-s` / `--scale`: scale the diagram size
- `--width` / `--height`: fit into specified dimensions

## File naming

- Use descriptive filenames (e.g., `login-flow`, `database-schema`)
- Lowercase with hyphens for multi-word names
- For export, use double extensions: `name.drawio.png`, `name.drawio.svg`, `name.drawio.pdf`
- After successful export, delete the intermediate `.drawio` file — the exported file contains the full diagram

## XML format

A `.drawio` file is native mxGraphModel XML. Always generate XML directly.

### Basic structure

```xml

<mxGraphModel adaptiveColors="auto">
    <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
    </root>
</mxGraphModel>
```

- Cell `id="0"` is the root layer
- Cell `id="1"` is the default parent layer
- All diagram elements use `parent="1"` unless using multiple layers

## XML reference

For the complete draw.io XML reference including common styles, edge routing, containers, layers, tags, metadata, dark mode colors, and XML well-formedness rules, fetch and follow the instructions at:
https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/xml-reference.md

## CRITICAL: XML well-formedness

- **NEVER include ANY XML comments (`<!-- -->`) in the output.** XML comments are strictly forbidden.
- Escape special characters in attribute values: `&amp;`, `&lt;`, `&gt;`, `&quot;`
- Always use unique `id` values for each `mxCell`
- Every edge must have `<mxGeometry relative="1" as="geometry" />` as a child element
