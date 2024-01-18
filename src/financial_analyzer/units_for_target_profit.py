def units_for_target_profit(fixed_costs, sales_price_per_unit, variable_cost_per_unit, desired_profit):
    """
    Calculate the number of units needed to be sold to achieve a desired profit.

    Parameters
    ----------
    fixed_costs : float
        Total fixed costs for the business, given as a float.
    sales_price_per_unit : float
        Selling price for each unit of the product/service, given as a float.
    variable_cost_per_unit : float
        Variable cost incurred for each unit produced, given as a float.
    desired_profit : float
        The target profit for the business, given as a float.

    Returns
    -------
    float
        The number of units that need to be sold to achieve the desired profit.

    Examples
    --------
    Context: You want to achieve a profit of $2,000 this month. Your fixed costs 
    are $3,000, each unit is sold for $5, and the  variable cost is $2/unit.

    >>> fixed_costs = 3000
    >>> sales_price_per_unit = 5
    >>> variable_cost_per_unit = 2
    >>> desired_profit = 2000
    >>> units_to_sell = units_for_target_profit(fixed_costs, 
                                                          sales_price_per_unit, 
                                                          variable_cost_per_unit, 
                                                          desired_profit)
    >>> print(units_to_sell)
    1000

    Output tells you how many units of the product must be sold to achieve desired profit
    """
    # input validation & error handling
    if sales_price_per_unit <= variable_cost_per_unit:
        raise ValueError("Sales price per unit must be greater than variable cost per unit.")
    elif desired_profit < 0:
        raise ValueError('desired profit must be greater than zero')
    elif fixed_costs < 0:
        raise ValueError('fixed cost must be greater than zero')
    elif sales_price_per_unit < 0:
        raise ValueError('sales_price_per_unit must be greater than zero')
    elif variable_cost_per_unit < 0:
        raise ValueError('variable_cost_per_unit must be greater than zero')
    elif not all(isinstance(arg, (int, float)) for arg in [fixed_costs, sales_price_per_unit, variable_cost_per_unit, desired_profit]):
        raise TypeError("All input values must be numeric.")
    else:
        return (fixed_costs + desired_profit) / (sales_price_per_unit - variable_cost_per_unit)


def test_units_for_target_profit():
    # Test Case 1: Basic example
    fixed_costs = 3000
    sales_price_per_unit = 5
    variable_cost_per_unit = 2
    desired_profit = 2000
    units_to_sell = units_for_target_profit(fixed_costs, sales_price_per_unit, variable_cost_per_unit, desired_profit)
    assert units_to_sell == 1000, f"Test Case 1 Failed: {units_to_sell}"

    # Test Case 2: Edge case with zero fixed costs and desired profit
    fixed_costs = 0
    sales_price_per_unit = 5
    variable_cost_per_unit = 2
    desired_profit = 1000
    units_to_sell = units_for_target_profit(fixed_costs, sales_price_per_unit, variable_cost_per_unit, desired_profit)
    assert units_to_sell == 500, f"Test Case 2 Failed: {units_to_sell}"

    # Test Case 3: Edge case with high fixed costs and desired profit
    fixed_costs = 10000
    sales_price_per_unit = 20
    variable_cost_per_unit = 5
    desired_profit = 5000
    units_to_sell = units_for_target_profit(fixed_costs, sales_price_per_unit, variable_cost_per_unit, desired_profit)
    assert units_to_sell == 1000, f"Test Case 3 Failed: {units_to_sell}"

    # Test Case 4: Edge case with very high sales price and variable cost
    fixed_costs = 5000
    sales_price_per_unit = 100
    variable_cost_per_unit = 80
    desired_profit = 10000
    units_to_sell = units_for_target_profit(fixed_costs, sales_price_per_unit, variable_cost_per_unit, desired_profit)
    assert units_to_sell == 250, f"Test Case 4 Failed: {units_to_sell}"

    print("All test cases passed.")

# Run the test cases
test_units_for_target_profit()