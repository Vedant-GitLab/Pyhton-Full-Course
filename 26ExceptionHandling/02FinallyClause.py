#Finally clause : yeh hamesha execute hoga 
try:
    l = [1, 2, 4, 6]
    i = int(input("Enter an intger value : "))
    print(l[i])
except:
    print("Invalid index")
finally:
    print("It will always executed")