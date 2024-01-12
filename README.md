# financial_analyzer

Calculate basic metrics of sales data and visualize the results.

## Installation

```bash
$ pip install financial_analyzer
```

## Functions 
- `roi(initial_investment, current_value)`: Calculate the return on investment using the initial and current value of investment. 
- `units_for_target_profit(fixed_costs, sales_price_per_unit, variable_cost_per_unit, desired_profit)`: Calculate the sales unit needed to reach desired profit. 
- `breakeven_point(fixed_costs, sales_price_per_unit, variable_cost_per_unit)`: Calculate the breakeven unit using fixed cost, variable cost, and sales price. 
- `plot_breakeven_point(fixed_costs, sales_price_per_unit, variable_cost_per_unit, max_units)`: Visulize fixed cost, variable cost, and revenue. 

## Usage

`financial_analyzer` can be used to calculate and plot an investment's roi and breakeven point as follows: 

```python 
from financial-calculations-package-group-3.financial_analyzer import calculate_roi, calculate_units_for_target_profit, calculate_break_even_point, plot_break_even_point
import matplotlib.pyplot as plt

initial_investment = 400 
current_value = 450
fixed_cost = 1000
sales_price_per_unit = 8 
variable_cost_per_unit = 2 

roi = roi(initial_investment, current_value)
units_tg_profit = units_for_target_profit(fixed_cost, sales_price_per_unit, variable_cost_per_unit, 200)
break_even = breakeven_point(fixed_cost, sales_price_per_unit, variable_cost_per_unit)
fig = plot_breakeven_point(fixed_cost, sales_price_per_unit, variable_cost_per_unit, 500)
plt.show() 
```

## Python Ecosystem 

`financial_analyzer` possess its focus on answering the commonly needed metrics in finance. The purpose of the package is to allow easy way to access these metrics, and reuse across different files. 

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Contributors

The following package was created by the following contributors: Alan Powichrowski, Chris Gao, Nicole T., Rafe Chang.

## License

`financial_analyzer` was created by Nicole Tu, Rafe Chang, Alan PowPowichrowski, Chris Gao. It is licensed under the terms of the MIT license.

## Credits

`financial_analyzer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
