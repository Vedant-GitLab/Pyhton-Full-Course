f = open('35FileHandling/myfile.txt', 'r') #is used to only read the file
#f = open('35FileHandling/myfile2.txt', 'w') #is used to only write or create the new file
# print(f)
text = f.read()
print(text)
f.close()  #file ko close krna jaroori hai nhito error aayega