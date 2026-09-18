#A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and  (member functions or methods). The user-defined objects are created using the class keyword.

#Object is the instance of the class used to access the properties of the class Now lets create an object of the class.

#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It must be provided as the extra parameter inside the method definition.

class person:
    name = "Vedant"
    occupation = "Student"
    clgfees = 1000
    def info(self):
        print(f"{self.name} is a {self.occupation} and his fees is {self.clgfees}")

a = person()
b = person()
c = person() #agar koi value assign nhi krenge toh defaukt value output me show hogi

a.name = "Ritik"
a.occupation = "Worker"
a.clgfees = 20000

b.name = "Nitin"
b.occupation = "shop"
b.clgfees = 13000
# print(a.name, a.occupation)
a.info()
b.info()
c.info()