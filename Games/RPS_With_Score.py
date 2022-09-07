import random as r

"""
Rock Paper Scissors with score keeping
"""

__author__ = "David Walker"
__version__ = "01/12/2022"
__pylint__ = "2.12.2"

def print_score():
        """
        Prints score
        """
        print(F"""Score:
Player: {PLAYER}
Computer: {OPPONENT}
Cat: {CAT}\n""")

if __name__ == '__main__':
    options = ['rock', 'paper', 'scissors']

    PLAYER = 0
    OPPONENT = 0
    CAT = 0

    CONT = 'y'
    while CONT == 'y':
        user = input("Pick one: rock, paper, or scissors\t")

        comp = options[r.randrange(0,2)]

        if user == options[0] and comp == options[1]:
            OPPONIENT = OPPONIENT + 1
            print("You lose\n")
            print_score()
        elif user == options[0] and comp == options[2]:
            PLAYER = PLAYER + 1
            print("You win\n")
            print_score()
        elif user == options[1] and comp == options[0]:
            PLAYER = PLAYER + 1
            print("You win\n")
            print_score()
        elif user == options[1] and comp == options[2]:
            OPPONIENT = OPPONIENT + 1
            print("You lose\n")
            print_score()
        elif user == options[2] and comp == options[0]:
            OPPONIENT = OPPONIENT + 1
            print("You lose\n")
            print_score()
        elif user == options[2] and comp == options[1]:
            PLAYER = PLAYER + 1
            print("You win\n")
            print_score()
        else:
            CAT = CAT + 1
            print("It's a tie\n")
            print_score()

        userinput = input("Play again? y/n\t")
        CONT = userinput