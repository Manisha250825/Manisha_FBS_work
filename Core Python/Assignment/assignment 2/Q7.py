number = int(input("Enter a three-digit number: "))
hundreds = number // 100
tens = (number % 100) // 10
units = number % 10
digit_sum = hundreds + tens + units
print(f"The sum of the digits is: {digit_sum}")