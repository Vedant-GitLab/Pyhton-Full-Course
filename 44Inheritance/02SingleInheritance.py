#Single Inheritance in Python : Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

#Syntax : The syntax for single inheritance in Python is straightforward and easy to understand. To create a new class that inherits from a parent class, simply specify the parent class in the class definition, inside the parentheses, like this:

# class
#     ChildClass(ParentClass):
#     # class body

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def makesound(self):
        print("Sound make by the animal!")

class dog(Animal): #inherits the properties of Animal class
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed

    def makesound(self):
        print("Bark!")

class cat(Animal): #inherits the properties of Animal class
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Cat")
        self.breed = breed

    def makesound(self):
        print("Meow!")

d = dog("Dog", "Doggerman")
d.makesound()

e = cat("Cat", "Catter")
e.makesound()

a = Animal("Dog", "German shepherd")
a.makesound()