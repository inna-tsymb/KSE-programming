def manage_inventory():
    """
    Demonstrates basic dictionary operations for a fruit inventory.
    """
    
    # 1. Creates an empty dictionary called inventory
    inventory = {}
    print(f"1. Initial empty inventory: {inventory}")

    # 2. Adds: “apples”: 5, “oranges”: 3, “bananas”: 7
    inventory["apples"] = 5
    inventory["oranges"] = 3
    inventory["bananas"] = 7
    print(f"2. After adding fruit: {inventory}")

    # 3. Prints total number of fruits
    # We can sum the values() of the dictionary
    total_fruits = sum(inventory.values())
    print(f"3. Total number of fruits: {total_fruits}")

    # 4. Updates apples to 8
    inventory["apples"] = 8
    print(f"4. After updating apples: {inventory}")

    # 5. Removes oranges
    # We can use 'del' or 'pop()'
    if "oranges" in inventory:
        del inventory["oranges"]
        print(f"5. After removing oranges: {inventory}")
    else:
        print("5. 'oranges' not found in inventory.")
    
    # Optional: Print final state and new total
    final_total = sum(inventory.values())
    print(f"\nFinal inventory: {inventory}")
    print(f"Final total number of fruits: {final_total}")

# Test the function
if __name__ == "__main__":
    manage_inventory()