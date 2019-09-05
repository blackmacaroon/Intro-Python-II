# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name 
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f'{self.name} - {self.current_room}'
    def __repr__(self):
        return f'{repr(self.name)} - {repr(self.current_room)}'

    # def Take_Item(self):
