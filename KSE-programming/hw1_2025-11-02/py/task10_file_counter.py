# Set function to count total words in a file
def count_words_in_file(filename):
    """
    Count the total number of words in a given file.

    Parameters:
    filename (str): The path to the file to analyze.

    Returns:
    int: The total number of words in the file.
    """
    total_words = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                total_words += len(words)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    return total_words  

# Test cases
if __name__ == "__main__":
    test_files = [
        "hello.txt",
        "2nd.txt",
        "non_existent_file.txt"
    ]
    for file in test_files:
        result = count_words_in_file(file)
        print(f"Total words in '{file}': {result}")