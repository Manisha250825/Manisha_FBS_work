P = float(input("Enter the Principal amount (P): "))
R = float(input("Enter the Annual Interest Rate (R) in %: "))
T = int(input("Enter the Time period (T) in years: "))
CI = P * (1 + R / 100) ** T - P
print(f"\nCompound Interest after {T} years is: ₹{CI:.2f}")