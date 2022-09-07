import math

"""
This is a program that will help in the calculations of areas of a shape
"""

__author__ = "David Walker"
__version__ = "10/20/2018"
__pylint__ = "2.12.2"

if __name__ == '__main__':
    print("Starting Calculations...")
    option = (input("Enter C for circle or T for Triangle: "))
    if option == 'C':
        radius = float(input("Enter Radius: "))
        area = math.pi * radius ** 2
        print('Area: %f' %area)
    elif option == 'T':
        base = float = float(input("enter Base of Triangle: "))
        height = float(input("Enter Height of Triangle: "))
        area = 0.5 * base * height
        print('Area: %f' %area)
    else:
        print("Invalid! Shape does not exist!")
    print("Exiting...")