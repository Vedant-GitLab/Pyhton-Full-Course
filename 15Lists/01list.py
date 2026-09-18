#lists are ordered collection of data items. they store multiple items iun a single variable. list items are seperated by commas and enclosed with square braclets. lists are mutable(changable).

marks = [4, 5, 7, "venu", True, 45, 5234]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# # print(marks[4])
# print("The length of this list is : ", len(marks))
# print(marks[-2]) #negative indexing
# print(marks[len(marks)-2]) #positive indexing


# if 4 in marks:  #to check the given is in list or not
#     print("yes")
# else:
#     print("no")

print(marks)
print(marks[:]) # It Means === [0:len(marks)]
print(marks[1:5])
print(marks[1:5:2])