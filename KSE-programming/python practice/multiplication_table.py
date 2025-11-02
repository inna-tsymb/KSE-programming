# Print multiplication table
number = int(input("Enter a number (1-10): "))

# Validate input
if number < 1 or number > 10:
    print("Please enter a number between 1 and 10")
else:
    print(f"\nMultiplication table for {number}:")
    print("-" * 20)
    
    for i in range(1, 11):
        result = number * i
        print(f"{number} × {i} = {result}")