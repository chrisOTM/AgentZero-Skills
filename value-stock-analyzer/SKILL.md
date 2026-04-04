---
name: "fair-value-stock-analysis"
description: "Comprehensive fair value stock analysis for value and dividend investors. Automatically analyzes any stock by ticker symbol or company name following professional valuation methodology."
version: "1.2.0"
author: "Agent Zero"
tags: ["finance", "investing", "valuation", "stocks", "value-investing"]
trigger_patterns:
  - "fair value analysis"
  - "analyze stock"
  - "value analysis"
  - "stock valuation"
  - "fundamental analysis"
  - "bewertung aktie"
  - "aktienanalyse"
  - "ticker:"
  - "analyze ticker"
  - "value"
allowed_tools:
  - search_engine
  - document_query
  - code_execution_tool
  - text_editor
  - call_subordinate
---

# 🔍 Fair Value Stock Analysis

## Tone & Style Guidelines

**Always apply these principles throughout the entire analysis:**

- **Sachlich und präzise**: State facts with their source year. No filler phrases like "impressive", "exceptional", or "remarkable growth". Let the numbers speak.
- **Investororientiert**: Every section must answer the question: *What does this mean for a long-term investor?* Avoid academic abstraction.
- **Keine Übertreibungen**: Do not use superlatives or marketing language. If a company has a strong moat, describe the mechanism — do not just call it "dominant".
- **Unsicherheit benennen**: Where data is estimated or incomplete, say so explicitly. Use "estimated", "based on TTM", "as of FY[YEAR]" consistently.
- **Einheitliche Zeitreferenzen**: Every data point must be tagged with its fiscal year or reporting date (e.g., "Owner Earnings FY2023: $4.2bn"). Never present numbers without a year.

---

## When to Use

Activate this skill when the user asks for:
- Analysis of a specific stock by ticker symbol (e.g., "Analyze AAPL", "Fair value of MSFT")
- Fundamental analysis of a company
- Value investing research on a specific stock
- Dividend analysis for a company
- Stock valuation and fair value estimation

---

## Analysis Process

Follow these 11 steps (Step 0 through Step 10) to create a comprehensive fair value analysis:

---

### Step 0: Sector & Industry Classification

**Before any analysis, classify the company into one of these categories:**

| Sector Type | Examples | Special Treatment |
|-------------|----------|-------------------|
| **Standard** | Tech, Consumer, Industrials, Healthcare | Default methodology applies |
| **REIT** | Realty Income, Simon Property, Vonovia | Use FFO/AFFO instead of EPS/FCF; NAV as primary valuation anchor |
| **Bank / Insurance** | JPMorgan, Allianz, Berkshire | Use P/Book, ROE, NIM, CET1 ratio; DCF not applicable |
| **Utility / Regulated** | NextEra, National Grid, RWE | Use RAB/EV, regulated asset growth, dividend as primary return driver |
| **Cyclical / Capital-Heavy** | Steel, Mining, Shipping | Normalize earnings through the cycle; EV/EBITDA over P/E |
| **Capital-Light / Software** | SaaS, Platforms | Emphasize Rule of 40, ARR growth, NRR; FCF margin trajectory |

**Apply the corresponding sector-specific metrics in Steps 3 and 5:**

#### REIT-specific additions:
- FFO (Funds from Operations) and AFFO per share (last 5 years)
- AFFO Payout Ratio (target: <85%)
- Occupancy rate and lease maturity profile
- NAV per share vs. current price (premium/discount)
- Debt / Total Assets and fixed-charge coverage ratio

#### Bank/Insurance-specific additions:
- Net Interest Margin (NIM) trend
- CET1 / Tier 1 Capital Ratio (regulatory buffer)
- Return on Tangible Equity (RoTE)
- Loan loss provisions as % of loan book
- Combined ratio (insurance only)
- P/Tangible Book Value vs. sector average

#### Utility-specific additions:
- Regulated Asset Base (RAB) growth
- EBITDA margin and interest coverage
- CapEx as % of revenue (infrastructure investment trajectory)
- Allowed Return on Equity (regulated return)
- Dividend as % of regulated earnings

---

### Step 1: Data Collection

1. **Identify the ticker symbol and exchange** from user input
2. **Gather current financial data** — verify each key metric from **at least 2 independent sources** before using it. Acceptable sources: company IR page / annual report, Bloomberg, Macrotrends, TIKR, Morningstar, Seeking Alpha, Yahoo Finance, Marketscreener. Note which sources were used.
3. **Required data points** (always label fiscal year):
   - Stock price (date of retrieval), market cap, enterprise value
   - Revenue, net income, EPS GAAP (last 10 fiscal years)
   - Operating cash flow, total capex, maintenance capex estimate (last 10 fiscal years)
   - D&A (depreciation & amortization, last 10 fiscal years)
   - Cash & short-term investments (year-end), total debt (year-end)
   - Invested capital (last 5 fiscal years, for ROIC calculation)
   - Dividend per share and payout history (if applicable)
