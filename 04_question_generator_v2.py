from random import *


for i in range(3):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    symbol = randint(1, 2)

    if symbol == 1:
        symbol = ">"

    elif symbol == 2:
        symbol = "<"
    
    gk_question = "{} {} {}".format(num1, symbol, num2)
    gk_ans = eval(gk_question) 

    print("{} = {}".format(gk_question, gk_ans))
    
    user_emotion = input("How are you feeling today? ")
    
    if user_emotion == "happy":
        print("correct")
    else:
        print("Sorry that is the wrong answer")
