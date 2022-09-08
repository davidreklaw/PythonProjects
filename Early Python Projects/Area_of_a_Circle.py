"""
This program will calculate the are of a circle
"""

__author__ = "David Walker"
__version__ = "08/28/2018"
__pylint__ = "2.12.2"

if __name__ == '__main__':
    radius = float(input("What is the radius of the circle?"))
    PI = 3.14159
    area = PI * radius ** 2
    print("The area of the circle is ", area)
    