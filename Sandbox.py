import random

operations = ["+", "*", "/", "-", "<", ">", "=="]
comparisons = ["<", ">", "=="]

num_1 = 4
num_2 = 6

for item in range(0, 5):
    operator = random.choice(operations)

    question = "{} {} {}".format(num_1, operator, num_2)

    if operator in comparisons:
        to_ask = "Is the following statment True or False? {}".format(question)
    else:
        to_ask = "{} = ".format(question)

    print(to_ask)

