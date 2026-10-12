import numpy as np

def expected_value_discrete(x: list, p: list) -> float:

    lenght = len(x)

    sum = 0
    for index in range(lenght):
        sum += x[index]*p[index]

    return float(sum)
    
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    pass