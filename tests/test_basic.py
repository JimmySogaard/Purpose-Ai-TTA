"""
Basic tests for Purpose-AI-TTA system
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from purpose_ai.tta_loop import TTALoop, Tanker, Folelser, Handling
from purpose_ai.capital_manager import CapitalManager
from purpose_ai.moonshot_sim import MoonshotSimulator, MoonshotScenario
from purpose_ai.hybrid_ai import HybridAI


def test_tta_loop():
    """Test TTA loop basic functionality"""
    print("Testing TTA Loop...")
    
    tta = TTALoop()
    result = tta.execute_full_cycle("I need to organize my thoughts and find purpose")
    
    assert isinstance(result, Handling)
    assert len(result.action_items) > 0
    assert 0 <= result.purpose_alignment <= 1.0
    assert 1 <= result.priority_level <= 5
    
    print("✓ TTA Loop test passed")


def test_capital_manager():
    """Test 369 capital management"""
    print("Testing Capital Manager...")
    
    manager = CapitalManager(total_capital=1000000)
    
    # Check 369 splits
    report = manager.get_balance_report()
    assert report['splits']['innovation']['allocated_percentage'] == 30.0
    assert report['splits']['stability']['allocated_percentage'] == 60.0
    assert report['splits']['giveback']['allocated_percentage'] == 10.0
    
    # Test allocation
    success = manager.allocate('innovation', 10000, 'Test project')
    assert success == True
    
    # Test giveback
    success = manager.giveback_to_folket(5000, 'Test community', 'Power to folket')
    assert success == True
    
    print("✓ Capital Manager test passed")


def test_moonshot_simulator():
    """Test moonshot simulation"""
    print("Testing Moonshot Simulator...")
    
    sim = MoonshotSimulator()
    
    # Test with built-in scenario
    scenarios = sim.list_scenarios()
    assert len(scenarios) > 0
    
    scenario = sim.scenarios_library[0]
    result = sim.simulate_scenario(scenario)
    
    assert 0 <= result.success_probability <= 1.0
    assert 0 <= result.expected_return <= 1.0
    # Check that recommendation contains one of the expected keywords
    assert any(keyword in result.recommendation for keyword in ['STRONGLY RECOMMENDED', 'RECOMMENDED', 'CONDITIONAL', 'NOT RECOMMENDED'])
    
    # Test Monte Carlo
    mc_result = sim.run_monte_carlo(scenario, iterations=100)
    assert 'success_rate' in mc_result
    assert 'recommendation' in mc_result
    
    print("✓ Moonshot Simulator test passed")


def test_hybrid_ai():
    """Test hybrid AI system"""
    print("Testing Hybrid AI...")
    
    hybrid = HybridAI()
    
    # Test provider listing
    providers = hybrid.list_providers()
    assert 'Grok' in providers
    assert 'Kimi' in providers
    assert 'Claude' in providers
    
    # Test provider switching
    success = hybrid.switch_provider('Claude')
    assert success == True
    assert hybrid.get_active_provider().get_provider_name() == 'Claude'
    
    print("✓ Hybrid AI test passed")


def test_integration():
    """Test integration of multiple components"""
    print("Testing Integration...")
    
    # Create instances
    tta = TTALoop()
    capital = CapitalManager(500000)
    sim = MoonshotSimulator()
    
    # Simulate a complete workflow
    # 1. Process thoughts
    actions = tta.execute_full_cycle("I want to create a community project")
    
    # 2. Allocate capital
    capital.allocate('innovation', 50000, 'Community project')
    
    # 3. Run moonshot simulation
    scenario = sim.scenarios_library[0]
    result = sim.simulate_scenario(scenario)
    
    # Verify workflow
    assert len(tta.history) > 0
    assert len(capital.transaction_history) > 0
    assert len(sim.simulation_history) > 0
    
    print("✓ Integration test passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("Running Purpose-AI-TTA Tests")
    print("="*60 + "\n")
    
    try:
        test_tta_loop()
        test_capital_manager()
        test_moonshot_simulator()
        test_hybrid_ai()
        test_integration()
        
        print("\n" + "="*60)
        print("✅ All tests passed!")
        print("="*60 + "\n")
        return True
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