4. **Use search_engine** for latest financial data and recent news
5. **Use document_query** for official earnings reports (10-K, 10-Q, annual report)

> ⚠️ **Data Quality Rule**: If a metric could only be sourced from one provider, flag it as "single-source estimate". Never present estimated figures as reported without disclosure. If data for a year is unavailable, write "n/a (FY[YEAR])" rather than leaving a blank or interpolating silently.

> ⚠️ **Maintenance CapEx Note**: Companies rarely report maintenance capex separately. Estimate it using one of these methods in priority order: (1) management guidance in annual report footnotes, (2) depreciation as a proxy (conservative lower bound for asset-light businesses), (3) capex minus stated growth capex from investor presentations. Always disclose the estimation method used.

---

### Step 2: Company Overview

Analyze and report:
- **Business model**: How does the company generate revenue and profit? Be specific about the monetization mechanism.
**Apply the corresponding sector-specific metrics in Steps 3 and 5:**

#### Standard sector-specific additions (Communication Services / Telecom / Media):
- **Network infrastructure**: High maintenance capex requirements, depreciation as proxy
- **Content/IP valuation**: Amortization of content libraries, subscriber metrics
- **Regulatory barriers**: Spectrum licenses, franchise agreements
- **Subscriber metrics**: Customer churn, ARPU trends, subscriber growth/losses
- **Advertising revenue cyclicality**: Sensitivity to economic cycles
- **Example**: Comcast (CMCSA) - see `/examples/CMCSA_Fair_Value_Analysis.md` for full analysis
- **Segment breakdown**: Revenue and operating profit by segment (most recent fiscal year, labeled)
- **Moat indicators**: Describe the actual mechanism — switching costs, network effects, brand pricing power, regulatory barriers, cost advantages. Do not just label; explain.

---

### Step 3: Financial Analysis (10-Year History)

#### 3a: Core Financial Table

Create a comprehensive table with fiscal year columns (FY[YEAR] format):

| Metric | FY[N-9] | ... | FY[N-1] | FY[N] | 10Y CAGR |
|--------|---------|-----|---------|-------|----------|
| Revenue ($m) | | | | | |
| Net Income ($m) | | | | | |
| EPS GAAP ($) | | | | | |
| D&A ($m) | | | | | |
| Operating Cash Flow ($m) | | | | | |
| Total Capex ($m) | | | | | |
| Maintenance Capex ($m, est.) | | | | | |
| Free Cash Flow ($m) | | | | | |
| **Owner Earnings ($m)** | | | | | |
| Cash & Equivalents ($m) | | | | | |
| Total Debt ($m) | | | | | |
| Net Debt ($m) | | | | | |
| Invested Capital ($m) | | | | | |
| **ROIC (post-tax, %)** | | | | | |

*For REITs: replace Net Income / EPS with FFO and AFFO per share. Replace Owner Earnings with AFFO.*
*For Banks: replace FCF/Owner Earnings section with NIM, CET1, RoTE, P/Book.*

#### 3b: Owner Earnings Calculation

**Owner Earnings (Buffett definition)** = Net Income + D&A − Maintenance Capex − Required Working Capital Changes

Calculate for each available fiscal year and enter into the table above. This figure represents what the business *actually earns* for shareholders after sustaining its competitive position — it is the primary input for the DCF in Step 5.

**Comparison check**: Calculate the Owner Earnings / Reported FCF ratio for each year. A persistent ratio significantly below 1.0 indicates that reported FCF overstates true earnings power (e.g., because growth capex is understated or working capital is managed aggressively). A ratio persistently above 1.0 may indicate conservative capex reporting. Flag divergences >20% and explain.

**Normalization**: If Owner Earnings show year-to-year volatility >30%, calculate the 3-year average as the normalized base. Disclose any one-time items excluded (litigation, asset sales, restructuring). State which figure is used as the DCF base and why.

#### 3c: ROIC–WACC Spread Analysis

**ROIC (post-tax)** = NOPAT / Invested Capital
- NOPAT = Operating Income × (1 − effective tax rate)
- Invested Capital = Total Equity + Total Debt − Cash & Equivalents (or use operating approach: Net PP&E + Net Working Capital + Goodwill/Intangibles)

Calculate ROIC for the last 5 fiscal years and construct the spread table:

