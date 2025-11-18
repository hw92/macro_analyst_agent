

# 📄 **macro_ai_agent — 1-Page Product Spec**

## **1. Product Overview**

The **macro ai agent** transforms complex macroeconomic information—news, policy, research, economic data—into **simple, personalized insights** and **actionable portfolio recommendations** for everyday investors.
 It powers the macro capabilities of your AI-for-Finance app and acts as a “macro strategist” that users can rely on for interpretation and decision guidance.

------

## **2. Problem**

- Macro is overwhelming and inaccessible to general users.
- Even sophisticated investors struggle with:
  - too much data
  - complex terminology
  - conflicting narratives
  - unclear links between macro events and portfolio actions

### **Core Need:**

People don’t just want to *understand* macro — they want to know
 **“what does this mean for me, and what should I do?”**

------

## **3. Solution**

A fully automated **AI Macro Economist Agent** that:

1. **Ingests** macro news, economic data, policy statements, research.
2. **Structures** them into a macro knowledge base.
3. **Reasons** about macro regimes.
4. **Explains** events in plain English.
5. **Maps** macro views to portfolio implications.
6. **Suggests** personalized action options.

This creates an **AI-driven macro strategist** available 24/7 for each user.

------

## **4. Core Features**

### **4.1 Macro Ingestion Engine**

- Fetches macro news, policy updates, economic releases
- Processes research PDFs (e.g., GS, MS)
- Records market data (CPI, unemployment, rates, spreads, FX)

### **4.2 Macro Knowledge Base**

- Text Knowledge: vector DB of macro documents
- Numeric Knowledge: time-series economic indicators
- Macro Ontology: conceptual graph connecting inflation → rates → spreads → asset classes

### **4.3 AI Macro Economist Agent**

- Uses tools for retrieval, data queries, ontology lookup
- Performs structured macro reasoning:
  - *What happened? Why does it matter? What regime are we in?*
- Produces simple, grounded explanations

### **4.4 Action Engine**

- Maps macro views → portfolio adjustments
- Uses rules + scenario logic (e.g., inflation cooling → duration up)
- Personalized by risk tolerance and current portfolio

### **4.5 User-Facing Outputs**

- Daily/weekly macro briefings
- “Explain this event” chatbot
- Macro alerts + recommended actions
- Personalized portfolio insights

------

## **5. Architecture Summary**

**World → Data → Knowledge → Reasoning → Action → User**

Modules:

1. **Ingestion Layer**
2. **Structuring Layer**
3. **Macro Knowledge Base (Text + Data + Ontology)**
4. **Macro Economist Agent**
5. **Action Engine**
6. **User Interface Layer**

The system can be deployed as:

- Backend FastAPI service
- Agent orchestrated via OpenAI/Claude/Gemini
- Next.js/Vercel front-end

------

## **6. KPIs / Success Metrics**

- Accuracy of macro explanations (human eval)
- Reduction in user confusion (“I understand why this matters”)
- Engagement: briefing opens, alerts clicked
- Conversion: users acting on insights
- Retention: weekly macro summary usage

------

## **7. MVP Scope (4–8 weeks)**

### **Included:**

- Basic ingestion (RSS + FOMC + CPI releases)
- Vector DB for macro documents
- Time-series API for inflation, unemployment, rates
- Basic ontology (hand-written rules)
- Macro Economist Agent (LLM + RAG)
- Action Engine (rule-based)
- Chat interface: “Explain this macro event to me”
- Weekly macro briefing

### **Not Included:**

- Real trading execution
- Deep quant signals
- ML-based allocation model
- Full portfolio optimization

(This keeps MVP simple and achievable.)

------

## **8. Long-Term Extensions**

- Scenario simulation engine
- Regime classification model (ML-based)
- Multi-agent architecture (data agent, reasoning agent, action agent)
- Personalized macro newsletters
- Automated rebalancing pipelines
- Full investment policy engine









# ⭐ **This diagram expresses the key idea:**

**World → Data → Knowledge → Reasoning → Action → User.**

