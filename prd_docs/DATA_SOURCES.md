# Data Sources - Detailed Ingestion Guide

**Version**: 1.0
**Last Updated**: 2025-11-18

---

## Priority Matrix

| Source | Priority | Difficulty | Cost | Value | MVP Status |
|--------|----------|------------|------|-------|------------|
| **FRED** | ⭐⭐⭐ High | Easy | Free | High | ✅ Include |
| **FOMC** | ⭐⭐⭐ High | Medium | Free | High | ✅ Include |
| **RSS Feeds** | ⭐⭐ Medium | Easy | Free | Medium | ✅ Include |
| **Bloomberg** | ⭐⭐ Medium | Hard | Paid | High | 🔶 Partial |
| **The Economist** | ⭐ Low | Medium | Paid | Medium | ❌ Future |
| **Goldman Sachs** | ⭐ Low | Hard | Restricted | High | 🔶 Manual |
| **NBER/Academic** | ⭐ Low | Medium | Free | Medium | ❌ Future |

---

## 1. FRED (Federal Reserve Economic Data)

### Overview
- **URL**: https://fred.stlouisfed.org/
- **Access**: Free API, generous rate limits
- **Data Type**: Time-series economic indicators
- **Update Frequency**: Varies by series (daily to annual)
- **MVP Status**: ✅ **Critical - Implement First**

### API Details

```python
# Get API key: https://fred.stlouisfed.org/docs/api/api_key.html
API_BASE_URL = "https://api.stlouisfed.org/fred"
API_KEY = "your_fred_api_key"

# Rate limit: 120 requests/minute
RATE_LIMIT = 120
```

### Key Series to Track

```python
PRIORITY_SERIES = {
    # Inflation
    "CPIAUCSL": "CPI for All Urban Consumers",
    "CPILFESL": "Core CPI (ex food & energy)",
    "PCEPI": "Personal Consumption Expenditures Price Index",
    "PCEPILFE": "Core PCE Price Index",

    # Employment
    "UNRATE": "Unemployment Rate",
    "PAYEMS": "Nonfarm Payrolls",
    "CIVPART": "Labor Force Participation Rate",
    "AHETPI": "Average Hourly Earnings",

    # GDP & Growth
    "GDP": "Gross Domestic Product",
    "GDPC1": "Real GDP",
    "A191RL1Q225SBEA": "Real GDP Growth Rate",

    # Interest Rates
    "DFF": "Federal Funds Effective Rate",
    "DGS2": "2-Year Treasury Rate",
    "DGS10": "10-Year Treasury Rate",
    "DGS30": "30-Year Treasury Rate",

    # Yield Curve
    "T10Y2Y": "10-Year minus 2-Year Treasury Spread",
    "T10Y3M": "10-Year minus 3-Month Treasury Spread",

    # Credit & Markets
    "BAMLH0A0HYM2": "High Yield Spread",
    "VIXCLS": "VIX Volatility Index",

    # Currency
    "DEXUSEU": "USD/EUR Exchange Rate",
    "DEXCHUS": "CNY/USD Exchange Rate",

    # Sentiment
    "UMCSENT": "University of Michigan Consumer Sentiment",
    "MANEMP": "ISM Manufacturing PMI",

    # Housing
    "MORTGAGE30US": "30-Year Mortgage Rate",
    "CSUSHPISA": "Case-Shiller Home Price Index",

    # Money Supply
    "M2SL": "M2 Money Stock",
    "WALCL": "Fed Balance Sheet Total Assets"
}
```

### Implementation

```python
# src/ingestion/econ_data.py

from fredapi import Fred
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict

class FREDIngestion:
    def __init__(self, api_key: str):
        self.fred = Fred(api_key=api_key)
        self.series_cache = {}

    def fetch_series(self, series_id: str, lookback_days: int = 365) -> pd.DataFrame:
        """
        Fetch a single time series from FRED.

        Args:
            series_id: FRED series ID (e.g., 'CPIAUCSL')
            lookback_days: How many days of history to fetch

        Returns:
            DataFrame with date index and value column
        """
        start_date = datetime.now() - timedelta(days=lookback_days)

        try:
            # Fetch data
            data = self.fred.get_series(series_id, observation_start=start_date)

            # Get metadata
            info = self.fred.get_series_info(series_id)

            return {
                "series_id": f"FRED:{series_id}",
                "data": data,
                "metadata": {
                    "name": info.get('title'),
                    "units": info.get('units'),
                    "frequency": info.get('frequency'),
                    "seasonal_adjustment": info.get('seasonal_adjustment'),
                    "last_updated": info.get('last_updated'),
                    "notes": info.get('notes')
                }
            }
        except Exception as e:
            print(f"Error fetching {series_id}: {e}")
            return None

    def fetch_all_priority_series(self) -> Dict:
        """Fetch all priority series."""
        results = {}
        for series_id, description in PRIORITY_SERIES.items():
            print(f"Fetching {series_id}: {description}")
            result = self.fetch_series(series_id)
            if result:
                results[series_id] = result
            time.sleep(0.5)  # Respect rate limit

        return results

    def store_to_db(self, series_data: Dict):
        """Store time-series data to TimescaleDB."""
        # Implementation in src/knowledge/time_series.py
        pass
```

### Ingestion Schedule

```python
# Daily ingestion at 10 AM ET (after most releases)
CRON_SCHEDULE = "0 10 * * *"

# Priority: Daily update for market-moving series
DAILY_SERIES = ["DFF", "DGS10", "VIXCLS", "DEXUSEU"]

# Weekly update for slower-moving series
WEEKLY_SERIES = ["M2SL", "UMCSENT"]

# Monthly update for monthly releases
MONTHLY_SERIES = ["CPIAUCSL", "UNRATE", "PAYEMS", "GDP"]
```

---

## 2. FOMC & Federal Reserve

### Overview
- **URL**: https://www.federalreserve.gov/
- **Access**: Public, no authentication
- **Data Type**: Policy statements, speeches, minutes
- **Update Frequency**: Event-driven (8 FOMC meetings/year)
- **MVP Status**: ✅ **Critical - Implement First**

### Content Types

```python
FOMC_CONTENT_TYPES = {
    "statements": {
        "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
        "frequency": "8x/year",
        "importance": "critical"
    },
    "minutes": {
        "url": "https://www.federalreserve.gov/monetarypolicy/fomcminutes{year}.htm",
        "frequency": "8x/year (3 weeks after meeting)",
        "importance": "high"
    },
    "speeches": {
        "url": "https://www.federalreserve.gov/newsevents/speeches.htm",
        "frequency": "weekly",
        "importance": "medium"
    },
    "testimonies": {
        "url": "https://www.federalreserve.gov/newsevents/testimony.htm",
        "frequency": "quarterly",
        "importance": "high"
    },
    "beige_book": {
        "url": "https://www.federalreserve.gov/monetarypolicy/beige-book-default.htm",
        "frequency": "8x/year",
        "importance": "medium"
    }
}
```

### Implementation

```python
# src/ingestion/fomc_scraper.py

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List, Dict

class FOMCScraper:
    def __init__(self):
        self.base_url = "https://www.federalreserve.gov"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macro AI Agent; +https://yoursite.com)"
        }

    def scrape_latest_statement(self) -> Dict:
        """Scrape the latest FOMC statement."""
        url = f"{self.base_url}/monetarypolicy/fomccalendars.htm"

        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find latest statement link
        statement_link = soup.find('a', text=lambda t: t and 'FOMC statement' in t)

        if statement_link:
            statement_url = self.base_url + statement_link['href']
            statement_response = requests.get(statement_url, headers=self.headers)
            statement_soup = BeautifulSoup(statement_response.content, 'html.parser')

            # Extract content
            content_div = statement_soup.find('div', class_='col-xs-12 col-sm-8 col-md-8')
            text = content_div.get_text(strip=True) if content_div else ""

            # Extract date
            date_element = statement_soup.find('p', class_='article__time')
            date_str = date_element.get_text(strip=True) if date_element else ""

            return {
                "title": "FOMC Statement",
                "content": text,
                "url": statement_url,
                "published_at": self._parse_date(date_str),
                "source_name": "Federal Reserve",
                "content_type": "policy",
                "macro_themes": ["monetary_policy"],
                "geography": ["us"],
                "importance": "high"
            }

        return None

    def scrape_speeches(self, limit: int = 10) -> List[Dict]:
        """Scrape recent Fed speeches."""
        url = f"{self.base_url}/newsevents/speeches.htm"
        # Similar implementation...
        pass

    def _parse_date(self, date_str: str) -> datetime:
        """Parse Fed date formats."""
        # Implementation varies by page format
        pass
```