| Year | ROIC (%) | WACC (est., %) | Spread (ROIC − WACC) | Value Creation |
|------|----------|---------------|----------------------|---------------|
| FY[N-4] | | | | Creating / Neutral / Destroying |
| FY[N-3] | | | | |
| FY[N-2] | | | | |
| FY[N-1] | | | | |
| FY[N] | | | | |

**Interpretation rules**:
- **Spread > +3%**: Sustainable value creation. High growth assumptions in DCF are credible.
- **Spread 0% to +3%**: Marginal value creation. Growth adds limited value; question DCF optimism.
- **Spread < 0%**: Value destruction. Every euro of growth invested at current ROIC destroys shareholder wealth. DCF growth assumptions must be paired with a credible path to ROIC improvement, or downgraded.

**Link to DCF**: The ROIC-WACC spread directly constrains which growth scenarios are internally consistent. If the base case assumes 8% growth but ROIC ≈ WACC, flag this as an inconsistency and either lower the growth assumption or model ROIC improvement explicitly.

#### 3d: Key Ratios (Most Recent Fiscal Year, Labeled)

- Gross margin, operating margin, net margin, FCF margin, Owner Earnings margin
- ROE, ROIC (post-tax) — see 3c for calculation
- ROIC vs. WACC spread (current year)
- Net debt / EBITDA
- Interest coverage (EBIT / interest expense)
- FCF conversion rate (FCF / Net Income)
- Owner Earnings conversion rate (Owner Earnings / Net Income)
- Payout ratio: EPS-based AND FCF-based AND Owner-Earnings-based (if dividend paying)

---

### Step 4: Earnings Quality Analysis

**This step must be completed before valuation.** Poor earnings quality invalidates the DCF inputs from Step 3. Complete all three sub-checks.

#### 4a: Accrual Ratio (Balance Sheet Method)

**Accrual Ratio** = (Net Operating Assets[t] − Net Operating Assets[t-1]) / Average Net Operating Assets

- Net Operating Assets = Total Assets − Cash − Total Liabilities + Total Debt
- Calculate for the last 3 fiscal years

| Year | NOA ($m) | ΔNetOperatingAssets ($m) | Accrual Ratio (%) | Signal |
|------|---------|--------------------------|------------------|--------|
| FY[N-2] | | | | |
| FY[N-1] | | | | |
| FY[N] | | | | |

**Interpretation**:
- Accrual Ratio **< 5%**: Earnings are largely cash-backed. 🟢
- Accrual Ratio **5–10%**: Moderate accruals; investigate working capital trends. 🟡
- Accrual Ratio **> 10%**: High accrual component; earnings may be overstated vs. cash reality. 🔴 Flag prominently.

A rising Accrual Ratio over consecutive years is a stronger warning signal than a single high reading.

#### 4b: Revenue / Receivables Divergence

Compare revenue growth to accounts receivable growth over the last 3 years:

| Year | Revenue YoY (%) | Accounts Receivable YoY (%) | Divergence | Signal |
|------|-----------------|-----------------------------|------------|--------|
| FY[N-2] | | | | |
| FY[N-1] | | | | |
| FY[N] | | | | |

**Interpretation**:
- Receivables growing **consistently faster** than revenue suggests aggressive revenue recognition, channel stuffing, or deteriorating collection quality. 🔴
- Receivables growing **in line** with revenue is neutral. 🟢
- Receivables growing **slower** than revenue indicates improving cash conversion. 🟢

If divergence > 10 percentage points in any year, note the business explanation (e.g., new contract timing, geographic mix shift) and assess whether it is plausible.

#### 4c: Cash Conversion Rate & FCF Quality

**Cash Conversion Rate (CCR)** = Operating Cash Flow / Net Income

| Year | Operating CF ($m) | Net Income ($m) | CCR | Signal |
|------|------------------|-----------------|-----|--------|
| FY[N-4] | | | | |
| FY[N-3] | | | | |
| FY[N-2] | | | | |
| FY[N-1] | | | | |
| FY[N] | | | | |

**Interpretation**:
- CCR **> 100%** consistently: Net income is conservatively stated; cash earnings exceed accounting earnings. 🟢
- CCR **80–100%**: Normal range for most businesses. 🟢
- CCR **< 80%** persistently: Net income is not fully converted to cash. Investigate: is this growth-driven working capital investment (temporary, acceptable) or structural earnings inflation (permanent, problematic)? 🟡
- CCR **< 60%** or declining trend: ⚠️ Red flag. State reason explicitly.

Also check: Does FCF include proceeds from asset sales or working capital releases that inflate it one-time? If so, note and adjust the normalized base.

#### 4d: Earnings Quality Summary

