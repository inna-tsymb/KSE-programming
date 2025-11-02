# Set function to look up phone numbers in a phone book

def find_phone_number(phone_book, name):    
    """
    Find the phone number for a given name in the phone book.

    Parameters:
    phone_book (dict): A dictionary mapping names to phone numbers.
    name (str): The name to look up.

    Returns:
    str: The phone number if found, otherwise a not found message.
    """
    return phone_book.get(name, "Phone number not found.")

# Test cases
if __name__ == "__main__":
    phone_book = {
        "Alice": "123-456-7890",
        "Bob": "987-654-3210",
        "Charlie": "555-555-5555"
    }
    test_names = ["Alice", "Bob", "David", "Charlie", "Eve"]
    for name in test_names:
        result = find_phone_number(phone_book, name)
        print(f"Phone number for {name}: {result}")