# Macro AI Agent - Detailed Project Plan

## Executive Summary

**Project**: AI-Powered Macro Economist Agent
**Timeline**: 8 weeks (MVP)
**Objective**: Build an automated macro intelligence system that transforms complex economic information into personalized, actionable portfolio insights.

---

## 📋 Project Phases

### Phase 1: Foundation & Core Backend (Weeks 1-3)

#### Week 1: Infrastructure & Data Ingestion

**1.1 Project Setup**
- [ ] Initialize `uv` project with `pyproject.toml`
- [ ] Set up Git repository structure
- [ ] Configure development environment
- [ ] Set up Supabase project (pgvector + TimescaleDB)
- [ ] Create environment variables template
- [ ] Set up testing framework (pytest)

**1.2 Macro Ingestion Pipeline**
- [ ] RSS feed fetcher for macro news
  - Bloomberg, Financial Times, Reuters feeds
  - Parse and extract article metadata
- [ ] FRED API integration
  - CPI, Unemployment, GDP, Fed Funds Rate
  - Handle API rate limits and errors
- [ ] FOMC statement scraper
  - Federal Reserve website scraper
  - Parse policy statements
- [ ] PDF processor (optional for MVP)
  - Research report ingestion
  - Text extraction and chunking

**Deliverables**:
- Working ingestion scripts in `src/ingestion/`
- Unit tests for each data source
- Data stored in `data/raw/`

---

#### Week 2: Knowledge Base Infrastructure

**2.1 Vector Store Setup**
- [ ] Supabase pgvector schema design
- [ ] Document embedding pipeline (OpenAI/Anthropic embeddings)
- [ ] Vector search implementation
- [ ] Metadata filtering logic

**2.2 Time-Series Database**
- [ ] TimescaleDB schema for economic indicators
- [ ] Data normalization and indexing
- [ ] Query optimization for range queries
- [ ] Historical data backfill scripts

**2.3 Macro Ontology**
- [ ] Design macro concept graph (JSON/YAML)
- [ ] Define relationships:
  - `inflation → rates → yields → equities`
  - `growth → earnings → equity valuations`
  - Risk-on/off regime rules
- [ ] Implement graph query functions

**Deliverables**:
- `src/knowledge/vector_store.py` - Vector DB operations
- `src/knowledge/time_series.py` - Time-series queries
- `src/knowledge/ontology.py` - Concept graph
- Populated Supabase database with sample data

---

#### Week 3: AI Macro Economist Agent

**3.1 Agent Tools Development**
- [ ] `retrieve_documents(query, k)` - Vector search tool
- [ ] `get_time_series(indicator, country, window)` - Data retrieval
- [ ] `query_macro_ontology(concept)` - Graph lookup
- [ ] `get_user_portfolio(user_id)` - Portfolio context
- [ ] Tool testing and validation

**3.2 Reasoning Chain Implementation**
- [ ] Structured reasoning framework:
  1. What happened?
  2. Why it matters?
  3. Macro regime classification
  4. Portfolio impact analysis
  5. Action generation
- [ ] Prompt engineering for macro analysis
- [ ] Output formatting (JSON structured response)

**3.3 LangGraph Agent Orchestration**
- [ ] Define agent state and workflow
- [ ] Implement tool calling logic
- [ ] Error handling and fallbacks
- [ ] Logging and observability

**3.4 Action Engine (Rule-Based)**
- [ ] Define macro regime → portfolio tilt mappings
- [ ] Implement personalization by risk profile
- [ ] Action suggestion generator
- [ ] Risk note generation

**Deliverables**:
- `src/agent/tools.py` - All agent tools
- `src/agent/prompts.py` - System prompts
- `src/agent/reasoning.py` - Reasoning logic
- `src/agent/agent.py` - LangGraph orchestration
- `src/action/mapper.py` - Macro → portfolio mapper
- `src/action/rules.py` - Rule engine
- Working agent in Jupyter notebook

---

### Phase 2: API Backend (Week 4)

**4.1 FastAPI Service**
- [ ] FastAPI application setup
- [ ] Pydantic models for requests/responses
- [ ] CORS and security middleware

**4.2 API Endpoints**
- [ ] `POST /chat` - Conversational macro Q&A
  - Request: user query + user_id
  - Response: structured reasoning + actions
- [ ] `GET /briefing` - Weekly macro summary
  - Auto-generated macro briefing
  - Key events and regime assessment
- [ ] `POST /actions` - Portfolio action suggestions
  - Input: user portfolio + macro context
  - Output: personalized actions
- [ ] `POST /ingest` - Manual data ingestion trigger
- [ ] Health check endpoints

**4.3 API Documentation**
- [ ] OpenAPI/Swagger documentation
- [ ] Example requests and responses
- [ ] Authentication (API keys/JWT)

**Deliverables**:
- `src/api/main.py` - FastAPI app
- `src/api/routes.py` - All endpoints
- `src/api/models.py` - Pydantic schemas
- API running locally on `localhost:8000`
- Postman/curl test collection

---

### Phase 3: Frontend Development (Weeks 5-8)

#### Week 5: CLI Interface (dev_v1)

**5.1 CLI Commands**
- [ ] `macro chat` - Interactive chat mode
- [ ] `macro query "question"` - One-shot query
- [ ] `macro briefing` - Generate briefing
- [ ] `macro ingest` - Trigger ingestion
- [ ] `macro status` - System health check

**5.2 CLI UI/UX**
- [ ] Rich terminal formatting
- [ ] Color-coded output
- [ ] Markdown rendering
- [ ] Progress indicators
- [ ] Error handling and user feedback

