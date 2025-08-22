a = int(input("enter a number:"))
b = a
rev = "0"
while a > 0:
    dg = a % 10
    rev = rev + str(dg)
    
if a == int(rev):
    print("palindrome")
else:
    print("not palindrome")