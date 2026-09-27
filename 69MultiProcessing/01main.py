#{Multiprocessing in Python : Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel. It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code. In this repl, we'll take a closer look at the multiprocessing module and its various functions and how they can be used in Python.
#Importing Multiprocessing : We can use multiprocessing by importing the multiprocessing module.
#import multiprocessing
#Now, to use multiprocessing we need to create a process object which calls a start() method. The start() method runs the process and then to stop the execution, we use the join( ) method. Here's how we can create a simple process.}

#Multi Threading and Multi Processing are little bit different. Threads, process ke andr hoti hai. Threads lightweight kaam ke lie use hoti hai aur processing poore ek complex work ke liye.


# import multiprocessing
# import requests

# def downloadfiles(url, name):
#     response = requests.get(url)
#     open (f"69MultiProcessing/file{name}.jpg", "wb").write(response.content)
#     print(f"Finished Downloading {name}")

# url = "https://picsum.photos/200/300"
# process = [ ]
# for i in range(5):
#     # downloadfiles(url, i)
#     p = multiprocessing.Process(target=downloadfiles, args=[url, i])
#     p.start()
#     process.append(p)

# for p in process:
#     p.join()
#(THIS CODE IS NOT WORKING DUE TO SOME ISSUES SO I USED CHATGPT)

import multiprocessing
import requests
import os


def downloadfiles(url, name):
    response = requests.get(url)

    os.makedirs("files", exist_ok=True)

    with open(f"69MultiProcessing/files{name}.jpg", "wb") as f:
        f.write(response.content)

    print(f"Finished Downloading {name}")


if __name__ == "__main__":

    url = "https://picsum.photos/200/300"

    processes = []

    for i in range(5):
        p = multiprocessing.Process(
            target=downloadfiles,
            args=[url, i]
        )

        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("All downloads completed!")