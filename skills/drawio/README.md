# /drawio — Draw.io Diagram Generation

## Overview

A utility skill for generating draw.io diagrams as native `.drawio` files with optional export to PNG, SVG, or PDF. Based on the [official draw.io MCP integration](https://github.com/jgraph/drawio-mcp).

## Input / Output

**Input:** Natural language description of the desired diagram (flowchart, ER diagram, architecture, sequence, etc.)

**Output:** A `.drawio` file or exported image (`.drawio.png`, `.drawio.svg`, `.drawio.pdf`) with embedded diagram XML for re-editability.

## Features

- Generates native mxGraphModel XML
- Supports all diagram types (flowchart, ER, sequence, class, network, architecture)
- Exports with embedded XML — the exported file is still editable in draw.io
- Auto-detects draw.io CLI on macOS, Linux, Windows, and WSL2

## Design Decisions

- **Native XML over Mermaid** — Mermaid requires server-side conversion. Native XML can be written directly to `.drawio` files.
- **Embedded diagrams** — Using `--embed-diagram` flag ensures exported images remain editable in draw.io.
- **Double extensions** — `name.drawio.png` signals the file contains embedded diagram XML.

## Source

Based on the public [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) project, adapted as a portable skill for use across AI coding assistants.
