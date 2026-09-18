# a = int(input("Enter an value between 5 and 9 : "))
# if (a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")


a = input("Enter a value between 5 and 9 : ")
if(a == "quit"):
    print("Program Existed")
else:
    a = int(a)
    if(a<5 or a>9):
        print("Value should be between 5 and 9")