"""
This is a program that will help in the calculations of areas of a shape
"""

import math

__author__ = "David Walker"
__version__ = "10/20/2018"
__pylint__ = "2.12.2"

if __name__ == '__main__':
    print("Starting Calculations...")
    option = (input("Enter C for circle or T for Triangle: "))
    if option == 'C':
        radius = float(input("Enter Radius: "))
        area = math.pi * radius ** 2
        print('Area: {area}')
    elif option == 'T':
        base = input("enter Base of Triangle: ")
        base = float(base)
        height = input("Enter Height of Triangle: ")
        height = float(height)
        area = 0.5 * base * height
        print('Area: {area}')
    else:
        print("Invalid! Shape does not exist!")
    print("Exiting...")
