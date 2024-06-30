
def add(a, b):
    """
    Returns the sum of a and b.
    """
    try:
        return a + b
    except TypeError:
        print("Error: Both inputs must be numbers.")
