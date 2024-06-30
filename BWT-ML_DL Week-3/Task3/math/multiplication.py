
def multiply(a, b):
    """
    Returns the product of a and b.
    """
    try:
        return a * b
    except TypeError:
        print("Error: Both inputs must be numbers.")
