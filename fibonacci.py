a = 0
b = 1
num = int(input("Enter how many Fibonacci numbers to print: "))

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, num):
        c = a + b
        print(c)
        a = b
        b = c
