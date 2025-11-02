# Set parameters for temperature conversion
celsius_offset = 32
celsius_factor = 9 / 5

# Set function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Formula: F = (C * 9/5) + 32

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    fahrenheit = (celsius * celsius_factor) + celsius_offset
    return fahrenheit

# Test cases
if __name__ == "__main__":
    test_temperatures = [0, 20, 37, 100, -40]
    for temp in test_temperatures:
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")