s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))   #union : the result after merging both sets
s1.update(s2)   #union update : ye kisi ek set se values uthakr dusre me rkhta hai jisse wo update ho jata hai
print(s1, s2)

#Example 2
cities1 = {"Tokyo", "Berlin", "Madrid", "Los Angeles"}
cities2 = {"Edinburgh", "Paris", "Queenstown", "Washington"}
print(cities1.union(cities2))
cities2.update(cities1)
print(cities1, cities2)