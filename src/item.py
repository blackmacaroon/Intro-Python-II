# Write a class to hold item information, should include name and description attributes 
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f'{self.name} - {self.description}'
    def __repr__(self):
        return f'{repr(self.name)} - {repr(self.description)}'
    
    # def on_grab(self):
    #     print(f"grabbed {self.name}")
    # def on_drop(self):
    #     print(f"dropped {self.name}")