# Quiz component 4 - Generate question (v3)
# Version 3 is a more efficient version of Version 2 using the choice_checker function

import random

# Functions go here

# Check if response to question is valid
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

# List of operators
comparisons = ["<", ">", "=="]

# List of valid responses
user_responses_list = ["true", "t", "false", "f"]

# Numbers are fixed for testing purposes
num_1 = 4
num_2 = 6

# Loop questions 5 times
for item in range(0, 5):

    # Randomly generate operator
    operator = random.choice(comparisons)

    # Generate question and evaluate answer
    question = "{} {} {}".format(num_1, operator, num_2)
    answer = eval(question)

    # Make evaluate variables ('True' / 'False') equal to strings so user_choice can recognise answer
    if answer == True:
        answer = "true"

    else:
        answer = "false"

    # Print out correct answer for testing purposes
    print("Correct answer = {}".format(answer))

    # Ask user generated question using choice checker
    user_choice = choice_checker("{} = ".format(question), user_responses_list, "Please enter 'True' or 'False")
    
    # If user's answer is correct, print "Correct", otherwise print "Sorry that is the wrong answer"
    if user_choice == answer:
        print("Correct\n")

    else:
        print("Sorry that is the wrong answer\n")




