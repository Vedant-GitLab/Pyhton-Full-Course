#Multithreading in Python : Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python.

#Importing Threading : We can use threading by importing the threading module.
#                      "import threading"

import threading
import time
from concurrent.futures import ThreadPoolExecutor

#indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds ")
    time.sleep(seconds)
    return seconds

def main():  #ye first example hai threading ka isko humne main function me daal diya hai taaki isko delete na krna pde jisse hum concurrent.futures ka code likh ske 
    time1 = time.perf_counter()  #use for perfomance counting
    #Normal code
    # func(4)
    # func(2)
    # func(1)

    #Creating a thread : To create a thread, we need to create a Thread object and then call its start() method. The start() method runs the thread and then to stop the execution, we use the join() method. Here's how we can create a simple thread.
    #Same code using thread
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()  #start sirf start krke background me complete hone ke liye chod deta hai 
    t2.start()
    t3.start()

    t1.join()  #end krne ke liye use hota hai
    t2.join()
    t3.join()

    #Calculating time
    time2 = time.perf_counter() 
    print(time2 - time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # future2= executor.submit(func, 2)
        # future3= executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        #second method to use Threadpoolexecutor by using map
        l =[3, 4, 5, 6]
        results = executor.map(func, l)
        for result in results:
            print(result)
poolingDemo()