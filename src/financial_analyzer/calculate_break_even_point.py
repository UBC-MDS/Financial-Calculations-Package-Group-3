def calculate_break_even_point(fixed_costs, sales_price_per_unit, variable_cost_per_unit):
    """
    Calculate the break-even point in units, given as set of cost and revenue parameters.

    Parameters
    ----------
    fixed_costs : float 
        Total fixed costs in the problem, given as a float.
    sales_price_per_unit : float
        The selling price of each unit in the problem, given as a float.
    variable_cost_per_unit : float
        The variable cost of each unit in the problem, given as a float.

    Returns
    -------
    float
        The break-even point in units for the given parameters.

    Examples
    --------
    Context: You are selling paintings, your fixed costs are 
    $5,000/month, each painting is sold for $20, the variable 
    costs (materials) for each painting are $10. What is your 
    break even point?
    >>> fixed_costs = 5000
    >>> sales_price_per_unit = 20
    >>> variable_cost_per_unit = 10
    >>> break_even_units = calculate_break_even_point(fixed_costs, 
    >>>     sales_price_per_unit, 
    >>>     variable_cost_per_unit)
    >>> print(break_even_units)
    500
    """
