num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
num3 = float(input("Enter a third number: "))
if num1 > num2 and num1 > num3:
    print("The largest number is num1")
elif num2 > num1 and num2 > num3:
    print("The largest number is num2")
else:
    print("The largest number is num3")