from room import Room
from player import Player
from story import (intro)
import time

# Declare all the rooms

room = {
    'yard':  Room("yard",
                     "north of you, a charming house beckons"),

    'foyer':    Room("foyer", """dim light filters in from dusty windows to the south. dark
passages run north and east."""),

    'bedroom': Room("grand bedroom", """a dark, quiet bedroom appears before you, it's decorated in deep purples and smells lightly of lavender, sage and amber. Ahead, you see a soft, warm bed on the north wall, your eyelids feel heavy and your knees are weak. You lay down for a quick nap. you never get up again."""),

    'narrow':   Room("narrow passage", """the narrow passage bends here from west
to north. the smell of breads and meats and garlic permeates the air."""),

    'kitchen': Room("kitchen", """you've found the kitchen
chamber! every inch of the table is covered in your favorite foods: buttery mashed potatoes, golden fried chicken, creamy cheesecake, hot pepperoni pizza, fresh baked focaccia, ripe juicy berries, melty cheese danish, sizzling crispy bacon, spicy red wine and a spongy angel-food cake dusted with confectioners sugar."""),
}

# Link rooms together

room['yard'].n_to = room['foyer']
room['foyer'].s_to = room['yard']
room['foyer'].n_to = room['bedroom']
room['foyer'].e_to = room['narrow']
room['bedroom'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['kitchen']
room['kitchen'].s_to = room['narrow']

# Declare Items
item = {"fork", "just in case."} 
current_room = room['yard']

#
# Main
#
# 
# Make a new player object that is currently in the 'yard' room.

quit = False

player = Player("Kayla", room['yard'])

while quit is False:
    # intro()
    print("you are in the", player.current_room)
    time.sleep(2)
    print("where will you go?")
    time.sleep(2)
    command = input(f"\n(N)orth\n(E)ast\n(S)outh\n(W)est\n(I)nspect area\n(Q)uit while I'm healthy\n\nCommand: ")
    command = command.lower().strip()    #normalize inputs - lowercase and strip removes any extra leading or tailing spaces
    # if command == '':
    #     continue
    # command = command[0]      #no matter how long the input, just take the first letter - not perfect "eat" can head east
    if command == 'q':
        quit: True
        print("so long!")
    if command == 'n':    # head north
        print("heading north")
        time.sleep(2)
        if player.current_room.n_to:
            player.switch_room(player.current_room.n_to)
        else:
            print("Can't go that way.")
    if command == 'e':    # head east
        print("heading east")
        time.sleep(2)
        if player.current_room.e_to:
            player.switch_room(player.current_room.e_to)
        else:
            print("Can't go that way.")
    if command == 's':    # head south
        print("heading south")
        time.sleep(2)
        if player.current_room.s_to:
            player.switch_room(player.current_room.s_to)
        else:
            print("Can't go that way.")
    if command == 'w':    # head west
        print("heading west")
        time.sleep(2)
        if player.current_room.w_to:
            player.switch_room(player.current_room.w_to)
        else:
            print("Can't go that way.")
        
        
    # elif command == 'i':    # investigate the area
    #     pass
    # else:
    #     print("not a valid command\ntry again")

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


