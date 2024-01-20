# unit test for units_for_target_profit

import pytest
from financial_analyzer.units_for_target_profit import units_for_target_profit

def test_units_for_target_profit():
    # Test Case 1: Basic example
    assert units_for_target_profit(3000, 5, 2, 2000) == 1667

    # Test Case 2: Edge case with zero fixed costs and desired profit
    assert units_for_target_profit(0, 5, 2, 1000) == 500

    # Test Case 3: Edge case with high fixed costs and desired profit
    assert units_for_target_profit(10000, 20, 5, 5000) == 1000

    # Test Case 4: Edge case with very high sales price and variable cost
    assert units_for_target_profit(5000, 100, 80, 10000) == 250

    # Test Case 5: Ensure the result is an integer
    result = units_for_target_profit(2000, 10, 5, 1000)
    assert isinstance(result, int)
