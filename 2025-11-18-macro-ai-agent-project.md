# Macro AI Agent - Project Plan

## Purpose

Build an AI-powered macro economist agent that transforms complex macroeconomic information (news, policy updates, economic data, research) into simple, personalized insights and actionable portfolio recommendations for everyday investors. This agent acts as a 24/7 "macro strategist" that helps users understand what macro events mean for their portfolios.

## Problem

Macroeconomic information is overwhelming and inaccessible:
- Too much data from disparate sources (news, research, economic releases)
- Complex terminology and conflicting narratives
- Unclear connection between macro events and portfolio actions
- Users want to know: **"What does this mean for me, and what should I do?"**

## Solution

An automated AI Macro Economist Agent that:
1. **Ingests** macro news, economic data, policy statements, and research
2. **Structures** them into a searchable knowledge base (vector DB + time-series)
3. **Reasons** about macro regimes using LLM + retrieval tools
4. **Explains** events in plain English with structured reasoning
5. **Maps** macro views to portfolio implications
6. **Suggests** personalized action options based on user risk profile

## Tech Stack

### Core
- **Language**: Python 3.11+
- **Package Management**: `uv` with `pyproject.toml`
- **API Framework**: FastAPI (backend service)
- **LLM Orchestration**: LangChain + LangGraph for agent workflows
- **LLM Providers**: Claude (Anthropic) - prefer `claude-haiku-4-5` for reasoning

### Data & Knowledge
- **Vector Database**: Supabase (pgvector) for macro document retrieval
- **Time-Series DB**: Supabase PostgreSQL with TimescaleDB extension
- **Data Ingestion**:
  - `feedparser` for RSS feeds
  - `requests` + `BeautifulSoup` for web scraping
  - FRED API (Federal Reserve Economic Data) for economic indicators

### Prototyping & Testing
- **Jupyter Notebooks** for testing retrieval, reasoning, and agent flows

### Frontends (Progressive Development)
- **CLI (dev_v1)**: Python `rich` + `typer` for terminal interface
  - Purpose: Initial testing, developer workflow, debugging
  - Fast iteration on agent behavior

- **Streamlit (dev_v2)**: Rapid web prototype
  - Purpose: Quick UI for stakeholder demos, user testing
  - Chat interface + macro briefing dashboard

- **Vite + React (dev_v3)**: Production-ready web app
  - Purpose: Pre-production, polished UX, deployment-ready
  - Modern SPA with TailwindCSS, React Query for API calls

### Supporting Libraries
- **PDF Processing**: `PyMuPDF` or `pypdf` for research reports
- **CLI Styling**: `rich` for beautiful terminal output
- **Deployment**: Vercel (Vite frontend) + Railway/Render (FastAPI backend)

## Project Structure

```
macro-ai-agent/
├── pyproject.toml              # uv project config
├── .env.example                # API keys template
├── README.md
│
├── notebooks/                  # Prototyping & experimentation
│   ├── 01_ingestion_test.ipynb
│   ├── 02_retrieval_test.ipynb
│   └── 03_agent_reasoning.ipynb
│
├── src/
│   ├── ingestion/              # Data fetching & processing
│   │   ├── news_fetcher.py     # RSS + macro news APIs
│   │   ├── econ_data.py        # FRED API integration
│   │   └── processors.py       # Chunking, tagging, cleaning
│   │
│   ├── knowledge/              # Knowledge base management
│   │   ├── vector_store.py     # Supabase pgvector operations
│   │   ├── time_series.py      # Economic data queries
│   │   └── ontology.py         # Hand-written macro concept graph
│   │
│   ├── agent/                  # AI Macro Economist Agent
│   │   ├── tools.py            # Tool definitions (retrieve, query data)
│   │   ├── prompts.py          # System prompts
│   │   ├── reasoning.py        # Structured macro reasoning logic
│   │   └── agent.py            # LangGraph agent orchestration
│   │
│   ├── action/                 # Portfolio action engine
│   │   ├── mapper.py           # Macro regime → portfolio tilts
│   │   └── rules.py            # Rule-based action logic
│   │
│   └── api/                    # FastAPI backend
│       ├── main.py             # FastAPI app
│       ├── routes.py           # Endpoints (/chat, /briefing, /actions)
│       └── models.py           # Pydantic schemas
│
├── frontends/
│   │
│   ├── cli/                    # dev_v1: CLI interface
│   │   ├── main.py             # Entry point (typer CLI)
│   │   ├── commands/
│   │   │   ├── chat.py         # Interactive chat mode
│   │   │   ├── briefing.py     # Generate macro briefing
│   │   │   └── query.py        # One-shot query mode
│   │   └── ui/
│   │       └── display.py      # Rich formatting utilities
│   │
│   ├── streamlit/              # dev_v2: Streamlit app
│   │   ├── app.py              # Main Streamlit app
│   │   ├── pages/
│   │   │   ├── chat.py         # Chat interface page
│   │   │   ├── briefing.py     # Weekly briefing page
│   │   │   └── portfolio.py    # Portfolio analysis page
│   │   └── components/
│   │       ├── message.py      # Chat message components
│   │       └── charts.py       # Macro data visualizations
│   │
│   └── vite-app/               # dev_v3: Production web UI
│       ├── package.json
│       ├── vite.config.js
│       ├── index.html
│       └── src/
│           ├── main.jsx
│           ├── App.jsx
│           ├── components/
│           │   ├── Chat/
│           │   ├── Briefing/
│           │   └── Portfolio/
│           ├── api/
│           │   └── client.js   # API client (fetch/axios)
│           └── styles/
│               └── tailwind.css
│
├── data/                       # Local data cache
│   ├── raw/                    # Ingested raw data
│   └── processed/              # Cleaned chunks
│
└── tests/                      # Unit tests
    ├── test_ingestion.py
    ├── test_retrieval.py
    └── test_agent.py
```

