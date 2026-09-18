questions = [
    "What is the capital of India?",
    "Who is known as the Father of Computer?",
    "How many bits are there in 1 byte?",
    "Which language is used for Python programming?",
    "Which planet is known as the Red Planet?"
]

options = [
    ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Bill Gates", "B. Steve Jobs", "C. Charles Babbage", "D. Alan Turing"],
    ["A. 4", "B. 8", "C. 16", "D. 32"],
    ["A. Java", "B. C++", "C. Python", "D. HTML"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"]
]

answers = ["B", "C", "B", "C", "B"]

prize = [1000, 2000, 5000, 10000, 20000]

money = 0

print("================================")
print("       WELCOME TO KBC")
print("================================")

i = 0

while i < len(questions):

    print("\nQuestion", i + 1, "for rs", prize[i])
    print(questions[i])

    j = 0
    while j < len(options[i]):
        print(options[i][j])
        j = j + 1

    user_answer = input("Enter your answer: ").upper()

    if user_answer == answers[i]:
        money = prize[i]
        print("Correct Answer!")
        print("You won rs", money)

    else:
        print("Wrong Answer!")
        print("Game Over!")
        print("Correct answer was:", answers[i])
        break

    i = i + 1

print("\n================================")
print("You take home rs", money)
print("================================")