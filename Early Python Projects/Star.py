from turtle import *

"""
Using the turtle module, a star will be drawn
"""

__author__ = "David Walker"
__version__ = "10/11/2018"
__pylint__ = "2.12.2"

if __name__ == '__main__':
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()