Provide a 3–5 sentence synthesis across 4a, 4b, and 4c:
- Overall earnings quality rating: 🟢 High / 🟡 Moderate / 🔴 Low
- State whether DCF inputs from Step 3 are used as-is, adjusted, or flagged with caveats
- If quality is Low, note the specific adjustment made to Owner Earnings / FCF before proceeding to Step 5

---

### Step 5: Valuation

#### 5a: Net Debt / Cash Bridge

Before running the DCF, establish the equity bridge:

| Item | Value (FY[YEAR]) |
|------|-----------------|
| Cash & short-term investments | +$Xm |
| Total financial debt | −$Xm |
| **Net Cash / (Net Debt)** | **±$Xm** |
| Per share | ±$X |

This figure is added to / subtracted from the DCF enterprise value to arrive at equity fair value per share.

*For REITs: also include off-balance-sheet lease obligations and preferred equity at liquidation value.*
*For Banks: skip bridge — valuation is equity-based (P/Book) by convention.*

---

#### 5b: DCF Calculation

**Primary DCF base: Owner Earnings** (normalized, from Step 3b).
**Secondary check: Normalized FCF** (3-year average, from Step 3a).

State both figures. If Owner Earnings and FCF diverge by more than 15%, explain the gap (maintenance capex estimation, D&A mismatch, working capital dynamics) and justify which figure is used as the DCF input. Default to the more conservative of the two unless a specific reason supports the higher figure.

> ⚠️ **Maintenance CapEx Note**: Companies rarely report maintenance capex separately. Estimate it using one of these methods in priority order: (1) management guidance in annual report footnotes, (2) depreciation as a proxy (conservative lower bound for asset-light businesses), (3) capex minus stated growth capex from investor presentations. Always disclose the estimation method used.

**For capital-intensive infrastructure companies (Telecom, Utilities, Industrials):**
- **Depreciation as proxy**: Often appropriate as assets require continual replacement
- **Ratio analysis**: Historical maintenance capex as % of total capex (if disclosed)
- **Industry benchmarks**: Typical maintenance capex ratios for sector
- **Comcast example**: Used depreciation as proxy for maintenance capex in analysis

| Assumption | Conservative | Realistic | Optimistic |
|------------|--------------|-----------|------------|
| Owner Earnings Base | As calculated | As calculated | As calculated |
| Growth (Years 1–5) | 4–6% | 7–10% | 11–14% |
| Growth (Years 6–10) | 2–4% | 4–6% | 6–9% |
| Terminal Growth Rate | 2.0% | 2.5% | 3.0% |
| Discount Rate (WACC) | 9.5% | 8.5% | 7.5% |

**ROIC consistency check** (mandatory): Cross-reference each growth scenario against the ROIC-WACC spread from Step 3c. If growth assumptions in a scenario imply reinvestment at ROIC < WACC, either (a) lower the growth rate, (b) model an explicit ROIC improvement path, or (c) flag the scenario as internally inconsistent. Do not proceed with inconsistent scenarios without disclosure.

**Terminal Value Methodology**: Use the **Gordon Growth Model** (perpetuity) as default:

> TV = OE₁₀ × (1 + g) / (WACC − g)

Discount TV back to present using the same WACC. Report TV as % of total DCF value — if TV exceeds 70% of total intrinsic value, show sensitivity: how does fair value change with ±0.5% terminal growth rate?

**Equity Fair Value per Share** = (PV of Owner Earnings + PV of Terminal Value + Net Cash) / Diluted shares outstanding

Show upside/downside to current price for each scenario.

---

#### 5c: Multiple Analysis

Compare current multiples to both historical 5-year averages and sector peers:

| Multiple | Current | 5Y Avg (FY[YEAR range]) | Sector Avg | Under/Overvalued? |
|----------|---------|------------------------|------------|-------------------|
| P/E (TTM) | | | | |
| Forward P/E | | | | |
| P/Owner Earnings | | | | |
| EV/EBITDA | | | | |
| P/FCF | | | | |
| FCF Yield (%) | | | | |
| P/Sales | | | | |

*P/Owner Earnings is added as a primary multiple. P/FCF serves as a cross-check.*
*For REITs: use Price/AFFO and EV/EBITDA instead of P/E.*
*For Banks: use P/Book and P/Tangible Book.*

---

#### 5d: Fair Value Band

Synthesize DCF and multiples into a consolidated range:

| Method | Conservative | Base Case | Optimistic |
|--------|--------------|-----------|------------|
| DCF / Owner Earnings | $X | $Y | $Z |
| P/Owner Earnings multiple | $X | $Y | $Z |
| EV/EBITDA multiple | $X | $Y | $Z |
| **Blended Fair Value** | **$X** | **$Y** | **$Z** |

