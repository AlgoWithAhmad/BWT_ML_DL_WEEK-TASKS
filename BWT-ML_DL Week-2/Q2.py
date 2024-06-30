def Is_even(number):
    # Check if the number is even
    if number % 2 == 0:
        print(f"The number {number} is even.")
        return True
    else:
        print(f"The number {number} is odd.")
        return False

# Example usage:
number = int(input("Enter an integer: "))
result = Is_even(number)

