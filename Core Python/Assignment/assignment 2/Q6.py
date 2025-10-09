basic_salary = float(input("Enter the basic salary of the employee: "))
da = 0.10 * basic_salary  # 10% of basic
ta = 0.12 * basic_salary  # 12% of basic
hra = 0.15 * basic_salary # 15% of basic
total_salary = basic_salary + da + ta + hra
print(f"Dearness Allowance (DA): ₹{da:.2f}")
print(f"Travel Allowance (TA): ₹{ta:.2f}")
print(f"House Rent Allowance (HRA): ₹{hra:.2f}")