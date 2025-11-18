# Macro AI Agent - Data Strategy

**Version**: 1.0
**Last Updated**: 2025-11-18

---

## Table of Contents

1. [Overview](#overview)
2. [The Data Challenge](#the-data-challenge)
3. [Data Taxonomy](#data-taxonomy)
4. [Unified Data Model](#unified-data-model)
5. [Source-Specific Ingestion Strategies](#source-specific-ingestion-strategies)
6. [Data Processing Pipeline](#data-processing-pipeline)
7. [Storage Architecture](#storage-architecture)
8. [Human & LLM Optimization](#human--llm-optimization)
9. [Implementation Plan](#implementation-plan)

---

## Overview

### Core Principle

**"Single Source of Truth, Multiple Views"**

All macro data flows through a unified processing pipeline that:
- Preserves original content (human-readable)
- Generates optimized chunks (LLM-readable)
- Maintains rich metadata (searchable)
- Tracks provenance (trustworthy)

---

## The Data Challenge

### Heterogeneous Data Sources

| Source Type | Examples | Format | Update Frequency | Complexity |
|------------|----------|--------|------------------|------------|
| **News Sites** | Bloomberg, FT, Reuters | HTML, RSS | Real-time | Medium |
| **Government Data** | FRED, BLS, Census | API, CSV, XLS | Daily/Monthly | Low |
| **Central Banks** | Fed, ECB, BoE | HTML, PDF | Event-driven | Medium |
| **Research Reports** | Goldman Sachs, JPM | PDF, Paywalled | Weekly | High |
| **Journals** | The Economist, WSJ | HTML, Paywalled | Weekly | Medium |
| **Academic Papers** | NBER, SSRN | PDF | Monthly | High |

### Key Challenges

1. **Format Diversity**: HTML, PDF, RSS, APIs, structured data
2. **Access Control**: Paywalls, API limits, scraping restrictions
3. **Data Quality**: Inconsistent metadata, duplicates, errors
4. **Temporal Sensitivity**: Macro data is time-bound and date-critical
5. **Semantic Complexity**: Same event described differently across sources
6. **Volume vs. Signal**: Too much noise, need smart filtering

---

## Data Taxonomy

### 1. Content Types (What is it?)

```yaml
content_types:
  news:
    - breaking_news        # Time-sensitive events
    - analysis            # Expert commentary
    - market_reaction     # Price/market responses

  data:
    - time_series         # CPI, GDP, unemployment
    - cross_sectional     # Country comparisons
    - survey_data         # Consumer confidence, PMI

  policy:
    - central_bank        # FOMC statements, speeches
    - government          # Fiscal policy, regulation
    - international       # IMF, World Bank reports

  research:
    - sell_side           # Goldman, JPM, MS research
    - buy_side            # Hedge fund letters
    - academic            # NBER, research papers
    - think_tank          # Brookings, AEI reports

  market_data:
    - prices              # Equities, bonds, commodities
    - flows               # Fund flows, positioning
    - volatility          # VIX, implied vol
```

### 2. Macro Themes (What's it about?)

```yaml
macro_themes:
  inflation:
    - headline_inflation
    - core_inflation
    - inflation_expectations
    - commodity_prices

  growth:
    - gdp_growth
    - employment
    - manufacturing
    - services
    - consumer_spending

  monetary_policy:
    - interest_rates
    - qe_qt              # Quantitative easing/tightening
    - central_bank_policy
    - liquidity

  fiscal_policy:
    - government_spending
    - taxation
    - deficits_debt

  geopolitics:
    - trade_policy
    - sanctions
    - conflicts
    - political_risk

  markets:
    - equity_markets
    - bond_markets
    - fx_markets
    - credit_markets
```

### 3. Geography (Where?)

```yaml
geography:
  regions:
    - global
    - us
    - europe
    - asia_pacific
    - emerging_markets
    - latam

  countries:
    - usa
    - china
    - japan
    - uk
    - germany
    - france
    # ... etc
```

### 4. Asset Classes (Impact on what?)

```yaml
asset_classes:
  equities:
    - us_large_cap
    - us_small_cap
    - international_developed
    - emerging_markets
    - sectors: [tech, financials, energy, healthcare, ...]

  fixed_income:
    - treasuries
    - corporate_bonds
    - high_yield
    - municipal
    - international_bonds

  alternatives:
    - commodities
    - real_estate
    - crypto
    - private_equity

  cash_fx:
    - cash
    - currency_pairs
```

---

## Unified Data Model

### Document Schema (All sources map to this)

```python
{
  # IDENTITY
  "id": "uuid-v4",
  "source_id": "original-id-from-source",
  "url": "https://...",

  # CONTENT (Human-readable)
  "title": "Fed Signals Pause in Rate Hikes",
  "content": "Full text content...",
  "summary": "AI-generated or source summary",
  "language": "en",

  # METADATA (Searchable & Filterable)
  "source": {
    "name": "Bloomberg",
    "type": "news_site",
    "credibility_score": 0.95,
    "paywall": true
  },

  "temporal": {
    "published_at": "2025-03-15T14:30:00Z",
    "ingested_at": "2025-03-15T15:00:00Z",
    "effective_date": "2025-03-15",  # When the event occurred
    "data_vintage": "2025-03-01"     # For economic data (e.g., CPI for Feb)
  },

  "classification": {
    "content_type": "news",
    "macro_themes": ["monetary_policy", "inflation"],
    "geography": ["us"],
    "asset_classes": ["equities", "fixed_income"],
    "sentiment": "dovish",  # hawkish/dovish/neutral (for policy)
    "importance": "high"    # high/medium/low
  },

  "entities": {
    "people": ["Jerome Powell", "Fed Chair"],
    "organizations": ["Federal Reserve", "FOMC"],
    "indicators": ["CPI", "PCE"],
    "concepts": ["interest rates", "inflation targeting"]
  },

  # ENRICHMENT (AI-generated)
  "ai_analysis": {
    "key_takeaways": ["Fed pausing rate hikes", "Data-dependent approach"],
    "macro_regime": "late_cycle_slowdown",
    "portfolio_impact": "positive_for_duration",
    "reasoning": "With inflation cooling..."
  },

  # CHUNKING (LLM-optimized)
  "chunks": [
    {
      "chunk_id": "uuid",
      "text": "chunk of 500-1000 tokens",
      "position": 0,
      "embedding": [0.1, 0.2, ...],  # 1536-dim vector
      "metadata": {}  # Inherits from parent
    }
  ],

  # PROVENANCE (Trust & Audit)
  "provenance": {
    "ingestion_method": "rss_feed",
    "processing_version": "v1.0",
    "verification_status": "verified",
    "human_reviewed": false
  },

  # RELATIONS (Graph)
  "related_documents": ["doc-id-1", "doc-id-2"],
  "related_data_series": ["FRED:CPIAUCSL"],
  "references": ["https://federalreserve.gov/..."]
}
```

---

## Source-Specific Ingestion Strategies

### 1. Bloomberg (News & Analysis)

**Access**: Subscription required, rate-limited

**Strategy**:
```python
{
  "method": "rss_feed + web_scraping",
  "sources": [
    "https://www.bloomberg.com/feeds/markets/news.rss",
    "https://www.bloomberg.com/feeds/economics/news.rss"
  ],
  "frequency": "every 15 minutes",
  "rate_limit": "10 requests/minute",
  "extraction": {
    "title": "rss:item:title",
    "summary": "rss:item:description",
    "full_text": "scrape article page (requires auth)",
    "published_at": "rss:item:pubDate"
  },
  "challenges": [
    "Paywall - need Bloomberg Terminal API or subscription",
    "Rate limiting - respect robots.txt",
    "JavaScript-rendered content"
  ],
  "alternatives": [
    "Bloomberg Terminal API (if available)",
    "Bloomberg Professional Services feed"
  ]
}
```

**Implementation Priority**: Medium (start with RSS, upgrade to API later)

---

### 2. FRED (Federal Reserve Economic Data)

**Access**: Free API, generous rate limits

**Strategy**:
```python
{
  "method": "official_api",
  "api": "https://fred.stlouisfed.org/docs/api/",
  "api_key": "required (free)",
  "frequency": "daily (data updated varies by series)",
  "series_of_interest": [
    "CPIAUCSL",      # CPI
    "UNRATE",        # Unemployment
    "DFF",           # Fed Funds Rate
    "DGS10",         # 10-Year Treasury
    "T10Y2Y",        # 10Y-2Y Spread
    "DEXUSEU",       # USD/EUR
    "UMCSENT",       # Consumer Sentiment
    # ... 100+ key series
  ],
  "data_format": {
    "observation_date": "2025-03-01",
    "value": 3.2,
    "units": "percent",
    "frequency": "monthly"
  },
  "storage": "time_series_db (TimescaleDB)",
  "metadata": {
    "series_name": "Consumer Price Index",
    "units": "Index 1982-1984=100",
    "seasonal_adjustment": "Seasonally Adjusted",
    "source": "Bureau of Labor Statistics"
  }
}
```

**Implementation Priority**: High (easy, reliable, free)

---

### 3. FOMC & Fed Statements (Federal Reserve)

**Access**: Public, no auth required

**Strategy**:
```python
{
  "method": "web_scraping",
  "sources": [
    "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "https://www.federalreserve.gov/newsevents/speeches.htm"
  ],
  "frequency": "event-driven (FOMC meets 8x/year)",
  "content_types": [
    "FOMC statements",
    "Press conference transcripts",
    "Meeting minutes",
    "Fed Chair speeches",
    "Beige Book reports"
  ],
  "extraction": {
    "statement": "parse HTML, extract main text",
    "date": "meeting date from page",
    "vote": "extract voting members",
    "dissents": "identify dissenting votes"
  },
  "enrichment": {
    "sentiment_analysis": "hawkish vs dovish",
    "key_phrase_extraction": "data-dependent, patient, etc.",
    "policy_change_detection": "rate change, QE/QT announcements"
  }
}
```

**Implementation Priority**: High (critical for macro analysis)

---

### 4. Goldman Sachs Research

**Access**: Restricted - requires GS client access

**Strategy**:
```python
{
  "method": "manual_upload + pdf_processing (MVP)",
  "long_term": "API integration (if available)",
  "process": [
    "1. Manual download of research PDFs",
    "2. Upload to data/raw/goldman_sachs/",
    "3. Automated PDF parsing",
    "4. Extract text, tables, charts",
    "5. Chunk and index"
  ],
  "pdf_processing": {
    "tool": "PyMuPDF or pypdf",
    "extract": ["text", "tables", "metadata"],
    "ocr": "if needed (for scanned PDFs)"
  },
  "metadata_extraction": {
    "title": "from PDF title or first page",
    "authors": "from byline",
    "date": "from publication date",
    "topics": "from section headings"
  },
  "challenges": [
    "Access restricted to GS clients",
    "PDF format varies (tables, charts)",
    "Copyright concerns"
  ]
}
```

**Implementation Priority**: Low for MVP (manual process OK), High for production

---

### 5. The Economist

**Access**: Subscription required, RSS available

**Strategy**:
```python
{
  "method": "rss_feed + web_scraping",
  "rss_feed": "https://www.economist.com/rss",
  "frequency": "weekly (Thursday publication)",
  "sections": [
    "Finance & Economics",
    "Business",
    "International",
    "Special Reports"
  ],
  "extraction": {
    "rss": "headlines and summaries",
    "full_text": "requires subscription + scraping"
  },
  "alternatives": [
    "Economist API (if available)",
    "Manual article selection and upload"
  ]
}
```

**Implementation Priority**: Medium

---

### 6. Academic Papers (NBER, SSRN)

**Access**: Mostly public, PDFs

**Strategy**:
```python
{
  "method": "api + pdf_download",
  "sources": {
    "nber": {
      "api": "https://www.nber.org/api/",
      "search": "macro-related working papers",
      "frequency": "weekly"
    },
    "ssrn": {
      "search": "economics + macro keywords",
      "frequency": "weekly"
    }
  },
  "filtering": {
    "relevance_threshold": 0.7,
    "keywords": ["monetary policy", "inflation", "business cycles"],
    "citations": "prioritize highly-cited papers"
  },
  "processing": "same as Goldman Sachs research PDFs"
}
```

**Implementation Priority**: Low (nice-to-have for deep research)

---

## Data Processing Pipeline

### 5-Stage Pipeline: RAW → CLEAN → ENRICH → CHUNK → INDEX

```
┌─────────────────────────────────────────────────────────────┐
│ STAGE 1: INGESTION (Source → Raw Storage)                  │
├─────────────────────────────────────────────────────────────┤
│ • Fetch from source (API, RSS, scrape, upload)             │
│ • Store raw content (HTML, PDF, JSON, CSV)                 │
│ • Location: data/raw/{source}/{date}/{filename}            │
│ • No processing - preserve original                         │
│ • Log: ingestion timestamp, source, method                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 2: CLEANING (Raw → Structured)                       │
├─────────────────────────────────────────────────────────────┤
│ • Parse format (HTML→text, PDF→text, JSON→fields)          │
│ • Extract metadata (title, date, author)                    │
│ • Remove boilerplate (ads, nav, footers)                    │
│ • Normalize dates, numbers, entities                        │
│ • Detect language, encoding                                 │
│ • Deduplication check                                       │
│ • Output: Unified Document JSON                             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 3: ENRICHMENT (Structured → Enhanced)                │
├─────────────────────────────────────────────────────────────┤
│ • Classification:                                           │
│   - Content type (news, data, policy, research)            │
│   - Macro themes (inflation, growth, policy)               │
│   - Geography (US, Europe, China, etc.)                    │
│   - Asset class impact (equities, bonds, etc.)             │
│ • Entity extraction:                                        │
│   - People (Jerome Powell, Janet Yellen)                   │
│   - Organizations (Fed, ECB, IMF)                          │
│   - Indicators (CPI, GDP, unemployment)                    │
│ • Sentiment analysis:                                       │
│   - Hawkish/dovish (for policy)                            │
│   - Positive/negative (for markets)                        │
│ • Importance scoring (high/medium/low)                     │
│ • AI-generated summary (if needed)                         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 4: CHUNKING (Enhanced → LLM-Ready)                   │
├─────────────────────────────────────────────────────────────┤
│ • Split long documents into chunks                          │
│ • Chunk size: 500-1000 tokens (configurable)               │
│ • Overlap: 50-100 tokens for context continuity            │
│ • Chunking strategies:                                      │
│   - Semantic (paragraph/section boundaries)                │
│   - Fixed-size (for uniform retrieval)                     │
│   - Sliding window (for dense coverage)                    │
│ • Preserve metadata in each chunk                          │
│ • Generate embeddings (OpenAI, Anthropic, or local)        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STAGE 5: INDEXING (Chunks → Searchable)                    │
├─────────────────────────────────────────────────────────────┤
│ • Vector DB insertion (Supabase pgvector):                 │
│   - Store embeddings                                        │
│   - Create vector indexes (HNSW or IVFFlat)                │
│   - Enable semantic search                                  │
│ • Time-series DB insertion (for numeric data):             │
│   - Store in TimescaleDB hypertables                       │
│   - Index by time and series_id                            │
│ • Full-text search index (PostgreSQL):                     │
│   - For keyword search                                      │
│   - Complement vector search                               │
│ • Graph DB (optional, future):                             │
│   - Store document relationships                           │
│   - Entity co-occurrence graph                             │
└─────────────────────────────────────────────────────────────┘
                            ↓
                    ✅ Ready for Retrieval
```

---

## Storage Architecture

### Multi-Tier Storage Strategy

```
┌───────────────────────────────────────────────────────────┐
│ TIER 1: Raw Storage (data/raw/)                          │
├───────────────────────────────────────────────────────────┤
│ Purpose: Preserve original data, enable reprocessing      │
│ Format: Original (HTML, PDF, JSON, CSV)                   │
│ Organization: {source}/{date}/{filename}                  │
│ Retention: 1 year (configurable)                          │
│ Backup: Yes (S3, cloud storage)                           │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│ TIER 2: Processed Storage (data/processed/)              │
├───────────────────────────────────────────────────────────┤
│ Purpose: Cleaned, structured data                         │
│ Format: JSON (Unified Document Schema)                    │
│ Organization: {source}/{date}/{doc_id}.json               │
│ Includes: Full text + metadata + enrichment               │
│ Human-readable: Yes                                        │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│ TIER 3: Vector Database (Supabase pgvector)              │
├───────────────────────────────────────────────────────────┤
│ Purpose: Semantic search, LLM retrieval                   │
│ Tables:                                                    │
│   - documents (metadata + full text)                      │
│   - chunks (embeddings + text + parent_doc_id)            │
│   - embeddings (vector index)                             │
│ Optimized for: Similarity search, filtering               │
│ LLM-readable: Yes (chunks optimized for context window)   │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│ TIER 4: Time-Series Database (TimescaleDB)               │
├───────────────────────────────────────────────────────────┤
│ Purpose: Numeric macro data (CPI, GDP, rates, etc.)      │
│ Tables:                                                    │
│   - observations (time, series_id, value)                 │
│   - series_metadata (series_id, name, units, freq)        │
│ Optimized for: Time-range queries, aggregations           │
│ Retention: 20+ years of historical data                   │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│ TIER 5: Cache Layer (Redis, optional)                    │
├───────────────────────────────────────────────────────────┤
│ Purpose: Fast access to frequently requested data         │
│ Cached items: Recent briefings, popular queries           │
│ TTL: 1 hour - 24 hours (configurable)                     │
└───────────────────────────────────────────────────────────┘
```

---

## Human & LLM Optimization

### The Dual-Readability Problem

**Challenge**: Same data needs to be:
- **Human-readable**: For review, debugging, trust
- **LLM-optimized**: For retrieval, reasoning, generation

**Solution**: Store both, optimize for each use case

### Human Readability

```json
{
  "display_format": {
    "title": "Clear, descriptive title",
    "summary": "2-3 sentence executive summary",
    "key_points": [
      "• Bullet point 1",
      "• Bullet point 2"
    ],
    "source_citation": "Bloomberg, March 15, 2025",
    "link": "https://...",
    "visual_aids": {
      "charts": ["CPI trend chart"],
      "tables": ["Rate change timeline"]
    }
  },
  "human_review_ui": {
    "tool": "Streamlit dashboard",
    "features": [
      "Browse by date/source/theme",
      "Flag incorrect classifications",
      "Edit metadata",
      "Approve for indexing"
    ]
  }
}
```

### LLM Optimization

```json
{
  "llm_format": {
    "chunking": {
      "strategy": "semantic_paragraphs",
      "size": "500-1000 tokens",
      "overlap": "100 tokens",
      "preserve_structure": "markdown headers"
    },
    "context_enhancement": {
      "prepend_metadata": true,
      "example": "Source: Bloomberg | Date: 2025-03-15 | Topic: Fed Policy\n\n{content}"
    },
    "embedding_optimization": {
      "model": "text-embedding-ada-002",
      "dimensions": 1536,
      "normalization": "L2"
    },
    "retrieval_metadata": {
      "always_include": ["date", "source", "theme"],
      "for_filtering": ["geography", "asset_class"],
      "for_ranking": ["importance", "credibility_score"]
    }
  }
}
```

### Hybrid Search Strategy

**Best Results**: Combine vector search + keyword search + metadata filters

```python
def retrieve_macro_context(query: str, filters: dict):
    """Hybrid retrieval for best precision and recall."""

    # Step 1: Vector search (semantic similarity)
    vector_results = vector_db.similarity_search(
        query_embedding=embed(query),
        top_k=20,
        filters=filters  # date range, themes, geography
    )

    # Step 2: Keyword search (exact matches)
    keyword_results = full_text_search(
        query=query,
        top_k=20,
        filters=filters
    )

    # Step 3: Merge and re-rank
    merged = reciprocal_rank_fusion(vector_results, keyword_results)

    # Step 4: Diversity filter (avoid redundant docs)
    diverse_results = maximal_marginal_relevance(merged, lambda_diversity=0.3)

    # Step 5: Return top K with metadata
    return diverse_results[:5]
```

---

## Implementation Plan

### Phase 1: MVP (Weeks 1-2)

**Priority Sources**:
1. ✅ FRED (easy, free, reliable)
2. ✅ FOMC Statements (critical, public)
3. ✅ RSS Feeds (Bloomberg, Economist, FT - headlines only)

**MVP Pipeline**:
- Ingest → Clean → Store (skip enrichment for now)
- Basic chunking (fixed-size, 800 tokens)
- Simple vector search

**Goal**: Get data flowing and retrievable

---

### Phase 2: Enhancement (Weeks 3-4)

**Add Enrichment**:
- Classification (content type, themes, geography)
- Entity extraction (using spaCy or LLM)
- Sentiment analysis (hawkish/dovish)

**Improve Chunking**:
- Semantic chunking (paragraph boundaries)
- Metadata prepending for context

**Add Sources**:
- Web scraping for full articles (if legal/ToS-compliant)
- Manual PDF uploads (Goldman Sachs research)

---

### Phase 3: Production (Weeks 5-8)

**Advanced Features**:
- Deduplication (cross-source)
- Human review UI (Streamlit dashboard)
- Data quality monitoring
- Automated reprocessing on pipeline updates

**Scaling**:
- Background job queue (Celery, or FastAPI BackgroundTasks)
- Incremental updates (only new data)
- Scheduled ingestion (cron jobs)

---

## Data Quality & Governance

### Data Quality Checks

```python
quality_checks = {
    "completeness": [
        "All required fields present",
        "No null content",
        "Valid dates"
    ],
    "accuracy": [
        "Dates are logical (not in future)",
        "Source credibility verified",
        "Numbers are reasonable"
    ],
    "consistency": [
        "Schema validation",
        "Taxonomy terms valid",
        "No duplicate IDs"
    ],
    "freshness": [
        "Data ingested within SLA",
        "No stale data in production index"
    ]
}
```

### Human Review Workflow

```
Ingest → Auto-Process → [Quality Check]
                              ↓
                         Pass? → Index
                              ↓
                         Fail? → Human Review Queue
                              ↓
                         Approve/Fix → Index
                              ↓
                         Reject → Archive (don't index)
```

---

## Example: End-to-End Flow

### Scenario: FOMC Statement Released

```
1. INGESTION
   - Scraper detects new statement on federalreserve.gov
   - Downloads HTML
   - Saves to data/raw/fomc/2025-03-15/statement.html

2. CLEANING
   - Parse HTML, extract main text
   - Extract metadata: date=2025-03-15, type=fomc_statement
   - Remove navigation, footers
   - Save to data/processed/fomc/2025-03-15/doc_uuid.json

3. ENRICHMENT
   - Classification:
     * content_type: policy
     * themes: [monetary_policy, inflation]
     * geography: [us]
     * asset_classes: [equities, fixed_income, fx]
   - Sentiment: "dovish" (detected phrases: "patient", "data-dependent")
   - Importance: "high" (FOMC always high importance)
   - Entities: [Jerome Powell, FOMC, inflation, rates]

4. CHUNKING
   - Split into 3 chunks (statement is short)
   - Prepend metadata to each chunk
   - Generate embeddings

5. INDEXING
   - Insert into vector DB
   - Create full-text search index
   - Link to related time-series data (Fed Funds Rate)

6. RETRIEVAL (later)
   - User asks: "What did the Fed say about inflation?"
   - Vector search finds this document
   - Agent reads and reasons
   - Generates insight
```

---

## Tooling & Libraries

### Ingestion
- `requests` - HTTP requests
- `httpx` - Async HTTP
- `feedparser` - RSS feeds
- `beautifulsoup4` - HTML parsing
- `fredapi` - FRED API client
- `PyMuPDF` or `pypdf` - PDF parsing

### Processing
- `spaCy` - NLP (entity extraction)
- `langchain` - Text splitting, chunking
- `tiktoken` - Token counting
- `markdownify` - HTML to Markdown

### Storage
- `supabase-py` - Supabase client
- `pgvector` - Vector DB
- `sqlalchemy` - ORM
- `redis-py` - Caching (optional)

### Enrichment
- `anthropic` - Claude API (for classification)
- `openai` - Embeddings
- `transformers` - Local models (optional)

---

## Next Steps

1. **Review & Approve** this strategy
2. **Create** `DATA_SCHEMA.md` with detailed table schemas
3. **Implement** FRED ingestion (easiest first)
4. **Build** processing pipeline in `src/ingestion/`
5. **Test** with sample data in Jupyter notebook

---

**Questions? Refinements needed? Let's discuss!**
