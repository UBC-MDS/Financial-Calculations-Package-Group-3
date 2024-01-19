from financial_analyzer.breakeven_point import breakeven_point
import pytest

def test_breakeven_point_typical():
    """Test breakeven point with typical values."""
    result = breakeven_point(5000, 20, 10)
    expected = 500
    assert result == expected, f"Break-even point calculation failed, expected: {expected}, got {result} instead."

def test_breakeven_point_zero_fixed_costs():
    """Test breakeven point with zero fixed costs."""
    result = breakeven_point(0, 20, 10)
    expected = 0
    assert result == expected, f"Break-even point with zero fixed cost, expected: {expected}, got {result} instead."
