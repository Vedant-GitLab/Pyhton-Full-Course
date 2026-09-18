cities1 = {"Tokyo", "Washington", "Madrid", "Los Angeles"}
cities2 = {"Edinburgh", "Tokyo", "Queenstown", "Washington"}
print(cities1.symmetric_difference(cities2)) # dono sets me common values ko minus krke display krna
cities2.symmetric_difference_update(cities1)
print(cities1, cities2)