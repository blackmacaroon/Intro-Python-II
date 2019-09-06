from room import Room
from player import Player

import time

# Declare all the rooms

room = {
    'outside':  Room("Outside",
                     "North of you, a house beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from dusty windows to the south. Dark
passages run north and east."""),

    'bedroom': Room("Grand bedroom", """A dark, quiet bedroom appears before you, it's decorated in deep purples and smells lightly of jasmine. Ahead, you see a soft, warm bed on the north wall, your eyelids feel heavy and your knees are weak. Just a quick nap."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of breads and meats and garlic permeates the air."""),

    'kitchen': Room("Kitchen Chamber", """You've found the long-lost kitchen
chamber! Come, child. Do not be afraid. Eat and be happy."""),
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
current_room = room['outside']

#
# Main
#
# 
# Make a new player object that is currently in the 'outside' room.

quit = False

player = Player("Kayla", room['outside'])

while quit is False:
    print("player room", player.current_room)
    command = input(f"\n(N)orth\n(E)ast\n(S)outh\n(W)est\n(I)nspect area\n(Q)uit the game\n\nCommand: ")
    command = command.lower().strip()    #normalize inputs - lowercase and strip removes any extra leading or tailing spaces
    # if command == '':
    #     continue
    # command = command[0]      #no matter how long the input, just take the first letter - not perfect "eat" can head east
    if command == 'q':
        quit: True
    if command == 'n':    # head north
        if player.current_room.n_to:
            player.switch_room(player.current_room.n_to)
        else:
            print("Can't go that way.")
        # print("heading north")
        # print(current_room)
        
    # elif command == 's':    # head south
    #     print("heading south")
    #     current_room = room[current_room].s_to
        
    # elif command == 'e':    # head east
    #     print("heading east")
    #     current_room = room[current_room].e_to
        
    # elif command == 'w':    # head west
    #     print("heading west")
    #     current_room = room[current_room].w_to
        
    # elif command == 'i':    # investigate the area
    #     pass
    else:
        print("not a valid command\ntry again")

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


