#Async IO in Python : Asynchronous I/O, or async for short, is a programming pattern that allows for high- performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

import asyncio
import time
import requests

async def function1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    print("func1")
    return "VEDANT"
async def function2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram2.ico", "wb").write(response.content) 
    print("func2")
async def function3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)
    print("func3")

async def main():          
    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()

    l = await asyncio.gather(  #ye sbhi functions ki values ko ek saath print krane ke liye use hota hai
        function1(),
        function2(),
        function3(),
    )
    print(l)

asyncio.run(main())