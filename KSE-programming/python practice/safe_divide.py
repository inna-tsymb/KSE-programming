def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling potential errors.
    - Catches ZeroDivisionError for division by zero.
    - Catches ValueError for non-numeric inputs.
    - Includes a 'finally' block that always executes.
    """
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Non-numeric input provided."
    else:
        return f"Result: {result}"
    finally:
        print("Execution of safe_divide is complete.")          

# Test cases
if __name__ == "__main__":      
    test_cases = [
        (10, 2),        # Normal case
        (5, 0),         # Division by zero
        ('a', 3),       # Non-numeric numerator
        (4, 'b'),       # Non-numeric denominator
        (7, 1.4)        # Float division
    ]
    
    for num, denom in test_cases:
        print(f"Dividing {num} by {denom}: {safe_divide(num, denom)}")  