Primary reference: **Base Case blended fair value**.

---

#### 5e: Potential Payback Period (PPP)

Calculate time to recover the current purchase price through accumulated Owner Earnings (use FCF as secondary reference):
- Static PPP (current normalized Owner Earnings, no growth assumed)
- Realistic PPP (base case growth assumptions applied)

---

### Step 6: Dividend Safety Analysis

*Complete this section only if the company currently pays a dividend. If no dividend is paid, state clearly: "No dividend paid as of FY[YEAR]. The following section is not applicable."*

#### 6a: Dividend Track Record

| Metric | FY[N-4] | FY[N-3] | FY[N-2] | FY[N-1] | FY[N] |
|--------|---------|---------|---------|---------|-------|
| DPS ($) | | | | | |
| YoY Growth (%) | | | | | |
| EPS Payout Ratio (%) | | | | | |
| FCF Payout Ratio (%) | | | | | |
| **Owner Earnings Payout Ratio (%)** | | | | | |

**Owner Earnings Payout Ratio** = Dividends Paid / Owner Earnings × 100. This is the most conservative and most meaningful payout metric, as it uses true economic earnings. FCF payout serves as a cross-check. Target thresholds for sustainability: <60% for cyclicals, <75% for stable compounders, <85% for utilities/REITs (use AFFO).

#### 6b: Dividend Cut Risk Assessment

| Factor | Assessment | Risk Level |
|--------|-----------|------------|
| Owner Earnings Payout Ratio | X% (target: <75%) | 🟢/🟡/🔴 |
| FCF Payout Ratio | X% (cross-check) | 🟢/🟡/🔴 |
| Earnings quality (from Step 4) | High / Moderate / Low | 🟢/🟡/🔴 |
| Earnings coverage trend | Stable / Deteriorating / Improving | |
| Net debt trajectory | Falling / Stable / Rising | |
| Dividend commitment language | Explicit / Vague / None | |
| Dividend history | Consecutive years of growth: X | |
| Owner Earnings volatility (3Y range) | Low / Medium / High | |
| Upcoming debt maturities vs. Owner Earnings | Manageable / Stretched | |

**Overall Cut Risk**: 🟢 Low / 🟡 Medium / 🔴 High

Provide a brief qualitative rationale (2–3 sentences) for the overall rating.

#### 6c: Yield-on-Cost Projection

Calculate projected yield-on-cost at today's entry price under base case dividend growth assumptions:

| Year | DPS (estimated) | Yield-on-Cost at Today's Price |
|------|----------------|-------------------------------|
| Year 1 | $X | X% |
| Year 3 | $X | X% |
| Year 5 | $X | X% |
| Year 10 | $X | X% |

State the assumed annual dividend growth rate and confirm it is supported by the Owner Earnings payout ratio trajectory. If dividend growth assumptions exceed Owner Earnings growth, flag this as unsustainable.

---

### Step 7: Qualitative Analysis

Evaluate:
- **Management quality**: CEO tenure and track record, insider ownership, compensation structure (does it align with per-share value growth, not just top-line?)
- **Capital allocation**: Dividend growth history, buyback discipline (was stock bought at sensible prices relative to Owner Earnings?), M&A track record — did acquired businesses earn above WACC?
- **Competitive positioning**: R&D intensity vs. peers, product/service pipeline, pricing power evidence
- **Industry dynamics**: Structural growth or decline, regulatory environment, disruption risk horizon
- **ESG & governance**: Relevant only where it poses material financial risk (e.g., carbon liability, supply chain exposure, board independence)

---

### Step 8: Moat Analysis

Rate moat strength (1–5) for each applicable dimension. Skip dimensions that genuinely do not apply rather than assigning a neutral score.

| Moat Dimension | Score (1–5) | Evidence |
|----------------|------------|---------|
| Switching costs | | Describe specific lock-in mechanism |
| Brand / pricing power | | Describe margin premium vs. generics |
| Network effects | | Describe how value increases with users |
| Cost advantages | | Describe scale, process, or location advantage |
| Regulatory / IP barriers | | Patents, licenses, regulated monopoly |

**Overall moat rating**: None / Narrow / Wide
**Moat durability**: Strengthening / Stable / Eroding — and why.

**Moat–ROIC consistency check**: The moat rating must be consistent with the ROIC-WACC spread from Step 3c. A "Wide" moat with persistent ROIC < WACC is a contradiction — resolve it explicitly (either downgrade moat or explain why ROIC is temporarily depressed).

---

### Step 9: Risk Assessment

