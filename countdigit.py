num = int(input("enter a number:"))
a = len(str(num))
count = 0
for i in range (a):
    count = i + count
    print(count)