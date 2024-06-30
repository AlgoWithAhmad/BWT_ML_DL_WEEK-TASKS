# 

def subtract(a, b):
    """
    Returns the difference of a and b.
    """
    try:
        return a - b
    except TypeError:
        print("Error: Both inputs must be numbers.")
