s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.intersection(s2))   #intersection : common values ko display krta hai
s1.intersection_update(s2)   #intersection update : sirf common values ko updated set me daalta hai
print(s1, s2)

#Example 2
cities1 = {"Tokyo", "Berlin", "Madrid", "Los Angeles"}
cities2 = {"Edinburgh", "Tokyo", "Queenstown", "Washington"}
print(cities1.intersection(cities2))
cities2.intersection_update(cities1)
print(cities1, cities2)