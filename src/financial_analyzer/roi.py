def roi(initial_investment, current_value):
    """ Calculate the Return on Investment (ROI).
    
    Parameters 
    ----------
    initial_investment : {float, int} 
        The initial amount invested.
    current_value : {float, int}  
        The current value of the investment.
    
    Returns
    --------
    float: The ROI expressed as a percentage.
    
    Examples 
    --------
    >>> roi(1000000, 1200000)
    """
    
    #Check data type
    if any(not isinstance(param, (float, int)) for param in [initial_investment, current_value]):
        raise TypeError("All parameters must be of type float or int.")

    #Check value
    if initial_investment < 0:
        raise ValueError("Initial investment should be positive!")
    
    return ((current_value - initial_investment) / initial_investment) * 100

