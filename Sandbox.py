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


user_responses = ["true", "t", "false", "f"]
comparisons = ["*", "+", "-"]

num_1 = random.randint(1,50)
num_2 = random.randint(1,50)

operator = random.choice(comparisons)
question = "{} {} {}".format(num_1, operator, num_2)
answer = eval(question)

print(question, "=", answer)
user_choice = choice_checker("True or False? ", user_responses, "Please enter 'True' or 'False'")


if user_choice == answer:
    print("Correct")

else:
    print("INCORRECT")

