a = input("enter a string:")
vowels ="a, e, i, o, u, A, E, I, O ,U"
count = 0
for char in a:
    if char in vowels:
        count += 1
print(count)