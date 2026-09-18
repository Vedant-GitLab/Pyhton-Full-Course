#string are immutable but we can make a new string by chnage its appearence
a = "v!! Vedant !!!!!!!!! Vedant"
print(len(a)) #show thw total no of characters in string
print(a)
print(a.upper()) #turn all letters into capital
print(a.lower()) #turn all letters into small
print(a.rstrip("!"))#used to remove selected character #strip only back characters not front 
print(a.replace("Vedant","john")) #used to replace the string
print(a.split(" ")) #used to split the string into list
print(a.capitalize()) #capotalize first letter

str1 = "Welcome to the console!!!"
print(len(str1))
print(str1.center(50)) #is used tp put strings in centre

print(a.count("Vedant")) #is used to count thr occurence of strings
print(str1.endswith("5")) #it tells our string was end with it or not in boolean format

str2 = "he's name is \" Vedant \" and he is honest man"
print(str2.find("is")) #is used to find given character

hi = "WelcomeToTheConsole001"
print(hi.isalnum()) #ye batata hai ki string me A-Z, a-z, 0-9 present hai ya nhi agar hai to true otherwise false
print(hi.isalpha()) #isme sirf A-Z aur a-z hi dekhta hai 

str1 = "hello world"
print(str1.islower()) #tells us all the letters are in small letters in bool format

str1 = "helofreinds\n"
print(str1.isprintable()) #\n is not printable so it gives false

str1 = "               "
print(str1.isspace()) #if spaces are present gives true otherwise false

str1 = "Hello Freinds I Am Vedant"
print(str1.istitle()) #gives true if all the first letters of string are Capital otherwise false

print(str1.startswith("H")) #like ends with

s1 = "Hii I Am Vedant A Engineering Student"
print(s1.swapcase()) #converts capital into small and small into capital

s2 = "his name is dan"
print(s2.title()) #first into capital

