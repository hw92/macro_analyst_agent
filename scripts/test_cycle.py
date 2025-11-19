"""
Test cycle script to demonstrate the macro AI agent workflow.
This is a simple simulation without actual LLM calls.
"""
import json
import sys
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table

console = Console()

def load_fake_data():
    """Load the fake data we generated"""
    data_dir = Path(__file__).parent.parent / "data" / "raw"

    with open(data_dir / "news_articles.json") as f:
        news = json.load(f)

    with open(data_dir / "economic_data.json") as f:
        econ_data = json.load(f)

    return news, econ_data

def display_data_ingestion(news, econ_data):
    """Simulate data ingestion step"""
    console.print("\n[bold cyan]Step 1: Data Ingestion[/bold cyan]")
    console.print("=" * 60)

    table = Table(title="Ingested Data Summary")
    table.add_column("Source", style="cyan")
    table.add_column("Count", style="green")
    table.add_column("Latest Date", style="yellow")

    table.add_row("News Articles", str(len(news)), news[0]['date'][:10])
    table.add_row("CPI Data Points", str(len(econ_data['CPI'])), econ_data['CPI'][-1]['date'][:10])
    table.add_row("GDP Data Points", str(len(econ_data['GDP'])), econ_data['GDP'][-1]['date'][:10])
    table.add_row("Unemployment Data", str(len(econ_data['UNEMPLOYMENT'])), econ_data['UNEMPLOYMENT'][-1]['date'][:10])

    console.print(table)
    console.print("\n[green]✓ Data ingestion complete![/green]")

def display_knowledge_base(news, econ_data):
    """Simulate knowledge base structuring"""
    console.print("\n[bold cyan]Step 2: Knowledge Base Structuring[/bold cyan]")
    console.print("=" * 60)

    console.print("\n[yellow]Vector Store:[/yellow]")
    console.print(f"  • Embedded {len(news)} news articles into vector database")
    console.print(f"  • Index size: {len(news)} documents")
    console.print(f"  • Vector dimension: 1536")

    console.print("\n[yellow]Time Series Database:[/yellow]")
    total_points = sum(len(econ_data[key]) for key in econ_data)
    console.print(f"  • Stored {total_points} economic data points")
    console.print(f"  • Series: CPI, GDP, Unemployment, Fed Funds Rate")

    console.print("\n[green]✓ Knowledge base structured![/green]")

def display_agent_reasoning(news):
    """Simulate agent reasoning"""
    console.print("\n[bold cyan]Step 3: AI Agent Reasoning[/bold cyan]")
    console.print("=" * 60)

    query = "What's the current macro regime and what does it mean for my portfolio?"

    console.print(f"\n[yellow]User Query:[/yellow] {query}")

    # Simulate retrieval
    console.print("\n[yellow]Retrieval:[/yellow]")
    relevant_articles = news[:3]
    for i, article in enumerate(relevant_articles, 1):
        console.print(f"  {i}. {article['title']} ({article['source']})")

    # Simulate macro analysis
    console.print("\n[yellow]Macro Analysis:[/yellow]")
    analysis = """
**Current Regime:** Moderating inflation with tight monetary policy

**Key Observations:**
- Inflation trending down but still above target
- Fed maintaining restrictive stance
- Labor market showing resilience
- Growth moderating but positive

**Implications:**
- Bonds: Duration risk remains elevated
- Equities: Quality over growth
- Alternatives: Consider inflation hedges
"""
    console.print(Markdown(analysis))

def display_portfolio_actions():
    """Simulate portfolio action generation"""
    console.print("\n[bold cyan]Step 4: Portfolio Actions[/bold cyan]")
    console.print("=" * 60)

    actions = [
        {
            "action": "Reduce duration in bond portfolio",
            "rationale": "High rates likely to persist with Fed on hold",
            "risk": "May miss gains if Fed pivots unexpectedly"
        },
        {
            "action": "Tilt towards value stocks",
            "rationale": "Value tends to outperform in high-rate environments",
            "risk": "Growth could rebound if rates fall"
        },
        {
            "action": "Maintain inflation hedge allocation",
            "rationale": "Inflation still above target, risks remain",
            "risk": "Hedges underperform if disinflation continues"
        }
    ]

    for i, action in enumerate(actions, 1):
        panel = Panel(
            f"[bold]{action['action']}[/bold]\n\n"
            f"[yellow]Rationale:[/yellow] {action['rationale']}\n\n"
            f"[red]Risk Note:[/red] {action['risk']}",
            title=f"Action {i}",
            border_style="green"
        )
        console.print(panel)

def run_test_cycle():
    """Run the complete test cycle"""
    console.print(Panel.fit(
        "[bold green]Macro AI Agent - Test Cycle[/bold green]\n"
        "Simulating the complete workflow",
        border_style="green"
    ))

    try:
        # Load fake data
        console.print("\n[dim]Loading fake data...[/dim]")
        news, econ_data = load_fake_data()

        # Step 1: Data Ingestion
        display_data_ingestion(news, econ_data)

        # Step 2: Knowledge Base
        display_knowledge_base(news, econ_data)

        # Step 3: Agent Reasoning
        display_agent_reasoning(news)

        # Step 4: Portfolio Actions
        display_portfolio_actions()

        # Summary
        console.print("\n" + "=" * 60)
        console.print("[bold green]✓ Test cycle complete![/bold green]")
        console.print("\n[dim]Next steps:[/dim]")
        console.print("  1. Set up Supabase database")
        console.print("  2. Add real API keys to .env")
        console.print("  3. Implement actual agent logic")
        console.print("  4. Build CLI/Streamlit interface")

    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] Fake data not found!")
        console.print("Run 'python scripts/generate_fake_data.py' first")
        sys.exit(1)

if __name__ == "__main__":
    run_test_cycle()
