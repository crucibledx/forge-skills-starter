---
description: Detect and classify a project's tech stack - language, framework, build tools, and structure
version: 1.0.0
type: utility
language: "*"
test:
  specimens:
    - specimen/python/fastapi
    - specimen/ts/express
---

# Detect Stack

Analyze a project directory to classify its tech stack. Returns structured information about the language, framework, build system, package manager, and project structure.

## Step 1 — Scan project root

Read the project root directory. Look for indicator files:

| File/Dir                                                    | Indicates                         |
|-------------------------------------------------------------|-----------------------------------|
| `package.json`                                              | Node.js / JavaScript / TypeScript |
| `tsconfig.json`                                             | TypeScript                        |
| `requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile` | Python                            |
| `go.mod`                                                    | Go                                |
| `pom.xml`, `build.gradle`, `build.gradle.kts`               | Java / Kotlin                     |
| `Cargo.toml`                                                | Rust                              |
| `Gemfile`                                                   | Ruby                              |
| `*.csproj`, `*.sln`                                         | C# / .NET                         |

## Step 2 — Detect framework

Based on the language, look for framework indicators:

### Python

| Indicator                 | Framework |
|---------------------------|-----------|
| `fastapi` in dependencies | FastAPI   |
| `django` in dependencies  | Django    |
| `flask` in dependencies   | Flask     |

### TypeScript / JavaScript

| Indicator                      | Framework  |
|--------------------------------|------------|
| `express` in dependencies      | Express.js |
| `next` in dependencies         | Next.js    |
| `react` in dependencies        | React      |
| `@nestjs/core` in dependencies | NestJS     |

### Go

| Indicator                            | Framework        |
|--------------------------------------|------------------|
| `github.com/gin-gonic/gin` in go.mod | Gin              |
| `github.com/gofiber/fiber` in go.mod | Fiber            |
| `net/http` imports                   | Standard library |

### Java

| Indicator                             | Framework   |
|---------------------------------------|-------------|
| `spring-boot` in pom.xml/build.gradle | Spring Boot |
| `quarkus` in pom.xml                  | Quarkus     |

## Step 3 — Detect build tools and structure

| Indicator                                      | Tool                      |
|------------------------------------------------|---------------------------|
| `Makefile`                                     | Make                      |
| `Dockerfile`, `docker-compose.yml`             | Docker                    |
| `package.json` scripts                         | npm/yarn/pnpm/bun scripts |
| Multiple `pom.xml` / `build.gradle`            | Multi-module project      |
| `nx.json`, `turbo.json`, `pnpm-workspace.yaml` | Monorepo                  |

## Step 4 — Produce classification

Output a structured classification:

```
Project: <project-name>
Language: <primary-language>
Framework: <detected-framework>
Build: <build-tool>
Package Manager: <package-manager>
Structure: <single-module | multi-module | monorepo>
Entry Points: <main files or directories>
Test Framework: <detected-test-framework>
```

If multiple languages/frameworks are detected, list all of them.

> "Here's what I detected. Does this look correct?"
