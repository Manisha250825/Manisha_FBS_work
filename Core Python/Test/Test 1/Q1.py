length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
radius = float(input("Enter the radius of the semicircle: "))
area_rectangle = length * breadth
area_semi_circle = (3.14 * radius ** 2) / 2
total_area = area_rectangle + area_semi_circle
perimeter = 2 * length + breadth + 3.14 * radius
print(f"Total Area: {total_area:.2f}")
print(f"Total Perimeter: {perimeter:.2f}")