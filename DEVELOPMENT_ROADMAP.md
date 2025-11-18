# Development Roadmap - Macro AI Agent

**Last Updated**: 2025-11-18
**Version**: 1.0
**Status**: Planning Phase

---

## Timeline Overview

```
Week 1-2:  Foundation (Infrastructure + Ingestion + Knowledge Base)
Week 3:    AI Agent Core (Tools + Reasoning + Action Engine)
Week 4:    API Backend (FastAPI + Endpoints)
Week 5:    CLI Interface (dev_v1)
Week 6:    Streamlit App (dev_v2)
Week 7-8:  Vite + React (dev_v3) + Polish + Deployment
```

**Total Duration**: 8 weeks
**MVP Target**: End of Week 8

---

## Phase 1: Foundation & Core Backend (Weeks 1-3)

### Week 1: Infrastructure & Data Ingestion

#### Day 1-2: Project Setup
- [ ] **Task 1.1**: Initialize project
  - Set up Git repository
  - Initialize `uv` project with `pyproject.toml`
  - Create directory structure
  - Set up `.env.example` and `.gitignore`
  - **Deliverable**: Working project skeleton
  - **Owner**: DevOps/Backend

- [ ] **Task 1.2**: Database setup
  - Create Supabase project
  - Enable pgvector extension
  - Enable TimescaleDB extension
  - Design initial schema (documents table, time_series table)
  - **Deliverable**: Configured Supabase instance
  - **Owner**: Backend

- [ ] **Task 1.3**: Development environment
  - Install dependencies (`uv pip install -e ".[dev]"`)
  - Set up pre-commit hooks
  - Configure pytest
  - Set up Jupyter Lab
  - **Deliverable**: Fully configured dev environment
  - **Owner**: All developers

#### Day 3-5: Data Ingestion Pipeline

- [ ] **Task 1.4**: RSS feed fetcher
  - Implement `src/ingestion/news_fetcher.py`
  - Support for Bloomberg, FT, Reuters RSS feeds
  - Parse feed items and extract metadata
  - Handle feed errors and retries
  - Unit tests
  - **Deliverable**: Working RSS ingestion
  - **Owner**: Backend

- [ ] **Task 1.5**: FRED API integration
  - Implement `src/ingestion/econ_data.py`
  - Fetch key indicators (CPI, unemployment, GDP, Fed Funds)
  - Handle API rate limits
  - Data normalization
  - Unit tests
  - **Deliverable**: FRED data ingestion working
  - **Owner**: Backend

- [ ] **Task 1.6**: FOMC scraper
  - Implement FOMC statement scraper
  - Parse Federal Reserve website
  - Extract policy statements
  - Unit tests
  - **Deliverable**: FOMC data ingestion
  - **Owner**: Backend

- [ ] **Task 1.7**: Data processing pipeline
  - Implement `src/ingestion/processors.py`
  - Text cleaning and chunking
  - Metadata tagging
  - Storage in `data/raw/`
  - **Deliverable**: End-to-end ingestion pipeline
  - **Owner**: Backend

#### Day 6-7: Testing & Integration

- [ ] **Task 1.8**: Notebook testing
  - Create `notebooks/01_ingestion_test.ipynb`
  - Test RSS feeds
  - Test FRED API
  - Test FOMC scraper
  - Verify data quality
  - **Deliverable**: Validated ingestion pipeline
  - **Owner**: Backend + QA

- [ ] **Task 1.9**: Documentation
  - Document ingestion pipeline
  - Add inline comments
  - Create usage examples
  - **Deliverable**: Ingestion docs
  - **Owner**: Backend

**Week 1 Milestone**: ✅ Working data ingestion pipeline with RSS, FRED, and FOMC

---

### Week 2: Knowledge Base Infrastructure

#### Day 8-10: Vector Store

- [ ] **Task 2.1**: Vector database schema
  - Design `documents` table in Supabase
  - Configure pgvector indexes
  - Set up embedding pipeline
  - **Deliverable**: Vector DB schema
  - **Owner**: Backend

- [ ] **Task 2.2**: Vector store implementation
  - Implement `src/knowledge/vector_store.py`
  - Embedding generation (OpenAI/Anthropic)
  - Document insertion
  - Semantic search functionality
  - Metadata filtering
  - Unit tests
  - **Deliverable**: Working vector store
  - **Owner**: Backend

