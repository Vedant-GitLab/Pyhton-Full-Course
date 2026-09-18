# list comprehension is used for creating new list from other iteration like lists, tuples, dictionaries, set and even in arrays and strings. 
#SYNTAX : list = [Expression(item) for item in iterable if condition]



# lst = [i for i in range(10)]
# print(lst)

# lst1 = [i*i for i in range(10)]  #iteratioin from one list to another
# print(lst1)
# lst1 = [i*i for i in range(10) if (i%2==0)]
# print(lst1)


names = ["vedant", "venu", "shesh", "amit", "ravi", "ankit"]
nameswith_v = [item for item in names if "v" in item]
print(nameswith_v)
print(type(names))
print(type(nameswith_v))

