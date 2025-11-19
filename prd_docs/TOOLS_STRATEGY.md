# Tools Strategy - Macro AI Economist Agent

**Version**: 1.0
**Last Updated**: 2025-11-18
**Purpose**: Define the tool ecosystem for the AI economist agent

---

## Table of Contents

1. [Overview](#overview)
2. [Tool Design Philosophy](#tool-design-philosophy)
3. [Core Tools Suite](#core-tools-suite)
4. [Tool Categories](#tool-categories)
5. [Tool Schemas](#tool-schemas)
6. [Tool Usage Patterns](#tool-usage-patterns)
7. [Error Handling & Reliability](#error-handling--reliability)
8. [Tool Orchestration](#tool-orchestration)
9. [Testing Strategy](#testing-strategy)
10. [Future Tools](#future-tools)

---

## Overview

### The Challenge

An LLM alone cannot:
- Access current economic data
- Retrieve specific documents from a knowledge base
- Query time-series databases
- Understand user's portfolio composition
- Execute complex multi-step analysis

### The Solution

**A curated suite of tools that give the AI economist "superpowers":**

```
LLM Brain + Tools = AI Economist
    ↓
LLM provides reasoning, tools provide facts
```

### Design Principles

```yaml
principles:
  focused: "Each tool does ONE thing well"
  reliable: "Fail gracefully with clear error messages"
  composable: "Tools work together for complex workflows"
  discoverable: "Clear names and descriptions"
  safe: "Read-only by default, validate inputs"
  fast: "Optimized for <2 second response times"
```

---

## Tool Design Philosophy

### Single Responsibility Principle

Each tool has ONE clear purpose:

✅ Good: `get_time_series(indicator, country, window)` - Retrieves economic data
❌ Bad: `get_macro_data()` - Too vague, does everything

### Composability Over Complexity

Prefer multiple simple tools over one complex tool:

```python
# ✅ Good: Composable
retrieve_documents("Fed policy", k=5)
get_time_series("DFF", "us", "12m")
query_macro_ontology("monetary_policy")

# ❌ Bad: One mega-tool
get_everything_about_fed()  # Does too much, hard to control
```

### Explicit Over Implicit

Tool parameters should be explicit:

```python
# ✅ Good: Explicit
get_time_series(indicator="CPIAUCSL", country="us", window="12m")

# ❌ Bad: Implicit
get_inflation_data()  # Which country? Time window? Indicator?
```

### Progressive Disclosure

Start simple, add complexity when needed:

```python
# MVP: Simple
retrieve_documents(query: str, k: int)

# V2: Add filters
retrieve_documents(
    query: str,
    k: int,
    filters: Optional[dict]  # {"themes": ["inflation"], "after": "2024-01-01"}
)

# V3: Add ranking
retrieve_documents(
    query: str,
    k: int,
    filters: Optional[dict],
    ranking_strategy: str = "hybrid"  # "semantic", "keyword", "hybrid"
)
```

---

## Core Tools Suite

### MVP Tools (5 Essential)

These 5 tools are sufficient for a functional macro economist:

```
1. retrieve_documents      → Get macro news/research/policy
2. get_time_series         → Get economic data (CPI, GDP, etc.)
3. query_macro_ontology    → Understand concept relationships
4. get_user_portfolio      → Know user's holdings/risk
5. suggest_actions         → Generate portfolio actions
```

### Why These 5?

```
User Query
    ↓
retrieve_documents      ← Context about events
get_time_series         ← Current data
    ↓
Agent Reasoning (with ontology)
    ↓
query_macro_ontology    ← Causal relationships
get_user_portfolio      ← Personalization context
    ↓
suggest_actions         ← Generate options
    ↓
Response with Actions
```

---

## Tool Categories

### 1. Retrieval Tools (Get Information)

**Purpose**: Retrieve documents and context

#### `retrieve_documents`

**What it does**: Semantic search over macro knowledge base

**When to use**:
- User asks about recent events ("What did the Fed say?")
- Need context about a macro topic
- Looking for research or analysis

**Returns**: List of relevant documents with content and metadata

**Design**:
```python
def retrieve_documents(
    query: str,
    k: int = 5,
    filters: Optional[dict] = None
) -> List[Document]:
    """
    Retrieve documents from vector database.

    Args:
        query: Search query (e.g., "Fed rate decision March 2025")
        k: Number of results (default 5, max 20)
        filters: Optional filters
            - themes: List[str] (e.g., ["inflation", "monetary_policy"])
            - after_date: str (ISO format)
            - before_date: str
            - source: List[str] (e.g., ["Bloomberg", "FOMC"])
            - importance: str ("high", "medium", "low")

    Returns:
        List of documents with:
        - content: Full text
        - title: Document title
        - source: Source name
        - published_at: Publication date
        - relevance_score: 0-1 similarity score
        - metadata: Additional context
    """
```

**Example usage**:
```python
# Simple query
docs = retrieve_documents("latest CPI report", k=3)

# With filters
docs = retrieve_documents(
    query="Fed policy stance",
    k=5,
    filters={
        "themes": ["monetary_policy"],
        "after_date": "2025-01-01",
        "importance": "high"
    }
)
```

---

### 2. Data Tools (Get Numbers)

**Purpose**: Retrieve quantitative economic data

#### `get_time_series`

**What it does**: Fetch economic indicators from time-series database

**When to use**:
- Need current data (latest CPI, unemployment, etc.)
- Want to show trends over time
- Need to verify claims with data

**Returns**: Time series data with metadata

**Design**:
```python
def get_time_series(
    indicator: str,
    country: str = "us",
    window: str = "12m",
    frequency: Optional[str] = None
) -> TimeSeriesData:
    """
    Fetch economic time series.

    Args:
        indicator: Indicator code
            Examples: "CPIAUCSL" (CPI), "UNRATE" (unemployment),
                     "DFF" (Fed Funds), "GDP" (GDP)
        country: Country code (default "us")
            Options: "us", "eu", "cn", "jp", "uk", "global"
        window: Time window
            Options: "1m", "3m", "6m", "12m", "24m", "5y", "10y", "ytd", "all"
        frequency: Override frequency ("monthly", "quarterly", "daily")

    Returns:
        TimeSeriesData with:
        - dates: List[datetime]
        - values: List[float]
        - metadata:
            - name: Full indicator name
            - units: Units (%, index, etc.)
            - frequency: Data frequency
            - last_updated: Last update timestamp
            - source: Data source (FRED, BLS, etc.)
        - statistics:
            - latest: Most recent value
            - change_mom: Month-over-month change
            - change_yoy: Year-over-year change
            - min/max/mean over window
    """
```

**Example usage**:
```python
# Get CPI for last year
cpi = get_time_series("CPIAUCSL", "us", "12m")
print(f"Latest CPI: {cpi.statistics.latest}%")
print(f"YoY change: {cpi.statistics.change_yoy}%")

# Get Fed Funds rate
fed_funds = get_time_series("DFF", "us", "24m")

# Get GDP
gdp = get_time_series("GDP", "us", "5y", frequency="quarterly")
```

**Indicator Catalog** (built-in):
```python
INDICATORS = {
    # Inflation
    "CPIAUCSL": "Consumer Price Index",
    "CPILFESL": "Core CPI (ex food & energy)",
    "PCEPI": "PCE Price Index",

    # Employment
    "UNRATE": "Unemployment Rate",
    "PAYEMS": "Nonfarm Payrolls",

    # Rates
    "DFF": "Federal Funds Rate",
    "DGS10": "10-Year Treasury Rate",

    # Growth
    "GDP": "Gross Domestic Product",
    "GDPC1": "Real GDP",

    # And 40+ more...
}
```

---

### 3. Knowledge Tools (Get Concepts)

**Purpose**: Access structured macro knowledge

#### `query_macro_ontology`

**What it does**: Look up concept relationships in the macro ontology

**When to use**:
- Need to explain causal relationships
- Want to understand how concepts connect
- Looking for asset class impacts

**Returns**: Concept definition and relationships

**Design**:
```python
def query_macro_ontology(
    concept: str,
    depth: int = 1
) -> ConceptGraph:
    """
    Query macro concept ontology.

    Args:
        concept: Macro concept
            Examples: "inflation", "fed_tightening", "risk_on",
                     "yield_curve_inversion"
        depth: Relationship depth (1 = direct, 2 = second-order)

    Returns:
        ConceptGraph with:
        - definition: Plain English explanation
        - category: Type (indicator, policy, regime, market)
        - causes: What drives this concept
        - effects: What this concept drives
        - related: Related concepts
        - asset_impacts:
            - equities: Impact and reasoning
            - bonds: Impact and reasoning
            - commodities: Impact and reasoning
            - fx: Impact and reasoning
        - examples: Historical examples
    """
```

**Example usage**:
```python
# Understand inflation impacts
inflation = query_macro_ontology("inflation")
print(inflation.definition)
print(inflation.effects)  # → ["rate_hikes", "bond_yields_rise", ...]
print(inflation.asset_impacts.bonds)  # → "Negative: rising yields..."

# Understand Fed tightening
tightening = query_macro_ontology("fed_tightening")
print(tightening.causes)  # → ["inflation", "overheating"]
print(tightening.effects)  # → ["higher_rates", "stronger_dollar", ...]
```

**Ontology Structure**:
```yaml
inflation:
  definition: "Rate of increase in price levels over time"
  category: "indicator"
  causes:
    - demand_exceeding_supply
    - money_supply_growth
    - supply_shocks
  effects:
    - central_bank_tightening
    - higher_interest_rates
    - currency_strength
  asset_impacts:
    equities: "Negative: Higher rates reduce valuations"
    bonds: "Negative: Yields rise, prices fall"
    commodities: "Positive: Inflation hedge"
    gold: "Positive: Store of value"
  related:
    - fed_policy
    - yield_curve
    - real_rates
```

---

### 4. User Context Tools (Get Personalization)

**Purpose**: Understand user's situation

#### `get_user_portfolio`

**What it does**: Retrieve user's portfolio and preferences

**When to use**:
- Generating personalized recommendations
- Understanding user's exposure to risks
- Tailoring communication to risk level

**Returns**: Portfolio composition and user profile

**Design**:
```python
def get_user_portfolio(
    user_id: str
) -> UserPortfolio:
    """
    Get user's portfolio and profile.

    Args:
        user_id: User identifier

    Returns:
        UserPortfolio with:
        - holdings: Dict of asset allocations
            - equities: % and breakdown
            - bonds: % and duration
            - alternatives: % and types
            - cash: %
        - total_value: Total portfolio value
        - risk_profile: "conservative", "moderate", "aggressive"
        - investment_horizon: "short" (<3y), "medium" (3-10y), "long" (10y+)
        - preferences:
            - themes_interested: List[str]
            - geography_focus: List[str]
            - income_needs: bool
        - constraints:
            - max_single_position: %
            - liquidity_needs: $
            - tax_considerations: str
    """
```

**Example usage**:
```python
portfolio = get_user_portfolio("user_12345")

print(f"Risk: {portfolio.risk_profile}")
print(f"Stocks: {portfolio.holdings.equities}%")
print(f"Bonds: {portfolio.holdings.bonds}%")

# Tailor advice to risk
if portfolio.risk_profile == "conservative":
    # Focus on capital preservation
elif portfolio.risk_profile == "aggressive":
    # Can suggest more tactical moves
```

---

### 5. Action Tools (Generate Recommendations)

**Purpose**: Generate portfolio action suggestions

#### `suggest_actions`

**What it does**: Map macro regime to portfolio adjustments

**When to use**:
- After analyzing macro regime
- When user asks "what should I do?"
- Generating briefing recommendations

**Returns**: List of actionable portfolio adjustments

**Design**:
```python
def suggest_actions(
    macro_regime: str,
    portfolio: dict,
    risk_level: str,
    max_actions: int = 3
) -> List[Action]:
    """
    Generate portfolio action suggestions.

    Args:
        macro_regime: Current macro regime
            Examples: "inflation_rising_hawkish_fed",
                     "growth_slowing_neutral_policy"
        portfolio: User's portfolio composition
        risk_level: "conservative", "moderate", "aggressive"
        max_actions: Maximum number of suggestions (default 3)

    Returns:
        List of Actions with:
        - action: What to do (concise)
        - rationale: Why this makes sense
        - implementation: Specific steps
        - expected_impact: What this achieves
        - risks: What could go wrong
        - suitability: Which risk profiles this fits
        - conviction: "high", "medium", "low"
        - timing: "immediate", "over_weeks", "opportunistic"
    """
```

**Example usage**:
```python
actions = suggest_actions(
    macro_regime="inflation_sticky_fed_hawkish",
    portfolio={"equities": 60, "bonds": 30, "cash": 10},
    risk_level="moderate",
    max_actions=3
)

for action in actions:
    print(f"\n{action.action}")
    print(f"Rationale: {action.rationale}")
    print(f"Risks: {action.risks}")
```

**Regime-to-Action Mappings** (examples):
```python
REGIME_ACTIONS = {
    "inflation_rising_hawkish_fed": [
        "reduce_duration",
        "rotate_value",
        "add_tips",
        "increase_commodities"
    ],
    "growth_slowing_neutral_policy": [
        "defensive_tilt",
        "quality_bias",
        "reduce_cyclicals",
        "extend_duration"
    ],
    "risk_off": [
        "increase_cash",
        "reduce_high_beta",
        "add_gold",
        "flight_to_quality"
    ]
}
```

---

## Tool Schemas

### LangChain Tool Format

For integration with LangChain/LangGraph:

```python
from langchain.tools import Tool
from pydantic import BaseModel, Field

# Pydantic input schema
class RetrieveDocumentsInput(BaseModel):
    query: str = Field(description="Search query for macro documents")
    k: int = Field(default=5, description="Number of documents to retrieve")
    filters: Optional[dict] = Field(default=None, description="Optional filters")

# Tool definition
retrieve_documents_tool = Tool(
    name="retrieve_documents",
    description="""Retrieve the most relevant macro/economy documents from the knowledge base.

    Use this to:
    • Find news articles about recent macro events
    • Retrieve policy statements (FOMC, ECB, etc.)
    • Access research reports and analysis

    When to use:
    • User asks about recent events ("What did the Fed say?")
    • You need context about macro developments
    • Looking for analysis or commentary
    """,
    func=retrieve_documents,
    args_schema=RetrieveDocumentsInput
)
```

### OpenAI Function Calling Format

For OpenAI-compatible agents:

```json
{
  "name": "retrieve_documents",
  "description": "Retrieve the most relevant macro/economy documents from the knowledge base using semantic search.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search query (e.g., 'Fed rate decision March 2025')"
      },
      "k": {
        "type": "integer",
        "description": "Number of documents to retrieve",
        "default": 5,
        "minimum": 1,
        "maximum": 20
      },
      "filters": {
        "type": "object",
        "description": "Optional filters",
        "properties": {
          "themes": {"type": "array", "items": {"type": "string"}},
          "after_date": {"type": "string", "format": "date"},
          "source": {"type": "array", "items": {"type": "string"}}
        }
      }
    },
    "required": ["query"]
  }
}
```

---

## Tool Usage Patterns

### Pattern 1: Data Verification

**Scenario**: User asks about current data

**Flow**:
```
User: "What's the latest inflation number?"
    ↓
Agent: get_time_series("CPIAUCSL", "us", "3m")
    ↓
Agent: [analyzes data]
    ↓
Response: "According to BLS, CPI is 3.2% YoY as of February..."
```

**Key**: ALWAYS retrieve data before citing numbers

---

### Pattern 2: Event Context

**Scenario**: User asks about a macro event

**Flow**:
```
User: "What did the Fed announce today?"
    ↓
Agent: retrieve_documents("Fed FOMC statement today", k=3)
    ↓
Agent: get_time_series("DFF", "us", "12m")  # Check rate decision
    ↓
Agent: query_macro_ontology("fed_tightening")  # Understand implications
    ↓
Response: [Structured analysis with context + data + impacts]
```

**Key**: Combine retrieval + data + concepts for complete analysis

---

### Pattern 3: Personalized Recommendations

**Scenario**: User wants portfolio advice

**Flow**:
```
User: "What should I do given rising inflation?"
    ↓
Agent: get_time_series("CPIAUCSL", "us", "12m")  # Verify inflation
    ↓
Agent: get_user_portfolio(user_id)  # Get context
    ↓
Agent: query_macro_ontology("inflation")  # Understand impacts
    ↓
Agent: suggest_actions(
    macro_regime="inflation_rising",
    portfolio=portfolio,
    risk_level=portfolio.risk_profile
)
    ↓
Response: [3 personalized actions with rationale]
```

**Key**: Personalize based on actual portfolio + risk profile

---

### Pattern 4: Multi-Step Analysis

**Scenario**: Complex question requiring multiple tools

**Flow**:
```
User: "Is the yield curve inversion predicting a recession?"
    ↓
Agent: get_time_series("T10Y2Y", "us", "24m")  # Get spread
    ↓
Agent: retrieve_documents("yield curve inversion recession", k=5)
    ↓
Agent: query_macro_ontology("yield_curve_inversion")
    ↓
Agent: get_time_series("UNRATE", "us", "12m")  # Check employment
    ↓
Agent: [Synthesize multiple data sources]
    ↓
Response: [Comprehensive analysis with historical context]
```

**Key**: Use multiple tools to triangulate answer

---

## Error Handling & Reliability

### Error Types

```python
class ToolError(Exception):
    """Base class for tool errors"""
    pass

class DataNotFoundError(ToolError):
    """Requested data doesn't exist"""
    pass

class InvalidParameterError(ToolError):
    """Invalid tool parameters"""
    pass

class RateLimitError(ToolError):
    """API rate limit exceeded"""
    pass

class TimeoutError(ToolError):
    """Tool execution timeout"""
    pass
```

### Graceful Degradation

**Principle**: Never fail silently, always provide context

```python
def get_time_series(indicator: str, country: str, window: str):
    try:
        data = fetch_from_database(indicator, country, window)
        if not data:
            raise DataNotFoundError(
                f"No data found for {indicator} in {country}. "
                f"Available indicators: {list_available_indicators()}"
            )
        return data

    except TimeoutError:
        return {
            "error": "Timeout fetching data",
            "fallback": "Last cached data from [date]",
            "cached_data": get_cached_data(indicator)
        }

    except RateLimitError:
        return {
            "error": "Rate limit exceeded",
            "retry_after": "60 seconds",
            "alternative": "Use cached data or retry later"
        }
```

### Tool Response Format

**Standard Response**:
```python
{
    "success": True,
    "data": {...},
    "metadata": {
        "execution_time_ms": 234,
        "cached": False,
        "source": "database",
        "timestamp": "2025-11-18T10:30:00Z"
    }
}
```

**Error Response**:
```python
{
    "success": False,
    "error": {
        "type": "DataNotFoundError",
        "message": "Indicator INVALID not found",
        "suggestion": "Available indicators: CPIAUCSL, UNRATE, GDP",
        "recoverable": True
    },
    "fallback": {
        "available": True,
        "data": "Last cached data from 2025-11-17"
    }
}
```

---

## Tool Orchestration

### Sequential Tool Use

Tools called one after another:

```python
# Step 1: Get context
docs = retrieve_documents("Fed decision")

# Step 2: Get data
fed_funds = get_time_series("DFF", "us", "12m")

# Step 3: Understand relationships
policy = query_macro_ontology("fed_tightening")

# Step 4: Personalize
portfolio = get_user_portfolio(user_id)

# Step 5: Generate actions
actions = suggest_actions(macro_regime, portfolio, risk_level)
```

### Parallel Tool Use

Tools called simultaneously (when possible):

```python
import asyncio

# Fetch multiple data series in parallel
async def get_macro_dashboard():
    results = await asyncio.gather(
        get_time_series("CPIAUCSL", "us", "12m"),
        get_time_series("UNRATE", "us", "12m"),
        get_time_series("DFF", "us", "12m"),
        get_time_series("DGS10", "us", "12m")
    )
    return {
        "cpi": results[0],
        "unemployment": results[1],
        "fed_funds": results[2],
        "treasury_10y": results[3]
    }
```

### Conditional Tool Use

Tools called based on context:

```python
def analyze_macro_event(event_type: str, query: str):
    # Always retrieve documents
    docs = retrieve_documents(query)

    # Conditionally get data based on event type
    if event_type == "data_release":
        indicator = extract_indicator(query)  # "CPI" → "CPIAUCSL"
        data = get_time_series(indicator, "us", "12m")

    elif event_type == "policy_decision":
        policy_docs = retrieve_documents(query, filters={"content_type": "policy"})
        rates = get_time_series("DFF", "us", "24m")

    # Always understand concepts
    concepts = query_macro_ontology(extract_concept(query))

    return analyze(docs, data, concepts)
```

---

## Testing Strategy

### Unit Tests

Test each tool in isolation:

```python
def test_retrieve_documents():
    # Test basic retrieval
    docs = retrieve_documents("inflation", k=3)
    assert len(docs) <= 3
    assert all(doc.content for doc in docs)

    # Test with filters
    docs = retrieve_documents(
        "Fed policy",
        filters={"after_date": "2025-01-01"}
    )
    assert all(doc.published_at >= "2025-01-01" for doc in docs)

    # Test error handling
    with pytest.raises(InvalidParameterError):
        retrieve_documents("query", k=100)  # Exceeds max

def test_get_time_series():
    # Test valid indicator
    cpi = get_time_series("CPIAUCSL", "us", "12m")
    assert cpi.metadata.name == "Consumer Price Index"
    assert len(cpi.dates) > 0

    # Test invalid indicator
    result = get_time_series("INVALID", "us", "12m")
    assert result.success == False
    assert "not found" in result.error.message
```

### Integration Tests

Test tool combinations:

```python
def test_macro_analysis_flow():
    # Simulate real agent workflow
    query = "What does rising CPI mean for my portfolio?"

    # Step 1: Retrieve context
    docs = retrieve_documents("CPI inflation", k=3)
    assert len(docs) > 0

    # Step 2: Get data
    cpi = get_time_series("CPIAUCSL", "us", "12m")
    assert cpi.success == True

    # Step 3: Understand impacts
    inflation_concept = query_macro_ontology("inflation")
    assert "bonds" in inflation_concept.asset_impacts

    # Step 4: Generate actions
    actions = suggest_actions(
        "inflation_rising",
        {"equities": 60, "bonds": 40},
        "moderate"
    )
    assert len(actions) > 0
    assert all(action.rationale for action in actions)
```

### Performance Tests

Ensure tools are fast:

```python
import time

def test_tool_performance():
    # Retrieval should be <2 seconds
    start = time.time()
    docs = retrieve_documents("Fed policy", k=5)
    duration = time.time() - start
    assert duration < 2.0, f"Retrieval too slow: {duration}s"

    # Time series should be <1 second
    start = time.time()
    data = get_time_series("CPIAUCSL", "us", "12m")
    duration = time.time() - start
    assert duration < 1.0, f"Data fetch too slow: {duration}s"
```

---

## Future Tools

### V2 Tools (Phase 2)

**Scenario Analysis**:
```python
def run_scenario_analysis(
    scenario: str,
    portfolio: dict,
    time_horizon: str
) -> ScenarioResults:
    """
    Run 'what-if' scenarios.

    Examples:
    - "Fed cuts rates by 100bps"
    - "Recession in next 6 months"
    - "Inflation returns to 2%"
    """
```

**Market Data**:
```python
def get_market_data(
    asset: str,
    metric: str,
    window: str
) -> MarketData:
    """
    Get real-time market data.

    Examples:
    - asset="SPY", metric="price"
    - asset="TLT", metric="yield"
    - asset="GLD", metric="volatility"
    """
```

**Peer Comparison**:
```python
def compare_to_peers(
    user_id: str,
    cohort: str
) -> Comparison:
    """
    Compare user's portfolio to peers.

    Cohorts: "same_risk", "same_age", "same_goals"
    """
```

### V3 Tools (Phase 3)

**Backtesting**:
```python
def backtest_strategy(
    strategy: dict,
    start_date: str,
    end_date: str
) -> BacktestResults:
    """
    Backtest a portfolio strategy.
    """
```

**Optimization**:
```python
def optimize_portfolio(
    current_portfolio: dict,
    constraints: dict,
    objective: str
) -> OptimizedPortfolio:
    """
    Optimize portfolio allocation.

    Objectives: "maximize_sharpe", "minimize_volatility", "maximize_return"
    """
```

---

## Tool Implementation Checklist

For each new tool:

- [ ] **Clear purpose**: One specific job
- [ ] **Good name**: Verb-noun (get_X, retrieve_Y, suggest_Z)
- [ ] **Typed parameters**: Use Pydantic models
- [ ] **Comprehensive docstring**: With examples
- [ ] **Error handling**: Graceful failures
- [ ] **Performance**: <2 seconds typical case
- [ ] **Unit tests**: Cover happy path and errors
- [ ] **Integration tests**: Test with other tools
- [ ] **Documentation**: Add to this doc

---

## Summary

### The 5 MVP Tools

```
retrieve_documents    → Context & news
get_time_series       → Economic data
query_macro_ontology  → Concept relationships
get_user_portfolio    → Personalization
suggest_actions       → Recommendations
```

### Key Principles

✅ **Single responsibility** - Each tool does one thing well
✅ **Composable** - Tools work together
✅ **Reliable** - Graceful error handling
✅ **Fast** - <2 second response times
✅ **Safe** - Read-only, validated inputs
✅ **Clear** - Self-documenting names and descriptions

### Next Steps

1. **Implement** the 5 MVP tools in `src/agent/tools.py`
2. **Test** each tool individually
3. **Integrate** with LangGraph agent
4. **Validate** with real queries
5. **Iterate** based on usage patterns

---

**Tools turn the LLM from a generalist into a specialist economist.** 🛠️
