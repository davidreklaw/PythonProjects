
"""
Using the turtle module, a star will be drawn
"""

import turtle

__author__ = "David Walker"
__version__ = "10/11/2018"
__pylint__ = "2.12.2"

if __name__ == '__main__':
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()
