#Lambda Functions in Python : In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

#lambda arguments: expresston

#Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# def double(x):
#     return x+2

def ved(f, value):
    return 6+f(value)

double = lambda x:x*2
cube = lambda x:x*x*x
avg = lambda x, y, z : (x+y+z)/3

print(double(5))
print(cube(2))
print(avg(2, 4, 6))
print(ved(lambda x:x*x, 2)) #2 ka square + 6, from line 11