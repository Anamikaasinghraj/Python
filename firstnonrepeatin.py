s = "aabbcdeff"

char_count = {}

# Count characters
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Find first non-repeating character
for char in s:
    if char_count[char] == 1:
        print("First non-repeating character:", char)
        break
