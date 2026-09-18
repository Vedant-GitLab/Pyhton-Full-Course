letter = "Hey my name is {} and i am from {}" 
name = "Vedant"
country = "India"
print(letter.format(name, country))
#in past year we format the string like given above but nowdays we have f-string method by whichh we can directly put the value in given string like given below 
letter1 = (f"Hey my name is {name} and i am from {country}")
letter1 = (f"We use f-string like this : Hey my name is {{name}} and i am from {{country}}")
print(letter1)


price = 2.43423
text = f"for only {price:.2f} dollars"
print(text)