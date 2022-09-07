import random

"""
The popular game from The Big Bang Theory
"""

__author__ = "David Walker"
__version__ = "10/18/2018"
__pylint__ = "2.12.2"

def compare(a1, a2):
    if a1 == a2:
        return("It's a tie!")
    elif a1 == 'rock':
        if a2 == 'scissors':
            return("Rock crushes scissors! You win!")
        elif a2 == 'paper':
            return('Paper covers rock! You lose!')
        elif a2 == 'lizard':
            return("Rock crushes lizard! You win!")
        else:
            return("Spock vaporizes rock! You lose!")
    elif a1 == 'scissors':
        if a2 == 'paper':
            return("Scissors cuts paper! You win!")
        elif a2 == 'rock':
            return("Rock crushes scissors! You lose!")
        elif a2 == 'lizard':
            return('Scissors decapitates lizard! You win!')
        else:
            return("Spock smashes scissors! You lose!")
    elif a1 == 'paper':
        if a2 == 'rock':
            return("Paper covers rock! You win!")
        elif a2 == 'scissors':
            return("Scissors cuts paper! You win!")
        elif a2 == 'lizard':
            return("Lizard eats paper! You lose!")
        else:
            return("Paper disproves Spock! You win!")
    elif a1 == 'lizard':
        if a2 == 'rock':
            return("Rock crushes lizard! You lose!")
        elif a2 == 'paper':
            return("Lizard eats paper! You win!")
        elif a2 == 'scissors':
            return("Scissors decapitates lizard! You lose!")
        else:
            return("Lizard poisons Spock! You win!")
    elif a1 == 'Spock':
        if a2 == 'rock':
            return("Spock vaporizes rock! You win!")
        elif a2 == 'scissors':
            return("Spock smashes scissors! You win!")
        elif a2 == 'paper':
            return("Paper disproves Spock! You lose!")
        else:
            return("Lizard poisons Spock! You lose!")

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
    comp_answer = random.randint(0,5)
    if comp_answer == 1:
        comp_answer = 'rock'
    elif comp_answer == 2:
        comp_answer = 'paper'
    elif comp_answer == 3:
        comp_answer = 'scissors'
    elif comp_answer == 4:
        comp_answer = 'lizard'
    else:
        comp_answer = 'Spock'

    print("The computer picks %s" %comp_answer)

    print(compare(user_answer, comp_answer))