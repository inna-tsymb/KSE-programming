# Simple phone book using dictionary
phone_book = {}

phone_book["Alice"] = "555-1234"
phone_book["Bob"] = "555-5678"
phone_book["Charlie"] = "555-9012"

# Look up a number
name = input("Enter name to search: ")
if name in phone_book:
    print(f"{name}'s number: {phone_book[name]}")
else:
    print("Name not found")

# Print all contacts
print("\nAll contacts:")
for name, number in phone_book.items():
    print(f"{name}: {number}")