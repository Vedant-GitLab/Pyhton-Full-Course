class Student:
    def __init__ (self):
        self._name = "Harry"

    def _funName(self):
        return "CodeWithHarry"

class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())

