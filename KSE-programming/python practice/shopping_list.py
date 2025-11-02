# Shopping list manager
shopping_list = []

while True:
    print("\n=== Shopping List ===")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear list")
    print("5. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        item = input("Enter item: ")
        shopping_list.append(item)
        print(f"Added {item}")
    
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed {item}")
        else:
            print("Item not found")
    
    elif choice == "3":
        if shopping_list:
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("List is empty")
    
    elif choice == "4":
        shopping_list.clear()
        print("List cleared")
    
    elif choice == "5":
        break