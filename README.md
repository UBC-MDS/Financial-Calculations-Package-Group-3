# financial_analyzer

Calculate basic metrics of sales data and visualize the results.

## Installation

```bash
$ pip install financial_analyzer
```

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

roi = calculate_roi(initial_investment, current_value)
units_tg_profit = calculate_units_for_target_profit(fixed_cost, sales_price_per_unit, variable_cost_per_unit, 200)
break_even = calculate_break_even_point(fixed_cost, sales_price_per_unit, variable_cost_per_unit)
fig = plot_break_even_point(fixed_cost, sales_price_per_unit, variable_cost_per_unit, 500)
plt.show() 
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`financial_analyzer` was created by Nicole Tu, Rafe Chang, Alan PowPowichrowski, Chris Gao. It is licensed under the terms of the MIT license.

## Credits

`financial_analyzer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
