"""
Geometry Calculator
Jeffrey Salmons
This program creates a menu for the user to calculate the area and perimeter/circumference of a circle and rectangle.
6/18/2026
"""

from circle import calc_area as circle_area
from circle import calc_circumference
from rectangle import calc_area as rectangle_area
from rectangle import calc_perimeter

# Aliases are necessary when importing modules because they both have the same function names 
# and this will allow us to use specified functions from each module without any mistakes.

print("Geometry Calculator")
print("-------------------")

while True:
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print(f"The area of the circle is {area:.3f}")

    elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))
        circumference = calc_circumference(radius)
        print(f"The circumference of the circle is {circumference:.3f}")
    
    elif choice == 3:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        area = rectangle_area(width, height)
        print(f"The area of the rectangle is {area}")

    elif choice == 4:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        perimeter = calc_perimeter(width, height)
        print(f"The perimeter of the rectangle is {perimeter}")