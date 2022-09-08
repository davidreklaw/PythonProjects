"""
Generates a given number of fibonacci numbers
"""

__author__ = "David Walker"
__version__ = "09/27/2018"
__pylint__ = "2.12.2"

def get_fib():
    """Gets the fibonacci sequence"""
    count = int(input("How many fibonacci numbers would you like to generate? "))

    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1, 1]
    else:
        fib = [1, 1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1

    return fib

if __name__ == '__main__':
    print(get_fib())
