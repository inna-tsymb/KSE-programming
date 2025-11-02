# Set function to count word frequency in a text

def count_word_frequency(text):
    """
    Count the frequency of each word in a given text.

    Parameters:
    text (str): The input text to analyze.

    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    word_freq = {}
    words = text.split()
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')  # Normalize the word
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq    

# Test cases
if __name__ == "__main__":
    test_texts = [
        "Hello world! Hello everyone.",
        "This is a test. This test is only a test.",
        "Word frequency count is fun. Fun is good.",
        "",
        "Repeat repeat REPEAT."
    ]
    for text in test_texts:
        result = count_word_frequency(text)
        print(f"Word frequency for '{text}': {result}")