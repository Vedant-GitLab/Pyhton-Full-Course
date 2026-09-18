#Inheritance in python : When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.
#Types : 1) Single Inheritance 2)Multiple Inheritance 3)Multilevel Inheritance 4)Hierarchical Inheritance 5)Hybrid Inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"Emolyee name is {self.name} and id is {self.id}")

class Programmer(Employee): #This is the inheritance method to put one class into another means a class inherits the properties of another class here programmer (Child) it inherits the properties of Employee class (parent) 
    def showlanguage(self):
         print("The Default language is Python")

a1 = Employee("Venu", 200)
a1.showdetails()
a2 = Programmer("Ravi", 546)
a2.showdetails()
a2.showlanguage()