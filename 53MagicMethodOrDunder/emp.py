#These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour. Magic methods, also known as "dunders" from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.


class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    def __repr__(self):
        return f"The name of the employee is {self.name} repr" #automatically fall back in repr when str is not working
    def __call__(self):
        print("Hey i am good")

