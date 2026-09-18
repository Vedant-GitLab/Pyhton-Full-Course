#In python anything that you enclose between single and double quotes is considered a string . A string is essentialy a sequence or array of textual data. String are used when working with unicode characters.
name = "Vedant"
freind = "Rohan"
otherfreind = 'Lovish'
#these are single line strings

apple = '''this
is 
a 
multiline
string
'''
#we can also use """ """ these quoteds for multiline string

print("Hello, " + name)
print(apple)

#We can also write index of string
print(name[0])
print(name[1])
print(name[-1])
#if we put a index which is not in a string, throws error for example
# print(name[6])

#Looping through the string
print("Lets use a for loop\n")
for character in name:
    print(character)