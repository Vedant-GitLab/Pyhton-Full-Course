#Hierarchical Inheritance : Hierarchical Inheritance is a type of inheritance in Object- Oriented Programming where multiple subclasses inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner.
#Syntax:
# class BaseClass:
#     pass
# class D1(BaseClass):
#     pass
# class D2(BaseClass):
#     pass
# class D3(D2):
#     pass
# class D4(D2)
#     pass

class A:
    def show_A(self):
        print("This is Class A")


class B(A):
    def show_B(self):
        print("This is Class B")


class C(A):
    def show_C(self):
        print("This is Class C")


obj1 = B()
obj1.show_A()
obj1.show_B()

obj2 = C()
obj2.show_A()
obj2.show_C()