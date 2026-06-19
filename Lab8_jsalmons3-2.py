"""
Geometry Calculator
Jeffrey Salmons
This program creates a menu for the user to calculate the area and perimeter/circumference of a circle and rectangle.
6/18/2026
"""

import circle
import rectangle

# Aliases are neccessary when importing modules because they both have the same function names 
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

    