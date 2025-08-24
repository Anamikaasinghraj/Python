decimal = int(input("Enter a decimal number: "))
hexa = ""

# Hexadecimal digit mapping
hex_digits = "0123456789ABCDEF"

while decimal > 0:
    remainder = decimal % 16
    hexa = hex_digits[remainder] + hexa   # pick the correct digit from mapping
    decimal = decimal // 16

print("Hexadecimal:", hexa)
