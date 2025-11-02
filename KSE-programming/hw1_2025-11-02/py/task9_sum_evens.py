# Set even divisor
even_divisor = 2

# Set function to sum even numbers in a given range
def sum_evens(start, end):
    """
    Sum all even numbers in a given range from start to end (inclusive).

    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range.

    Returns:
    int: The sum of all even numbers in the range.
    """
    total = 0
    for number in range(start, end + 1):
        if number % even_divisor == 0:
            total += number
    return total    

# Test cases
if __name__ == "__main__":
    test_ranges = [
        (1, 10),
        (5, 15),
        (10, 20),
        (0, 0),
        (1, 1)
    ]
    for start, end in test_ranges:
        result = sum_evens(start, end)
        print(f"Sum of even numbers from {start} to {end}: {result}")