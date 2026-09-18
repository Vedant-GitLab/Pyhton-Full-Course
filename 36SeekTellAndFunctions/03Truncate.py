# truncate() function : When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specitic size, you can use the truncate function.
#Here is an example of how to use the truncate function :


with open('36SeekTellAndFunctions/Sample.txt', 'w') as f:
    f.write("Hello World")
    f.truncate(5) #truncate is used to select the size of file means here only 5 characters should be in file

with open('36SeekTellAndFunctions/Sample.txt', 'r') as f:
    print(f.read())