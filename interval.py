# Get input from user
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print("Prime numbers between", start, "and", end, "are:")

# Loop through each number in the interval
for num in range(start, end + 1):
    if num > 1:  # 1 is not a prime number
        is_prime = True
        for i in range(2, num):  # Check for factors
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

