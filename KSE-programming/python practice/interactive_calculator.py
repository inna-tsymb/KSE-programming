# Interactive Calculator
print("=" * 40)
print("PYTHON CALCULATOR")
print("=" * 40)

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform all operations
print("\nResults:")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

# Check for division by zero
if num2 != 0:
    print(f"Division: {num1} / {num2} = {num1 / num2:.2f}")
else:
    print("Division: Cannot divide by zero!")