**Deliverables**:
- `frontends/cli/main.py` - CLI entry point
- `frontends/cli/commands/` - All commands
- `frontends/cli/ui/display.py` - Rich formatting
- Fully functional CLI for developer testing

---

#### Week 6: Streamlit App (dev_v2)

**6.1 Streamlit Pages**
- [ ] **Chat Interface**
  - Conversational UI
  - Message history
  - Reasoning step display
- [ ] **Weekly Briefing**
  - Auto-generated summary
  - Economic indicator charts
  - Macro regime visualization
- [ ] **Portfolio Impact**
  - Current portfolio display
  - Action cards with rationale
  - Risk notes

**6.2 Streamlit Components**
- [ ] Chat message components
- [ ] Economic data charts (Plotly/Altair)
- [ ] Action card components
- [ ] Navigation and layout

**Deliverables**:
- `frontends/streamlit/app.py` - Main Streamlit app
- `frontends/streamlit/pages/` - All pages
- `frontends/streamlit/components/` - Reusable components
- Deployed Streamlit app for stakeholder demos

---

#### Weeks 7-8: Vite + React App (dev_v3)

**7.1 React Application Setup**
- [ ] Vite project initialization
- [ ] TailwindCSS configuration
- [ ] React Router setup
- [ ] API client (axios/fetch)
- [ ] State management (React Query)

**7.2 Core Components**
- [ ] **Chat Interface**
  - Real-time messaging
  - Streaming responses
  - Message history
  - Reasoning expansion
- [ ] **Dashboard**
  - Macro regime summary
  - Economic indicator widgets
  - Key events timeline
- [ ] **Portfolio Analysis**
  - Holdings visualization
  - Action recommendations
  - Drag-to-adjust allocations
  - Impact simulation

**7.3 UI/UX Polish**
- [ ] Responsive design (mobile-friendly)
- [ ] Loading states and skeletons
- [ ] Error boundaries
- [ ] Animations and transitions
- [ ] Dark mode support

**7.4 Deployment Preparation**
- [ ] Environment configuration
- [ ] Build optimization
- [ ] Vercel deployment setup
- [ ] Backend deployment (Railway/Render)
- [ ] CI/CD pipeline

**Deliverables**:
- `frontends/vite-app/` - Complete React SPA
- Production-ready web application
- Deployed to staging environment
- User testing feedback incorporated

---

## 🎯 Success Criteria (MVP Validation)

### Functional Requirements
- ✅ Agent successfully retrieves macro documents
- ✅ Agent reasons about macro events correctly
- ✅ Agent maps macro views to portfolio actions
- ✅ All three frontends (CLI, Streamlit, Vite) functional

### Quality Metrics
- **Accuracy**: 80%+ correctness on 10 sample queries (human eval)
- **Performance**: <5 sec response time for chat queries
- **Usability**: 3-5 test users understand briefings without confusion
- **Coverage**: Handle 5+ macro event types (inflation, policy, growth, geo, markets)

### Technical Requirements
- ✅ Comprehensive test coverage (>70%)
- ✅ API documentation complete
- ✅ Error handling robust
- ✅ Logging and monitoring in place
- ✅ Deployment pipeline working

---

## 📊 Resource Requirements

### External Services
- **Supabase**: Database (pgvector + TimescaleDB)
- **Anthropic API**: Claude for agent reasoning
- **OpenAI API** (optional): Embeddings
- **FRED API**: Economic data (free)
- **News APIs**: Bloomberg, Reuters (may require subscription)

### Development Tools
- Python 3.11+
- `uv` package manager
- Git/GitHub
- Docker (optional for local dev)
- Postman/curl for API testing
- Jupyter Lab for prototyping

---

## 🚨 Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| API rate limits (FRED, news) | High | Implement caching, request throttling |
| LLM hallucinations | High | Strict retrieval discipline, validation layer |
| Data quality issues | Medium | Data validation, cleaning pipelines |
| Scope creep | High | Strict MVP focus, defer advanced features |
| Integration complexity | Medium | Incremental integration, extensive testing |
| Deployment issues | Medium | Early deployment to staging, CI/CD |

---

## 🔄 Iteration & Feedback Loops

**Week 3**: Internal testing with CLI
**Week 4**: API testing with Postman
**Week 5**: CLI user testing with 2-3 developers
**Week 6**: Streamlit demo with stakeholders
**Week 7**: Beta testing with 5-10 users
**Week 8**: Final polish based on feedback

---

## 📦 Deliverables Summary

### Week 3
- Working backend (ingestion + knowledge base + agent)
- Jupyter notebooks demonstrating functionality

### Week 5
- FastAPI backend fully operational
- CLI interface (dev_v1) complete

### Week 6
- Streamlit app (dev_v2) ready for demos

### Week 8
- Vite + React app (dev_v3) production-ready
- Full system deployed to staging
- Documentation complete
- User testing feedback incorporated

---

## 🚀 Post-MVP Roadmap

### Phase 4: Enhancements (Weeks 9-12)
- ML-based regime classification
- Scenario simulation engine
- Multi-agent architecture
- Personalized macro newsletters
- Real-time alerts and notifications

### Phase 5: Advanced Features (Weeks 13-16)
- Portfolio optimization engine
- Automated rebalancing
- Advanced quant signals
- Full investment policy engine
- Mobile app (React Native)

---

## 📝 Notes

- **Focus on MVP**: Keep scope tight, defer advanced features
- **User-Centric**: Prioritize usability and clarity over complexity
- **Iterative Development**: Build, test, refine continuously
- **Documentation**: Keep docs updated throughout development
- **Testing**: Test early and often, especially agent reasoning

---

**Last Updated**: 2025-11-18
**Version**: 1.0
**Status**: Planning Phase
