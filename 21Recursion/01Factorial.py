#Recursion is the process of defining something in terms of itself. for example if we place two mirrors facing eachother then any object between them would be reflect recursively.
# RECURSIVE FUNCTION : In python we know that a function can call their functions. it is even possible for the function call itself. these type of construct are termed as recursive functions. 


#factorial(7) = 7*6*5*4*3*2*1          
#factorial(6) = 6*5*4*3*2*1          
#factorial(5) = 5*4*3*2*1          
#factorial(4) = 4*3*2*1    
#factorial(n) = n * factorial(n-1)      
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1) #here we call factorial in factorial function
print(factorial(5))
print(5*factorial(4))

for i in range(10):
    print(factorial(i), end=" ")  