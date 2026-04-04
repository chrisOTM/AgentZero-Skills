---
name: "good-morning-trader"
description: "Daily pre-trading briefing skill for options sellers (short puts, calls, spreads, iron condors). Analyzes volatility dashboard, macro calendar, market sentiment, and technical analysis to provide actionable trading signals with stoplight ratings."
version: "1.0.0"
author: "TradingAssistant Project"
tags: ["trading", "options", "volatility", "morning-routine", "pre-market", "stillhalter", "vix", "sentiment"]
trigger_patterns:
  - "morning briefing"
  - "pre trading briefing"
  - "trading briefing"
  - "market analysis"
  - "marktanalyse"
  - "vix analysis"
  - "start trading day"
  - "trading routine"
  - "briefing"
  - "morgen analyse"
  - "trader briefing"
  - "options briefing"
allowed_tools: ["call_subordinate", "code_execution_tool", "search_engine", "document_query"]
---

# 🌅 Good Morning Trader – Daily Pre-Trading Briefing

## When to Use

This skill activates when the trader needs their complete morning routine briefing before starting the trading day. It provides a comprehensive analysis of all market factors relevant to option sellers (Stillhalter) trading short puts, calls, credit spreads, iron condors, and strangles/straddles on US markets (CBOE: SPX, SPY, NDX, QQQ, individual stocks) and European markets (Eurex: ODAX, OESX).

**Typical Activation:**
- Trader says "Good morning" or "Morgenroutine" or "Guten Morgen"
- Requests for "pre-trading briefing" or "morning analysis"
- Before market open to assess day conditions

---

## The Process

### Phase 1: Data Collection (yfinance Primary)

**PRIMARY METHOD: Use Python/yfinance script for reliable data**

Execute the market data collection script first:
```python
python /a0/usr/skills/good-morning-trader/scripts/market_data.py
```

This provides via yfinance (Yahoo Finance API):
- VIX spot with classification
- SPY technical levels (20/50/200 SMA)
- Global markets (Nikkei, DAX)
- Macro assets (10Y Treasury, Gold, Oil)
- Automatic Buying Power calculation

**SECONDARY METHOD: Researcher for sentiment/macro data**

For data not available via yfinance, delegate to researcher:
- VIX term structure (VIX9D, VIX3M, VIX6M) - check contango/backwardation
- VVIX, SKEW index
- CNN Fear & Greed Index
- CBOE Put/Call Ratios
- AAII Sentiment Survey
- Market breadth (% SPX > 50-MA/200-MA)
- Today's macro calendar (Fed speakers, economic data)
- Geopolitical risks

**Always cross-check critical levels with yfinance as primary source.**

---

### Phase 2: Structured Analysis

Analyze all data blocks sequentially. Each block ends with a clear stoplight recommendation.

#### BLOCK 1: VOLATILITY DASHBOARD

**VIX Classification:**
- < 18: Normal (green light for selling)
- 18–25: Elevated (yellow - wider strikes, smaller size)
- 25–35: Fear Zone (red - extreme caution, high assignment risk)
- > 35: Panic (red - consider buying volatility, not selling)

**Term Structure Analysis:**
- Contango (VIX9D < VIX < VIX3M < VIX6M): Normal, healthy for sellers
- Backwardation (inverted): Warning signal, near-term stress

**IV Rank/IV Percentile (50+ = attractive for sellers):**
- > 70: Excellent selling opportunities
- 50–70: Good
- 30–50: Marginal
- < 30: Avoid new positions

**ACTION RATING:** 🟢 Green Light / 🟡 Caution / 🔴 Stop

---

#### BLOCK 2: MACRO & ECONOMIC CALENDAR

**High-Impact Event Assessment:**
- FOMC decisions: 🔴 Avoid new positions
- Fed Chair speeches: 🟡 Avoid positions before event
- CPI/PCE inflation: 🔴 High volatility expected
- NFP (Non-Farm Payrolls): 🔴 Major market mover
- Earnings for held positions: Watch for IV crush opportunities

**Geopolitical Risk Check:**
- Oil prices > $100 halten: Belastung
- Handelskonflikte: Belastung
- Währungsbewegungen > 1% über Nacht: Risiko

**ACTION RATING:** 🟢 Normal Trading / 🟡 Reduced Activity / 🔴 No New Trades

---

#### BLOCK 3: MARKET SENTIMENT & BREADTH

**Sentiment Indicators:**

