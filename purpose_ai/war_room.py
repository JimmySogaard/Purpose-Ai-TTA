"""
War Room Interface - Fri Tale (Free Speech)
Interactive CLI for the adaptive AI war room
"""

import asyncio
from typing import Optional
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown

from .tta_loop import TTALoop
from .hybrid_ai import HybridAI
from .capital_manager import CapitalManager
from .moonshot_sim import MoonshotSimulator


class WarRoom:
    """
    Adaptive AI War Room - Fri Tale Interface
    Power to folket through open dialogue and purposeful action
    """
    
    def __init__(self, initial_capital: float = 1000000):
        self.console = Console()
        self.tta_loop = TTALoop()
        self.hybrid_ai = HybridAI()
        self.capital_manager = CapitalManager(initial_capital)
        self.moonshot_sim = MoonshotSimulator()
        self.session_active = False
        
    def display_banner(self):
        """Display the war room banner"""
        banner = """
╔═══════════════════════════════════════════════════════════╗
║         PURPOSE-AI-TTA: ADAPTIVE AI WAR ROOM              ║
║         Chaos-to-Purpose Elevation System                 ║
║                                                           ║
║  TTA Loop: Tanker → Følelser → Handling                  ║
║  Hybrid AI: Grok | Kimi | Claude                         ║
║  Capital System: 369 Splits                              ║
║  Ethos: Power to Folket                                  ║
╚═══════════════════════════════════════════════════════════╝
        """
        self.console.print(banner, style="bold cyan")
        
    def display_menu(self):
        """Display main menu options"""
        menu = Table(title="War Room Commands", show_header=True, header_style="bold magenta")
        menu.add_column("Command", style="cyan")
        menu.add_column("Description", style="white")
        
        menu.add_row("tta", "Execute TTA Loop (Thoughts → Feelings → Actions)")
        menu.add_row("fri-tale", "Free speech mode - Open dialogue")
        menu.add_row("capital", "View capital management (369 splits)")
        menu.add_row("moonshot", "Run moonshot simulations")
        menu.add_row("ai", "Manage AI providers (Grok/Kimi/Claude)")
        menu.add_row("history", "View session history")
        menu.add_row("help", "Show this menu")
        menu.add_row("exit", "Exit war room")
        
        self.console.print(menu)
        
    async def execute_tta_command(self):
        """Execute TTA Loop command"""
        self.console.print("\n[bold cyan]TTA Loop - Chaos to Purpose[/bold cyan]")
        self.console.print("Enter your thoughts (chaos, ideas, concerns):")
        
        user_input = Prompt.ask("Input")
        
        if not user_input:
            self.console.print("[yellow]No input provided[/yellow]")
            return
            
        self.console.print("\n[cyan]Processing TTA cycle...[/cyan]")
        
        # Execute full TTA cycle
        actions = self.tta_loop.execute_full_cycle(user_input)
        
        # Display results
        self.console.print("\n[bold green]Results:[/bold green]")
        
        result_panel = f"""
**Tanker (Thoughts):**
{actions.feelings.thoughts.analyzed_thoughts}

**Følelser (Feelings):**
- Sentiment: {actions.feelings.sentiment_score}
- Emotions: {', '.join(actions.feelings.emotional_tags)}
- Intuition: {actions.feelings.intuition_signal}

**Handling (Actions):**
- Priority Level: {actions.priority_level}/5
- Purpose Alignment: {actions.purpose_alignment:.2%}
- Action Items:
"""
        for i, action in enumerate(actions.action_items, 1):
            result_panel += f"\n  {i}. {action}"
            
        self.console.print(Panel(result_panel, title="TTA Cycle Complete", border_style="green"))
        
    async def fri_tale_mode(self):
        """Free speech mode - Open dialogue with AI"""
        self.console.print("\n[bold cyan]Fri Tale Mode - Power to Folket[/bold cyan]")
        self.console.print("Speak freely. Your voice matters. (Type 'back' to return)\n")
        
        while True:
            message = Prompt.ask("[bold]You[/bold]")
            
            if message.lower() in ['back', 'exit', 'quit']:
                break
                
            # Get AI response
            response = await self.hybrid_ai.generate_response(message)
            self.console.print(f"\n[bold green]AI ({self.hybrid_ai.get_active_provider().get_provider_name()})[/bold green]: {response}\n")
            
    def show_capital_status(self):
        """Display capital management status"""
        self.console.print("\n[bold cyan]369 Capital Management System[/bold cyan]")
        
        report = self.capital_manager.get_balance_report()
        
        capital_table = Table(title="Capital Allocation", show_header=True, header_style="bold magenta")
        capital_table.add_column("Category", style="cyan")
        capital_table.add_column("Percentage", style="yellow")
        capital_table.add_column("Amount", style="green")
        capital_table.add_column("Description", style="white")
        
        for name, split_data in report['splits'].items():
            capital_table.add_row(
                split_data['category'],
                f"{split_data['allocated_percentage']}%",
                f"${split_data['remaining_amount']:,.2f}",
                split_data['description']
            )
            
        self.console.print(capital_table)
        self.console.print(f"\n[bold]Give-back Pool:[/bold] ${report['giveback_pool']:,.2f}")
        self.console.print("[italic]Ethos: Power to Folket[/italic]\n")
        
    def run_moonshot_menu(self):
        """Display moonshot simulation menu"""
        self.console.print("\n[bold cyan]Moonshot Simulation Engine[/bold cyan]")
        
        scenarios = self.moonshot_sim.list_scenarios()
        
        self.console.print("\nAvailable Moonshot Scenarios:")
        for i, scenario_name in enumerate(scenarios, 1):
            self.console.print(f"  {i}. {scenario_name}")
            
        choice = Prompt.ask("\nSelect scenario number (or 'back')")
        
        if choice.lower() == 'back':
            return
            
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(scenarios):
                scenario = self.moonshot_sim.scenarios_library[idx]
                
                # Run simulation
                self.console.print(f"\n[cyan]Running simulation for: {scenario.name}[/cyan]")
                result = self.moonshot_sim.simulate_scenario(scenario)
                
                # Display results
                result_text = f"""
**Scenario:** {result.scenario.name}
**Description:** {result.scenario.description}

**Risk Level:** {result.scenario.risk_level:.1%}
**Potential Impact:** {result.scenario.potential_impact:.1%}
**Success Probability:** {result.success_probability:.1%}
**Expected Return:** {result.expected_return:.1%}

**Best Case:** {result.best_case}
**Worst Case:** {result.worst_case}

**Recommendation:** {result.recommendation}
"""
                self.console.print(Panel(result_text, title="Simulation Results", border_style="green"))
                
        except (ValueError, IndexError):
            self.console.print("[red]Invalid selection[/red]")
            
    def manage_ai_providers(self):
        """Manage AI provider settings"""
        self.console.print("\n[bold cyan]Hybrid AI Provider Management[/bold cyan]")
        
        providers = self.hybrid_ai.list_providers()
        active = self.hybrid_ai.get_active_provider().get_provider_name()
        
        self.console.print(f"\nActive Provider: [bold green]{active}[/bold green]")
        self.console.print("\nAvailable Providers:")
        for provider in providers:
            status = "✓" if provider == active else " "
            self.console.print(f"  [{status}] {provider}")
            
        if Confirm.ask("\nSwitch provider?"):
            new_provider = Prompt.ask("Enter provider name")
            if self.hybrid_ai.switch_provider(new_provider):
                self.console.print(f"[green]Switched to {new_provider}[/green]")
            else:
                self.console.print("[red]Invalid provider name[/red]")
                
    def show_history(self):
        """Show session history"""
        self.console.print("\n[bold cyan]Session History[/bold cyan]")
        
        if not self.tta_loop.history:
            self.console.print("[yellow]No history yet[/yellow]")
            return
            
        for i, entry in enumerate(self.tta_loop.history[-5:], 1):  # Show last 5
            timestamp = entry['timestamp'].strftime("%H:%M:%S")
            thoughts = entry['thoughts'].raw_input[:50]
            self.console.print(f"\n{i}. [{timestamp}] {thoughts}...")
            
    async def run(self):
        """Main war room loop"""
        self.session_active = True
        self.display_banner()
        self.console.print("\n[bold]Welcome to the Adaptive AI War Room[/bold]")
        self.console.print("[italic]Your space for chaos-to-purpose elevation[/italic]\n")
        
        while self.session_active:
            self.console.print("\nType 'help' for commands")
            command = Prompt.ask("[bold cyan]Command[/bold cyan]").lower().strip()
            
            if command == "exit":
                self.console.print("\n[bold]Exiting war room. Power to folket![/bold]")
                self.session_active = False
                
            elif command == "help":
                self.display_menu()
                
            elif command == "tta":
                await self.execute_tta_command()
                
            elif command == "fri-tale":
                await self.fri_tale_mode()
                
            elif command == "capital":
                self.show_capital_status()
                
            elif command == "moonshot":
                self.run_moonshot_menu()
                
            elif command == "ai":
                self.manage_ai_providers()
                
            elif command == "history":
                self.show_history()
                
            else:
                self.console.print("[yellow]Unknown command. Type 'help' for options.[/yellow]")


async def main():
    """Entry point for the war room"""
    war_room = WarRoom()
    await war_room.run()


if __name__ == "__main__":
    asyncio.run(main())
