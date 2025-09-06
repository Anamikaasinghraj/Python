# Palindromic Word Finder

def is_palindrome(word):
    """Check if a word is palindrome"""
    word = word.lower()  # make it case-insensitive
    return word == word[::-1]  # reverse and compare


# Take input from user
text = input("Enter a sentence or words: ")

# Split the text into words
words = text.split()

# Find palindromes
palindromes = []

for word in words:
    if is_palindrome(word) and len(word) > 1:  # ignore single letters
        palindromes.append(word)

# Show results
if palindromes:
    print("Palindromic words found:", ", ".join(palindromes))
else:
    print("No palindromic words found.")
