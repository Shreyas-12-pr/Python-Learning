# Python Learning / LeetCode Practice Repository

A personal Python practice repository for LeetCode-style algorithm and data structure problems.

## Overview

This repository is organized around coding challenges and practice templates. It includes:

- `problems/` — categorized problem folders for algorithms and data structures
- `templates/` — reusable Python starter files for common problem patterns
- `tests/` — sample tests for verifying solution behavior
- `notes/` — study notes on algorithms, patterns, and problem-solving techniques

## Goals

- Practice algorithmic thinking and problem solving in Python
- Keep solutions organized by topic and technique
- Provide reusable templates for frequent patterns like BFS, DFS, binary search, and union-find
- Track study notes for interview preparation and concept review

## Repository Structure

- `problems/`
  - Organized by topic (e.g. `array`, `graph_theory`, `dynamic_programming`)
  - Each folder contains individual problem implementations and supporting files
- `templates/`
  - Starter files for common approaches
  - Useful when beginning a new problem or reviewing a pattern
- `notes/`
  - Markdown notes for algorithm concepts, techniques, and interview strategies
- `tests/`
  - Example test cases to validate solutions with pytest

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the environment:

- Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

- Windows Command Prompt:

```cmd
.\.venv\Scripts\activate.bat
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Use pytest to run the repository tests:

```bash
pytest
```

## Adding a New Problem

1. Add a new folder under `problems/<category>/`.
2. Create a solution file with a clear name.
3. Optionally add a test file or update `tests/test_examples.py`.
4. Use templates from `templates/` when appropriate.

## Notes and Study Tips

- Keep notes current in `notes/` as you learn new patterns.
- Review templates regularly to reinforce common approaches.
- Use problem categories to focus practice on a particular skill.

## Project Metadata

- Package name: `leetcode`
- Python requirement: `>=3.10`
- Test runner: `pytest`

---
