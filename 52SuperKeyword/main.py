# super keyword : The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.
# When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

class Parentclass:
    def Parent_Method(self):
        print("This is a Parent method")

class Childclass(Parentclass):
    def Parent_Method(self):
        print("Venu")
        super().Parent_Method()
    def Child_Method(self):
        print("This is a child method")
        super().Parent_Method()

child_object = Childclass()
child_object.Child_Method()
child_object.Parent_Method()


#Basically hum iska use isliye krte hai qki jb humko multiple data chahiye hota hai parent class se tb hum sbko copy paste nhi kr skte isliye hum super() keyword ka use krke data ko inherit ko krte hai