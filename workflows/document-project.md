---
description: End-to-end project documentation workflow using /document skill with draw.io diagrams
---

# Document Project Workflow

Generate comprehensive project documentation with architecture diagrams.

## Prerequisites

- The `/document` skill must be available
- The `/drawio` skill must be available
- draw.io desktop app installed (for PNG export)

## Steps

1. **Run the document skill**

   ```
   /document
   ```

   This will:
    - Detect the project stack
    - Analyze the directory structure
    - Identify the architecture pattern
    - Generate architecture diagrams using draw.io
    - Write structured Markdown documentation

2. **Review the generated diagrams**

   Open each `.drawio.png` file and verify:
    - No overlapping elements
    - Clear labels on all components
    - Consistent color coding (per `drawio-conventions` rule)
    - Readable font sizes
    - Clean arrow routing (no spaghetti)

3. **Review the generated documentation**

   Check the Markdown output for:
    - Accurate project description
    - Correct tech stack information
    - Working code examples
    - Proper diagram references
    - Complete API documentation (if applicable)

4. **Iterate if needed**

   Ask the agent to fix any issues:
    - "Move the database component below the service layer"
    - "Add the Redis cache to the architecture diagram"
    - "The API routes table is missing the DELETE endpoints"

5. **Commit the documentation**

   ```bash
   git add docs/
   git commit -m "docs: add architecture documentation and diagrams"
   ```
