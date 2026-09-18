# Map, Filter and Reduce In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.

# MAP : The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

# Syntax : map(function, iterable)

# The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

def cube(x):
    return x*x*x
print (cube(2))

l = [1, 2, 5, 6, 8]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

newl = list(map(cube,l))
print(newl)

# FILTER : The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following
# syntax: filter(predtcate, iterable)

def filter_function(a):
   return a >4
newl = list(filter(filter_function, l))
print(newl) 