### Sentiment Analysis

```python
# For FOMC statements, extract hawkish/dovish signals

HAWKISH_PHRASES = [
    "persistent inflation",
    "inflation pressures",
    "further increases",
    "additional tightening",
    "restrictive policy",
    "vigilant",
    "committed to bringing inflation down"
]

DOVISH_PHRASES = [
    "inflation has moderated",
    "disinflation",
    "patient",
    "data-dependent",
    "judicious",
    "monitor",
    "sufficient restrictiveness"
]

def classify_fomc_sentiment(text: str) -> str:
    """Classify FOMC statement as hawkish/dovish/neutral."""
    hawkish_count = sum(1 for phrase in HAWKISH_PHRASES if phrase in text.lower())
    dovish_count = sum(1 for phrase in DOVISH_PHRASES if phrase in text.lower())

    if hawkish_count > dovish_count + 2:
        return "hawkish"
    elif dovish_count > hawkish_count + 2:
        return "dovish"
    else:
        return "neutral"
```

---

## 3. RSS Feeds (News Aggregation)

### Overview
- **Access**: Free (headlines), paywalled (full text)
- **Data Type**: Macro news, analysis
- **Update Frequency**: Real-time
- **MVP Status**: ✅ **Include (headlines only)**

### RSS Feed Sources

```python
RSS_FEEDS = {
    "bloomberg": {
        "markets": "https://www.bloomberg.com/feeds/markets/news.rss",
        "economics": "https://www.bloomberg.com/feeds/economics/news.rss",
        "politics": "https://www.bloomberg.com/feeds/politics/news.rss"
    },
    "reuters": {
        "business": "https://www.reutersagency.com/feed/?best-topics=business-finance",
        "economy": "https://www.reutersagency.com/feed/?best-topics=economy"
    },
    "ft": {
        "markets": "https://www.ft.com/markets?format=rss",
        "economics": "https://www.ft.com/economics?format=rss"
    },
    "wsj": {
        "economy": "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
        "markets": "https://feeds.a.dj.com/rss/RSSMarketsMain.xml"
    },
    "economist": {
        "finance": "https://www.economist.com/finance-and-economics/rss.xml",
        "business": "https://www.economist.com/business/rss.xml"
    }
}
```

### Implementation

```python
# src/ingestion/news_fetcher.py

import feedparser
from datetime import datetime
from typing import List, Dict

class RSSFeedIngestion:
    def __init__(self):
        self.feeds = RSS_FEEDS

    def fetch_feed(self, feed_url: str) -> List[Dict]:
        """Fetch and parse an RSS feed."""
        feed = feedparser.parse(feed_url)

        articles = []
        for entry in feed.entries:
            articles.append({
                "title": entry.get('title'),
                "summary": entry.get('summary', entry.get('description', '')),
                "url": entry.get('link'),
                "published_at": self._parse_date(entry.get('published')),
                "source_name": feed.feed.get('title', 'Unknown'),
                "content_type": "news",
                # Note: Full text requires scraping (check robots.txt, ToS)
                "full_text_available": False
            })

        return articles

    def fetch_all_feeds(self) -> List[Dict]:
        """Fetch all configured RSS feeds."""
        all_articles = []

        for source, feeds in self.feeds.items():
            for feed_name, feed_url in feeds.items():
                print(f"Fetching {source}/{feed_name}...")
                articles = self.fetch_feed(feed_url)

                # Add source metadata
                for article in articles:
                    article['feed_source'] = source
                    article['feed_category'] = feed_name

                all_articles.extend(articles)
                time.sleep(1)  # Be respectful

        return all_articles

    def _parse_date(self, date_str: str) -> datetime:
        """Parse RSS date formats."""
        from email.utils import parsedate_to_datetime
        try:
            return parsedate_to_datetime(date_str)
        except:
            return datetime.now()
```

