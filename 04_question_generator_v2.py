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

    if gk_ans == True:
        gk_ans = "True"
    
    else:
        gk_ans = "False"

    print("Correct Answer = {}".format(gk_ans))
    
    user_choice = input("{} = ".format(gk_question))
    
    if user_choice == gk_ans:
        print("Correct\n")
    else:
        print("Sorry that is the wrong answer\n")
