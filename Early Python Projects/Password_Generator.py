"""
Given a password length, a given number of passwords will be generated
"""

import random

__author__ = "David Walker"
__version__ = "10/25/2018"
__pylint__ = "2.12.2"

if __name__ == '__main__':
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?.,<>'

    length = input('Password length? ')
    length = int(length)

    PASSWORDS = input('How many passwords would you like? ')
    PASSWORDS = int(PASSWORDS)

    for p in range(PASSWORDS):
        PASSWORD = ''
        for c in range(length):
            PASSWORD += random.choice(CHARS)
        print(PASSWORD)
