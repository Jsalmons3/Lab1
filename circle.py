"""
Circle Calculator
Jeffrey Salmons
This program makes a forumla for the area and circumference of a circle.
6/18/2026
"""
import math

def calc_area(radius):
    area = math.pi * radius ** 2
    return area

def calc_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference