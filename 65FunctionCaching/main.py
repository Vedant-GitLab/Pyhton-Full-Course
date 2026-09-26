#Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularty useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently. In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called, Here's an example:

import functools
import time
@functools.lru_cache(maxsize=None)

#we can write those lines like:
# from functools import lru_cache
# @lru_cache(maxsize=None)

def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20 \n")
print(fx(5))
print("Done for 5 \n")
print(fx(2))
print("Done for 2 \n")

#dobara me itna time nhi lega turant print kr dega (functools module) apne cache memory me ye data save kr shuka hai ki isko itna hi time lgega
#Aur isko MEMORIZATION TECHNIQUE kehte hai
print(fx(20))
print("Done for 20 \n")
print(fx(5))
print("Done for 5 \n")
print(fx(2))
print("Done for 2 \n")

#iske liye fir time lgeg qki ye nyi value hai 
print(fx(34))
print("Done for 2 \n")