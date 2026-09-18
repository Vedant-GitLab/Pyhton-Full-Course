import os #importing os module

if(not os.path.exists("data")):
    os.mkdir("data") #make the file named by "data"

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")