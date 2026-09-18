fruit = "pineapple"
fruitlen = len(fruit)
print(fruitlen)
print(fruit[0:5]) #it goes from 0 to (n-1) it menas hare i put 5 so it goes from 0 to 4
print(fruit[ :5]) #if we dont put 0 so python assume automatically
print(fruit[0: ]) #if we dont put the end valut then python automatically assume the max value of string
#we can also use - indexing
print(fruit[0:len(fruit)-5])
print(fruit[-5:-1])
print(fruit[-5: ])