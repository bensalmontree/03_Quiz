from random import *

score = 0
for i in range(3):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    symbol = randint(1,3)

    if symbol == 1:
        question = int(input("What is " + str(num1) + "+" + str(num2) + "?"))
        answer = num1 + num2
        if question == answer:
            score = score + 1

    elif symbol == 2:
        question = int(input("What is " + str(num1) + "-" + str(num2) + "?"))
        answer = num1 - num2
        if question == answer:
            score = score + 1

    elif symbol == 3:
        question = int(input("What is " + str(num1) + "*" + str(num2) + "?"))
        answer = num1 * num2
        if question == answer:
            score = score + 1


print("Your score was " + str(score))

