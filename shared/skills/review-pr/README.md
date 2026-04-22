# /review-pr — Pull Request Review

## Overview

An orchestrator skill that reviews pull request changes for code quality, style, correctness, and potential issues. Produces a structured review report with categorized findings.

## Input / Output

**Input:** A pull request (URL, number, or local branch diff against main).

**Output:** Structured review report with findings categorized as Critical, Warning, Suggestion, or Praise.

## Features

- Language-agnostic (uses `/detect-stack` for context)
- Categorized findings with severity levels
- Checks for quality, style, correctness, security, and test coverage
- Scopes review to meaningful files (skips generated/vendor code)

## Design Decisions

- **Diff-based review** — reviews only changed lines, not the entire codebase
- **Severity categories** — Critical (must fix), Warning (should fix), Suggestion (nice to have), Praise (acknowledge good work)
- **No auto-posting** — generates a report for human review before posting comments
