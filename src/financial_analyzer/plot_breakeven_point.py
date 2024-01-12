import plotly.express as px

def plot_breakeven_point(fixed_costs, sales_price_per_unit, variable_cost_per_unit, max_units):
    """
    Plot a break-even point graph which shows the relationship between total cost,
    total revenue, and number of units sold. This plot will include 3 lines, one for
    Total Revenue, one for Total Cost (Varialbe + Fixed), and one for Fixed Cost.

    Parameters
    ----------
    fixed_costs : float
        Total fixed costs in the problem, given as a float.
    sales_price_per_unit : float
        The selling price of each unit in the problem, given as a float.
    variable_cost_per_unit : float
        The variable cost of each unit in the problem, given as a float.
    max_units : int
        The maximum number of units to include in the plot, given as an integer.

    Returns
    -------
    None
        This function does not return a value. It displays a plot.

    Examples
    --------
    Context: Want to visualize cafe sales. Your fixed costs are $1,000, each coffee 
    sells for $5, the variable cost for each cup is $2. To visualize (altair plot) 
    your costs and revenue up to selling 500 cups, you use this function.
    
    >>> fixed_costs = 1000
    >>> sales_price_per_unit = 5
    >>> variable_cost_per_unit = 2
    >>> max_units = 500
    >>> plot_break_even_point(fixed_costs, sales_price_per_unit, variable_cost_per_unit, max_units)
    
    This will display an altair plot with the total cost, fixed cost, and total revenue lines, 
    illustrating the point where they intersect as the break-even point.
    """
