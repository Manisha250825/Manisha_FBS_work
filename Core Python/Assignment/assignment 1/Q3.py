dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))
if divisor == 0:
    print("Error: Division by zero is not allowed.")
else:
    quotient = dividend // divisor
    remainder = dividend % divisor
    print(f"\nQuotient = {quotient}")
    print(f"Remainder = {remainder}")