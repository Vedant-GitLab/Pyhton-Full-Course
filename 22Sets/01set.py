#set are unorderd collection of data items. They store multiple items in a single variable. set items are seperated by commas and enclosed within curly brackets {}. sets are unchangable or immutable it means you cannot change items of the set once created. sts do not contaoins duplicate items.

s = {1, 2, 3, 2, 4, 2, 5}
print(s)

info = {"Raj", 22, "CST", False, 19 }
print(info)

ved = { }
print(type(ved))
ved1 = set( )
print(type(ved1))

for value in info:
    print(value)