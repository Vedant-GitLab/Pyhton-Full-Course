#the continue statement skips the rest of the loop statements and causes the next iteration to occur.
for i in range(12):
    if(i==10):
        print("skips the iteration")
        continue
    print("5 X ", i+1, " = ", 5*(i+1))
