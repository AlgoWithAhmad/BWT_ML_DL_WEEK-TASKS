
def mod(a, b):
    """
    Returns the modulus of a and b.
    """
    try:
        return a % b
    except TypeError:
        print("Error: Both inputs must be numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
