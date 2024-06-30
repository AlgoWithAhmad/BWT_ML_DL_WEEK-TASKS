def convert_temperature(temp, scale):
    # Check if the scale is Celsius
    if scale == "C":
        # Convert Celsius to Fahrenheit
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is {converted_temp:.2f}°F")
        return converted_temp
    # Check if the scale is Fahrenheit
    elif scale == "F":
        # Convert Fahrenheit to Celsius
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is {converted_temp:.2f}°C")
        return converted_temp
    else:
        print("Invalid scale. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        return None

# Example usage:
temp = float(input("Enter the temperature value: "))
scale = input("Enter the scale ('C' for Celsius, 'F' for Fahrenheit): ").upper()
convert_temperature(temp, scale)
