import random

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list ( or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item is not in list
        print(error)
        print()

comparisons = ["<", ">", "=="]
user_responses_list = ["true", "t", "false", "f"]

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

    user_choice = choice_checker("{} = ".format(question), user_responses_list, "Please enter 'True' or 'False")
    
    if user_choice == answer:
        print("Correct\n")

    else:
        print("Sorry that is the wrong answer\n")


