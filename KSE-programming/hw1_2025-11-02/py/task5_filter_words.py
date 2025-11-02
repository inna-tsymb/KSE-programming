# Set function to filter words by length

def filter_long_words(words, min_length):   
    """
    Filter words that are longer than a specified minimum length.

    Parameters:
    words (list of str): List of words to filter.
    min_length (int): Minimum length a word must have to be included.

    Returns:
    list of str: List of words longer than min_length.
    """
    long_words = [word for word in words if len(word) > min_length]
    return long_words

# Test cases
if __name__ == "__main__":
    test_words = [
        (["apple", "banana", "kiwi", "cherry", "fig", "grape"], 4),
        (["hello", "world", "python", "is", "fun"], 3),
        (["a", "ab", "abc", "abcd", "abcde"], 2),
        ([], 3),
        (["short", "tiny", "small"], 5)
    ]
    for words, length in test_words:
        result = filter_long_words(words, length)
        print(f"Words longer than {length} in {words}: {result}")   