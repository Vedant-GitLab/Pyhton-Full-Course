#Getters : Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method:

#Basically Getters are used to get the value
class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    #Getetr
    @property
    def ten_value(self):
        return 10*self._value #here we use 10* to multiply self.value(10) by 10 = 100

obj = Myclass(10)
print(obj.ten_value)
obj.show()