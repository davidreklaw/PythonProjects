"""
The game of rock, paper, scissors
"""

import random

__author__ = "David Walker"
__version__ = "02/15/2019"
__pylint__ = "2.12.2"

def compare(user1answer, user2):
    """Compares answers and determines a winner"""
    if user1answer == user2:
        return "It's a tie!"
    if user1answer == 'rock':
        if user2 == 'scissors':
            return "{user1}, you win!"
        return "{user1}, you lose!"
    if user1answer == 'scissors':
        if user2 == 'paper':
            return "{user1}, you win!"
        return "{user1}, you lose!"
    if user1answer == 'paper':
        if user2 == 'rock':
            return "{user1}, you win!"
        return "{user1}, you lose!"
    return "Invalid input! You have not entered rock, paper or scissors, try again."

if __name__ == '__main__':
    user1 = input("What's your name?")
    user1_answer = input('{user1}, do you want to chose rock, paper, or scissors?')
    USER2ANSWER = random.randint(0,3)
    if USER2ANSWER == 1:
        USER2ANSWER = 'rock'
    elif USER2ANSWER == 2:
        USER2ANSWER = 'paper'
    else:
        USER2ANSWER = 'scissors'

    print("The computer picks {user2_answer}")
    print(compare(user1_answer, USER2ANSWER))
