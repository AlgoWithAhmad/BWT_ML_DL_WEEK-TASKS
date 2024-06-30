
def divide(a, b):
    """
    Returns the division of a by b.
    """
    try:
        return a / b
    except TypeError:
        print("Error: Both inputs must be numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
