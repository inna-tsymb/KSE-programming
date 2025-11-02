# Set function to calculate basic statistics for a list of numbers

def calculate_stats(numbers):
    """
    Calculate basic statistics (mean, median, mode, min, max) for a list of numbers.
    
    Parameters:
    numbers (list of float): List of numbers to calculate statistics for.
    
    Returns:
    dict: A dictionary containing mean, median, mode, min, and max.
    """

    if not numbers:
        return {
            "mean": None,
            "median": None,
            "mode": None,
            "min": None,
            "max": None
        }

    n = len(numbers)
    sorted_numbers = sorted(numbers)

    # Calculate mean
    mean = sum(numbers) / n

    # Calculate median
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    # Calculate mode
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    mode = max(frequency, key=frequency.get)

    # Calculate min and max
    minimum = min(numbers)
    maximum = max(numbers)

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "min": minimum,
        "max": maximum
    }

   # Test cases
if __name__ == "__main__":
    test_lists = [
        [1, 2, 2, 3, 4],
        [5, 1, 3, 3, 2, 4],
        [10, 20, 30],
        [],
        [7]
    ]
    
    for lst in test_lists:
        stats = calculate_stats(lst)
        print(f"List: {lst}")
        print(f"Statistics: {stats}\n")