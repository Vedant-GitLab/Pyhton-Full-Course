#Setters : It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter
#Basically are used to change the value
class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    #Getter
    @property
    def ten_value(self):
        return 10*self._value #here we use 10* to multiply self.value(10) by 10 = 100

    #Setter
    @ten_value.setter
    def ten_value(self, new_value): #here the value is 67 and 6.7 = 10 because self._value = new_value/10
        self._value = new_value/10

obj = Myclass(10)
obj.ten_value = 67 #yaha pr setter automatically call hoga aur @ten_value.setter ke paas jayega
print(obj.ten_value)
obj.show()