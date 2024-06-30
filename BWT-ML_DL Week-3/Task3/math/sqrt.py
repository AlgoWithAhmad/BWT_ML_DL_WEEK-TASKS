
import math

def sqrt(a):
    """
    Returns the square root of a.
    """
    try:
        return math.sqrt(a)
    except TypeError:
        print("Error: Input must be a number.")
    except ValueError:
        print("Error: Input must be a non-negative number.")
