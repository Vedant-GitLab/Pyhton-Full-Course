#Access Specifiers/Modifiers : Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance. Let us see the each one of access specifiers in detail:

#Types of access specifiers : 1. Public access modifier 2. Private access modifier 3. Protected access modifier

#pehli baat python me Access Specifier jaisi koi cheez nhi hoti hai yeh sirf ek convention hai

class Employee:          
    def __init__(self):
        # self.name = "Ved"    #public specifier : isko bahar se access kiya ja skta hai
        self.__name = "ved"  #private specifier : isko __ ki help se private kiya jata hai aur isko indirectly access kr skte hai _class__object ki help se


a = Employee()
#print(a.name)  #private specifier ko directly access nhi kiya ja skta hai
print(a._Employee__name)  #indeirectly access kr skte hai and this concept (a._Employee__name) is called name mangling
print(a.__dir__())  #a = employee jitne functions use ho rhe hai saarre print honge
