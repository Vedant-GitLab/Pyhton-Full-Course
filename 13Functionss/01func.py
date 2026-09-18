#a function is a block of code that perform a specific tasks whenever it is called. in bigger programs where we have large amount of codes. it is advisable to create or use existing functions that make the program flow organized and neat.
#it is used to seperate the code
# 1. user defined : jinko user bnata hai, Aur jin functions ke aage 'def' lgega wo user defined hote hai
# 2. Built in : pehle se bne hote hai min(), max(), list(), tuple(), dict(), range(), set(), print() etc.

def CalculateGmean (a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater (a,b):
    if(a>b):
        print("First number is grater")
    else:
        print("Second number is greater")

def isLesser(a,b):
    pass  #kuch mt kro, baad me use krne ke liye


a = 9
b = 8
CalculateGmean(a,b)
isGreater(a,b)

c = 8                
d = 7
CalculateGmean(c,d)
isGreater(c,d)