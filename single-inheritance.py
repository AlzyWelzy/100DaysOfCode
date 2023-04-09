class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def talk(self):
        print(f"{self.name} says hello")


class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def talk(self):
        print(f"{self.name} says meow")


neko = Cat("Neko", "Cat", "Persian")
neko.talk()

cow = Animal("Bessie", "Cow")
cow.talk()
