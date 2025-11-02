# Set even divisor
even_divisor = 2

# Set function to check even or odd
def check_even_odd(number):
    """
    Check if a number is even or odd.

    Parameters:
    number (int): The number to check.

    Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if number % even_divisor == 0:
        return "Even"
    else:
        return "Odd"
    

    # Test cases
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 10, 15, 20]
    for num in test_numbers:
        result = check_even_odd(num)
        print(f"{num} is {result}")
    
