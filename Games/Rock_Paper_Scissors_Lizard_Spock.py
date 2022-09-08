"""
The popular game from The Big Bang Theory
"""

import random

__author__ = "David Walker"
__version__ = "10/18/2018"
__pylint__ = "2.12.2"

def compare(answer1, answer2):
    """Compares the two answers to determine a winner"""
    if answer1 == answer2:
        return "It's a tie!"
    if answer1 == 'rock':
        if answer2 == 'scissors':
            return "Rock crushes scissors! You win!"
        if answer2 == 'paper':
            return 'Paper covers rock! You lose!'
        if answer2 == 'lizard':
            return "Rock crushes lizard! You win!"
        return "Spock vaporizes rock! You lose!"
    if answer1 == 'scissors':
        if answer2 == 'paper':
            return "Scissors cuts paper! You win!"
        if answer2 == 'rock':
            return "Rock crushes scissors! You lose!"
        if answer2 == 'lizard':
            return 'Scissors decapitates lizard! You win!'
        return "Spock smashes scissors! You lose!"
    if answer1 == 'paper':
        if answer2 == 'rock':
            return "Paper covers rock! You win!"
        if answer2 == 'scissors':
            return "Scissors cuts paper! You win!"
        if answer2 == 'lizard':
            return "Lizard eats paper! You lose!"
        return "Paper disproves Spock! You win!"
    if answer1 == 'lizard':
        if answer2 == 'rock':
            return "Rock crushes lizard! You lose!"
        if answer2 == 'paper':
            return "Lizard eats paper! You win!"
        if answer2 == 'scissors':
            return "Scissors decapitates lizard! You lose!"
        return "Lizard poisons Spock! You win!"
    if answer1 == 'Spock':
        if answer2 == 'rock':
            return "Spock vaporizes rock! You win!"
        if answer2 == 'scissors':
            return "Spock smashes scissors! You win!"
        if answer2 == 'paper':
            return "Paper disproves Spock! You lose!"
        return "Lizard poisons Spock! You lose!"

if __name__ == '__main__':
    print('''The rules are quite simple:
    Scissors cuts paper.
    Paper covers rock.
    Rock crushes lizard.
    Lizard poisons Spock.
    Spock smashes scissors.
    Scissors decapitates lizard.
    Lizards eats paper.
    Paper disproves Spock.
    Spock vaporizes rock.
    And as it always has, rock crushes scissors''')

    user_answer = input("Do you pick rock, paper, scissors, lizard, or Spock? ")
    COMPUTERANSWER = random.randint(0,5)
    if COMPUTERANSWER == 1:
        COMPUTERANSWER = 'rock'
    elif COMPUTERANSWER == 2:
        COMPUTERANSWER = 'paper'
    elif COMPUTERANSWER == 3:
        COMPUTERANSWER = 'scissors'
    elif COMPUTERANSWER == 4:
        COMPUTERANSWER = 'lizard'
    else:
        COMPUTERANSWER = 'Spock'

    print("The computer picks {COMPUTERANSWER}")

    print(compare(user_answer, COMPUTERANSWER))
