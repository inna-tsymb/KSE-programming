# Pattern Challenge: Drawing Two Triangle Patterns
# Write a program that prints two triangle patterns using nested loops. 
# The first pattern should be a right-angled triangle, and the second pattern should be an inverted right-angled triangle.    

# Set function to draw patterns
def draw_patterns(rows=5):
    """
    Prints two triangle patterns using nested loops based on a
    specified number of rows.
    """
    # First Pattern: Right-Angled Triangle
    print("First Pattern:")
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()  # New line after each row

    print()  # Blank line between patterns

    # Second Pattern: Inverted Right-Angled Triangle
    print("Second Pattern:")
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end="")
        print()  # New line after each row

# Run the draw patterns function
if __name__ == "__main__":  
    draw_patterns()