| Risk Type | Specific Risk | Probability | Impact | Mitigant |
|-----------|--------------|-------------|--------|----------|
| Operational | | Low/Med/High | Low/Med/High | |
| Financial | | Low/Med/High | Low/Med/High | |
| Competitive | | Low/Med/High | Low/Med/High | |
| Macro / Cyclical | | Low/Med/High | Low/Med/High | |
### Step 4: Earnings Quality Analysis

**This step must be completed before valuation.** Poor earnings quality invalidates the DCF inputs from Step 3. Complete all three sub-checks.

**Example from Comcast analysis:** Cash Conversion Rate consistently >100% indicates high earnings quality, while Owner Earnings/FCF divergence of 15.3% required explanation and conservative choice of Owner Earnings as DCF base.
| Earnings quality | From Step 4 summary | Low/Med/High | Low/Med/High | |

Highlight any **red flags** (e.g., Owner Earnings payout >90%, FCF payout >90%, net debt/EBITDA >4x, accrual ratio >10%, CCR <60%, revenue concentration >40% in one customer, insider selling) with a ⚠️ marker.

---

### Step 10: Scenario Analysis & Final Recommendation

#### Scenario Summary (5–10 year horizon)

| Scenario | Owner Earnings CAGR | ROIC at Exit | Exit Multiple (P/OE) | Fair Value | Expected Annual Return |
|----------|---------------------|-------------|----------------------|------------|----------------------|
| 🐂 Bull | X% | X% | X× | $X | X% CAGR |
| 🎯 Base | X% | X% | X× | $Y | Y% CAGR |
| 🐻 Bear | X% | X% | X× | $Z | Z% CAGR |

State the key assumption that differentiates each scenario. Ensure all scenarios are internally consistent with the ROIC-WACC spread established in Step 3c.

#### Action Framework

The Margin of Safety required scales with business quality and earnings predictability:

| Moat / Quality | Required MoS for Buy | Notes |
|----------------|---------------------|-------|
| Wide Moat + High Earnings Quality | ≥15% below base fair value | Predictable cash flows justify tighter MoS |
| Narrow Moat or Moderate Quality | ≥25% below base fair value | Moderate uncertainty warrants wider buffer |
| No Moat or Low Earnings Quality | ≥40% below base fair value | High uncertainty; only deep value justifies entry |

#### Price Zones & Action Plan

Based on the calculated Fair Value (FV), define the following price zones and corresponding action plan:

| Price Zone | Action | Position Size |
|------------|--------|---------------|
| < [FV×0.70] (70% of FV) | ⭐ Strong Buy | Full position |
| [FV×0.70] – [FV×0.90] (70‑90% of FV) | 🟢 Buy / Accumulate | Half position / DCA |
| [FV×0.90] – [FV×1.10] (90‑110% of FV) | 🟡 Hold | No new purchases |
| > [FV×1.10] (>110% of FV) | 🔴 Reduce / Sell | Take profits |

*Replace [FV] with the actual base fair value calculated in Step 5.*

**Current price relative to base fair value**: X% of fair value → [Action based on moat-adjusted MoS and price zone table above]

**Key metrics to monitor going forward** (list 4–6 specific, measurable indicators with trigger thresholds, e.g., "ROIC drops below WACC for 2 consecutive years → thesis review"):

---

### Executive Summary

Place this at the **top of the final output** (write last, present first):

| | |
|---|---|
| **Company** | Name (Ticker, Exchange) |
| **Sector / Type** | e.g., Consumer Staples / Standard |
| **Price (date)** | $X (as of YYYY-MM-DD) |
| **Base Fair Value** | $X (blended DCF/OE + multiples) |
| **Upside / Downside** | X% |
| **Recommendation** | ⭐/🟢/🟡/🔴 |
| **Required MoS** | X% (based on moat + earnings quality) |
| **Earnings Quality** | 🟢 High / 🟡 Moderate / 🔴 Low |
| **ROIC–WACC Spread** | +X% / −X% (FY[YEAR]) |
| **Dividend Cut Risk** | 🟢/🟡/🔴 (if applicable) |
| **Moat** | None / Narrow / Wide |
| **Key Risk** | One-line summary |
| **Data Sources** | [Source 1], [Source 2] (as of FY[YEAR]) |

Follow with a 3–5 sentence investment thesis in plain language. State what needs to be true for the base case to play out. No superlatives.

---

## Output Format

Structure the final output in this order:
1. **Executive Summary** (always first — written last)
2. Steps 0–10 in sequence, each clearly labeled
3. Tables for all quantitative sections
4. Sector-specific sections activated where applicable (Step 0)
5. Earnings Quality section (Step 4) always completed before valuation
6. Dividend Safety section (Step 6) only if dividend is paid; omission noted explicitly

