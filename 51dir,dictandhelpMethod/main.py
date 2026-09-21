#dir() : The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object. 

# x = [1, 2, 3]
# print(dir(x))  #dir is used to check all the methods which are able to apply on given data
# print(x.__add__) #__?__ ye double underscore wale methods ko dunder methods kehte hai



#dict _: The _dict __ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
p = Person("john", 78)
print(p.__dict__)  #it print a dictionary representation of an object attribute

#hetp() : The help() function is used to get help documentation for an object, including a description of its attributes and methods.
print(help(str))
print(help(Person))