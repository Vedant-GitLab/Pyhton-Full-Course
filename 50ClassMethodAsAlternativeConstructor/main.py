class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

e1 = Employee("Vedant", 23000)
print(e1.name)
print(e1.salary)

string = "Ankit-12000"
# e2 = Employee(string.split("-")[0], string.split("-")[1]) #agar humko baar baar kisi string ko split krke data show krna hoga to hum aise nhi kr skte isliye ek class bnana pdega 
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)


#Class Methods as Alternative Constructors : In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use. However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as altemative constructors.        A class method belongs to the class rather than to an instance of the class. One common use case for class methods as altemnative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. For example, consider a class named "Person" that has two attributes: "name" and "age", The default constructor for the class might look like this: