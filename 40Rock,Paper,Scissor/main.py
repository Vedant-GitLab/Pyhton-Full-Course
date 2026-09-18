import random
options = ['Rock', 'Paper', 'Scissor']

user = input("Enter your choice by selecting Rock, Paper and Scissor : ").capitalize()
computer = random.choice(options)

print("User choice is : ",user)
print("Computer choice is : ", computer)

if user==computer:
    print("Draw!")
elif(user=="Rock" and computer=="Scissor") :
    print("You won!")
elif(user=="Paper" and computer=="Rock"):
    print("You won!")
elif(user=="Scissor" and computer=="Paper"):
    print("You won!")
else:
    print("computer won!") 