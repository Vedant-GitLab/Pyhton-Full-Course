x = 4        #Global Variable
print(x)

def hello():
    x = 5              #Local Variable
    print(f"This is local variable {x}")
    print("Hello harry")

hello()
print(f"This is a Global variable {x}")