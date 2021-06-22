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

valid_responses = ["true", "false"]
comparisons = ["<", ">", "=="]
add_sub = ["+", "-", "*"]
mul_div = ["*"]

true_answer = "true"
false_answer = "false"
tf_questions = ["incorrect_question", "correct_question"]
incorrect_question = ""
correct_question = ""

question = "1 + 1"
correct_answer = eval(question)
incorrect_answer = correct_answer - 1

for item in range(0, 5):
    gen_question = random.choice(tf_questions)

    if gen_question == correct_question:

        print("{} = {}".format(question, correct_answer))
        user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or 'False'")

        if user_choice == true_answer:
            print("Correct\n")
        else:
            print("INCORRECT\n")

    else:

        print("{} = {}".format(question, incorrect_answer))
        user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or False'")

        if user_choice == false_answer:
            print("Correct\n")
        else:
            print("INCORRECT\n")