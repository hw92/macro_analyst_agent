"""
Generate fake macro economic data for testing the agent.
"""
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import random

# Fake news articles
NEWS_SOURCES = ["Bloomberg", "Reuters", "Financial Times", "Wall Street Journal"]
NEWS_TOPICS = [
    "Federal Reserve raises interest rates by 25 basis points",
    "CPI inflation rises to 3.2% year-over-year",
    "GDP growth slows to 1.8% in Q3",
    "Unemployment rate holds steady at 3.7%",
    "Treasury yields spike on strong jobs report",
    "Oil prices surge amid Middle East tensions",
    "Dollar strengthens against major currencies",
    "Housing market shows signs of cooling",
    "Consumer confidence index falls to 6-month low",
    "Manufacturing PMI expands for third consecutive month"
]

def generate_fake_news(num_articles=20):
    """Generate fake news articles"""
    articles = []
    base_date = datetime.now() - timedelta(days=30)

    for i in range(num_articles):
        date = base_date + timedelta(days=random.randint(0, 30))
        article = {
            "id": f"article_{i+1}",
            "title": random.choice(NEWS_TOPICS),
            "source": random.choice(NEWS_SOURCES),
            "date": date.isoformat(),
            "content": f"This is a fake article about {random.choice(NEWS_TOPICS).lower()}. "
                      f"Economists are closely watching the implications for the broader economy. "
                      f"Market participants are adjusting their portfolios accordingly.",
            "tags": random.sample(["inflation", "fed", "gdp", "employment", "markets", "bonds"], k=3)
        }
        articles.append(article)

    return articles

def generate_fake_economic_data():
    """Generate fake economic time series data"""
    base_date = datetime.now() - timedelta(days=365)
    data = {
        "CPI": [],
        "GDP": [],
        "UNEMPLOYMENT": [],
        "FEDERAL_FUNDS_RATE": []
    }

    # Generate monthly data for the past year
    for i in range(12):
        date = (base_date + timedelta(days=30*i)).isoformat()

        data["CPI"].append({
            "date": date,
            "value": round(2.0 + random.uniform(-0.5, 1.5), 2),
            "unit": "percent"
        })

        data["GDP"].append({
            "date": date,
            "value": round(2.5 + random.uniform(-1.0, 1.0), 2),
            "unit": "percent"
        })

        data["UNEMPLOYMENT"].append({
            "date": date,
            "value": round(3.8 + random.uniform(-0.3, 0.3), 1),
            "unit": "percent"
        })

        data["FEDERAL_FUNDS_RATE"].append({
            "date": date,
            "value": round(5.0 + random.uniform(-0.5, 0.5), 2),
            "unit": "percent"
        })

    return data

def save_fake_data():
    """Save fake data to files"""
    data_dir = Path(__file__).parent.parent / "data" / "raw"
    data_dir.mkdir(parents=True, exist_ok=True)

    # Generate and save news articles
    news_articles = generate_fake_news(20)
    with open(data_dir / "news_articles.json", "w") as f:
        json.dump(news_articles, f, indent=2)

    print(f"✓ Generated {len(news_articles)} fake news articles")

    # Generate and save economic data
    econ_data = generate_fake_economic_data()
    with open(data_dir / "economic_data.json", "w") as f:
        json.dump(econ_data, f, indent=2)

    print(f"✓ Generated economic time series data")
    print(f"  - CPI: {len(econ_data['CPI'])} data points")
    print(f"  - GDP: {len(econ_data['GDP'])} data points")
    print(f"  - Unemployment: {len(econ_data['UNEMPLOYMENT'])} data points")
    print(f"  - Federal Funds Rate: {len(econ_data['FEDERAL_FUNDS_RATE'])} data points")

    return news_articles, econ_data

if __name__ == "__main__":
    print("Generating fake macro economic data...")
    print("=" * 60)
    save_fake_data()
    print("=" * 60)
    print("Fake data generation complete!")
