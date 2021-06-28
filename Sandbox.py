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
add_sub = ["+", "-", "*"]
mul_div = ["*"]
valid_responses = ["true", "false"]
difficulty_list = ["easy", "normal", "hard", "xxx"]
tf_questions = ["incorrect_question", "correct_question"]

true_answer = "true"
false_answer = "false"

select_difficulty = ""
rounds_played = 0

select_difficulty = choice_checker("Select between a 'Easy', 'Normal', or 'Hard' quiz... ", difficulty_list, "Please enter 'Easy', 'Normal' or 'Hard'... \n")
print()

if select_difficulty == "easy":
    rounds = 10
    heading = "--- 10 Easy Difficulty Math Questions ---\n"
    print(heading)

    end_game = "no"
    while end_game == "no":

        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        operator = random.choice(comparisons)

        question = "{} {} {}".format(num1, operator, num2)
        correct_answer = eval(question)

        if correct_answer == True:
            answer = "true"

        else:
            answer = "false"
        
        print(correct_answer)
        print("{} ".format(question, correct_answer))
        user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or 'False'")

        
        if user_choice == answer:
            print("Correct\n")
        else:
            print("INCORRECT\n")