#Multiple Inheritance in Python : Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

#Syntax : In Python, multiple inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.

# class ChildClass(ParentClass1,
# ParentClass2, ParentClass3):
# # class body


class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dance:
    def __init__(self, dancer):
        self.dance = self.dance

    def show(self):
        print(f"The dance style is {self.dance}")

class EmployeeDance(Employee, Dance):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance

o = EmployeeDance("Raghav", "Break Dance")
print(o.name)
print(o.dance)
o.show()  #class EmployeeDance(Employee, Dance) <--- iss class me jo pehle likha hoga wahi print hoga jaise Employee hai isliye pehle Employee class ka show function run hoga