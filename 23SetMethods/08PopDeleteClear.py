#pop : kisi bhi ek value ko pop kr dega
cities = {"Agra", "Delhi", "Lucknow", "Ghaziabad"}
itmes = cities.pop()
print(cities)
print(itmes)

#clear : pure set me sabhi values hata dega
cities.clear()
print(cities)

# #delete : it delete the whole set
# del cities
# print(cities)

#in : used to check the given value is present in set or not
info = {"hi", "I am", "Vedant", 19, "Btech"}
if "Vedant" in info:
    print("Is present in info")
else:
    print("Not Present")