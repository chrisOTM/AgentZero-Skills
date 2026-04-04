# Fair Value Stock Analysis

This skill provides a structured fair value analysis workflow for value and dividend investors.
It is designed to analyze a company by ticker or name using a detailed, investor-focused methodology.

## Overview

`fair-value-stock-analysis` guides an agent through a multi-step research and valuation process covering:

- company classification by sector type
- data collection from multiple sources
- long-term financial analysis
- owner earnings and ROIC-based analysis
- earnings quality checks
- valuation scenarios
- dividend safety
- moat analysis
- scenario-based recommendations

The emphasis is on factual, dated, investor-relevant analysis rather than promotional language.

## Files

- `value-stock-analyzer/SKILL.md`
- `value-stock-analyzer/examples/CMCSA_Fair_Value_Analysis.md`

## Workflow

The skill expects analysis that is:

- precise and source-aware
- explicit about fiscal years and reporting dates
- transparent about uncertainty and estimates
- tailored to long-term investors
- adaptable to sector-specific cases such as REITs, banks, insurers, utilities, and capital-light software businesses

In practice, the skill walks through sector classification, data collection, financial analysis, earnings quality, valuation, and final recommendation.

## Typical Activation

This skill is intended for prompts such as:

- `fair value analysis`
- `analyze stock`
- `stock valuation`
- `fundamental analysis`
- `aktienanalyse`
- `analyze ticker`

See `SKILL.md` for the complete trigger list and workflow.

## Example Output

An example implementation is included in:

- `value-stock-analyzer/examples/CMCSA_Fair_Value_Analysis.md`

That example shows how the methodology can be applied to a real company analysis.

## Intended Use

This skill is best suited to long-form company research where the user wants more than a quick opinion.
It is designed for careful valuation work, not short-form trading commentary or generic stock summaries.

## Tooling Notes

This skill repository is documentation-first.
There is no dedicated build or test framework for validating this skill automatically.

When editing this skill, verify:

- YAML frontmatter remains coherent
- Markdown tables and headings render cleanly
- examples still match the methodology described in `SKILL.md`
- file paths and references are still valid
- claims remain consistent with the skill's factual, date-labeled style

See the repository-level `AGENTS.md` for detailed agent instructions.
