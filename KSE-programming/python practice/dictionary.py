# 1. Create an empty dictionary
inventory = {}

# 2. Add items
inventory["apples"] = 5
inventory["oranges"] = 3
inventory["bananas"] = 7

# 3. Print total number of fruits
total_fruits = sum(inventory.values())
print(f"Total number of fruits: {total_fruits}")

# 4. Update apples to 8
inventory["apples"] = 8

# 5. Remove oranges
inventory.pop("oranges")

# Final inventory (optional to print)
print("Updated inventory:", inventory)