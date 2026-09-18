#Exception handling is the process of responding to unwanted and unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or sustem crashing, and witout this process. exception would disrupt the normal operation of a program.

# a = input("Enter a number : ")
# print(f"Multiplication table {a} is : ")
# try: 
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid input")

# print("Some imp lines")
# print("Program end")


try:
    num = int(input("Enter an integer : "))
    a = [2, 4, 5]
    print(a[num])
except ValueError:
    print("Numbered entered is not an integer")

except IndexError:
    print("Invalid index")