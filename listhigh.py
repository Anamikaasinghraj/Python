numbers = [5, 12, 7, 3, 9, 15, 2]

# Assume the first element is the maximum
max_value = numbers[0]

# Loop through the rest of the list
for i in range(1, len(numbers)):
    if numbers[i] < max_value:
        max_value = numbers[i]

print("Maximum value:", max_value)