| Indicator | Bullish Signal | Bearish Signal |
|-----------|---------------|----------------|
| CNN Fear & Greed | 0–24 (Extreme Fear) = contrarian buy | 75–100 (Extreme Greed) = caution |
| AAII Bull-Bear Spread | < -10% = contrarian bullish | > +30% = caution |
| Put/Call Total | > 1.2 = fear/possible bottom | < 0.7 = complacency |

**Breadth Analysis:**
- % S&P 500 > 50-MA < 30%: Weak breadth, bear market characteristics
- Advance/Decline negative: Broad weakness confirms

**ACTION RATING:** 🟢 Favorable / 🟡 Mixed / 🔴 Unfavorable

---

#### BLOCK 4: TECHNICAL ANALYSIS

**SPX/SPY Multiple Timeframe:**

| Timeframe | Check Points |
|-----------|--------------|
| Weekly | Overall trend, major S/R levels |
| Daily | Position vs 20/50/200-SMA, trend structure |
| Intraday | Key levels, overnight gaps |

**Key Levels to Identify:**
- Previous day's high/low
- Overnight high/low
- Max Pain for current expiry
- Major gamma levels if available

**Trend Assessment:**
- Above 20/50/200-SMA: Bullish alignment 🟢
- Between SMAs: Mixed 🟡
- Below all SMAs: Bearish 🔴

**DAX Considerations:**
- Correlation to US futures (>0.85)
- European session leads US sometimes
- VDAX vs. VIX comparison

**Global Correlations:**
- 10Y Treasury Yield dropping: Risk-off (Flight to safety) 🔴
- Gold rising: Risk-off 🔴
- Oil spiking: Inflation pressure 🔴
- EUR/USD moving >1%: Currency risk for European traders

**ACTION RATING:** 🟢 Technicals Support Trades / 🟡 Neutral / 🔴 Technicals Warn

---

### Phase 3: Dashboard Summary & Final Verdict

**Create Stoplight Dashboard:**

| Category | Rating |
|----------|--------|
| Volatility Environment | 🟢🟡🔴 |
| Macro Risk Today | 🟢🟡🔴 |
| Market Sentiment | 🟢🟡🔴 |
| Technical Structure | 🟢🟡🔴 |
| New Trades Possible | 🟢🟡🔴 |

**OVERALL VERDICT:**
- 🟢 **Normal Trading Day**: Standard position sizing, normal strategies
- 🟡 **Caution Mode**: Reduce size by 25-50%, wider strikes, avoid events
- 🔴 **Management Only**: No new positions, manage existing, raise cash
- ⏸ **Trading Pause**: Close/existing positions only, high cash position

### Output Principles

**Keep all explanations concise:**
- Each ACTION rating: **One sentence maximum** (10-15 words)
- Verdict: **One sentence** summarizing the key factor
- Rationale: **One short phrase** per recommendation
- If user needs detail, they will ask for it

---


## Output Format

