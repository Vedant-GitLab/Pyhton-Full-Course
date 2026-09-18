cities1 = {"Tokyo", "Berlin", "Madrid", "Los Angeles"}
cities2 = {"Edinburgh", "Tokyo", "Queenstown", "Washington"}
print(cities1.difference(cities2)) #aesi values jo original set me hai lekin dusre me nhi
cities2.difference_update(cities1)
print(cities1, cities2)