from financial_analyzer.plot_breakeven_point import plot_breakeven_point
import pytest
import altair as alt


def test_graph_type():    
    """Create sample plot and test the plo type"""
    fixed_cost = 2
    sales_price_per_uni = 1
    variable_cost_per_unit = 0.5
    max_unit = 10

    sample_plot, _ = plot_breakeven_point(fixed_cost, sales_price_per_uni, variable_cost_per_unit, max_unit)

    assert str(type(sample_plot)) == "<class 'altair.vegalite.v5.api.LayerChart'>", \
        "The output should be a layered chart"

def test_graph_depth():    
    """Create sample plot and test the depth of the layers"""
    fixed_cost = 2
    sales_price_per_uni = 1
    variable_cost_per_unit = 0.5
    max_unit = 10

    sample_plot, _ = plot_breakeven_point(fixed_cost, sales_price_per_uni, variable_cost_per_unit, max_unit)

    assert len(sample_plot.layer) == 9, f"There should be 9 layers, instead of {len(sample_plot.layer)}" 

def test_graph_each_layer():
    """Create sample plot and test """
    fixed_cost = 2
    sales_price_per_uni = 1
    variable_cost_per_unit = 0.5
    max_unit = 10

    sample_plot, _ = plot_breakeven_point(fixed_cost, sales_price_per_uni, variable_cost_per_unit, max_unit)

    for i, layer in enumerate(sample_plot.layer):
        assert isinstance(layer, alt.Chart), f"Layer {i+1} is not an Altair Chart"

def test_plot_data():
    """Evaluates the format of data created by the plotting chart"""

    fixed_cost = 2
    sales_price_per_uni = 1
    variable_cost_per_unit = 0.5
    max_unit = 10

    _, plot_df = plot_breakeven_point(fixed_cost, sales_price_per_uni, variable_cost_per_unit, max_unit)
    assert plot_df.shape == (max_unit, 5), "The dataframe created for ploting has wrong dimension"
    
    assert list(plot_df.columns) == ['Units', 'Total Revenue', \
                                     'Total Cost', 'Fixed Cost','Total Variable Cost'], \
                                        "The dataset does not have the correct column names"
    
    assert all(isinstance(value, int) and value > 0 for value in plot_df['Units']), \
        "The units should all be non-negative values"
