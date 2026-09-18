#seek() function : The seek0 function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:

with open('36SeekTellAndFunctions/file.txt', 'r') as f:
    print(type(f))
    #Move to the 10th byte in the file
    f.seek(10)  #used to read the element after 10 byte

    #Read the next 5 bytes
    data = f.read(5)
print(data)