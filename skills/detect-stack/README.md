# /detect-stack — Project Tech Stack Detection

## Overview

A utility skill that analyzes a project directory to classify its tech stack. Detects language, framework, build system, package manager, and project structure. Used as a building block by other skills that need to understand the project before operating on it.

## Input / Output

**Input:** A project directory to analyze (defaults to current working directory).

**Output:** Structured classification of the project:

- Primary language(s)
- Framework(s)
- Build tool(s)
- Package manager
- Project structure (single module, multi-module, monorepo)
- Entry points
- Test framework

## Supported Languages

Python, TypeScript, JavaScript, Go, Java, Kotlin, Rust, Ruby, C#/.NET.

## Design Decisions

- **File-based detection over CLI** — reads indicator files directly instead of running build tool commands, which may not be installed
- **Multi-framework support** — a project can use multiple frameworks (e.g. Express.js + React)
- **Confidence-free** — reports what it finds without confidence scores. If detection is ambiguous, it lists all possibilities
