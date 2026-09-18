#Constructors : A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.
#A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.
#Syntax of Python Constructor

#def _init_(self):
# initializations

#there are two types of constructor: 1) Parameterized Constructor  2) Default constructor

class person:
    
    # def __init__(self):  #this is a default constructor cause it has no parameters
    #     print("Hey I am Vedant")
    def __init__(self, name, occ):
        print("Hey i am vedant")
        self.name = name
        self.occ = occ
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("Harry", "Youtuber")
b = person("Vedant", "Stdudent")
a.info()
b.info()
# print(a.name)
