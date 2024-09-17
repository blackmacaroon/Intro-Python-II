# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name 
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f'{self.name} - You are currently in {self.current_room}'
    def __repr__(self):
        return f'({repr(self.name)} - You are currently in {repr(self.current_room)})'

    def switch_room(self, new_room):
        self.current_room = new_room

    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, item):
        self.items.remove(item)