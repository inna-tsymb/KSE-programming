# Count word frequencies in a sentence
sentence = input("Enter a sentence: ")

# Convert to lowercase and split into words
words = sentence.lower().split()

# Count frequencies using dictionary
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display results
print("\nWord frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# Alternative using get()
word_count2 = {}
for word in words:
    word_count2[word] = word_count2.get(word, 0) + 1