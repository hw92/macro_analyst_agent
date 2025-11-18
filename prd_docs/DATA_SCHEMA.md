# Data Schema - Macro AI Agent

**Version**: 1.0
**Last Updated**: 2025-11-18
**Database**: PostgreSQL 15+ with pgvector and TimescaleDB extensions

---

## Table of Contents

1. [Overview](#overview)
2. [Database Extensions](#database-extensions)
3. [Core Tables](#core-tables)
4. [Time-Series Tables](#time-series-tables)
5. [Taxonomy Tables](#taxonomy-tables)
6. [User & Portfolio Tables](#user--portfolio-tables)
7. [Indexes & Performance](#indexes--performance)
8. [Schema Diagrams](#schema-diagrams)

---

## Overview

### Design Principles

1. **Separation of Concerns**: Text data (documents) vs. numeric data (time-series)
2. **Denormalization for Speed**: Store metadata with chunks for fast retrieval
3. **Flexibility**: JSONB for semi-structured data
4. **Scalability**: Partitioning for large tables
5. **Human-Readable**: Use ENUMs and readable values

---

## Database Extensions

```sql
-- Enable required PostgreSQL extensions
CREATE EXTENSION IF NOT EXISTS vector;        -- pgvector for embeddings
CREATE EXTENSION IF NOT EXISTS timescaledb;   -- TimescaleDB for time-series
CREATE EXTENSION IF NOT EXISTS pg_trgm;       -- Full-text search (trigram)
CREATE EXTENSION IF NOT EXISTS btree_gin;     -- GIN indexes for JSONB
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";   -- UUID generation
```

---

## Core Tables

### 1. `documents` - Master Document Table

Stores all macro documents (news, research, policy statements).

```sql
CREATE TABLE documents (
    -- Identity
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_id TEXT,  -- Original ID from source (if exists)
    url TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),

    -- Content (Human-readable)
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    summary TEXT,
    language VARCHAR(10) DEFAULT 'en',

    -- Source metadata
    source_name VARCHAR(100) NOT NULL,  -- 'Bloomberg', 'FRED', 'FOMC', etc.
    source_type VARCHAR(50) NOT NULL,   -- 'news', 'data', 'policy', 'research'
    source_credibility DECIMAL(3,2) DEFAULT 0.80,  -- 0.00 to 1.00
    is_paywalled BOOLEAN DEFAULT false,

    -- Temporal metadata
    published_at TIMESTAMPTZ NOT NULL,
    ingested_at TIMESTAMPTZ DEFAULT NOW(),
    effective_date DATE,  -- When the event/data is effective
    data_vintage DATE,    -- For economic data (e.g., CPI for Feb published in Mar)

    -- Classification
    content_type VARCHAR(50) NOT NULL,  -- 'news', 'analysis', 'data_release', etc.
    macro_themes TEXT[],                -- ['inflation', 'monetary_policy']
    geography TEXT[],                   -- ['us', 'global']
    asset_classes TEXT[],               -- ['equities', 'fixed_income']
    sentiment VARCHAR(20),              -- 'hawkish', 'dovish', 'neutral', 'positive', 'negative'
    importance VARCHAR(20),             -- 'high', 'medium', 'low'

    -- Entities (extracted)
    entities JSONB,  -- {"people": [...], "organizations": [...], "indicators": [...]}

    -- AI-generated analysis
    ai_analysis JSONB,  -- {"key_takeaways": [...], "macro_regime": "...", ...}

    -- Provenance
    ingestion_method VARCHAR(50),       -- 'rss_feed', 'web_scraping', 'api', 'manual_upload'
    processing_version VARCHAR(20),
    verification_status VARCHAR(20) DEFAULT 'pending',  -- 'pending', 'verified', 'flagged'
    human_reviewed BOOLEAN DEFAULT false,

    -- Relations
    related_document_ids UUID[],
    related_data_series TEXT[],  -- e.g., ['FRED:CPIAUCSL']
    references TEXT[],           -- URLs or citations

    -- Full-text search
    content_tsv TSVECTOR GENERATED ALWAYS AS (
        to_tsvector('english', coalesce(title, '') || ' ' || coalesce(content, ''))
    ) STORED
);

-- Indexes
CREATE INDEX idx_documents_published_at ON documents(published_at DESC);
CREATE INDEX idx_documents_source_name ON documents(source_name);
CREATE INDEX idx_documents_content_type ON documents(content_type);
CREATE INDEX idx_documents_macro_themes ON documents USING GIN(macro_themes);
CREATE INDEX idx_documents_geography ON documents USING GIN(geography);
CREATE INDEX idx_documents_asset_classes ON documents USING GIN(asset_classes);
CREATE INDEX idx_documents_entities ON documents USING GIN(entities);
CREATE INDEX idx_documents_content_tsv ON documents USING GIN(content_tsv);

-- Full-text search function
CREATE INDEX idx_documents_fts ON documents USING GIN(content_tsv);
```

---

### 2. `chunks` - Document Chunks for LLM Retrieval

Stores document chunks with embeddings for semantic search.

```sql
CREATE TABLE chunks (
    -- Identity
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    chunk_index INTEGER NOT NULL,  -- Position in document (0, 1, 2, ...)
    created_at TIMESTAMPTZ DEFAULT NOW(),

    -- Content
    text TEXT NOT NULL,
    token_count INTEGER,

    -- Embedding (1536 dimensions for OpenAI ada-002)
    embedding vector(1536),

    -- Metadata (denormalized from parent document for fast filtering)
    published_at TIMESTAMPTZ NOT NULL,
    source_name VARCHAR(100) NOT NULL,
    content_type VARCHAR(50) NOT NULL,
    macro_themes TEXT[],
    geography TEXT[],
    asset_classes TEXT[],
    importance VARCHAR(20),

    -- Constraints
    UNIQUE(document_id, chunk_index)
);

-- Indexes
CREATE INDEX idx_chunks_document_id ON chunks(document_id);
CREATE INDEX idx_chunks_published_at ON chunks(published_at DESC);
CREATE INDEX idx_chunks_source_name ON chunks(source_name);
CREATE INDEX idx_chunks_macro_themes ON chunks USING GIN(macro_themes);

-- Vector similarity index (HNSW for best performance)
CREATE INDEX idx_chunks_embedding ON chunks USING hnsw(embedding vector_cosine_ops);

-- Alternative: IVFFlat (faster build, slower query)
-- CREATE INDEX idx_chunks_embedding ON chunks USING ivfflat(embedding vector_cosine_ops) WITH (lists = 100);
```

---

### 3. `ingestion_log` - Track All Ingestion Runs

```sql
CREATE TABLE ingestion_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source_name VARCHAR(100) NOT NULL,
    ingestion_method VARCHAR(50) NOT NULL,
    started_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    status VARCHAR(20) NOT NULL,  -- 'running', 'success', 'failed', 'partial'
    documents_fetched INTEGER DEFAULT 0,
    documents_processed INTEGER DEFAULT 0,
    documents_indexed INTEGER DEFAULT 0,
    errors JSONB,  -- Array of error messages
    metadata JSONB  -- Additional run details
);

CREATE INDEX idx_ingestion_log_source ON ingestion_log(source_name);
CREATE INDEX idx_ingestion_log_started_at ON ingestion_log(started_at DESC);
```

---

## Time-Series Tables

### 4. `time_series_metadata` - Economic Indicator Metadata

```sql
CREATE TABLE time_series_metadata (
    series_id VARCHAR(100) PRIMARY KEY,  -- e.g., 'FRED:CPIAUCSL'
    source VARCHAR(50) NOT NULL,         -- 'FRED', 'BLS', 'ECB', etc.
    name TEXT NOT NULL,                  -- 'Consumer Price Index for All Urban Consumers'
    description TEXT,
    units VARCHAR(100),                  -- 'Index 1982-1984=100', 'Percent', etc.
    frequency VARCHAR(20),               -- 'monthly', 'quarterly', 'annual', 'daily'
    seasonal_adjustment VARCHAR(50),     -- 'Seasonally Adjusted', 'Not Seasonally Adjusted'
    geography VARCHAR(50) DEFAULT 'us',  -- 'us', 'eu', 'cn', etc.
    category VARCHAR(50),                -- 'inflation', 'employment', 'rates', etc.
    source_url TEXT,
    last_updated TIMESTAMPTZ,
    notes TEXT,
    metadata JSONB
);

CREATE INDEX idx_ts_metadata_source ON time_series_metadata(source);
CREATE INDEX idx_ts_metadata_category ON time_series_metadata(category);
CREATE INDEX idx_ts_metadata_geography ON time_series_metadata(geography);
```

---

### 5. `time_series_observations` - Actual Economic Data

**Note**: This table uses TimescaleDB hypertable for time-series optimization.

```sql
CREATE TABLE time_series_observations (
    time TIMESTAMPTZ NOT NULL,
    series_id VARCHAR(100) NOT NULL REFERENCES time_series_metadata(series_id),
    value DOUBLE PRECISION,
    value_text TEXT,  -- For non-numeric values (rare)
    is_preliminary BOOLEAN DEFAULT false,
    is_revised BOOLEAN DEFAULT false,
    revision_number INTEGER DEFAULT 0,
    metadata JSONB,

    PRIMARY KEY (series_id, time)
);

-- Convert to TimescaleDB hypertable
SELECT create_hypertable('time_series_observations', 'time', chunk_time_interval => INTERVAL '1 month');

-- Indexes
CREATE INDEX idx_ts_obs_series_id ON time_series_observations(series_id, time DESC);
CREATE INDEX idx_ts_obs_time ON time_series_observations(time DESC);

-- Continuous aggregate for monthly averages (example)
CREATE MATERIALIZED VIEW ts_monthly_avg
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 month', time) AS bucket,
    series_id,
    AVG(value) AS avg_value,
    MIN(value) AS min_value,
    MAX(value) AS max_value,
    COUNT(*) AS observation_count
FROM time_series_observations
GROUP BY bucket, series_id
WITH NO DATA;

-- Refresh policy (auto-update every day)
SELECT add_continuous_aggregate_policy('ts_monthly_avg',
    start_offset => INTERVAL '3 months',
    end_offset => INTERVAL '1 day',
    schedule_interval => INTERVAL '1 day');
```

---

## Taxonomy Tables

### 6. `macro_ontology` - Concept Graph

Stores relationships between macro concepts (inflation → rates → bonds).

```sql
CREATE TABLE macro_ontology (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    concept VARCHAR(100) NOT NULL UNIQUE,
    category VARCHAR(50),  -- 'indicator', 'policy', 'market', 'theme'
    definition TEXT,
    related_concepts JSONB,  -- {"parent": [...], "children": [...], "related": [...]}
    impact_on_assets JSONB,  -- {"equities": "negative", "bonds": "positive", ...}
    tags TEXT[],
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_ontology_concept ON macro_ontology(concept);
CREATE INDEX idx_ontology_category ON macro_ontology(category);
CREATE INDEX idx_ontology_tags ON macro_ontology USING GIN(tags);
```

---

### 7. `macro_themes` - Theme Taxonomy

```sql
CREATE TABLE macro_themes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    category VARCHAR(50),  -- 'inflation', 'growth', 'policy', 'markets', 'geopolitics'
    description TEXT,
    keywords TEXT[],  -- For auto-classification
    parent_theme_id INTEGER REFERENCES macro_themes(id),
    level INTEGER DEFAULT 0  -- 0 = top-level, 1 = sub-theme, etc.
);

-- Example data
INSERT INTO macro_themes (name, category, description, keywords) VALUES
    ('inflation', 'macro', 'Price level changes', ARRAY['CPI', 'inflation', 'deflation', 'prices']),
    ('monetary_policy', 'policy', 'Central bank actions', ARRAY['Fed', 'ECB', 'interest rates', 'QE', 'hawkish', 'dovish']),
    ('growth', 'macro', 'Economic growth', ARRAY['GDP', 'growth', 'recession', 'expansion']),
    ('employment', 'macro', 'Labor market', ARRAY['unemployment', 'jobs', 'NFP', 'wages']);
```

---

## User & Portfolio Tables

### 8. `users` - User Accounts

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    last_login_at TIMESTAMPTZ,

    -- Profile
    risk_profile VARCHAR(20) DEFAULT 'moderate',  -- 'conservative', 'moderate', 'aggressive'
    investment_horizon VARCHAR(20),               -- 'short', 'medium', 'long'
    experience_level VARCHAR(20),                 -- 'beginner', 'intermediate', 'advanced'

    -- Preferences
    preferences JSONB,  -- {"themes": [...], "geography": [...], "notification_frequency": "..."}

    -- Status
    is_active BOOLEAN DEFAULT true,
    subscription_tier VARCHAR(20) DEFAULT 'free'  -- 'free', 'basic', 'premium'
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_risk_profile ON users(risk_profile);
```

---

### 9. `portfolios` - User Portfolios

```sql
CREATE TABLE portfolios (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(200) DEFAULT 'My Portfolio',
    is_default BOOLEAN DEFAULT false,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),

    -- Holdings (simplified for MVP)
    holdings JSONB NOT NULL,  -- {"equities": 0.60, "bonds": 0.30, "cash": 0.10, ...}

    -- Metadata
    total_value DECIMAL(15,2),
    currency VARCHAR(10) DEFAULT 'USD',

    UNIQUE(user_id, name)
);

CREATE INDEX idx_portfolios_user_id ON portfolios(user_id);
```

---

### 10. `user_queries` - Query History & Feedback

```sql
CREATE TABLE user_queries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    session_id UUID,

    -- Query
    query TEXT NOT NULL,
    query_type VARCHAR(50),  -- 'chat', 'briefing', 'actions'
    created_at TIMESTAMPTZ DEFAULT NOW(),

    -- Response
    response JSONB NOT NULL,  -- Full agent response
    documents_retrieved UUID[],  -- Document IDs used
    data_series_retrieved TEXT[],  -- Time-series used

    -- Performance
    response_time_ms INTEGER,
    token_count INTEGER,

    -- Feedback
    user_rating INTEGER CHECK (user_rating BETWEEN 1 AND 5),
    user_feedback TEXT,
    flagged BOOLEAN DEFAULT false,
    flag_reason TEXT
);

CREATE INDEX idx_user_queries_user_id ON user_queries(user_id);
CREATE INDEX idx_user_queries_created_at ON user_queries(created_at DESC);
CREATE INDEX idx_user_queries_flagged ON user_queries(flagged) WHERE flagged = true;
```

---

### 11. `action_suggestions` - Portfolio Actions Generated

```sql
CREATE TABLE action_suggestions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    portfolio_id UUID REFERENCES portfolios(id) ON DELETE CASCADE,
    query_id UUID REFERENCES user_queries(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),

    -- Context
    macro_regime VARCHAR(100),  -- 'inflation_rising_hawkish_fed'
    triggering_event TEXT,      -- 'CPI increased 0.4% MoM'

    -- Actions
    actions JSONB NOT NULL,  -- [{"action": "...", "rationale": "...", "risk_note": "..."}]

    -- User interaction
    viewed BOOLEAN DEFAULT false,
    acted_on BOOLEAN DEFAULT false,
    dismissed BOOLEAN DEFAULT false,
    user_notes TEXT
);

CREATE INDEX idx_action_suggestions_user_id ON action_suggestions(user_id);
CREATE INDEX idx_action_suggestions_created_at ON action_suggestions(created_at DESC);
CREATE INDEX idx_action_suggestions_acted_on ON action_suggestions(acted_on);
```

---

## Indexes & Performance

### Vector Search Performance

```sql
-- HNSW index parameters (tune based on dataset size)
-- m: number of connections per layer (default 16, higher = better recall, slower build)
-- ef_construction: size of dynamic candidate list (default 64, higher = better quality, slower build)

CREATE INDEX idx_chunks_embedding ON chunks
USING hnsw(embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- At query time, set ef_search (higher = better recall, slower query)
SET hnsw.ef_search = 40;  -- Default is 40
```

### Composite Indexes for Common Queries

```sql
-- Query: Recent documents by theme
CREATE INDEX idx_documents_theme_date ON documents(macro_themes, published_at DESC);

-- Query: Chunks by source and date (for filtered retrieval)
CREATE INDEX idx_chunks_source_date ON chunks(source_name, published_at DESC);

-- Query: Time-series by geography and category
CREATE INDEX idx_ts_metadata_geo_cat ON time_series_metadata(geography, category);
```

### Partitioning (For Large-Scale Deployment)

```sql
-- Partition documents by month (for very large datasets)
CREATE TABLE documents_partitioned (
    LIKE documents INCLUDING ALL
) PARTITION BY RANGE (published_at);

-- Create monthly partitions
CREATE TABLE documents_2025_01 PARTITION OF documents_partitioned
    FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE documents_2025_02 PARTITION OF documents_partitioned
    FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');

-- etc.
```

---

## Schema Diagrams

### Entity Relationship Diagram (Simplified)

```
┌─────────────────────┐
│     documents       │
│ ─────────────────── │
│ • id (PK)           │
│ • title             │
│ • content           │
│ • source_name       │
│ • published_at      │
│ • macro_themes[]    │
│ • ...               │
└─────────────────────┘
          │
          │ 1:N
          ▼
┌─────────────────────┐
│      chunks         │
│ ─────────────────── │
│ • id (PK)           │
│ • document_id (FK)  │
│ • text              │
│ • embedding vector  │
│ • macro_themes[]    │
│ • ...               │
└─────────────────────┘

┌─────────────────────┐       ┌─────────────────────┐
│ ts_metadata         │ 1:N   │ ts_observations     │
│ ─────────────────── │───────│ ─────────────────── │
│ • series_id (PK)    │       │ • series_id (FK)    │
│ • name              │       │ • time              │
│ • units             │       │ • value             │
│ • category          │       │ • ...               │
└─────────────────────┘       └─────────────────────┘

┌─────────────────────┐       ┌─────────────────────┐
│       users         │ 1:N   │    portfolios       │
│ ─────────────────── │───────│ ─────────────────── │
│ • id (PK)           │       │ • id (PK)           │
│ • email             │       │ • user_id (FK)      │
│ • risk_profile      │       │ • holdings JSONB    │
└─────────────────────┘       └─────────────────────┘
          │
          │ 1:N
          ▼
┌─────────────────────┐
│   user_queries      │
│ ─────────────────── │
│ • id (PK)           │
│ • user_id (FK)      │
│ • query             │
│ • response JSONB    │
└─────────────────────┘
          │
          │ 1:N
          ▼
┌─────────────────────┐
│ action_suggestions  │
│ ─────────────────── │
│ • id (PK)           │
│ • user_id (FK)      │
│ • actions JSONB     │
└─────────────────────┘
```

---

## Database Setup Scripts

### Complete Initialization Script

```sql
-- File: scripts/init_db.sql

-- 1. Enable extensions
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS timescaledb;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS btree_gin;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. Create tables (in dependency order)
-- [Insert all CREATE TABLE statements from above]

-- 3. Create views
CREATE VIEW recent_documents AS
SELECT
    id, title, source_name, published_at, macro_themes, importance
FROM documents
WHERE published_at >= NOW() - INTERVAL '7 days'
ORDER BY published_at DESC;

CREATE VIEW high_importance_unread AS
SELECT *
FROM documents
WHERE importance = 'high'
  AND id NOT IN (SELECT unnest(documents_retrieved) FROM user_queries)
ORDER BY published_at DESC;

-- 4. Create functions
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply to tables with updated_at
CREATE TRIGGER update_documents_updated_at BEFORE UPDATE ON documents
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_portfolios_updated_at BEFORE UPDATE ON portfolios
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- 5. Insert seed data
-- [Macro themes, sample ontology, etc.]

-- 6. Grant permissions (for app user)
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_user;
```

---

## Data Migration & Versioning

### Schema Versioning

```sql
CREATE TABLE schema_versions (
    version INTEGER PRIMARY KEY,
    description TEXT,
    applied_at TIMESTAMPTZ DEFAULT NOW(),
    script_name TEXT
);

-- Track current version
INSERT INTO schema_versions (version, description, script_name) VALUES
    (1, 'Initial schema', 'V1__initial_schema.sql');
```

### Migration Example (Add new column)

```sql
-- V2__add_ai_confidence.sql

BEGIN;

-- Add column
ALTER TABLE documents ADD COLUMN ai_confidence DECIMAL(3,2);

-- Backfill (optional)
UPDATE documents SET ai_confidence = 0.80 WHERE ai_analysis IS NOT NULL;

-- Update version
INSERT INTO schema_versions (version, description, script_name) VALUES
    (2, 'Add AI confidence score', 'V2__add_ai_confidence.sql');

COMMIT;
```

---

## Sample Queries

### 1. Semantic Search with Filters

```sql
-- Find documents similar to query embedding, filtered by theme and date
SELECT
    d.id,
    d.title,
    d.published_at,
    d.source_name,
    c.text,
    1 - (c.embedding <=> :query_embedding) AS similarity
FROM chunks c
JOIN documents d ON c.document_id = d.id
WHERE
    c.published_at >= :start_date
    AND c.published_at <= :end_date
    AND c.macro_themes && :themes  -- Overlaps with array
ORDER BY c.embedding <=> :query_embedding  -- Cosine distance
LIMIT 5;
```

### 2. Get Time-Series Data

```sql
-- Get CPI data for last 12 months
SELECT
    time,
    value,
    series_id
FROM time_series_observations
WHERE
    series_id = 'FRED:CPIAUCSL'
    AND time >= NOW() - INTERVAL '12 months'
ORDER BY time DESC;
```

### 3. User Portfolio with Recent Actions

```sql
-- Get user's portfolio and recent action suggestions
SELECT
    p.name AS portfolio_name,
    p.holdings,
    p.total_value,
    a.actions,
    a.created_at,
    a.acted_on
FROM portfolios p
LEFT JOIN action_suggestions a ON p.id = a.portfolio_id
WHERE p.user_id = :user_id
  AND a.created_at >= NOW() - INTERVAL '30 days'
ORDER BY a.created_at DESC;
```

### 4. Document Statistics

```sql
-- Count documents by source and content type
SELECT
    source_name,
    content_type,
    COUNT(*) AS doc_count,
    MAX(published_at) AS latest_document
FROM documents
WHERE published_at >= NOW() - INTERVAL '7 days'
GROUP BY source_name, content_type
ORDER BY doc_count DESC;
```

---

## Next Steps

1. **Review** this schema with the team
2. **Create** `scripts/init_db.sql` with complete setup
3. **Set up** Supabase project and run initialization
4. **Test** with sample data
5. **Optimize** indexes based on query patterns

---

**Questions or need modifications? Let's refine this!**
