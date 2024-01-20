from financial_analyzer.roi import roi
import pytest

def test_roi_inputs_data_type():
    """
    Test TypeError with input parameters that are not of type float or int.
    """
    
    with pytest.raises(TypeError) as custom_string:
        roi("1000000", 1200000)

    assert str(custom_string.value) == "All parameters must be of type float or int."

    with pytest.raises(TypeError) as custom_string:
        roi(1000000, "1200000")

    assert str(custom_string.value) == "All parameters must be of type float or int."

    with pytest.raises(TypeError) as custom_string:
        roi("1000000", "1200000")

    assert str(custom_string.value) == "All parameters must be of type float or int."

def test_roi_negative_initial_investment():
    """
    Test if ValueError is raised when the initial investment is not positive.
    """
    
    with pytest.raises(ValueError) as custom_string:
        roi(-1000000, 1200000)

    assert str(custom_string.value) == "Initial investment should be positive!"

def test_roi_valid_calculation():
    """
    Test if the calculation is correct.
    """
    
    result = roi(1000000, 1200000)
    assert result == 20.0