#tuples are ordered collection of data items. they store multiple items in a single variable. Tuple items are seperated by commas and enclosed within round brackets(). tuples are immutable we can not alter them after creation.

tup = (1, 2, 3, 4, "Venu", True)
print(type(tup))
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])

#it is like lists we can also write it in negative indexing

if "Venu" in tup:
    print("it is present in tuple")
else:
    print("not present")


tup2 = tup[1:3]
print(tup2)

