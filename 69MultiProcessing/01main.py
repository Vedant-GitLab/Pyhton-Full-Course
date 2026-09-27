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

import multiprocessing
import requests
import os


def downloadfiles(url, name):
    response = requests.get(url)

    os.makedirs("files", exist_ok=True)

    with open(f"files/{name}.jpg", "wb") as f:
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