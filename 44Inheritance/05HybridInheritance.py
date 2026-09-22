#Hybrid Inheritance in Python : Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class. In Python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

#Syntax
# class BaseClass:
#     pass

# class Derived1(BaseClass):
#     pass

# class Derived2(BaseClass):
#     pass

# class Derived3(Derived1, Derived2):
#     pass


class A:
    def show_A(self):
        print("Class A")


class B(A):
    def show_B(self):
        print("Class B")


class C(A):
    def show_C(self):
        print("Class C")


class D(B, C):
    def show_D(self):
        print("Class D")


obj = D()

obj.show_A()
obj.show_B()
obj.show_C()
obj.show_D()