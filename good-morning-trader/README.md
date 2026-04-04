# Good Morning Trader

This skill generates a structured pre-trading briefing for options sellers.
It is aimed at traders who want a fast view of volatility, macro risk, sentiment, and technical structure before opening new positions.

## Overview

`good-morning-trader` is built around a four-block market review:

1. Volatility dashboard
2. Macro and economic calendar
3. Market sentiment and breadth
4. Technical analysis

Each block ends with a stoplight-style action rating so the final output can quickly signal whether conditions support normal trading, reduced risk, or no new trades.

## Main Files

- `good-morning-trader/SKILL.md`
- `good-morning-trader/README.md`
- `good-morning-trader/scripts/market_data.py`

## Typical Activation

This skill is intended for prompts such as:

- `good morning`
- `morgenroutine`
- `guten morgen`
- `pre trading briefing`
- `market analysis`
- `start trading day`

See `SKILL.md` for the full trigger list and detailed operating instructions.

## Workflow

The skill is designed to:

1. Gather market data.
2. Review the volatility environment.
3. Check macro events and headline risk.
4. Evaluate sentiment and market breadth.
5. Summarize technical structure.
6. Produce a final trading verdict.

The default perspective is conservative and capital-preservation-oriented.
It is especially suited to short premium strategies such as short puts, short calls, credit spreads, iron condors, and strangles.

## Market Data Helper

This skill includes the repository's only current executable helper script:

- `good-morning-trader/scripts/market_data.py`

The script uses:

- `yfinance`
- `pandas`

Run it from the repository root with:

```bash
python good-morning-trader/scripts/market_data.py
```

For a lightweight validation step:

```bash
python -m py_compile good-morning-trader/scripts/market_data.py
```

## Intended Audience

This skill is best suited for:

- options sellers
- volatility-aware traders
- traders managing risk before market open
- users trading US markets and, where relevant, European index markets

It is less suitable for:

- pure day trading workflows
- long-only investing workflows
- beginners without options knowledge

## Repository Notes

This repository does not currently define a formal build or automated test runner for skill files.
For edits to this skill, verify:

- frontmatter remains coherent
- headings and tables render cleanly
- trigger phrases and references still match `SKILL.md`
- the helper script still compiles if changed

See the repository-level `AGENTS.md` for broader agent guidance.