---

                       ┌─────────────────────────────────┐
                       │   MACRO INTELLIGENCE ENGINE     │
                       │         (AI + Macro)            │
                       └─────────────────────────────────┘
                                      │
                                      ▼
        ┌─────────────────────────────────────────────────────────┐
        │ 1. INGESTION LAYER (Macro World → Raw Inputs)          │
        ├─────────────────────────────────────────────────────────┤
        │ • Macro news (RSS/APIs)                                │
        │ • Economic releases (CPI, GDP, jobs)                   │
        │ • Central bank statements (FOMC, ECB)                  │
        │ • Research reports (GS, MS, academia)                  │
        │ • Market data (rates, spreads, FX, volatility)         │
        └─────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        ┌─────────────────────────────────────────────────────────┐
        │ 2. STRUCTURING LAYER (Clean → Chunk → Tag)              │
        ├─────────────────────────────────────────────────────────┤
        │ • Text cleaning & chunking                             │
        │ • Metadata tagging (topic, region, asset class)        │
        │ • Entity recognition (Fed, CPI, tariffs…)              │
        │ • Classification (inflation / growth / policy / geo)   │
        └─────────────────────────────────────────────────────────┘
                                      │
                ┌─────────────────────┼─────────────────────┐
                ▼                     ▼                     ▼
   ┌──────────────────┐   ┌──────────────────┐   ┌────────────────────────┐
   │ TEXTUAL KB        │   │ NUMERIC KB       │   │ MACRO ONTOLOGY/GRAPH  │
   ├──────────────────┤   ├──────────────────┤   ├────────────────────────┤
   │ Vector DB         │   │ Time-series DB   │   │ Concept links:         │
   │ • news chunks     │   │ • CPI, rates     │   │ inflation→rates→growth│
   │ • research chunks │   │ • spreads, FX    │   │ risk-on/off logic      │
   └──────────────────┘   └──────────────────┘   └────────────────────────┘
                ▲                     ▲                     ▲
                └─────────────── 3. MACRO KNOWLEDGE BASE ───┘
                                      │
                                      ▼
        ┌─────────────────────────────────────────────────────────┐
        │ 4. AI MACRO ECONOMIST AGENT                             │
        ├─────────────────────────────────────────────────────────┤
        │ • Retrieves documents & data from KB                    │
        │ • Performs macro reasoning (regime evaluation)          │
        │ • Interprets events (“why it matters”)                  │
        │ • Links macro view → portfolio actions                  │
        │ • Generates plain-language insights                     │
        └─────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        ┌─────────────────────────────────────────────────────────┐
        │ 5. ACTION ENGINE (Decision Layer)                       │
        ├─────────────────────────────────────────────────────────┤
        │ • Risk-on/off tilt                                      │
        │ • Duration adjustments                                  │
        │ • Sector/asset class tilts                              │
        │ • Personalized by user risk profile & holdings          │
        └─────────────────────────────────────────────────────────┘
                                      │
                                      ▼
        ┌─────────────────────────────────────────────────────────┐
        │ 6. USER EXPERIENCE (Outputs)                            │
        ├─────────────────────────────────────────────────────────┤
        │ • Macro summary (“What happened?”)                      │
        │ • Interpretation (“Why does it matter?”)                │
        │ • Impact (“What it means for your portfolio”)           │
        │ • Action suggestions (“What you can do next”)           │
        └─────────────────────────────────────────────────────────┘





---

Below is a **complete system prompt + tool schema** for your **Macro Economist Agent**, ready to plug into your AI-for-Finance app (FastAPI, LangChain, LangGraph, OpenAI Agents, Claude Tools, etc.).

It is written in **production style**, combining:

- strict behavior rules
- retrieval discipline
- macro reasoning structure
- portfolio-aware action mapping
- output format control

This is the type of system prompt you can show to Allio or include in your architecture doc.











# **A complete system prompt + tool schema** for your **Macro Economist Agent*

------

##  🔥 **SYSTEM PROMPT — “MACRO ECONOMIST AGENT”**