```markdown
# 🌅 GOOD MORNING TRADER – [DATE]

---

## BLOCK 1: VOLATILITY DASHBOARD

### VIX & Volatility Structure
| Indicator | Value | Assessment |
|-----------|-------|------------|
| VIX Spot | [X.XX] | [Range] |
| VIX9D | [X.XX] | - |
| VIX3M | [X.XX] | - |
| Term Structure | [Contango/Backwardation] | [Signal] |
| VVIX | [XXX.XX] | [Level] |
| SKEW Index | [XXX.XX] | [Tail Risk Assessment] |

**ACTION:** 🟢🟡🔴 [One-sentence recommendation]

---

## BLOCK 2: MACRO & CALENDAR

### Today's High-Impact Events
| Time (ET) | Event | Impact |
|-----------|-------|--------|
| [HH:MM] | [Event] | 🔴🟡🟢 |

### Geopolitical Risks
- [Risk factor 1]
- [Risk factor 2]

**ACTION:** 🟢🟡🔴 [One-sentence recommendation]

---

## BLOCK 3: SENTIMENT & BREADTH

| Indicator | Value | Interpretation |
|-----------|-------|----------------|
| CNN Fear & Greed | [X/100] | [Zone] |
| AAII Bull-Bear | [XX.X%] | [Signal] |
| Put/Call (Total) | [X.XX] | [Signal] |
| % SPX > 50-MA | [XX%] | [Breadth signal] |

**ACTION:** 🟢🟡🔴 [One-sentence recommendation]

---

## BLOCK 4: TECHNICAL ANALYSIS

### SPX Levels
| Level | Value | Significance |
|-------|-------|--------------|
| Current | [X,XXX] | - |
| 20-SMA | [X,XXX] | [Above/Below] |
| 50-SMA | [X,XXX] | [Above/Below] |
| 200-SMA | [X,XXX] | [Above/Below] |
| Key Support | [X,XXX] | [Critical/Major] |
| Key Resistance | [X,XXX] | [Critical/Major] |

### Overnight/Global
| Asset | Value | Signal |
|-------|-------|--------|
| 10Y Treasury | [X.XX%] | [Rising/Falling] |
| Gold | [$X,XXX] | [Safe haven flow] |
| Oil | $[XX.XX] | [Inflation pressure] |
| EUR/USD | [X.XXXX] | [Currency risk] |

**ACTION:** 🟢🟡🔴 [One-sentence recommendation]

---

# 🚦 DAILY DASHBOARD SUMMARY

| Category | Rating |
|----------|--------|
| Volatility | 🟢🟡🔴 |
| Macro Risk | 🟢🟡🔴 |
| Sentiment | 🟢🟡🔴 |
| Technical | 🟢🟡🔴 |
| **OVERALL** | **🟢🟡🔴** |

## Today's Trading Plan

**Verdict:** [One-sentence overall assessment]

### Specific Actions:
1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

### Scenario Planning:
| Scenario | Trigger | Action |
|----------|---------|--------|
| Bull | [Condition] | [Response] |
| Bear | [Condition] | [Response] |
| Base | [Condition] | [Response] |

**Next Check:** [Time/Condition for update]

*Trade safe, stay disciplined!* 📊🛡️
```

---

## Trading Rules Reference

### VIX-basierte Maximale Buying Power Allokation

| VIX-Spanne | Maximale Buying Power Allokation |
|------------|----------------------------------|
| 0–15 | 25% |
| 15–20 | 30% |
| 20–30 | 35% |
| 30–40 | 40% |
| >40 | 50% |

**Hinweis:** Höhere VIX-Werte erlauben höhere Allokation da die erwartete Rendite (höhere Prämien) das verbesserte Preisrisiko kompensieren. Bei niedrigem VIX (<15) ist die Prämie zu gering für das Risiko – daher nur 25% Buying Power nutzen.

### DTE Guidelines for Different VIX Zones

| VIX | Min DTE | Target DTE | Max DTE |
|-----|---------|------------|---------|
| < 15 | 30 | 45 | 60 |
| 15–25 | 45 | 60 | 80 |
| > 25 | Avoid new or 60+ | 60–80 | 90 |

---

## Example Interaction

**User:** "Good morning, I'm ready to trade"

**Agent Response:**
> # 🌅 Good Morning Trader!
>
> I'll prepare your complete pre-trading briefing. Let me gather all market data first...
>
> *[Delegates to researcher for data collection]*
>
> *[After receiving data, proceeds with 4-block analysis]*
>
> *[Presents structured briefing with stoplight ratings]*

---

## Tips for Best Results

### When GREEN LIGHT (🟢):
- Normal position sizing
- Standard strike selection (16-20 delta)
- Target 40-60 DTE
- Focus on high IV rank names (>50)

### When YELLOW LIGHT (🟡):
- Reduce position size by 25-50%
- Wider strikes, lower delta (12-16)
- Avoid high-event days
- Have exit plans ready
- Consider defined risk strategies (spreads vs. naked)

### When RED LIGHT (🔴):
- No new positions unless VIX > 35 (opportunity buying)
- Manage existing: adjust stops, take profits
- Raise cash position
- Focus on hedging existing positions
- Paper trade only or watchlist preparation

### Macro Event Rules:
- **Fed Days:** No new positions 2 hours before/after
- **NFP/CPI:** Flat or hedged before 8:30 ET
- **Earnings:** IV crush plays only, avoid new risk

---

## Sub-Agents

### researcher (Data Collection)
**Role:** Market data specialist  
**Task:** Gather all real-time market data for briefing  
**Profile:** researcher

---

## Files

### scripts/generate_briefing.py
Optional helper script to format calculations

### templates/
Optional templates for consistent output formatting

---

## Version History

| Version | Date | Changes |
|-----------|------|---------|
| 1.0.0 | 2026-03-30 | Initial release with 4-block structure |

---

*This skill is optimized for European-based option sellers trading US and European markets with focus on capital preservation and consistent premium income.*