### Deduplication Strategy

```python
def deduplicate_news(articles: List[Dict]) -> List[Dict]:
    """
    Remove duplicate articles (same event from multiple sources).

    Strategy:
    1. Normalize titles (lowercase, remove punctuation)
    2. Calculate title similarity (Jaccard or edit distance)
    3. Keep article from highest-credibility source
    """
    from difflib import SequenceMatcher

    def similarity(a, b):
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    unique_articles = []
    seen_titles = []

    for article in articles:
        title = article['title']

        # Check similarity with existing titles
        is_duplicate = False
        for seen_title in seen_titles:
            if similarity(title, seen_title) > 0.85:  # Threshold
                is_duplicate = True
                break

        if not is_duplicate:
            unique_articles.append(article)
            seen_titles.append(title)

    return unique_articles
```

---

## 4. Bloomberg

### Overview
- **Access**: Subscription required (Bloomberg Terminal or Bloomberg Professional Services)
- **Data Type**: News, analysis, market data
- **Cost**: $2000+/month (Terminal), $300+/month (Professional Services)
- **MVP Status**: 🔶 **Partial (RSS only for MVP)**

### Options

#### Option A: Bloomberg Terminal API (if available)
```python
# Requires Bloomberg Terminal installation
# Uses blpapi library

from blpapi import Session, SessionOptions

def fetch_bloomberg_news(query: str):
    """Fetch news using Bloomberg Terminal API."""
    # Requires Terminal subscription
    # Implementation requires BLPAPI documentation
    pass
```

#### Option B: Bloomberg Professional Services Feed
- Structured data feed
- API access
- Subscription required

#### Option C: RSS + Web Scraping (MVP Approach)
```python
# Use Bloomberg RSS feeds (headlines only)
# Full text requires subscription
# Respect robots.txt and ToS

BLOOMBERG_RSS = "https://www.bloomberg.com/feeds/economics/news.rss"

# For full text:
# - Manual article selection
# - Upload PDFs/screenshots
# - Or use Bloomberg API when budget allows
```

**MVP Recommendation**: Use RSS for headlines, manual upload for key articles

---

## 5. The Economist

### Overview
- **Access**: Subscription required
- **Data Type**: In-depth macro analysis
- **Update Frequency**: Weekly (Thursday)
- **MVP Status**: ❌ **Future (manual for MVP)**

### Approach

#### Option A: Manual Upload (MVP)
```python
# 1. Manually select relevant articles
# 2. Copy/paste or export as PDF
# 3. Upload to data/raw/economist/
# 4. Process like other research PDFs
```

#### Option B: Web Scraping (with subscription)
```python
# Requires:
# - The Economist subscription
# - Compliance with ToS
# - Session management for auth

class EconomistScraper:
    def __init__(self, username, password):
        self.session = requests.Session()
        self.login(username, password)

    def login(self, username, password):
        # Login to Economist website
        pass

    def fetch_article(self, url):
        # Fetch authenticated article
        pass
```

**MVP Recommendation**: Skip for MVP, add in Phase 2

---

## 6. Goldman Sachs Research

### Overview
- **Access**: Restricted to GS clients
- **Data Type**: Research reports, market commentary
- **Format**: PDF
- **MVP Status**: 🔶 **Manual upload only**

### Approach

#### Manual Upload Workflow
```
1. Obtain research PDFs (requires GS client access)
2. Upload to: data/raw/goldman_sachs/{date}/{filename}.pdf
3. Automated processing pipeline:
   - PDF parsing (PyMuPDF)
   - Text extraction
   - Table extraction
   - Metadata extraction
   - Chunking and indexing
```

