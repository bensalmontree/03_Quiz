# Quiz component 4 - Generate question (v1)
# Version 1 generates a random basic math question

from random import *

# Set score to 0
score = 0

# Loop questions 3 times
for i in range(3):
    
    # Randomly generate numbers and symbol ('+', '-' etc)
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    symbol = randint(1, 3)

    # If generated symbol is '1', ask a addition question
    if symbol == 1:
        question = int(input("What is " + str(num1) + "+" + str(num2) + "? "))
        answer = num1 + num2
    # If user's answer is correct add 1 to score 
        if question == answer:
            score = score + 1

    # If generated symbol is '2', ask a subtraction question
    elif symbol == 2:
        question = int(input("What is " + str(num1) + "-" + str(num2) + "? "))
        answer = num1 - num2
    # If user's answer is correct add 1 to score 
        if question == answer:
            score = score + 1

    # If generated symbol is '3', ask a multiplication question
    elif symbol == 3:
        question = int(input("What is " + str(num1) + "*" + str(num2) + "? "))
        answer = num1 * num2
    # If user's answer is correct add 1 to score 
        if question == answer:
            score = score + 1

# Print out total sum of score
print("Your score was " + str(score))

