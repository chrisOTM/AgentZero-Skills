# AGENTS.md

## Purpose

This repository contains Agent Zero skills, not a conventional application package.
Most files are Markdown skill definitions with YAML frontmatter.
There is currently one executable helper script: `good-morning-trader/scripts/market_data.py`.

This guide is for coding agents operating inside `/home/chris/Coding/AgentZero/Skills`.
Prefer small, targeted edits that preserve the existing structure and writing style.

## Rule Sources

I checked for additional repository rules in these locations:

- `.cursor/rules/`
- `.cursorrules`
- `.github/copilot-instructions.md`

None of those files exist in this repository at the time of writing.
There is also no pre-existing root `AGENTS.md` in this workspace.

## Repository Layout

- `good-morning-trader/`
- `life-coach/`
- `value-stock-analyzer/`

Observed file patterns:

- Each skill is centered on a `SKILL.md` file.
- Some skills include supporting docs such as `README.md` or `examples/*.md`.
- Helper code, if present, lives under a local subdirectory such as `scripts/`.

## Current Tooling Reality

This repo does **not** currently define a formal build, lint, or test system.
There is no `package.json`, `pyproject.toml`, `Makefile`, `pytest` config, ESLint config, or similar project manifest.

Agents should not invent a toolchain when making routine edits.
Document the absence of automation clearly, then use the smallest appropriate verification step.

## Build / Lint / Test Commands

Run commands from the repository root unless a narrower working directory is needed.

### General repository checks

- List top-level skill directories: `ls`
- Search for text usage: `rg "pattern" .`
- Inspect tracked changes: `git status --short`

### Build

- No formal build step exists.
- For this repository, “build” usually means validating changed Markdown/YAML-like content and any touched helper scripts.

### Lint

- No lint runner is configured.
- For Markdown-heavy changes, manually check heading structure, fenced blocks, tables, and frontmatter consistency.
- For Python changes, use syntax validation:
  - `python -m py_compile good-morning-trader/scripts/market_data.py`

### Test

- No automated test suite is configured.
- There is no `pytest`, `unittest`, `vitest`, `jest`, or Playwright setup in this repo.

### Run the existing helper script

- Execute the market data helper directly:
  - `python good-morning-trader/scripts/market_data.py`

This script depends on external packages and network access:

- `yfinance`
- `pandas`

If execution fails because dependencies are missing, report that explicitly instead of silently working around it.

### Single-test guidance

- There is currently **no single-test command**, because there is no configured test runner.
- If you add tests in the future, update this file with the exact per-test invocation.
- Until then, the closest equivalent is targeted verification of the changed artifact:
  - Single Python file syntax check: `python -m py_compile path/to/file.py`
  - Single script execution: `python path/to/script.py`
  - Single document review: inspect one changed `SKILL.md` or `README.md` end-to-end

## What To Verify After Changes

After editing Markdown skill files:

- Frontmatter still parses visually as valid YAML.
- Required metadata keys remain coherent.
- Headings are ordered logically.
- Lists, tables, and code fences render cleanly.
- Cross-file references and paths still exist.

After editing Python:

- Run `python -m py_compile` on the touched file.
- If practical, run the script entrypoint you changed.
- Do not claim runtime validation if network or dependencies prevented execution.

## Skill File Conventions

Use the existing `SKILL.md` files as the primary style reference.

Expected structure near the top of a skill file:

1. YAML frontmatter bounded by `---`
2. Core metadata such as `name`, `description`, `version`, `author`, `tags`
3. Trigger metadata such as `trigger_patterns`
4. Optional tool metadata such as `allowed_tools`
5. A Markdown body with sections, phases, examples, and output guidance

When editing frontmatter:

- Keep key names lowercase with underscores where already used.
- Preserve existing quoting style if present.
- Keep arrays readable and compact unless they become long enough to justify multiline formatting.
- Do not rename metadata keys unless the whole repository is being migrated intentionally.

## Markdown Style Guidelines

- Preserve the repo’s documentation-first structure.
- Prefer clear section headings over dense paragraphs.
- Use ordered phases when describing a process.
- Use tables only when they improve scanability.
- Keep examples concrete and close to the skill’s real workflow.
- Match the file’s existing language. Some files are English, some German, and some mixed.
- Within a single section, keep terminology consistent.
- Keep agent instructions direct and operational.

For analytical content, follow the strongest existing pattern from `value-stock-analyzer/SKILL.md`:

- Be factual and precise.
- Attach dates, fiscal years, or reporting periods to numeric claims.
- State uncertainty explicitly.
- Avoid hype, marketing language, and unsupported conclusions.

## Python Style Guidelines

The current Python code is lightweight, script-oriented, and procedural.
Preserve that unless there is a clear reason to introduce more structure.

### Imports

- Group imports by standard library, third-party, then local imports.
- Keep imports at the top of the file unless a lazy import is required.
- Remove unused imports when touching a file.

### Formatting

- Follow PEP 8 style for spacing and line length.
- Use 4 spaces for indentation.
- Prefer readable intermediate variables over dense expressions.
- Keep functions short and single-purpose when practical.

### Types

- Type hints are not yet common in this repo.
- Do not add broad type-annotation churn to small maintenance edits.
- For new or expanded Python logic, add type hints where they clarify inputs/outputs without creating noise.

### Naming

- Functions and variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Filenames: lowercase, use hyphens for skill directories and underscores for Python modules when needed
- Use descriptive names tied to the domain, such as `vix_data`, `macro_data`, or `trigger_patterns`

### Error handling

- Catch exceptions only where the code can degrade gracefully or add useful context.
- Prefer explicit, user-readable error messages.
- Do not swallow failures silently.
- For data-fetching scripts, return or print structured failure information, as `market_data.py` already does.
- Avoid broad exception handling around large blocks unless the script is intentionally best-effort.

## Change Strategy For Agents

- Prefer minimal edits over broad rewrites.
- Preserve file layout and section ordering unless the current structure is clearly broken.
- Do not normalize every style inconsistency in untouched files.
- If a repository-wide convention is unclear, follow the local file you are editing.
- Keep examples, commands, and file paths repository-real.

## When Adding New Files

- Put new skill guidance beside the relevant skill, not in a generic misc folder.
- Name support docs clearly, for example `README.md`, `examples/...`, or `scripts/...`.
- If you add a new executable script, document how to run it in this file.
- If you introduce a real test runner or linter, update the command section immediately.

## Preferred Agent Workflow

1. Inspect the target skill directory and nearby files first.
2. Determine whether the change is documentation-only or includes executable code.
3. Make the smallest correct edit.
4. Run the narrowest meaningful verification step.
5. Report exactly what was validated and what could not be validated.

## Quick Summary

- This is a Markdown-first skills repository.
- There is no configured build/lint/test framework today.
- The only current executable code is a Python helper under `good-morning-trader/scripts/`.
- No Cursor or Copilot rule files are present.
- Favor precise, structured, minimal edits that respect each skill file’s local style.
