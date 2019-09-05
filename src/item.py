# Write a class to hold item information, should include name and description attributes 
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f'{self.name} - {self.description}'
    def __repr__(self):
        return f'{repr(self.name)} - {repr(self.description)}'


# kitchen_knife = Item("PokeyStick", "a 10-inch chef's knife")
# print(kitchen_knife)