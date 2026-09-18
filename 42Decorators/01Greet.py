def greet(fx):
    def mfx(*args, **kwargs): # *args and **kwargs are used when we have to do calculative problems otherwise we dont need to use any parameter
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet   
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a+b)

# greet (hello)()
hello()
# greet (add)(3, 4)
add(3, 4)