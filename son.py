num = int(input("Enter a number: "))

if num < 1:
    print("Not a natural number")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("Sum of natural numbers is", sum)
