#In Python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code.


class Employee:
    companyName = "VENU"  #class variable
    noOfemployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02    #Instance Variable
        Employee.noOfemployees += 1

        
    def showDetails(self):
        print(f"The name of the employee is {self.name} and he gets the raise in salary of {self.raise_amount}% in {self.noOfemployees} sized {self.companyName} Company")

# Employee.showDetails(emp1)
emp1 = Employee("Vedant")
emp1.raise_amount = 0.03   
emp1.companyName = "NITIN"
emp1.showDetails()

emp2 = Employee("Ritik")
emp2.showDetails()


#Class Variables : Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.

#Instance Variables : Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that  is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.