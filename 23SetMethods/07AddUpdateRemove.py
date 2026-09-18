#Add()
cities = {"Agra", "Delhi", "Lucknow", "Ghaziabad"}
cities.add("Hyderabad")
print(cities)
#update()
cities1 = {"Bareilly", "Sitapur", "Ndls"}
cities.update(cities1)
print(cities, cities1)
#remove()/discard()
cities.remove("Agra")
print(cities)
cities.discard("Agra")
print(cities)