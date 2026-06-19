"""
Geometry Calculator
Jeffrey Salmons
This program creates a menu for the user to calculate the area and perimeter/circumference of a circle and rectangle.
6/18/2026
"""

from circle import calc_area as circle_area
from rectangle import calc_area as rectangle_area

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
    