#### PDF Processing

```python
# src/ingestion/pdf_processor.py

import fitz  # PyMuPDF
from typing import Dict

class PDFProcessor:
    def process_research_pdf(self, pdf_path: str) -> Dict:
        """Extract text and metadata from research PDF."""

        doc = fitz.open(pdf_path)

        # Extract text
        full_text = ""
        for page in doc:
            full_text += page.get_text()

        # Extract metadata
        metadata = doc.metadata

        # Extract tables (basic)
        tables = []
        for page in doc:
            tables.extend(page.find_tables())

        return {
            "title": metadata.get('title', ''),
            "authors": metadata.get('author', ''),
            "published_at": metadata.get('creationDate', ''),
            "content": full_text,
            "tables": tables,
            "source_name": "Goldman Sachs",
            "content_type": "research",
            "importance": "high"
        }
```

**MVP Recommendation**: Manual uploads for key reports, automate processing

---

## 7. Academic Papers (NBER, SSRN)

### Overview
- **Access**: Public (mostly free)
- **Data Type**: Academic research
- **Update Frequency**: Weekly/Monthly
- **MVP Status**: ❌ **Future**

### NBER Working Papers

```python
# NBER has an API: https://www.nber.org/api/

class NBERIngestion:
    def search_papers(self, keywords: List[str]) -> List[Dict]:
        """Search NBER for macro-related papers."""
        # API implementation
        pass

    def download_pdf(self, paper_id: str) -> str:
        """Download paper PDF."""
        url = f"https://www.nber.org/papers/{paper_id}.pdf"
        # Download implementation
        pass
```

**MVP Recommendation**: Skip for MVP, add in Phase 3

---

## Ingestion Schedule

### Recommended Cron Jobs

```bash
# data/ingestion_schedule.cron

# FRED: Daily at 10 AM ET
0 10 * * * /usr/bin/python /app/src/ingestion/run_fred.py

# FOMC: Check daily for new statements
0 11 * * * /usr/bin/python /app/src/ingestion/run_fomc.py

# RSS Feeds: Every 2 hours
0 */2 * * * /usr/bin/python /app/src/ingestion/run_rss.py

# Manual uploads: Process every 4 hours
0 */4 * * * /usr/bin/python /app/src/ingestion/run_manual_processor.py
```

---

## Compliance & Ethics

### Web Scraping Guidelines

1. **Check robots.txt**: Respect website crawling rules
2. **Respect Rate Limits**: Don't overwhelm servers
3. **Read ToS**: Comply with Terms of Service
4. **Use Official APIs**: Prefer APIs over scraping
5. **Attribution**: Always cite sources
6. **Copyright**: Respect copyright, don't republish

### Example: robots.txt Check

```python
from urllib.robotparser import RobotFileParser

def can_scrape(url: str) -> bool:
    """Check if URL is allowed per robots.txt."""
    rp = RobotFileParser()
    rp.set_url(f"{url}/robots.txt")
    rp.read()
    return rp.can_fetch("MacroAIAgent", url)
```

---

## Data Quality Metrics

### Track These Metrics

```python
QUALITY_METRICS = {
    "ingestion_success_rate": "% of successful ingestions",
    "data_freshness": "Time since last update per source",
    "deduplication_rate": "% of duplicates found",
    "processing_errors": "Count of processing failures",
    "coverage": "% of expected documents ingested"
}
```

### Monitoring Dashboard

```python
# Track in database
CREATE TABLE ingestion_metrics (
    timestamp TIMESTAMPTZ,
    source_name VARCHAR(100),
    metric_name VARCHAR(100),
    metric_value DECIMAL,
    metadata JSONB
);
```

---

## Next Steps

1. **Implement FRED ingestion** (highest priority, easiest)
2. **Implement FOMC scraper** (high value)
3. **Set up RSS aggregation** (good coverage)
4. **Create manual upload workflow** (for Bloomberg, GS, Economist)
5. **Build monitoring dashboard** (track data quality)

---

**Ready to start implementing? Let's build the FRED ingestion first!**
