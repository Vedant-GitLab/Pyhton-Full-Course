#reduce : The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

#Syntax : reduce(function, iterable)

#The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple. The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] #1+2=3, 3+3=6, 6+4=10, 10+5=15

# Calculate the sun of the numbers using the reduce function
sum = reduce( lambda x, y: x + y, numbers)

# Print the sum
print(sum)