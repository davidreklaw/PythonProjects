"""
RPG Game
"""

__author__ = "David Walker"
__version__ = "10/25/2018"
__pylint__ = "2.12.2"

def showInstructions():
    """Shows the instructions"""
    print('''
  RPG Game
  ========

  Get to the Garden with a key and a potion
  Avoid the monster!

  Commands:
    go [direction]
    get [item]
  ''')

def showStatus():
    """Shows the stats of the game"""
    print('---------------------------')
    print('You are in the ' + CURRENTROOM)
    print('Inventory : ' + str(inventory))
    if "item" in rooms[CURRENTROOM]:
        print('You see a ' + rooms[CURRENTROOM]['item'])
    print("---------------------------")

if __name__ == '__main__':
    inventory = []

    rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item' : 'monster'
                },

            'Dining Room' : {
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion'
                },
            'Garden' : {
                  'north' : 'Dining Room'
            }

         }

    CURRENTROOM = 'Hall'

    showInstructions()

    while True:

        showStatus()

        MOVE = ''
        while MOVE == '':
            MOVE = input('>')

        MOVE = MOVE.lower().split()

        if MOVE[0] == 'go':
            if MOVE[1] in rooms[CURRENTROOM]:
                CURRENTROOM = rooms[CURRENTROOM][MOVE[1]]
            else:
                print('You can\'t go that way!')

        if MOVE[0] == 'get' :
            if "item" in rooms[CURRENTROOM] and MOVE[1] in rooms[CURRENTROOM]['item']:
                inventory += [MOVE[1]]
                print(MOVE[1] + ' got!')
                del rooms[CURRENTROOM]['item']
            else:
                print('Can\'t get ' + MOVE[1] + '!')

        if 'item' in rooms[CURRENTROOM] and 'monster' in rooms[CURRENTROOM]['item']:
            print('A monster has got you... GAME OVER!')
            break

        if CURRENTROOM == 'Garden' and 'key' in inventory and 'potion' in inventory:
            print('You escaped the house... YOU WIN!')
            break