- [ ] **Task 2.3**: Data ingestion to vector DB
  - Process raw data and generate embeddings
  - Batch insertion to Supabase
  - Error handling
  - **Deliverable**: Populated vector DB
  - **Owner**: Backend

#### Day 11-12: Time-Series Database

- [ ] **Task 2.4**: Time-series schema
  - Design time-series tables
  - Configure TimescaleDB hypertables
  - Set up indexes for time-range queries
  - **Deliverable**: Time-series schema
  - **Owner**: Backend

- [ ] **Task 2.5**: Time-series implementation
  - Implement `src/knowledge/time_series.py`
  - Data insertion from FRED
  - Range queries
  - Aggregation functions
  - Unit tests
  - **Deliverable**: Working time-series DB
  - **Owner**: Backend

#### Day 13-14: Macro Ontology

- [ ] **Task 2.6**: Ontology design
  - Design macro concept graph (JSON/YAML)
  - Define relationships:
    - `inflation → rates → yields → equities`
    - `growth → earnings → valuations`
    - Risk-on/off rules
  - **Deliverable**: Macro ontology file
  - **Owner**: Product + Backend

- [ ] **Task 2.7**: Ontology implementation
  - Implement `src/knowledge/ontology.py`
  - Graph query functions
  - Concept lookup
  - Relationship traversal
  - Unit tests
  - **Deliverable**: Working ontology system
  - **Owner**: Backend

- [ ] **Task 2.8**: Notebook testing
  - Create `notebooks/02_retrieval_test.ipynb`
  - Test vector search
  - Test time-series queries
  - Test ontology lookups
  - **Deliverable**: Validated knowledge base
  - **Owner**: Backend + QA

**Week 2 Milestone**: ✅ Fully functional knowledge base (vector + time-series + ontology)

---

### Week 3: AI Macro Economist Agent

#### Day 15-17: Agent Tools

- [ ] **Task 3.1**: Tool definitions
  - Implement `src/agent/tools.py`
  - `retrieve_documents(query, k)` - Vector search
  - `get_time_series(indicator, country, window)` - Data retrieval
  - `query_macro_ontology(concept)` - Graph lookup
  - `get_user_portfolio(user_id)` - Portfolio context
  - Tool validation and testing
  - **Deliverable**: All agent tools working
  - **Owner**: Backend + AI

- [ ] **Task 3.2**: System prompts
  - Implement `src/agent/prompts.py`
  - Design macro economist system prompt
  - Reasoning chain instructions
  - Output format specification
  - **Deliverable**: Production-ready prompts
  - **Owner**: AI + Product

#### Day 18-19: Reasoning Chain

- [ ] **Task 3.3**: Reasoning implementation
  - Implement `src/agent/reasoning.py`
  - Structured reasoning framework:
    1. What happened?
    2. Why it matters?
    3. Macro regime classification
    4. Portfolio impact analysis
    5. Action generation
  - JSON output formatting
  - **Deliverable**: Reasoning engine
  - **Owner**: AI + Backend

- [ ] **Task 3.4**: LangGraph orchestration
  - Implement `src/agent/agent.py`
  - Define agent state and workflow
  - Tool calling logic
  - Error handling and retries
  - Logging and observability
  - **Deliverable**: Working LangGraph agent
  - **Owner**: AI + Backend

#### Day 20-21: Action Engine

- [ ] **Task 3.5**: Action mapper
  - Implement `src/action/mapper.py`
  - Define regime → portfolio tilt mappings
  - Personalization by risk profile
  - **Deliverable**: Macro-to-portfolio mapper
  - **Owner**: Product + Backend

- [ ] **Task 3.6**: Rule engine
  - Implement `src/action/rules.py`
  - Rule-based action logic
  - Action suggestion generator
  - Risk note generation
  - **Deliverable**: Action engine
  - **Owner**: Backend

- [ ] **Task 3.7**: Agent testing
  - Create `notebooks/03_agent_reasoning.ipynb`
  - Test agent with sample queries
  - Validate reasoning chain
  - Test action generation
  - Human evaluation of outputs
  - **Deliverable**: Validated agent
  - **Owner**: AI + QA

**Week 3 Milestone**: ✅ Fully functional AI Macro Economist Agent

---

