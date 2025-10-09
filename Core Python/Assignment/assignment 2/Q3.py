feet = int(input("Enter distance in feet: "))
inches = int(input("Enter additional inches: "))
total_inches = feet * 12 + inches
centimeters = total_inches * 2.54
meters = int(centimeters // 100)
remaining_cm = centimeters % 100
print(f"{feet} feet and {inches} inches is equal to:")
print(f"{meters} meter(s) and {remaining_cm:.2f} centimeter(s)")
