import turtle

"""
Using the turtle module, a spiral will be drawn
"""

__author__  = "David Walker"
__version__ = "10/18/2018"
__pylint__ = "2.12.2"

if __name__ == '__main__':
    turtle.pensize(2)
    turtle.bgcolor("black")
    colors = ['red', 'yellow', 'purple', 'blue']
    turtle.tracer(False)
    turtle.speed(0)
    turtle.shape('turtle')
    for x in range(600):
        turtle.fd(2*x)
        turtle.color(colors[x %4])
        turtle.left(91)
        turtle.tracer(True)