---

## Important Notes

- **Owner Earnings is the primary DCF input**: FCF is a cross-check, not the base. Explain any gap >15% between the two.
- **ROIC–WACC spread constrains growth assumptions**: Do not model high growth at ROIC ≈ WACC. Inconsistent scenarios must be flagged or corrected.
- **Earnings quality gates valuation**: If Step 4 yields a Low quality rating, apply a haircut to Owner Earnings before DCF or widen the MoS threshold. Document the adjustment.
- **Dual-source verification**: Every key metric from at least 2 sources, or flagged as "single-source estimate".
- **Year-tagging is mandatory**: No number without a fiscal year or retrieval date.
- **Maintenance CapEx**: Disclose estimation method. Never silently use total capex as maintenance capex for growth companies.
- **Terminal value sensitivity**: Report TV as % of total DCF; show ±0.5% terminal growth sensitivity if TV > 70%.
- **Net Cash Bridge**: Always adjust DCF enterprise value to equity value per share.
- **Sector routing**: Activate Step 0 sector metrics before proceeding. No FCF-based DCF for banks.
- **Moat–ROIC consistency**: A Wide Moat claim must be supported by a positive ROIC-WACC spread. Resolve contradictions explicitly.
- **MoS is not fixed**: Scale the required margin of safety to moat width and earnings quality (see Step 10 framework).
- **No marketing language**: Describe mechanisms and present evidence. Let the analysis speak.

---

## Checklist

Before delivering the analysis, verify:

**Data & Sourcing**
- [ ] Sector classified; sector-specific metrics activated
- [ ] All data points labeled with fiscal year or retrieval date
- [ ] Each key metric verified from at least 2 sources (or flagged as single-source)
- [ ] 10-year financial history table complete (n/a where unavailable)
- [ ] Maintenance capex estimated with method disclosed

**Earnings Quality (Step 4 — must complete before valuation)**
- [ ] Accrual Ratio calculated for last 3 years; interpretation provided
- [ ] Revenue / Receivables divergence checked for last 3 years
- [ ] Cash Conversion Rate calculated for last 5 years; trend assessed
- [ ] Earnings quality summary rating assigned (🟢/🟡/🔴)
- [ ] Any adjustments to Owner Earnings / FCF from quality findings documented

**Owner Earnings & ROIC (Step 3)**
- [ ] Owner Earnings calculated for all available years; normalization documented
- [ ] Owner Earnings vs. FCF gap assessed; explanation provided if >15%
- [ ] ROIC calculated for last 5 years using consistent invested capital definition
- [ ] ROIC–WACC spread table completed and interpreted
- [ ] ROIC consistency check applied to DCF growth assumptions

**Valuation (Step 5)**
- [ ] Owner Earnings (not FCF) used as primary DCF base; FCF cross-check included
- [ ] Net Debt / Cash bridge calculated and applied
- [ ] Terminal Value reported as % of intrinsic value; sensitivity shown if >70%
- [ ] All three DCF scenarios internally consistent with ROIC-WACC spread
- [ ] P/Owner Earnings multiple included in multiple analysis
- [ ] Blended fair value established

**Dividend (Step 6 — if applicable)**
- [ ] Owner Earnings payout ratio calculated (primary) and FCF payout (cross-check)
- [ ] Cut risk table completed with quality rating incorporated
- [ ] Yield-on-cost projection confirmed sustainable vs. Owner Earnings growth

**Qualitative & Risk**
- [ ] Moat dimensions scored with evidence; overall rating consistent with ROIC spread
- [ ] Risk table includes earnings quality risk row and mitigants
- [ ] Red flags marked with ⚠️

**Recommendation**
- [ ] MoS threshold set based on moat + earnings quality (not fixed at 30%)
- [ ] Scenario analysis uses Owner Earnings CAGR and ROIC at exit
- [ ] Key monitoring metrics listed with explicit trigger thresholds
- [ ] Executive summary written last, placed first; includes ROIC spread and earnings quality
- [ ] No superlatives, no unsupported claims, no missing year references
**Link to DCF**: The ROIC-WACC spread directly constrains which growth scenarios are internally consistent. If the base case assumes 8% growth but ROIC ≈ WACC, flag this as an inconsistency and either lower the growth assumption or model ROIC improvement explicitly.

**Example from Comcast analysis**: ROIC-WACC spread of +13.8% supports growth assumptions in DCF scenarios.
#### 5c: Multiple Analysis

Compare current multiples to both historical 5-year averages and sector peers:

| Multiple | Current | 5Y Avg (FY[YEAR range]) | Sector Avg | Under/Overvalued? |
|----------|---------|------------------------|------------|-------------------|
| P/E (TTM) | | | | |
| Forward P/E | | | | |
| P/Owner Earnings | | | | |
| EV/EBITDA | | | | |
| P/FCF | | | | |
| FCF Yield (%) | | | | |
| P/Sales | | | | |

**Sector-specific considerations:**
- **Telecom/Media**: EV/EBITDA often more relevant than P/E due to high depreciation
- **Capital-intensive**: P/FCF may be more stable than P/E
- **High-debt companies**: EV/EBITDA accounts for capital structure differences
- **Example (Comcast)**: P/E 5.3x vs. 12.0x historical indicates significant undervaluation

*P/Owner Earnings is added as a primary multiple. P/FCF serves as a cross-check.*
*For REITs: use Price/AFFO and EV/EBITDA instead of P/E.*
*For Banks: use P/Book and P/Tangible Book.*
| Risk Type | Specific Risk | Probability | Impact | Mitigant |
|-----------|--------------|-------------|--------|----------|
| Operational | | Low/Med/High | Low/Med/High | |
| Financial | High debt load, interest rate sensitivity | Low/Med/High | Low/Med/High | Strong cash flow generation, hedging strategies |
| Competitive | Intensifying competition, pricing pressure | Low/Med/High | Low/Med/High | Market leadership, cost advantages |
| Macro / Cyclical | Economic downturn affecting ad revenue | Low/Med/High | Low/Med/High | Diversified revenue streams |
| Regulatory / Legal | Changing regulations, antitrust concerns | Low/Med/High | Low/Med/High | Lobbying efforts, regulatory compliance |
| Earnings quality | From Step 4 summary | Low/Med/High | Low/Med/High | |

**Sector-specific risk considerations:**
- **Telecom/Media**: Cord-cutting trends, content licensing costs, spectrum auctions
- **High-debt companies**: Interest rate sensitivity, refinancing risk, covenant compliance
- **Example (Comcast)**: High debt load (~$90B) flagged as financial risk

Highlight any **red flags** (e.g., Owner Earnings payout >90%, FCF payout >90%, net debt/EBITDA >4x, accrual ratio >10%, CCR <60%, revenue concentration >40% in one customer, insider selling) with a ⚠️ marker.
## Important Notes

- **Owner Earnings is the primary DCF input**: FCF is a cross-check, not the base. Explain any gap >15% between the two.
- **ROIC–WACC spread constrains growth assumptions**: Do not model high growth at ROIC ≈ WACC. Inconsistent scenarios must be flagged or corrected.
- **Earnings quality gates valuation**: If Step 4 yields a Low quality rating, apply a haircut to Owner Earnings before DCF or widen the MoS threshold. Document the adjustment.
- **Dual-source verification**: Every key metric from at least 2 sources, or flagged as "single-source estimate".
- **Year-tagging is mandatory**: No number without a fiscal year or retrieval date.
- **Maintenance CapEx**: Disclose estimation method. Never silently use total capex as maintenance capex for growth companies.
- **Terminal value sensitivity**: Report TV as % of total DCF; show ±0.5% terminal growth sensitivity if TV > 70%.
- **Net Cash Bridge**: Always adjust DCF enterprise value to equity value per share.
- **Sector routing**: Activate Step 0 sector metrics before proceeding. No FCF-based DCF for banks.
- **Moat–ROIC consistency**: A Wide Moat claim must be supported by a positive ROIC-WACC spread. Resolve contradictions explicitly.
- **MoS is not fixed**: Scale the required margin of safety to moat width and earnings quality (see Step 10 framework).
- **No marketing language**: Describe mechanisms and present evidence. Let the analysis speak.
- **High-debt companies**: Pay special attention to interest coverage, debt maturity profile, and refinancing risk.
- **Capital-intensive industries**: Use depreciation as conservative proxy for maintenance capex when not separately disclosed.
- **Recent example**: See `/examples/CMCSA_Fair_Value_Analysis.md` for Comcast Corporation analysis

---

## Example Analyses

Full example implementations are available in the `/examples/` directory:

1. **Comcast Corporation (CMCSA)** - Communication Services / Telecom
   - Path: `/examples/CMCSA_Fair_Value_Analysis.md`
   - Key learnings: High debt load analysis, infrastructure moat assessment, capital-intensive maintenance capex estimation
   
Additional sector-specific examples will be added for:
- REITs (Real Estate Investment Trusts)
- Banks & Insurance companies
- Utilities & Regulated industries
- Capital-Light Software companies
- Cyclical / Capital-Heavy industries