## Deliverables (MVP Scope: 4-8 weeks)

### Phase 1: Core Backend (Week 1-3)

#### 1. **Macro Ingestion Pipeline**
- RSS feed ingestion for macro news (Bloomberg, FT, Reuters)
- FRED API integration for key indicators (CPI, unemployment, Fed Funds rate)
- FOMC statement scraper (Federal Reserve policy updates)
- Basic PDF processing for research reports (optional for MVP)

#### 2. **Macro Knowledge Base**
- Supabase vector store for macro documents (pgvector)
- Time-series tables for economic indicators (CPI, rates, spreads)
- Simple hand-written macro ontology (JSON/YAML graph):
  - `inflation → rates → yields → equities`
  - Risk-on/off regime rules

#### 3. **AI Macro Economist Agent**
- LangGraph-based agent with tools:
  - `retrieve_documents(query)` → vector search
  - `get_time_series(indicator, country, window)` → numeric data
  - `query_macro_ontology(concept)` → concept graph lookup
- Structured reasoning chain:
  - What happened? → Why it matters? → Macro regime? → Portfolio impact? → Actions?
- Output format: JSON with macro summary, reasoning, and action options

#### 4. **Action Engine (Rule-Based)**
- Simple rule-based mapper:
  - `inflation_rising + fed_hawkish → reduce_duration, shift_to_value`
  - `growth_cooling → defensive_tilt, quality_bias`
- Personalization by user risk profile (conservative/moderate/aggressive)

#### 5. **FastAPI Backend Service**
- `/chat` endpoint: user query → agent reasoning → response
- `/briefing` endpoint: generate weekly macro summary
- `/actions` endpoint: get personalized portfolio suggestions

### Phase 2: Frontend Development (Week 3-6)

#### 6. **CLI Interface (dev_v1)** - Week 3
- Commands:
  - `macro chat` - Interactive chat mode
  - `macro query "What does CPI mean for my portfolio?"` - One-shot query
  - `macro briefing` - Generate weekly macro summary
  - `macro ingest` - Manually trigger data ingestion
- Rich terminal formatting (colors, tables, markdown rendering)
- **Purpose**: Developer testing, debugging agent behavior

#### 7. **Streamlit App (dev_v2)** - Week 4-5
- Pages:
  - **Chat Interface**: conversational macro Q&A
  - **Weekly Briefing**: auto-generated macro summary with visuals
  - **Portfolio Impact**: show portfolio + suggested actions
- Components:
  - Chat message display with reasoning steps
  - Economic indicator charts (CPI, rates over time)
  - Action cards (recommended portfolio adjustments)
- **Purpose**: Stakeholder demos, user feedback sessions

#### 8. **Vite + React App (dev_v3)** - Week 6-8
- Modern SPA with:
  - Responsive design (mobile-friendly)
  - Real-time chat with streaming responses
  - Dashboard with macro regime visualization
  - Portfolio analysis page with drag-to-adjust allocations
- TailwindCSS for styling
- React Query for API state management
- **Purpose**: Pre-production, deployment-ready app

## Development Workflow

```
Week 1-2:  Backend core (ingestion + knowledge base + agent)
Week 3:    CLI (dev_v1) - test agent behavior
Week 4:    Streamlit (dev_v2) - stakeholder demos
Week 5:    Refine agent based on feedback
Week 6-7:  Vite app (dev_v3) - production UI
Week 8:    Polish, testing, deployment prep
```

## Success Metrics (for MVP validation)

- **Functional**: Agent successfully retrieves + reasons about macro events
- **Accuracy**: Human eval of 10 sample queries (correctness of reasoning)
- **Usability**: 3-5 test users can understand briefings without confusion
- **Performance**: <5 sec response time for chat queries
- **Frontend Progression**: Each UI iteration improves UX (CLI → Streamlit → Vite)

## Next Steps

1. Set up `uv` project with `pyproject.toml`
2. Configure Supabase (pgvector + TimescaleDB)
3. Implement ingestion pipeline (FRED API + RSS feeds)
4. Build vector store + time-series query layer
5. Create macro ontology (JSON graph)
6. Develop LangGraph agent with tools
7. Build FastAPI backend
8. Implement CLI (dev_v1)
9. Build Streamlit app (dev_v2)
10. Develop Vite + React app (dev_v3)
