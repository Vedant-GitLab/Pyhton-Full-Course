#READING A FILE
# f = open('35FileHandling/myfile2.txt', 'r') 
# text = f.read()
# print(text)
# f.close()


#WRITING A FILE
# f = open('35FileHandling/myfile2.txt', 'w') 
# f.write("Hello World")
# f.close()


#APPEND A FILE
# f = open('35FileHandling/myfile2.txt', 'a') 
# f.write("Hello World")
# f.close()


#WITH: isko muse krne ke baad file ko close krne ki jaroorat nhi hai
with open('35FileHandling/myfile2.txt', 'w') as f :  
    f.write("I am inside with") 