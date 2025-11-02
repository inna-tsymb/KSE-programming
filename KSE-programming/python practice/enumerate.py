shopping_items = ["milk", "bread", "eggs", "butter", "cheese"]

# Task 1 & 2: Print each item with its number and mark even positions
for i, item in enumerate(shopping_items, start=1):
    mark = " ⭐" if i % 2 == 0 else ""
    print(f"{i}. {item}{mark}")

# Task 3: Find and print the position of "eggs"
position = shopping_items.index("eggs") + 1
print(f"\n'eggs' is at position {position}")