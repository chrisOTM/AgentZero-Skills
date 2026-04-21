# Good Morning Trader – Version 1.3.0

This skill generates a structured pre‑trading briefing for options sellers, **now including real‑time news impact assessment**. It is aimed at traders who want a fast view of volatility, macro risk, sentiment, technical structure, and the most relevant news before opening new positions.

## Overview

`good‑morning‑trader` is built around a five‑phase market review:

1. **Phase 1**: Data Collection (yfinance Primary)
2. **Phase 1.5**: News Collection and Impact Assessment
3. **Phase 2**: Structured Analysis (Volatility Dashboard, Macro Calendar, Sentiment & Breadth, Technical Analysis)
4. **Phase 3**: Dashboard Summary & Final Verdict

Each block ends with a stoplight‑style action rating so the final output can quickly signal whether conditions support normal trading, reduced risk, or no new trades.

**Key Enhancement:** Phase 1.5 ensures the briefing always incorporates the most recent financial/market news, with impact ratings (High/Medium/Low) and integration into each analysis block.

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

1. Gather market data via the optimized `market_data_optimized.py` script.
2. **Collect real‑time news headlines** using `search_engine` queries.
3. Review the volatility environment.
4. Check macro events and headline risk, now explicitly integrating news impacts.
5. Evaluate sentiment and market breadth.
6. Summarize technical structure.
7. Produce a final trading verdict that reflects both data **and** news.

The default perspective is conservative and capital‑preservation‑oriented.
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
- volatility‑aware traders
- traders managing risk before market open
- users trading US markets and, where relevant, European index markets
- **traders who require news‑aware briefings**

It is less suitable for:

- pure day trading workflows
- long‑only investing workflows
- beginners without options knowledge

## Repository Notes

This repository does not currently define a formal build or automated test runner for skill files.
For edits to this skill, verify:

- frontmatter remains coherent
- headings and tables render cleanly
- trigger phrases and references still match `SKILL.md`
- the helper script still compiles if changed
- **the news‑collection phase (Phase 1.5) is correctly integrated**

## Version History

- **1.3.0** (2026‑04‑21): Added dedicated News Collection phase and integrated news impact assessment into all analysis blocks.
- **1.2.0** (2026‑04‑20): Replaced browser_agent with search_engine for sentiment/macro data collection.
- **1.1.0** (2026‑04‑16): Optimized: browser_agent focus, caching, avoids web‑scraping bottlenecks.
- **1.0.0** (2026‑03‑30): Initial release with 4‑block structure.

See the repository‑level `AGENTS.md` for broader agent guidance.

See the repository-level `AGENTS.md` for broader agent guidance.
