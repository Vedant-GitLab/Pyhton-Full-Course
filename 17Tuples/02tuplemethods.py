#Tuples are immutable but if we want to change them then first we have to convert it into a list and then after doing changes change into tuple
country = ("India", "Australia", "Newzealand", "America")
print(country)
temp = list(country) #convert into list
print(temp)
temp.append("Russia") #add item
print(temp)
temp.pop(3) #remove item
print(temp)
temp[2] = "Finland" #change item
print(temp)
country = tuple(temp) #again convert into tuple 
print(country)


#concatation of tuples
tup1 = ("ved", "Ami", "Ank", "Rav")
tup2 = ("Vis", "Sub", "Ris", "Cha")
tup = tup1 + tup2
print(tup)

tuple1 = (2, 3, 5, 2, 3, 4, 7, 5, 3, 3 )
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8) #(element, strat, end) use to find the index of given element by giving start and end points
res = len(tuple1)
print(res)
