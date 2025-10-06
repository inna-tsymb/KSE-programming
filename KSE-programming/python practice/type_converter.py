# Type Conversion Practice
print("DATA TYPE CONVERTER")
print("-" * 30)

# String to numbers
str_num = input("Enter a number as text: ")
print(f"Original: {str_num} (type: {type(str_num)})")

# Convert to integer
int_num = int(str_num)
print(f"As integer: {int_num} (type: {type(int_num)})")

# Convert to float
float_num = float(str_num)
print(f"As float: {float_num} (type: {type(float_num)})")

# Number to string
age = int(input("\nEnter your age: "))
age_str = str(age)
message = "You are " + age_str + " years old"
print(message)