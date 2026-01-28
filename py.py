class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return f"\n{self.name} makes a sound"
    
    def isHostile(self):
        if self.species == "yes":
            return f"{self.name} is hostile"
        else:
            return f"{self.name} is not hostile"



name = input("What kind of animal: ")
species = input("Is animal hostile: ")
animal = Animal(name, species)
print(animal.speak(),"\n",animal.isHostile())
