"""
Moonshot Simulation Engine
Simulates high-risk, high-reward scenarios for decision making
"""

import random
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime


@dataclass
class MoonshotScenario:
    """Represents a moonshot simulation scenario"""
    name: str
    description: str
    risk_level: float  # 0.0 to 1.0
    potential_impact: float  # 0.0 to 1.0
    resources_required: Dict[str, float]
    timeline_months: int


@dataclass
class SimulationResult:
    """Results from a moonshot simulation"""
    scenario: MoonshotScenario
    success_probability: float
    expected_return: float
    worst_case: str
    best_case: str
    recommendation: str
    timestamp: datetime


class MoonshotSimulator:
    """
    Moonshot Simulation Engine
    Helps evaluate and simulate high-impact, transformative initiatives
    """
    
    def __init__(self):
        self.simulation_history = []
        self.scenarios_library = self._initialize_scenarios()
        
    def _initialize_scenarios(self) -> List[MoonshotScenario]:
        """Initialize default moonshot scenarios"""
        return [
            MoonshotScenario(
                name="AI-Driven Social Impact",
                description="Use AI to solve community challenges at scale",
                risk_level=0.6,
                potential_impact=0.9,
                resources_required={'capital': 100000, 'time': 80, 'team': 5},
                timeline_months=12
            ),
            MoonshotScenario(
                name="Decentralized Governance Platform",
                description="Build platform for direct democracy and community decision-making",
                risk_level=0.7,
                potential_impact=0.95,
                resources_required={'capital': 150000, 'time': 100, 'team': 8},
                timeline_months=18
            ),
            MoonshotScenario(
                name="Open Source Innovation Lab",
                description="Create collaborative space for community-driven innovation",
                risk_level=0.4,
                potential_impact=0.7,
                resources_required={'capital': 50000, 'time': 60, 'team': 3},
                timeline_months=9
            )
        ]
    
    def simulate_scenario(self, scenario: MoonshotScenario, context: Dict[str, Any] = None) -> SimulationResult:
        """
        Run simulation for a moonshot scenario
        Uses Monte Carlo-style simulation with risk factors
        """
        # Calculate success probability based on risk and resources
        base_probability = 1.0 - scenario.risk_level
        
        # Add context modifiers
        if context:
            if context.get('team_experience', 0) > 0.7:
                base_probability += 0.1
            if context.get('market_conditions', 0) > 0.6:
                base_probability += 0.1
                
        success_probability = min(base_probability, 0.95)
        
        # Calculate expected return
        expected_return = scenario.potential_impact * success_probability
        
        # Generate simulation results
        result = SimulationResult(
            scenario=scenario,
            success_probability=success_probability,
            expected_return=expected_return,
            worst_case=self._generate_worst_case(scenario),
            best_case=self._generate_best_case(scenario),
            recommendation=self._generate_recommendation(success_probability, expected_return),
            timestamp=datetime.now()
        )
        
        self.simulation_history.append(result)
        return result
    
    def run_monte_carlo(self, scenario: MoonshotScenario, iterations: int = 1000) -> Dict[str, Any]:
        """
        Run Monte Carlo simulation with multiple iterations
        """
        outcomes = []
        
        for _ in range(iterations):
            # Simulate with random variations
            risk_factor = random.uniform(0.8, 1.2)
            impact_factor = random.uniform(0.8, 1.2)
            
            adjusted_risk = min(scenario.risk_level * risk_factor, 1.0)
            adjusted_impact = min(scenario.potential_impact * impact_factor, 1.0)
            
            success = random.random() > adjusted_risk
            outcome_value = adjusted_impact if success else 0
            
            outcomes.append({
                'success': success,
                'value': outcome_value,
                'risk': adjusted_risk,
                'impact': adjusted_impact
            })
        
        # Analyze results
        success_rate = sum(1 for o in outcomes if o['success']) / iterations
        avg_value = sum(o['value'] for o in outcomes) / iterations
        
        return {
            'scenario_name': scenario.name,
            'iterations': iterations,
            'success_rate': success_rate,
            'average_value': avg_value,
            'confidence_interval': self._calculate_confidence_interval(outcomes),
            'recommendation': 'PROCEED' if success_rate > 0.6 else 'CAUTION' if success_rate > 0.4 else 'RECONSIDER'
        }
    
    def _generate_worst_case(self, scenario: MoonshotScenario) -> str:
        """Generate worst case scenario description"""
        return f"Resources invested without achieving {scenario.name}. Learning experience but financial loss."
    
    def _generate_best_case(self, scenario: MoonshotScenario) -> str:
        """Generate best case scenario description"""
        return f"{scenario.name} succeeds beyond expectations, creating massive positive impact for folket."
    
    def _generate_recommendation(self, probability: float, expected_return: float) -> str:
        """Generate recommendation based on simulation"""
        if probability > 0.7 and expected_return > 0.6:
            return "STRONGLY RECOMMENDED - High probability of significant impact"
        elif probability > 0.5 and expected_return > 0.4:
            return "RECOMMENDED - Good opportunity with acceptable risk"
        elif probability > 0.3:
            return "CONDITIONAL - Proceed with caution and risk mitigation"
        else:
            return "NOT RECOMMENDED - High risk, consider alternatives"
    
    def _calculate_confidence_interval(self, outcomes: List[Dict]) -> Dict[str, float]:
        """Calculate 95% confidence interval"""
        values = sorted([o['value'] for o in outcomes])
        n = len(values)
        
        return {
            'lower_bound': values[int(n * 0.025)],
            'upper_bound': values[int(n * 0.975)]
        }
    
    def list_scenarios(self) -> List[str]:
        """List all available moonshot scenarios"""
        return [scenario.name for scenario in self.scenarios_library]
    
    def get_scenario_by_name(self, name: str) -> MoonshotScenario:
        """Get a specific scenario by name"""
        for scenario in self.scenarios_library:
            if scenario.name.lower() == name.lower():
                return scenario
        return None
