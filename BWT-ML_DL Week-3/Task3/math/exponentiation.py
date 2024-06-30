
def exponent(a, b):
    """
    Returns a raised to the power of b.
    """
    try:
        return a ** b
    except TypeError:
        print("Error: Both inputs must be numbers.")
