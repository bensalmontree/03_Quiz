# Quiz component 4 - Generate question

import random

comparisons = ["<", ">", "=="]

num_1 = 4
num_2 = 6

for item in range(0, 5):
    operator = random.choice(comparisons)

    question = "{} {} {}".format(num_1, operator, num_2)
    answer = eval(question)

    if answer == True:
        answer = "true"

    else:
        answer = "false"

    print("Correct answer = {}".format(answer))

    user_choice = input("{} = ".format(question)).lower()
    
    if user_choice == answer:
        print("Correct\n")

    else:
        print("Sorry that is the wrong answer\n")

