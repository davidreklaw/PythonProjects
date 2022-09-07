import sys
import random

"""
The game of rock, paper, scissors
"""

__author__ = "David Walker"
__version__ = "02/15/2019"
__pylint__ = "2.12.2"

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("%s, you win!" %user1)
        else:
            return("%s, you lose!" %user1)
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("%s, you win!" %user1)
        else:
            return("%s, you lose!" %user1)
    elif u1 == 'paper':
        if u2 == 'rock':
            return("%s, you win!" %user1)
        else:
            return("%s, you lose!" %user1)
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")

if __name__ == '__main__':
    user1 = input("What's your name?")
    user1_answer = input('%s, do you want to chose rock, paper, or scissors?' %user1)
    user2_answer = random.randint(0,3)
    if user2_answer == 1:
        user2_answer = 'rock'
    elif user2_answer == 2:
        user2_answer = 'paper'
    else:
        user2_answer = 'scissors'

    print("The computer picks %s" %user2_answer)
    print(compare(user1_answer, user2_answer))