## Phase 2: API Backend (Week 4)

### Week 4: FastAPI Service

#### Day 22-23: FastAPI Setup

- [ ] **Task 4.1**: FastAPI application
  - Implement `src/api/main.py`
  - Configure CORS
  - Security middleware
  - Health check endpoint
  - **Deliverable**: Basic FastAPI app
  - **Owner**: Backend

- [ ] **Task 4.2**: Pydantic models
  - Implement `src/api/models.py`
  - Request/response schemas
  - Validation rules
  - **Deliverable**: API data models
  - **Owner**: Backend

#### Day 24-26: API Endpoints

- [ ] **Task 4.3**: Chat endpoint
  - Implement `POST /chat` in `src/api/routes.py`
  - Integrate with agent
  - Handle streaming responses (optional)
  - Error handling
  - Unit tests
  - **Deliverable**: Working chat endpoint
  - **Owner**: Backend

- [ ] **Task 4.4**: Briefing endpoint
  - Implement `GET /briefing`
  - Auto-generate weekly macro summary
  - Integration with agent
  - Unit tests
  - **Deliverable**: Working briefing endpoint
  - **Owner**: Backend

- [ ] **Task 4.5**: Actions endpoint
  - Implement `POST /actions`
  - Portfolio-based action suggestions
  - Integration with action engine
  - Unit tests
  - **Deliverable**: Working actions endpoint
  - **Owner**: Backend

- [ ] **Task 4.6**: Ingestion endpoint
  - Implement `POST /ingest`
  - Manual data ingestion trigger
  - Background task handling
  - Unit tests
  - **Deliverable**: Working ingestion endpoint
  - **Owner**: Backend

#### Day 27-28: Testing & Documentation

- [ ] **Task 4.7**: API testing
  - Integration tests for all endpoints
  - Performance testing
  - Load testing (optional)
  - **Deliverable**: Tested API
  - **Owner**: Backend + QA

- [ ] **Task 4.8**: API documentation
  - OpenAPI/Swagger docs
  - Example requests/responses
  - Postman collection
  - **Deliverable**: Complete API docs
  - **Owner**: Backend

**Week 4 Milestone**: ✅ Fully functional FastAPI backend with all endpoints

---

## Phase 3: Frontend Development (Weeks 5-8)

### Week 5: CLI Interface (dev_v1)

#### Day 29-30: CLI Core

- [ ] **Task 5.1**: CLI setup
  - Implement `frontends/cli/main.py`
  - Typer CLI framework
  - Command structure
  - **Deliverable**: CLI skeleton
  - **Owner**: Frontend

- [ ] **Task 5.2**: Chat command
  - Implement `frontends/cli/commands/chat.py`
  - Interactive chat mode
  - Message history
  - **Deliverable**: Working chat command
  - **Owner**: Frontend

#### Day 31-32: CLI Commands

- [ ] **Task 5.3**: Query command
  - Implement `frontends/cli/commands/query.py`
  - One-shot query mode
  - **Deliverable**: Working query command
  - **Owner**: Frontend

- [ ] **Task 5.4**: Briefing command
  - Implement `frontends/cli/commands/briefing.py`
  - Generate and display briefing
  - **Deliverable**: Working briefing command
  - **Owner**: Frontend

- [ ] **Task 5.5**: CLI UI/UX
  - Implement `frontends/cli/ui/display.py`
  - Rich terminal formatting
  - Color-coded output
  - Markdown rendering
  - Progress indicators
  - **Deliverable**: Polished CLI interface
  - **Owner**: Frontend

#### Day 33-35: Testing & Polish

- [ ] **Task 5.6**: CLI testing
  - Test all commands
  - User acceptance testing (2-3 developers)
  - Bug fixes
  - **Deliverable**: Production-ready CLI
  - **Owner**: Frontend + QA

**Week 5 Milestone**: ✅ Fully functional CLI interface (dev_v1)

---

### Week 6: Streamlit App (dev_v2)

#### Day 36-37: Streamlit Setup

- [ ] **Task 6.1**: Streamlit app setup
  - Implement `frontends/streamlit/app.py`
  - Page structure
  - Navigation
  - **Deliverable**: Streamlit skeleton
  - **Owner**: Frontend

#### Day 38-40: Streamlit Pages

