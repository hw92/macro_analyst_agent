# Macro AI Agent

> Transform complex macroeconomic information into simple, personalized portfolio insights using AI.

An AI-powered macro economist agent that ingests economic news, data, and research, then provides clear explanations and actionable portfolio recommendations for everyday investors.

---

## Table of Contents

- [Overview](#overview)
- [Documentation](#documentation)
- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Development](#development)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Documentation

Comprehensive project documentation is available in the `prd_docs/` directory:

- **[PROJECT_PLAN.md](prd_docs/PROJECT_PLAN.md)** - Detailed 8-week development plan with phases, tasks, and deliverables
- **[DEVELOPMENT_ROADMAP.md](prd_docs/DEVELOPMENT_ROADMAP.md)** - Day-by-day roadmap with milestones, dependencies, and team structure
- **[DATA_STRATEGY.md](prd_docs/DATA_STRATEGY.md)** - Complete data ingestion and processing framework
- **[DATA_SCHEMA.md](prd_docs/DATA_SCHEMA.md)** - Database schema with 11+ tables for PostgreSQL/Supabase
- **[DATA_SOURCES.md](prd_docs/DATA_SOURCES.md)** - Detailed ingestion guides for FRED, FOMC, Bloomberg, and more

---

## Overview

### The Problem

Macroeconomic information is overwhelming and inaccessible:
- Too much data from disparate sources (news, research, economic releases)
- Complex terminology and conflicting narratives
- Unclear connection between macro events and portfolio actions
- Investors want to know: **"What does this mean for me, and what should I do?"**

### The Solution

The **Macro AI Agent** is an automated system that:

1. **Ingests** macro news, economic data, policy statements, and research
2. **Structures** them into a searchable knowledge base (vector DB + time-series)
3. **Reasons** about macro regimes using LLM + retrieval tools
4. **Explains** events in plain English with structured reasoning
5. **Maps** macro views to portfolio implications
6. **Suggests** personalized action options based on user risk profile

---

## Features

### Core Capabilities

- **Macro Intelligence Engine**
  - RSS feed aggregation (Bloomberg, FT, Reuters)
  - FRED API integration for economic indicators
  - FOMC statement scraping
  - Research report processing (PDF)

- **Knowledge Base**
  - Vector database for semantic search (Supabase pgvector)
  - Time-series database for economic data (TimescaleDB)
  - Hand-crafted macro ontology (concept graph)

- **AI Macro Economist Agent**
  - Structured macro reasoning chain
  - Retrieval-augmented generation (RAG)
  - Multi-tool orchestration (LangGraph)
  - Transparent, grounded explanations

- **Action Engine**
  - Rule-based macro-to-portfolio mapper
  - Personalized by risk profile
  - Risk-aware action suggestions

- **Multiple Interfaces**
  - **CLI** (dev_v1): Fast developer interface
  - **Streamlit** (dev_v2): Stakeholder demos
  - **Vite + React** (dev_v3): Production web app

---

## Architecture

```
World → Data → Knowledge → Reasoning → Action → User
```

### System Components

1. **Ingestion Layer**: Fetches macro news, data, and research
2. **Structuring Layer**: Cleans, chunks, and tags content
3. **Macro Knowledge Base**: Text (vector DB) + Numeric (time-series) + Ontology
4. **AI Agent**: Retrieves, reasons, and generates insights
5. **Action Engine**: Maps macro views to portfolio adjustments
6. **User Interface**: CLI, Streamlit, or React app

### Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.11+ |
| **Package Manager** | `uv` |
| **API Framework** | FastAPI |
| **LLM Orchestration** | LangChain + LangGraph |
| **LLM Provider** | Claude (Anthropic) |
| **Vector Database** | Supabase (pgvector) |
| **Time-Series DB** | Supabase PostgreSQL + TimescaleDB |
| **Economic Data** | FRED API |
| **CLI** | Typer + Rich |
| **Web Prototype** | Streamlit |
| **Production Web** | Vite + React + TailwindCSS |

---

## Quick Start

### Prerequisites

- Python 3.11 or higher
- `uv` package manager ([Install uv](https://github.com/astral-sh/uv))
- Supabase account (free tier works)
- Anthropic API key
- FRED API key (free)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/macro-ai-agent.git
cd macro-ai-agent
```

2. **Install dependencies with uv**

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

3. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env and add your API keys
```

4. **Set up Supabase**

- Create a Supabase project at [supabase.com](https://supabase.com)
- Enable pgvector extension
- Enable TimescaleDB extension
- Copy your project URL and API keys to `.env`

5. **Initialize the database**

```bash
python scripts/init_db.py
```

6. **Run initial data ingestion**

```bash
macro ingest
```

7. **Start the FastAPI server**

```bash
uvicorn src.api.main:app --reload
```

8. **Try the CLI**

```bash
# Interactive chat
macro chat

# One-shot query
macro query "What does rising CPI mean for my portfolio?"

# Generate briefing
macro briefing
```

---

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
│   ├── cli/                    # dev_v1: CLI interface
│   ├── streamlit/              # dev_v2: Streamlit app
│   └── vite-app/               # dev_v3: Production web UI
│
├── data/                       # Local data cache
│   ├── raw/                    # Ingested raw data
│   └── processed/              # Cleaned chunks
│
└── tests/                      # Unit tests
```

---

## Development

### Setting Up Development Environment

```bash
# Install with dev dependencies
uv pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Lint and format
ruff check .
black .
mypy src/
```

### Running Jupyter Notebooks

```bash
jupyter lab

# Or start notebook server
jupyter notebook
```

### Development Workflow

1. **Week 1-2**: Backend core (ingestion + knowledge base + agent)
2. **Week 3**: CLI (dev_v1) - test agent behavior
3. **Week 4**: Streamlit (dev_v2) - stakeholder demos
4. **Week 5**: Refine agent based on feedback
5. **Week 6-7**: Vite app (dev_v3) - production UI
6. **Week 8**: Polish, testing, deployment prep

---

## Usage

### CLI Interface

```bash
# Interactive chat mode
macro chat

# One-shot query
macro query "Explain the latest CPI print"

# Generate weekly briefing
macro briefing

# Trigger data ingestion
macro ingest

# System health check
macro status
```

### API Endpoints

```bash
# Chat endpoint
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What does rising inflation mean?", "user_id": "user123"}'

# Briefing endpoint
curl http://localhost:8000/briefing

# Actions endpoint
curl -X POST http://localhost:8000/actions \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user123", "portfolio": {...}}'
```

### Streamlit App

```bash
# Run Streamlit app
streamlit run frontends/streamlit/app.py
```

### Vite React App

```bash
# Navigate to frontend directory
cd frontends/vite-app

# Install dependencies
npm install

# Run dev server
npm run dev

# Build for production
npm run build
```

---

## API Documentation

Once the FastAPI server is running, visit:

- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### Key Endpoints

#### `POST /chat`
Conversational macro Q&A

**Request:**
```json
{
  "query": "What does rising CPI mean for my portfolio?",
  "user_id": "user123"
}
```

**Response:**
```json
{
  "macro_summary": "CPI increased 0.4% MoM...",
  "why_it_matters": "Rising inflation pressures...",
  "macro_regime": "Inflation rising, Fed hawkish...",
  "impact_on_portfolio": ["Duration risk increases...", "Value over growth..."],
  "actions": [
    {
      "action": "Reduce duration exposure",
      "rationale": "Rising rates hurt bonds...",
      "risk_note": "May miss gains if Fed pivots..."
    }
  ]
}
```

#### `GET /briefing`
Generate weekly macro summary

#### `POST /actions`
Get personalized portfolio suggestions

---

## Roadmap

### MVP (Weeks 1-8) ✅

- [x] Project setup and structure
- [ ] Data ingestion pipeline
- [ ] Vector database setup
- [ ] AI agent with reasoning chain
- [ ] FastAPI backend
- [ ] CLI interface
- [ ] Streamlit prototype
- [ ] Vite + React production UI

### Phase 2 (Weeks 9-12)

- [ ] ML-based regime classification
- [ ] Scenario simulation engine
- [ ] Multi-agent architecture
- [ ] Personalized macro newsletters
- [ ] Real-time alerts

### Phase 3 (Weeks 13-16)

- [ ] Portfolio optimization engine
- [ ] Automated rebalancing
- [ ] Advanced quant signals
- [ ] Mobile app (React Native)
- [ ] Full investment policy engine

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style

- Follow PEP 8 (enforced by `ruff` and `black`)
- Use type hints
- Write docstrings for public functions
- Add tests for new features

---

## Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_agent.py

# Run with coverage
pytest --cov=src --cov-report=html

# Run with verbose output
pytest -v

# Run only fast tests
pytest -m "not slow"
```

---

## Deployment

### Backend (Railway/Render)

```bash
# Deploy to Railway
railway up

# Or deploy to Render
render deploy
```

### Frontend (Vercel)

```bash
# Deploy to Vercel
cd frontends/vite-app
vercel deploy
```

---

## License

MIT License - see [LICENSE](LICENSE) file for details

---

## Acknowledgments

- Federal Reserve Economic Data (FRED) for economic indicators
- Anthropic for Claude AI
- Supabase for database infrastructure
- LangChain community for AI tooling

---

## Support

- **Documentation**: [Link to docs]
- **Issues**: [GitHub Issues](https://github.com/yourusername/macro-ai-agent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/macro-ai-agent/discussions)

---

**Built with passion for making macro economics accessible to everyone.**
