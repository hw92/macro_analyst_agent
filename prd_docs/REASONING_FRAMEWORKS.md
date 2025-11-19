# Reasoning Frameworks - Macro Analysis Chains

**Version**: 1.0
**Last Updated**: 2025-11-18
**Purpose**: Detailed reasoning frameworks for macro economic analysis

---

## Overview

This document provides **operational playbooks** for how the Macro AI Agent reasons about different types of macro events. These are the step-by-step analytical chains that transform data into insights.

---

## Table of Contents

1. [The 5-Question Framework](#the-5-question-framework)
2. [Causal Chain Analysis](#causal-chain-analysis)
3. [Macro Regime Classification](#macro-regime-classification)
4. [Portfolio Impact Mapping](#portfolio-impact-mapping)
5. [Event-Specific Frameworks](#event-specific-frameworks)
6. [Decision Trees](#decision-trees)

---

## The 5-Question Framework

### Core Structure

Every macro analysis follows these 5 questions in order:

```
1. What happened?
   ↓
2. Why does it matter?
   ↓
3. What's the macro regime?
   ↓
4. What's the portfolio impact?
   ↓
5. What are the action options?
```

### Question 1: What Happened?

**Objective**: State the facts clearly and precisely

**Process**:
1. Retrieve relevant data/documents
2. Identify the core event or data point
3. Provide context (vs expectations, vs prior, vs trend)
4. Cite source and date

**Template**:
```
[Indicator/Event] [action verb] to [value] [unit] in [time period],
[compared to] [prior value] and [vs expectations if available].

Source: [Source], [Date]
```

**Examples**:

✅ Good:
"The Consumer Price Index rose 0.4% month-over-month in February 2025, bringing the year-over-year rate to 3.2% (vs 3.1% in January and expectations of 3.0%). Source: BLS, March 12, 2025"

❌ Bad:
"Inflation went up last month" (too vague, no data, no source)

**Checklist**:
- [ ] Specific numbers provided
- [ ] Time period stated
- [ ] Comparison provided (vs prior, expectations, or trend)
- [ ] Source cited with date
- [ ] Units specified (%, points, index level, etc.)

---

### Question 2: Why Does It Matter?

**Objective**: Explain economic significance and causal implications

**Process**:
1. Assess magnitude (significant, modest, or negligible change?)
2. Identify causal channels (how does this affect other variables?)
3. Provide historical context (how does this compare to past episodes?)
4. Explain policy/market implications

**Framework**:

```
MAGNITUDE ASSESSMENT
├── Large move (>2 std deviations): "Significant..."
├── Moderate move (1-2 std dev): "Notable..."
└── Small move (<1 std dev): "Modest..."

CAUSAL CHANNELS
├── Direct effects (immediate, mechanical)
│   Example: Higher CPI → Real wages decline
└── Indirect effects (through policy/markets)
    Example: Higher CPI → Fed tightens → Rates rise → Valuations fall

HISTORICAL CONTEXT
├── Compare to recent trend (last 6-12 months)
├── Compare to long-term average
└── Compare to similar historical episodes
    Example: "This is similar to early 2022 when inflation first accelerated"

IMPLICATIONS
├── Policy response likely? (Fed, fiscal authority)
├── Market reaction expected? (repricing)
└── Economic impact? (growth, spending, investment)
```

**Template**:
```
This [magnitude] because:

1. **[Direct effect]**: [Explanation]
2. **[Policy implication]**: [How policymakers might respond]
3. **[Historical context]**: [Comparison to past]
4. **[Market significance]**: [Why markets care]

Causal chain: [A] → [B] → [C] → [D]
```

**Example**:

✅ Good:
"This re-acceleration in inflation is **significant** because:

1. **Sticky services inflation**: Core services (ex-housing) remain at 4.2% YoY, showing inflation is broadening beyond just goods
2. **Fed policy implication**: This likely keeps the Fed on hold through Q2, delaying rate cut expectations from June to September
3. **Historical context**: Similar to early 2022, when inflation proved more persistent than expected, leading to aggressive tightening
4. **Market significance**: Bond yields will likely rise as rate cut bets are pushed out

Causal chain: Persistent inflation → Fed stays hawkish → Rate cuts delayed → Bond prices fall"

❌ Bad:
"This is bad for stocks" (no explanation of why or how)

---

### Question 3: What's the Macro Regime?

**Objective**: Classify the current macro environment across 4 dimensions

**Dimensions**:

```
1. INFLATION TREND
   ├── Rising (accelerating)
   ├── Falling (disinflating/deflating)
   ├── Stable (oscillating around target)
   └── Uncertain (mixed signals)

2. GROWTH TRAJECTORY
   ├── Expanding (above trend, accelerating)
   ├── Solid (at trend)
   ├── Slowing (decelerating but positive)
   ├── Contracting (recession)
   └── Uncertain (conflicting data)

3. POLICY STANCE
   ├── Tightening (raising rates, QT)
   ├── Easing (cutting rates, QE)
   ├── Neutral (on hold, data-dependent)
   └── Mixed (fiscal vs monetary divergence)

4. RISK SENTIMENT
   ├── Risk-on (low VIX, tight spreads, strong flows)
   ├── Risk-off (high VIX, wide spreads, defensive)
   ├── Neutral (mixed signals)
   └── Transitioning (regime shifting)
```

**Process**:
1. Retrieve recent data for each dimension
2. Classify each dimension
3. Synthesize into regime label
4. Identify regime transitions

**Classification Logic**:

**Inflation:**
- Rising: CPI trend accelerating (3-month MA > 6-month MA)
- Falling: CPI trend decelerating
- Stable: CPI oscillating within 0.5pp of target
- Uncertain: Conflicting signals (headline vs core diverging)

**Growth:**
- Expanding: GDP growth > potential (2%+), accelerating
- Solid: GDP at potential, stable
- Slowing: GDP growth positive but decelerating
- Contracting: GDP growth negative (recession)

**Policy:**
- Tightening: Fed raising rates or reducing balance sheet
- Easing: Fed cutting rates or expanding balance sheet
- Neutral: Fed on hold, "data-dependent"
- Mixed: Fiscal and monetary policy diverging

**Risk Sentiment:**
- Risk-on: VIX < 15, credit spreads tight, strong equity flows
- Risk-off: VIX > 25, widening spreads, defensive flows
- Neutral: VIX 15-25, mixed flows
- Transitioning: Volatility picking up, flows reversing

**Regime Labels**:

Combine dimensions into regime:

```
Examples:
• "Late-cycle, sticky inflation, Fed on hold, cautious markets"
• "Mid-cycle expansion, inflation normalizing, Fed paused, risk-on"
• "Early recession, deflation risk, Fed easing, risk-off"
• "Stagflation, inflation rising, growth slowing, policy dilemma"
```

**Template**:
```
📈 MACRO REGIME

Current assessment:
• Inflation: [rising/falling/stable] ([current %], [trend])
• Growth: [expanding/slowing/contracting] ([GDP % or proxy])
• Policy: [tightening/easing/neutral] ([Fed stance])
• Risk Sentiment: [risk-on/off/neutral] ([VIX or credit spreads])

**Regime Label**: [Descriptive label]

**Regime Dynamics**: [Is this stable or transitioning? What could change it?]
```

---

### Question 4: What's the Portfolio Impact?

**Objective**: Map macro regime to specific asset class implications

**Framework**: Asset Class Impact Matrix

```
EQUITIES
├── Direction: [Positive/Negative/Neutral/Mixed]
├── Magnitude: [Large/Moderate/Small]
├── Time Horizon: [Immediate/Medium-term/Long-term]
├── Sector Breakdown:
│   ├── Cyclicals (consumer disc, industrials): [Impact]
│   ├── Defensives (utilities, staples, healthcare): [Impact]
│   ├── Financials: [Impact]
│   ├── Tech: [Impact]
│   └── Energy/Commodities: [Impact]
└── Style Factors:
    ├── Growth vs Value: [Which favored?]
    ├── Large vs Small Cap: [Which favored?]
    └── Quality vs High Beta: [Which favored?]

FIXED INCOME
├── Direction: [Positive/Negative/Neutral]
├── Duration Impact:
│   ├── Short-term (1-3Y): [Impact]
│   ├── Intermediate (5-7Y): [Impact]
│   └── Long-term (10Y+): [Impact]
├── Credit:
│   ├── Investment Grade: [Impact]
│   └── High Yield: [Impact]
├── Inflation-Linked: [TIPS impact]
└── Yield Curve: [Steepening/Flattening/Twisting]

ALTERNATIVES
├── Commodities: [Impact, which ones?]
├── Gold: [Impact]
├── Real Estate: [Impact]
└── Crypto (if relevant): [Impact]

CURRENCIES
├── USD: [Strengthening/Weakening]
└── Key pairs: [EUR/USD, USD/JPY, etc.]

CASH
└── Attractiveness: [Increasing/Decreasing]
```

**Causal Logic by Macro Event**:

**Inflation Rising:**
- Equities: Negative (multiple compression from higher rates)
  - Value > Growth (lower valuations more resilient)
  - Commodities, energy: Positive (inflation beneficiaries)
- Bonds: Negative (yields rise, prices fall)
  - Short duration > Long duration
  - TIPS > Nominal (inflation protection)
- Gold: Positive (inflation hedge, real rate watch)

**Growth Slowing:**
- Equities: Negative (earnings pressure)
  - Defensives > Cyclicals
  - Quality > High beta
  - Large cap > Small cap
- Bonds: Positive (rate cut expectations, safe haven)
  - Long duration > Short (benefit from falling yields)
  - Investment grade > High yield (credit quality matters)
- Gold: Positive (safe haven, Fed easing)

**Fed Tightening:**
- Equities: Negative (higher discount rates)
  - Financials: Positive initially (NIM expansion)
  - Tech: Negative (long-duration growth hit hardest)
- Bonds: Negative (yields rise)
- USD: Positive (higher rates attract capital)

**Risk-Off:**
- Equities: Negative (deleveraging, selling)
  - Defensives > Cyclicals
  - Quality > Junk
- Bonds: Positive (safe haven bid)
  - Treasuries > Credit
- Gold: Positive (safe haven)
- USD, JPY: Positive (safe haven currencies)

**Template**:
```
🎯 PORTFOLIO IMPACT

**Equities**: [Direction] ([Rationale])
• Sectors: [Which benefit, which suffer]
• Styles: [Growth vs Value, Large vs Small, etc.]
• Expected magnitude: [X%]

**Fixed Income**: [Direction] ([Rationale])
• Duration: [Short/Int/Long impact]
• Credit: [IG vs HY spread dynamics]
• Expected magnitude: [X bps yield move]

**Alternatives**: [Impact on commodities, gold, real estate]

**Currencies**: [USD direction, key pairs]

**Cash**: [Relative attractiveness]

**Time Horizon**: [Immediate, weeks, months]

**Conviction**: [High/Medium/Low]
```

---

### Question 5: What Are the Action Options?

**Objective**: Generate 1-3 specific, actionable portfolio adjustments

**Framework**:

```
ACTION GENERATION PROCESS

Step 1: Identify macro-driven risks in user's portfolio
├── Check portfolio composition (get_user_portfolio)
├── Map to macro impacts (from Q4 analysis)
└── Prioritize by magnitude and likelihood

Step 2: Generate action candidates
├── Defensive moves (reduce risk)
├── Offensive moves (capture opportunity)
└── Hedging moves (protect downside while maintaining upside)

Step 3: Filter by user risk profile
├── Conservative: Focus on defense, capital preservation
├── Moderate: Balanced between defense and opportunity
└── Aggressive: More willing to take tactical risk

Step 4: Rank and select top 1-3
├── Highest expected benefit
├── Clear implementation
└── Reasonable risk/reward
```

**Action Template**:

```
### [Action Title]

**What to do**: [Specific, implementable action]

**Rationale**: [Why this makes sense given macro analysis]

**Implementation**:
• Step 1: [Concrete step]
• Step 2: [Concrete step]
• Timing: [When to execute]
• Example: [Specific ETFs, funds, or allocation %]

**Expected impact**:
• [What this achieves for portfolio]
• [Quantify if possible]

**Risks**:
• [What could go wrong]
• [Scenarios where this backfires]

**Suitable for**: [Risk profile]

**Conviction**: [High/Medium/Low]
```

**Action Categories**:

1. **Duration Management** (bonds)
   - Reduce duration (expect rising rates)
   - Extend duration (expect falling rates)
   - Barbell strategy (short + long, avoid middle)

2. **Equity Style Rotation**
   - Growth → Value (rising rates)
   - Value → Growth (falling rates, expansion)
   - Large → Small (risk-on, growth accelerating)
   - Cyclicals → Defensives (growth slowing)

3. **Sector Rotation**
   - Tech → Financials (rising rates)
   - Cyclicals → Defensives (recession risk)
   - Energy → Other (oil prices falling)

4. **Asset Class Rebalancing**
   - Stocks → Bonds (risk-off)
   - Bonds → Stocks (risk-on)
   - Increase cash (uncertainty)

5. **Geographic Rotation**
   - US → International (dollar weakening)
   - Developed → Emerging (risk-on, growth)

6. **Inflation Protection**
   - Add TIPS (inflation rising)
   - Add commodities (inflation, supply shocks)
   - Add gold (monetary debasement, uncertainty)

7. **Quality/Defensive Tilt**
   - Low volatility, high quality (uncertainty)
   - Dividend stocks (income seekers, defensives)

**Risk Considerations for Each Action**:
- What assumptions must hold true?
- What could invalidate the thesis?
- What is the downside scenario?
- Are there implementation risks (liquidity, costs, taxes)?

---

## Causal Chain Analysis

### The Transmission Mechanism

Understanding how macro events flow through the economy and into markets:

```
INFLATION SHOCK (e.g., CPI rises unexpectedly)
↓
Central Bank Response
├── If transitory → Wait and see
└── If persistent → Tighten policy
    ↓
    Interest Rates Rise
    ↓
    ┌─────────────┬─────────────┬─────────────┐
    ↓             ↓             ↓             ↓
Economic     Bond Prices   Equity        Currency
Impact       Fall          Valuations    Strengthens
│            │             Fall          │
↓            ↓             │             ↓
Slower       Losses for    ↓             EM Pressure
Growth       Bondholders   Lower         Capital
│                          Multiples     Outflows
↓                          │
Weaker                     ↓
Earnings                   Sector Rotation
                           (Growth → Value)
```

### Key Causal Chains

**1. Monetary Transmission**
```
Fed raises rates
→ Bank lending rates increase
→ Borrowing costs rise for consumers/businesses
→ Less consumption and investment
→ Slower economic growth
→ Lower inflation (eventually)
→ Weaker corporate earnings
→ Stock prices fall
```

**2. Fiscal Transmission**
```
Government increases spending
→ More demand in economy
→ Potential inflationary pressure
→ Higher growth (short-term)
→ Higher deficits
→ More bond issuance
→ Upward pressure on yields
→ Potential crowding out of private investment
```

**3. Dollar Strength Chain**
```
Fed hawkish / Rate differential widens
→ USD strengthens
→ US exports less competitive
→ Foreign imports cheaper (disinflationary)
→ EM currencies weaken
→ EM debt stress (USD-denominated debt)
→ Risk-off sentiment
→ Capital flows from EM to US
```

**4. Yield Curve Dynamics**
```
Short rates rise (Fed tightens)
+ Long rates fall/stable (growth concerns)
→ Yield curve flattens / inverts
→ Banks squeezed (borrow short, lend long)
→ Credit tightening
→ Recession signal
→ Risk-off
```

**5. Risk-On / Risk-Off Toggle**
```
RISK-ON Triggers:
• Fed easing
• Strong growth data
• Low VIX
• Positive earnings
→ Flows into equities, EM, high yield, commodities
→ Out of Treasuries, gold, safe havens

RISK-OFF Triggers:
• Geopolitical shocks
• Growth scares
• Financial stress
• High volatility
→ Flows into Treasuries, gold, USD, JPY
→ Out of equities, EM, high yield
```

---

## Macro Regime Classification

### Regime Matrix

Combine inflation × growth to get macro regime:

```
                    INFLATION
                Rising  |  Falling
            ┌─────────┴─────────┐
   Expanding│ Overheating  Mid-cycle
   GROWTH   │ (Stagflation risk)│
            ├──────────┼─────────┤
 Contracting│ Stagflation   Deflation
            │ (Worst)   │ (Recession)
            └──────────┴─────────┘
```

**Regime Characteristics**:

**1. Mid-Cycle (Goldilocks)**
- Inflation: Falling or stable near target
- Growth: Expanding at trend
- Policy: Neutral / data-dependent
- Assets: Risk-on, equities favored
- Best for: Balanced portfolios

**2. Overheating**
- Inflation: Rising above target
- Growth: Expanding above trend
- Policy: Tightening
- Assets: Value > Growth, commodities up
- Best for: Real assets, short duration

**3. Stagflation**
- Inflation: Rising
- Growth: Contracting or weak
- Policy: Dilemma (ease for growth or tighten for inflation?)
- Assets: Difficult environment, commodities/TIPS/gold
- Worst for: Equities and bonds (both hurt)

**4. Deflation / Recession**
- Inflation: Falling, potentially negative
- Growth: Contracting
- Policy: Easing aggressively
- Assets: Bonds rally, equities weak, defensives outperform
- Best for: High-quality bonds, cash

---

## Decision Trees

### Example: Fed Rate Decision Analysis

```
Fed announces rate decision
│
├─ Rate CUT?
│  ├─ Yes
│  │  ├─ Was it expected?
│  │  │  ├─ Yes → Neutral (priced in)
│  │  │  └─ No → Risk-on (dovish surprise)
│  │  │     → Bonds rally, stocks up, USD down
│  │  │
│  │  └─ What's the reason?
│  │     ├─ Insurance cut (economy OK) → Mild positive
│  │     ├─ Growth concerns → Mixed (bonds up, stocks cautious)
│  │     └─ Financial stress → Risk-off initially
│  │
│  ├─ Rate HIKE?
│  │  ├─ Was it expected?
│  │  │  ├─ Yes → Neutral (priced in)
│  │  │  └─ No → Risk-off (hawkish surprise)
│  │  │     → Bonds fall, stocks down, USD up
│  │  │
│  │  └─ How hawkish is guidance?
│  │     ├─ "Data-dependent" → Moderate impact
│  │     ├─ "More hikes likely" → Large impact
│  │     └─ "Peak rates" → Relief rally
│  │
│  └─ HOLD?
│     ├─ Guidance matters most
│     │  ├─ Hawkish hold ("higher for longer") → Negative
│     │  │  → Push out cut expectations
│     │  ├─ Neutral hold ("data-dependent") → Range-bound
│     │  └─ Dovish hold ("close to cuts") → Positive
│     │     → Pull forward cut expectations
│     │
│     └─ Economic Assessment?
│        ├─ Upgraded growth → Hawkish tilt
│        ├─ Downgraded growth → Dovish tilt
│        ├─ Upgraded inflation → Hawkish
│        └─ Downgraded inflation → Dovish
```

---

## Next Steps

1. **Implement** these frameworks in agent reasoning logic
2. **Test** on historical events to validate
3. **Refine** based on performance
4. **Document** edge cases and exceptions
5. **Update** as macro environment evolves

---

**These frameworks turn macro analysis from art into science—repeatable, structured, and rigorous.** 📊🧠
