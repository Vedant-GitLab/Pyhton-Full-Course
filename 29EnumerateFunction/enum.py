# marks = [1, 23, 43, 64, 32, 23, 89]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Awesome Vedant!")
#     index += 1


#Enumerate Function : The enumerate function is a built iin function in python that allows  you to loop over a sequence (such as list tuple and string) and get the index and value of each element in the sequenceat he same time. 
marks = [1, 23, 43, 64, 32, 23, 89]

for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Awesome Vedant!")



fruits = ["apple", "mango", "banana", "guava"]
for index, fruit in enumerate(fruits):
    print(index, fruit)