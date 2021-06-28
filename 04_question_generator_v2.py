# Quiz component 4 - Generate question (v2)
# Version 2 generates a greater / lower question

from random import *

# Loop questions 3 times
for i in range(3):

    # Randomly generate numbers and symbol
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    symbol = randint(1, 2)

    # If symbol is '1', ask a greater (>) question
    if symbol == 1:
        symbol = ">"

    # If symbol is '2', ask a lower (<) question
    elif symbol == 2:
        symbol = "<"
    
    # Generate question and evaluate answer
    gk_question = "{} {} {}".format(num1, symbol, num2)
    gk_ans = eval(gk_question)

    # Make evaluate variables ('True' / 'False') equal to strings so user_choice can recognise gk_ans
    if gk_ans == True:
        gk_ans = "True"
    
    else:
        gk_ans = "False"

    # Print out correct answer for testing purposes
    print("Correct Answer = {}".format(gk_ans))

    # Ask user generated question
    user_choice = input("{} = ".format(gk_question))
    
    # If user's answer is correct, print "Correct", otherwise print "Sorry that is the wrong answer"
    if user_choice == gk_ans:
        print("Correct\n")
    else:
        print("Sorry that is the wrong answer\n")
