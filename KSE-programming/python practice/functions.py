def hours_to_minutes(hours):
    """
    1. Function that converts hours to minutes.
    """
    return hours * 60

def is_palindrome(word):
    """
    2. Function that checks if a word is a palindrome.
    It cleans the word of non-alphanumeric characters and ignores case.
    """
    # Clean the word: remove spaces/punctuation and make lowercase
    cleaned_word = "".join(filter(str.isalnum, word)).lower()
    # Check if the cleaned word is the same as its reverse
    return cleaned_word == cleaned_word[::-1]

def get_larger_number(num1, num2):
    """
    3. Function that returns the larger of two numbers.
    """
    if num1 > num2:
        return num1
    else:
        return num2
    
# Test cases
if __name__ == "__main__":
    # Test hours_to_minutes
    print("Testing hours_to_minutes:")
    test_hours = [1, 2.5, 0, 10, 0.75]
    for hours in test_hours:
        minutes = hours_to_minutes(hours)
        print(f"{hours} hours is {minutes} minutes.")

    # Test is_palindrome
    print("\nTesting is_palindrome:")
    test_words = ["Racecar", "hello", "A man a plan a canal Panama", "Python", "12321", "Not a palindrome!"]
    for word in test_words:
        result = is_palindrome(word)
        print(f'"{word}" is a palindrome: {result}')            