- [ ] **Task 6.2**: Chat page
  - Implement `frontends/streamlit/pages/chat.py`
  - Conversational UI
  - Message history
  - Reasoning step display
  - **Deliverable**: Working chat page
  - **Owner**: Frontend

- [ ] **Task 6.3**: Briefing page
  - Implement `frontends/streamlit/pages/briefing.py`
  - Auto-generated summary
  - Economic indicator charts (Plotly)
  - Macro regime visualization
  - **Deliverable**: Working briefing page
  - **Owner**: Frontend

- [ ] **Task 6.4**: Portfolio page
  - Implement `frontends/streamlit/pages/portfolio.py`
  - Current portfolio display
  - Action cards
  - Risk notes
  - **Deliverable**: Working portfolio page
  - **Owner**: Frontend

#### Day 41-42: Components & Polish

- [ ] **Task 6.5**: Streamlit components
  - Implement `frontends/streamlit/components/`
  - Chat message components
  - Chart components
  - Action card components
  - **Deliverable**: Reusable components
  - **Owner**: Frontend

- [ ] **Task 6.6**: Stakeholder demo
  - Prepare demo
  - Present to stakeholders
  - Collect feedback
  - **Deliverable**: Feedback report
  - **Owner**: Product + Frontend

**Week 6 Milestone**: ✅ Fully functional Streamlit app (dev_v2)

---

### Week 7-8: Vite + React App (dev_v3) + Deployment

#### Day 43-45: React Setup

- [ ] **Task 7.1**: Vite project setup
  - Initialize Vite project
  - Configure TailwindCSS
  - Set up React Router
  - Configure API client
  - Set up React Query
  - **Deliverable**: React app skeleton
  - **Owner**: Frontend

- [ ] **Task 7.2**: API client
  - Implement `frontends/vite-app/src/api/client.js`
  - Axios/fetch wrapper
  - Error handling
  - Request/response interceptors
  - **Deliverable**: Working API client
  - **Owner**: Frontend

#### Day 46-49: React Components

- [ ] **Task 7.3**: Chat interface
  - Implement `frontends/vite-app/src/components/Chat/`
  - Real-time messaging
  - Streaming responses
  - Message history
  - Reasoning expansion
  - **Deliverable**: Working chat interface
  - **Owner**: Frontend

- [ ] **Task 7.4**: Dashboard
  - Implement `frontends/vite-app/src/components/Briefing/`
  - Macro regime summary
  - Economic indicator widgets
  - Key events timeline
  - **Deliverable**: Working dashboard
  - **Owner**: Frontend

- [ ] **Task 7.5**: Portfolio analysis
  - Implement `frontends/vite-app/src/components/Portfolio/`
  - Holdings visualization
  - Action recommendations
  - Drag-to-adjust allocations
  - Impact simulation
  - **Deliverable**: Working portfolio page
  - **Owner**: Frontend

#### Day 50-52: UI/UX Polish

- [ ] **Task 7.6**: Responsive design
  - Mobile-friendly layouts
  - Tablet optimization
  - Desktop layouts
  - **Deliverable**: Fully responsive app
  - **Owner**: Frontend

- [ ] **Task 7.7**: UI enhancements
  - Loading states and skeletons
  - Error boundaries
  - Animations and transitions
  - Dark mode support
  - **Deliverable**: Polished UI/UX
  - **Owner**: Frontend

#### Day 53-56: Deployment

- [ ] **Task 7.8**: Backend deployment
  - Deploy to Railway/Render
  - Environment configuration
  - Database connection
  - API testing in production
  - **Deliverable**: Deployed backend
  - **Owner**: DevOps

- [ ] **Task 7.9**: Frontend deployment
  - Deploy to Vercel
  - Environment configuration
  - Build optimization
  - **Deliverable**: Deployed frontend
  - **Owner**: DevOps

- [ ] **Task 7.10**: CI/CD pipeline
  - GitHub Actions setup
  - Automated testing
  - Automated deployment
  - **Deliverable**: Working CI/CD
  - **Owner**: DevOps

- [ ] **Task 7.11**: Final testing
  - End-to-end testing
  - Beta user testing (5-10 users)
  - Bug fixes
  - Performance optimization
  - **Deliverable**: Production-ready system
  - **Owner**: QA + All

**Week 8 Milestone**: ✅ Production-ready Vite + React app (dev_v3) + Full system deployed

