from room import Room
from player import Player
from item import Item
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside",
                     "North of you, the house beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'bedroom': Room("Grand bedroom", """A dark, quiet bedroom appears before you, it's decorated in deep purples and smells lightly of jasmine. Ahead, you see a soft, warm bed on the north wall, but the floor is lava."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of bread permeates the air."""),

    'kitchen': Room("Kitchen Chamber", """You've found the long-lost kitchen
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['bedroom']
room['foyer'].e_to = room['narrow']
room['bedroom'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['kitchen']
room['kitchen'].s_to = room['narrow']

# Declare Items
item = {"fork", "just in case."} 
#
# Main
#
# Intro scene
def displayIntro():
    print("welcome to the game")
    print("you could win")
    print("or die")
    time.sleep(3)
    print("i mean, we all die, right?")
    time.sleep(3)
    print("but yours could be nasty.")
    time.sleep(5)
    print("although, dementia and strokes and cancer don't seem plesant...")
    time.sleep(5)
    print("you know what? nevermind. welcome to the game where you die no matter what.")

def setStage():


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
quit = False





displayIntro()