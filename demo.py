#!/usr/bin/env python3
"""
Demo script for Purpose-AI-TTA
Shows key features and capabilities
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from purpose_ai.tta_loop import TTALoop
from purpose_ai.capital_manager import CapitalManager
from purpose_ai.moonshot_sim import MoonshotSimulator
from purpose_ai.hybrid_ai import HybridAI
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


def print_banner():
    """Print demo banner"""
    console = Console()
    banner = """
╔═══════════════════════════════════════════════════════════╗
║         PURPOSE-AI-TTA DEMONSTRATION                      ║
║         Adaptive AI War Room System                       ║
╚═══════════════════════════════════════════════════════════╝
    """
    console.print(banner, style="bold cyan")


def demo_tta_loop(console):
    """Demonstrate TTA Loop"""
    console.print("\n[bold cyan]1. TTA LOOP DEMONSTRATION[/bold cyan]")
    console.print("Processing: 'I have many ideas but feel overwhelmed'\n")
    
    tta = TTALoop()
    result = tta.execute_full_cycle(
        "I have many ideas but feel overwhelmed and don't know where to start"
    )
    
    table = Table(title="TTA Cycle Results", show_header=True)
    table.add_column("Stage", style="cyan")
    table.add_column("Output", style="white")
    
    table.add_row(
        "Tanker (Thoughts)",
        f"Analyzed {len(result.feelings.thoughts.analyzed_thoughts)} thought components"
    )
    table.add_row(
        "Følelser (Feelings)",
        f"Sentiment: {result.feelings.sentiment_score:.1f}\nEmotions: {', '.join(result.feelings.emotional_tags)}"
    )
    table.add_row(
        "Handling (Actions)",
        f"Priority: {result.priority_level}/5\nAlignment: {result.purpose_alignment:.1%}\nActions: {len(result.action_items)}"
    )
    
    console.print(table)


def demo_capital_management(console):
    """Demonstrate 369 Capital Management"""
    console.print("\n[bold cyan]2. 369 CAPITAL MANAGEMENT[/bold cyan]")
    console.print("Starting with $1,000,000\n")
    
    manager = CapitalManager(total_capital=1000000)
    
    table = Table(title="Capital Allocation (369 System)", show_header=True)
    table.add_column("Category", style="cyan")
    table.add_column("Split", style="yellow")
    table.add_column("Amount", style="green")
    table.add_column("Purpose", style="white")
    
    report = manager.get_balance_report()
    
    table.add_row(
        "Innovation (3)",
        "30%",
        f"${report['splits']['innovation']['remaining_amount']:,.0f}",
        "Moonshot projects"
    )
    table.add_row(
        "Stability (6)",
        "60%",
        f"${report['splits']['stability']['remaining_amount']:,.0f}",
        "Core operations"
    )
    table.add_row(
        "Give-back (9)",
        "10%",
        f"${report['splits']['giveback']['remaining_amount']:,.0f}",
        "Power to Folket"
    )
    
    console.print(table)
    
    # Demo transactions
    console.print("\n[bold]Sample Transactions:[/bold]")
    manager.allocate('innovation', 50000, 'AI Research Lab')
    manager.giveback_to_folket(10000, 'Local Community', 'Education Initiative')
    
    console.print("  ✓ Allocated $50,000 to Innovation (AI Research Lab)")
    console.print("  ✓ Gave back $10,000 to Folket (Education Initiative)")


def demo_moonshot_simulation(console):
    """Demonstrate Moonshot Simulations"""
    console.print("\n[bold cyan]3. MOONSHOT SIMULATION[/bold cyan]")
    
    sim = MoonshotSimulator()
    scenario = sim.scenarios_library[0]
    
    console.print(f"\nScenario: [bold]{scenario.name}[/bold]")
    console.print(f"Description: {scenario.description}")
    
    result = sim.simulate_scenario(scenario)
    
    table = Table(title="Simulation Results", show_header=True)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="white")
    
    table.add_row("Risk Level", f"{scenario.risk_level:.1%}")
    table.add_row("Potential Impact", f"{scenario.potential_impact:.1%}")
    table.add_row("Success Probability", f"{result.success_probability:.1%}")
    table.add_row("Expected Return", f"{result.expected_return:.1%}")
    table.add_row("Recommendation", result.recommendation)
    
    console.print(table)


def demo_hybrid_ai(console):
    """Demonstrate Hybrid AI"""
    console.print("\n[bold cyan]4. HYBRID AI PROVIDERS[/bold cyan]")
    
    hybrid = HybridAI()
    
    table = Table(title="Available AI Providers", show_header=True)
    table.add_column("Provider", style="cyan")
    table.add_column("Status", style="green")
    
    for provider in hybrid.list_providers():
        status = "✓ Active" if provider == hybrid.get_active_provider().get_provider_name() else "Available"
        table.add_row(provider, status)
    
    console.print(table)
    console.print("\n[italic]Supports seamless switching and consensus mode[/italic]")


def demo_integration(console):
    """Demonstrate integrated workflow"""
    console.print("\n[bold cyan]5. INTEGRATED WORKFLOW[/bold cyan]")
    console.print("Complete chaos-to-purpose pipeline:\n")
    
    steps = [
        "1. Capture chaotic thoughts (TTA: Tanker)",
        "2. Process emotional context (TTA: Følelser)",
        "3. Generate purposeful actions (TTA: Handling)",
        "4. Simulate moonshot scenarios",
        "5. Allocate capital using 369 system",
        "6. Execute with AI guidance (Hybrid AI)",
        "7. Give back to Folket (Community support)"
    ]
    
    for step in steps:
        console.print(f"  [cyan]✓[/cyan] {step}")
    
    console.print("\n[bold green]Result:[/bold green] Chaos transformed into purpose-driven action!")


def main():
    """Run demonstration"""
    console = Console()
    
    print_banner()
    
    console.print("\n[bold]Demonstrating Purpose-AI-TTA capabilities...[/bold]\n")
    
    try:
        demo_tta_loop(console)
        demo_capital_management(console)
        demo_moonshot_simulation(console)
        demo_hybrid_ai(console)
        demo_integration(console)
        
        console.print("\n" + "="*60)
        console.print("\n[bold green]✅ Demo Complete![/bold green]")
        console.print("\n[italic]Power to Folket - Purpose-AI-TTA[/italic]")
        console.print("\n[bold]To run the interactive war room:[/bold]")
        console.print("  python main.py")
        console.print("\n" + "="*60 + "\n")
        
    except Exception as e:
        console.print(f"\n[red]Error during demo: {e}[/red]")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
