# Set a vowels list
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Set function to count vowels in a text

def count_vowels(text):
    """
    Count the number of vowels in a given text.

    Parameters:
    text (str): The input text to analyze.

    Returns:
    int: The count of vowels in the text.
    """
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Test cases
if __name__ == "__main__":
    test_text = [
        "Hello World",
        "This is a test string.",
        "Python programming is fun!",
        "AEIOU are vowels.",
        "bcdfghjklmnpqrstvwxyz"
    ]
    for s in test_text:
        result = count_vowels(s)
        print(f"Number of vowels in '{s}': {result}")