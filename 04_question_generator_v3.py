import random

num1 = random.randint(1, 10)
num2 = random.randint(1,10)
symbol = random.randint(1, 2)

if symbol == 1:
    symbol = ">"

elif symbol == 2:
    symbol = "<"

question = "{} {} {}".format(num1, symbol, num2)
answer = eval(question)

print(answer)
user_choice = input("(T/F) " + question + ": ")

if user_choice == answer:
    print("Correct")

else:
    print("Incorrect")
