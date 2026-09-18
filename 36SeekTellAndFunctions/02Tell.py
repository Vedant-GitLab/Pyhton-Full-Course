#tellO function : The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position, For example:

with open('36SeekTellAndFunctions/file.txt', 'r') as f:
    print(type(f))
    #Move to the 10th byte in the file
    f.seek(10)  #used to read the element after 10 byte

    #Read the next 5 bytes
    print(f.tell()) #ye batata hai ki abhi hum kaha hai file me mtlb hum kitne characters aage hai
    data = f.read(5)
print(data)