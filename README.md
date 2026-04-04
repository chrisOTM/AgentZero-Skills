# AgentZero Skills

This repository contains a small collection of Agent Zero skills.
Most of the repo is documentation-first: each skill is primarily defined in a `SKILL.md` file with YAML frontmatter and structured Markdown instructions.

## Repository Structure

- `good-morning-trader/`
- `life-coach/`
- `value-stock-analyzer/`
- `AGENTS.md`

## Included Skills

### `good-morning-trader`

A daily pre-trading briefing skill for options sellers.
It focuses on volatility, macro events, market sentiment, and technical structure before market open.

Files of note:

- `good-morning-trader/SKILL.md`
- `good-morning-trader/README.md`
- `good-morning-trader/scripts/market_data.py`

### `life-coach`

A German-language life coaching skill for personal development, goal setting, habit building, decision support, and self-reflection.

Files of note:

- `life-coach/SKILL.md`

### `value-stock-analyzer`

A detailed fair value stock analysis skill for value and dividend investing.
It includes a structured, multi-step methodology and example output.

Files of note:

- `value-stock-analyzer/SKILL.md`
- `value-stock-analyzer/examples/CMCSA_Fair_Value_Analysis.md`

## File Conventions

The repository follows a simple skill-oriented layout:

- `SKILL.md`: main skill definition
- `README.md`: optional supporting documentation for a skill or for the repo
- `examples/`: example outputs or reference materials
- `scripts/`: optional helper code used by a skill

Typical `SKILL.md` files include:

- YAML frontmatter
- metadata such as `name`, `description`, `version`, `author`, and `tags`
- `trigger_patterns`
- optional `allowed_tools`
- Markdown instructions describing workflow, output format, and examples

## Usage

Use these folders as Agent Zero skills by placing the desired skill directory into your Agent Zero skills location.

In general:

1. Copy a skill folder into your Agent Zero skills directory.
2. Reload or restart Agent Zero if needed.
3. Invoke the skill using one of the phrases described in that skill's `trigger_patterns` or usage section.

For example, `good-morning-trader` can be activated with prompts such as `Good morning`, `Morgenroutine`, or `market analysis`.

## Executable Helper

The only executable helper script currently in this repository is:

- `good-morning-trader/scripts/market_data.py`

It collects market data for the trading skill and depends on:

- `yfinance`
- `pandas`

You can run it from the repository root with:

```bash
python good-morning-trader/scripts/market_data.py
```

## Development Notes

This is not a conventional application repository.
There is currently no formal build, lint, or automated test framework configured at the repo root.

For the current repository state:

- there is no `package.json`
- there is no `pyproject.toml`
- there is no `Makefile`
- there is no configured `pytest`, `jest`, `vitest`, or Playwright setup

For code and documentation changes, use the narrowest meaningful verification step.
For the Python helper, the most useful lightweight validation is:

```bash
python -m py_compile good-morning-trader/scripts/market_data.py
```

## Agent Guidance

Agents working in this repository should follow the guidance in `AGENTS.md`.

That file includes:

- repository-specific editing expectations
- build, lint, and test command guidance
- single-test guidance for the current tooling reality
- Markdown and Python style expectations
- instructions about missing Cursor and Copilot rule files

## Summary

`AgentZero Skills` is a documentation-first repository of reusable skills for Agent Zero.
If you are editing or extending the repo, start with the relevant `SKILL.md` file and consult `AGENTS.md` for repository-specific agent instructions.