```
You are the Macro Economist Agent inside an AI-for-Finance application.

Your mission is:
1. Interpret macroeconomic news, policy updates, research insights, and economic data.
2. Explain clearly what happened, why it matters, and how it affects the investor’s portfolio.
3. Use structured macro reasoning grounded in retrieved documents and numeric data.
4. Provide actionable, personalized portfolio recommendations aligned with the user's
   risk level, investment horizon, and current holdings.
5. Avoid hallucinations. If information is uncertain, state uncertainty clearly.

------------------------------------
YOUR IDENTITY AND BEHAVIOR
------------------------------------
• You think like a professional macro economist, but speak like a patient educator.
• You translate complex macro narratives into simple, practical insights.
• You are politically neutral. You analyze policy impacts, not ideology.
• Your reasoning must be grounded in retrieved documents, data series, and the macro ontology.
• You obey tool results exactly. Do not invent numbers or data.

------------------------------------
MACRO REASONING FRAMEWORK
------------------------------------
For every query or event, follow this reasoning chain:

1. WHAT HAPPENED?
   - Summarize the event only after retrieving documents.
   - Examples: “CPI increased to X,” “Fed signaled no cuts,” “Tariffs announced.”

2. WHY DOES IT MATTER?
   - Explain causal channels.
   - Use macro ontology concepts:
       inflation → policy rate → yields → equities/credit
       growth → earnings → equity premium
       liquidity → risk-on/off behavior

3. WHAT IS THE MACRO REGIME?
   - Classify using retrieved data:
       • Inflation Trend: rising / falling / uncertain
       • Growth: expanding / cooling
       • Policy: tightening / easing / paused
       • Risk Sentiment: risk-on / risk-off

4. WHAT IS THE IMPLICATION FOR THE USER?
   - Connect macro to portfolio exposures.
   - Identify risks and opportunities relevant to the user’s holdings.

5. WHAT ARE THE ACTION OPTIONS?
   - Provide 1–3 reasonable adjustments.
   - Always include a risk note.
   - Do NOT give prescriptive financial advice—only informed options.

------------------------------------
ALLOWED OUTPUT FORMAT
------------------------------------
Always output in this structure:

{
  "macro_summary": "...",
  "why_it_matters": "...",
  "macro_regime": "...",
  "impact_on_portfolio": [
      "point 1",
      "point 2"
  ],
  "actions": [
      {
        "action": "...",
        "rationale": "...",
        "risk_note": "..."
      }
  ]
}

------------------------------------
ERROR HANDLING
------------------------------------
• If data is insufficient: "Information insufficient for conclusion."
• If tools return empty: "No relevant macro data found. Provide more context."
• If user asks outside macro domain: redirect politely.

------------------------------------
PRIMARY DIRECTIVE
------------------------------------
Your output must always be:
- Grounded
- Simple
- Actionable
- Personalized
- Structured
- Transparent in reasoning

Never provide advice without showing the reasoning steps.
Never hallucinate macro data or policy facts.
```

------

## 🔧 **TOOL SCHEMA**

This is a clean schema you can plug into:

- OpenAI Assistants API tools
- LangChain tools
- FastAPI server tools
- Claude function calling
- Node.js or Python agent frameworks

### **1. retrieve_documents**

Retrieves macro text chunks from your vector DB.

```
{
  "name": "retrieve_documents",
  "description": "Retrieve most relevant macro/economy documents from the knowledge base.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {"type": "string"},
      "k": {"type": "integer", "description": "Number of documents", "default": 5}
    },
    "required": ["query"]
  }
}
```

------

### **2. get_time_series**

Fetch macro time-series data (inflation, rates, unemployment, FX, spreads).

```
{
  "name": "get_time_series",
  "description": "Return numeric macroeconomic time series for the requested indicator.",
  "parameters": {
    "type": "object",
    "properties": {
      "indicator": {"type": "string", "description": "e.g., CPI, GDP, UNEMPLOYMENT"},
      "country": {"type": "string"},
      "window": {"type": "string", "description": "e.g., 12m, 24m, YTD"}
    },
    "required": ["indicator", "country"]
  }
}
```

------

### **3. query_macro_ontology**

Access the conceptual macro graph.

```
{
  "name": "query_macro_ontology",
  "description": "Query macro concept connections such as inflation→rates→equities.",
  "parameters": {
    "type": "object",
    "properties": {
      "concept": {"type": "string"}
    },
    "required": ["concept"]
  }
}
```

------

### **4. get_user_portfolio**

Fetch user’s holdings, risk profile, and preferences.

```
{
  "name": "get_user_portfolio",
  "description": "Return portfolio, risk tolerance, and investment horizon for the user.",
  "parameters": {
    "type": "object",
    "properties": {
      "user_id": {"type": "string"}
    },
    "required": ["user_id"]
  }
}
```

------

### **5. suggest_actions**

Given macro view + portfolio, computes potential action options.

```
{
  "name": "suggest_actions",
  "description": "Generate portfolio adjustment options based on macro regime and user profile.",
  "parameters": {
    "type": "object",
    "properties": {
      "macro_regime": {"type": "string"},
      "portfolio": {"type": "object"},
      "risk_level": {"type": "string"}
    },
    "required": ["macro_regime", "portfolio", "risk_level"]
  }
}
```

------

## 🚀 **HOW THIS ALL WORKS TOGETHER (Flow)**

**User asks:**
 “What does today’s CPI print mean for my portfolio?”

Agent does:

1. `retrieve_documents("US CPI release")`
2. `get_time_series("CPI", "US", "12m")`
3. `get_user_portfolio(user_id)`
4. Reason:
   - inflation ↑? ↓?
   - Fed reaction?
   - risk-on/off?
   - which holdings impacted?
5. `suggest_actions(...)`
6. Output JSON with structured insight + options.
