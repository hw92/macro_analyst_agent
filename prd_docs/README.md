# Product Requirements & Design Documents

This folder contains comprehensive planning and design documentation for the Macro AI Agent project.

---

## 📋 Planning Documents

### [PROJECT_PLAN.md](PROJECT_PLAN.md)
**Detailed 8-Week MVP Development Plan**

- Complete project phases breakdown (Weeks 1-8)
- Deliverables for each week
- Success criteria and metrics
- Risk mitigation strategies
- Resource requirements
- Post-MVP roadmap

**Use this for**: Understanding overall project scope and timeline.

---

### [DEVELOPMENT_ROADMAP.md](DEVELOPMENT_ROADMAP.md)
**Day-by-Day Implementation Roadmap**

- 56-day detailed task breakdown
- Daily assignments and milestones
- Dependencies and critical path
- Team structure recommendations
- Sprint planning guidelines
- Release schedule

**Use this for**: Day-to-day project execution and task assignment.

---

## 📊 Data Architecture Documents

### [DATA_STRATEGY.md](DATA_STRATEGY.md)
**Complete Data Ingestion & Processing Framework**

- 5-stage processing pipeline (Ingestion → Clean → Enrich → Chunk → Index)
- Unified data model for all sources
- Data taxonomy (content types, themes, geography, asset classes)
- Multi-tier storage architecture
- Human & LLM optimization strategies
- Hybrid search approach

**Use this for**: Understanding how data flows through the system.

---

### [DATA_SCHEMA.md](DATA_SCHEMA.md)
**Database Schema & Design**

- Complete PostgreSQL schema (11+ tables)
- Vector database setup (pgvector)
- Time-series database design (TimescaleDB)
- Indexes and performance optimization
- Sample queries and migrations
- Schema versioning

**Use this for**: Database setup and implementation.

---

### [DATA_SOURCES.md](DATA_SOURCES.md)
**Detailed Data Source Integration Guide**

- 7+ data sources with priority matrix
- FRED API integration (40+ economic series)
- FOMC scraper implementation
- RSS feed aggregation
- Bloomberg, Goldman Sachs, The Economist strategies
- Compliance and rate limiting guidelines
- Implementation code examples

**Use this for**: Implementing data ingestion for specific sources.

---

## 🧠 AI Agent & Prompt Engineering

### [PROMPT_STRATEGY.md](PROMPT_STRATEGY.md)
**Comprehensive Prompt Engineering Framework**

- Core philosophy: Making an AI think like an economist
- The economist's mind (frameworks, models, mental toolkits)
- 7-layer prompt architecture
- Reasoning frameworks and structured analysis
- Behavioral guardrails (DOs and DON'Ts)
- Testing and iteration methodology

**Use this for**: Understanding how the AI agent is designed to think and reason.

---

### [SYSTEM_PROMPTS.md](SYSTEM_PROMPTS.md)
**Production-Ready System Prompts**

- MACRO_ECONOMIST_CORE: Main identity and guidelines
- Mode-specific prompts (Chat, Briefing, Actions)
- Complete tool descriptions
- Few-shot examples with reasoning chains
- Implementation guide for `src/agent/prompts.py`

**Use this for**: Copy-paste ready prompts for immediate implementation.

---

### [REASONING_FRAMEWORKS.md](REASONING_FRAMEWORKS.md)
**Macro Analysis Operational Playbooks**

- The 5-Question Framework (detailed step-by-step)
- Causal chain analysis (transmission mechanisms)
- Macro regime classification (inflation × growth matrix)
- Portfolio impact mapping (asset-class-by-asset-class)
- Decision trees for different scenarios
- Action generation with risk considerations

**Use this for**: Understanding the structured reasoning process the agent follows.

---

### [TOOLS_STRATEGY.md](TOOLS_STRATEGY.md)
**Tool Ecosystem for the AI Agent**

- Tool design philosophy (single responsibility, composability)
- 5 core MVP tools (retrieve, data, ontology, portfolio, actions)
- Complete tool schemas (LangChain & OpenAI formats)
- Tool usage patterns (data verification, event context, personalization)
- Error handling and reliability strategies
- Testing framework and performance benchmarks

**Use this for**: Implementing and testing the agent's tool ecosystem.

---

## 📂 Quick Reference

| Document | Purpose | Audience | Phase |
|----------|---------|----------|-------|
| PROJECT_PLAN.md | High-level plan | PM, Stakeholders | Planning |
| DEVELOPMENT_ROADMAP.md | Execution plan | Developers, PM | Implementation |
| DATA_STRATEGY.md | Data architecture | Engineers, Architects | Design |
| DATA_SCHEMA.md | Database design | Backend Engineers | Implementation |
| DATA_SOURCES.md | Ingestion guides | Data Engineers | Implementation |
| PROMPT_STRATEGY.md | Agent design | AI Engineers, Architects | Design |
| SYSTEM_PROMPTS.md | Production prompts | AI Engineers | Implementation |
| REASONING_FRAMEWORKS.md | Analysis playbooks | AI Engineers, PM | Implementation |
| TOOLS_STRATEGY.md | Tool ecosystem | AI Engineers | Implementation |

---

## 🚀 Getting Started

1. **For Project Managers**: Start with `PROJECT_PLAN.md` and `DEVELOPMENT_ROADMAP.md`
2. **For Backend Engineers**: Review `DATA_STRATEGY.md`, `DATA_SCHEMA.md`, and `DATA_SOURCES.md`
3. **For AI Engineers**: Study `PROMPT_STRATEGY.md`, `SYSTEM_PROMPTS.md`, and `REASONING_FRAMEWORKS.md`
4. **For New Team Members**: Read all documents in order listed above

---

## 📝 Document Status

| Document | Version | Last Updated | Status |
|----------|---------|--------------|--------|
| PROJECT_PLAN.md | 1.0 | 2025-11-18 | ✅ Complete |
| DEVELOPMENT_ROADMAP.md | 1.0 | 2025-11-18 | ✅ Complete |
| DATA_STRATEGY.md | 1.0 | 2025-11-18 | ✅ Complete |
| DATA_SCHEMA.md | 1.0 | 2025-11-18 | ✅ Complete |
| DATA_SOURCES.md | 1.0 | 2025-11-18 | ✅ Complete |
| PROMPT_STRATEGY.md | 1.0 | 2025-11-18 | ✅ Complete |
| SYSTEM_PROMPTS.md | 1.0 | 2025-11-18 | ✅ Complete |
| REASONING_FRAMEWORKS.md | 1.0 | 2025-11-18 | ✅ Complete |
| TOOLS_STRATEGY.md | 1.0 | 2025-11-18 | ✅ Complete |

---

**All documents are living documents and will be updated as the project evolves.**

For questions or clarifications, please open an issue or contact the project team.
