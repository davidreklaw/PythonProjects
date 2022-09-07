import random

"""
Given a password length, a given number of passwords will be generated
"""

__author__ = "David Walker"
__version__ = "10/25/2018"
__pylint__ = "2.12.2"

if __name__ == '__main__':
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?.,<>'

    length = input('Password length? ')
    length = int(length)

    passwords = input('How many passwords would you like? ')
    passwords = int(passwords)

    for p in range(passwords):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        print(password)
