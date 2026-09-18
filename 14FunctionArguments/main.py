#there are four type of arguments that we caan provide in a functiuomn
# *Default arguments *Keyword arguments *Variable length arguments *Required arguments

def average(a=3, b=2): #here 3 and 2 are default arguments
    print("The average is ", (a+b)/2)
average(a=4) #the value of b is automatically taken cause it is defaault

def name(fname, mname = "columbus", lname = "zeus"):
    print(fname, mname, lname)
name("Xavier")

#______________________________________________________________________________________

average(b=4, a=6) #values are simultaneously

#______________________________________________________________________________________

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is : ", sum/len(numbers))
average(4, 5, 6)

#______________________________________________________________________________________

# average(5) here we do not give the value of b so it is "required"