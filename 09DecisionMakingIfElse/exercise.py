# time = float(input("Enter time = "))
# print("Now the time is = ", time, "O'clock")

# if(time>=1.01 and time<=11.59):
#     print("Good Morning")
# elif(time>=12.00 and time<=17.00):
#     print("Good afternoon")
# if (time>=17.01 and time<=24.00):
#     print("Good Night")
# if (time>=24.01):
#     print("This time is not valid")


import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
timestamp = time.strftime('%D:%M:%Y')
print(timestamp)