---

## Success Criteria (MVP Validation)

### Functional Requirements
- ✅ Agent successfully retrieves macro documents from vector DB
- ✅ Agent reasons about macro events with structured chain
- ✅ Agent maps macro views to portfolio actions
- ✅ All three frontends (CLI, Streamlit, Vite) functional
- ✅ FastAPI backend handles all requests reliably

### Quality Metrics
- **Accuracy**: 80%+ correctness on 10 sample queries (human eval)
- **Performance**: <5 sec response time for chat queries
- **Usability**: 3-5 test users understand briefings without confusion
- **Coverage**: Handle 5+ macro event types (inflation, policy, growth, geo, markets)

### Technical Requirements
- ✅ Test coverage >70%
- ✅ API documentation complete (OpenAPI)
- ✅ Error handling robust across all layers
- ✅ Logging and monitoring in place
- ✅ Deployment pipeline working (CI/CD)

---

## Risk Management

| Risk | Probability | Impact | Mitigation | Owner |
|------|------------|--------|-----------|--------|
| API rate limits (FRED, news) | High | High | Implement caching, throttling | Backend |
| LLM hallucinations | High | High | Strict retrieval discipline | AI |
| Data quality issues | Medium | Medium | Validation, cleaning | Backend |
| Scope creep | High | High | Strict MVP focus | Product |
| Integration complexity | Medium | Medium | Incremental integration | Backend |
| Deployment issues | Medium | Medium | Early staging deployment | DevOps |
| Timeline slippage | Medium | High | Weekly sprint reviews | PM |

---

## Post-MVP Roadmap

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

### Phase 6: Scale & Productionize (Weeks 17-20)
- Multi-user support
- Authentication and authorization
- Billing and subscription management
- Enterprise features
- White-label options

---

## Dependencies Graph

```
Week 1 (Ingestion) → Week 2 (Knowledge Base) → Week 3 (Agent)
                                                      ↓
                                                Week 4 (API)
                                                      ↓
                            ┌─────────────────────────┼─────────────────────────┐
                            ↓                         ↓                         ↓
                      Week 5 (CLI)           Week 6 (Streamlit)       Week 7-8 (React)
```

**Critical Path**: Week 1 → Week 2 → Week 3 → Week 4
**Parallel Track**: Week 5, 6, 7-8 can partially overlap

---

## Team Structure (Recommended)

| Role | Responsibilities | Time Commitment |
|------|-----------------|-----------------|
| **Backend Engineer** | Ingestion, Knowledge Base, Agent, API | Full-time (8 weeks) |
| **AI Engineer** | Agent reasoning, Prompts, LLM integration | Full-time (Weeks 3-8) |
| **Frontend Engineer** | CLI, Streamlit, React app | Full-time (Weeks 5-8) |
| **Product Manager** | Requirements, Ontology, User testing | Part-time (2-3 days/week) |
| **QA Engineer** | Testing, Validation, Bug tracking | Part-time (Weeks 3-8) |
| **DevOps Engineer** | Deployment, CI/CD, Infrastructure | Part-time (Weeks 4, 8) |

**Minimum Team**: 2-3 full-time developers (Backend/AI + Frontend + Product/QA)

---

## Tracking & Reporting

### Weekly Sprint Reviews
- **When**: End of each week (Friday)
- **Attendees**: All team members
- **Agenda**:
  - Demo completed work
  - Review blockers
  - Plan next week

### Daily Standups
- **When**: Daily (15 min)
- **Format**: What done? What next? Blockers?

### Tools
- **Project Management**: GitHub Projects / Jira
- **Communication**: Slack / Discord
- **Docs**: Notion / Confluence
- **Code**: GitHub

---

## Release Plan

| Milestone | Date | Release Type | Audience |
|-----------|------|-------------|----------|
| Week 3 | Day 21 | Internal Alpha | Developers only |
| Week 5 | Day 35 | CLI Beta | Internal team + 2-3 testers |
| Week 6 | Day 42 | Streamlit Demo | Stakeholders |
| Week 7 | Day 49 | React Beta | 5-10 beta users |
| Week 8 | Day 56 | MVP Release | Public (limited) |

---

**Next Steps**: Start Week 1, Day 1 - Project Setup

**Status**: Ready to begin development ✅
