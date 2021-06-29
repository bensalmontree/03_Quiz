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

# List of operators
comparisons = ["<", ">", "=="]
add_sub = ["+", "-", "*"]
mul = ["*"]

# List of valid responses
valid_responses = ["true", "false"]
difficulty_list = ["easy", "normal", "hard", "xxx"]

# Define correct and incorrect questions + list
tf_questions = ["incorrect_question", "correct_question"]
true_answer = "true"
false_answer = "false"

# Define select_difficulty and set 'rounds_played' to 0
select_difficulty = ""
rounds_played = 0

# Ask user what difficulty of questions they want to play
select_difficulty = choice_checker("Select between a 'Easy', 'Normal', or 'Hard' quiz... ", difficulty_list, "Please enter 'Easy', 'Normal' or 'Hard'... \n")
print()

# For selected difficulty print matching heading and rounds number
if select_difficulty == "easy":
    rounds = 10
    heading = "--- 10 Easy Difficulty Math Questions ---\n"
    print(heading)

if select_difficulty == "normal":
    rounds = 15
    heading = "--- 15 Normal Difficulty Math Questions ---\n"
    print(heading)

if select_difficulty == "hard":
    rounds = 25
    heading = "--- 25 HARD DIFFICULTY Math Questions ---\n"
    print(heading)

# Start of Loop
end_game = "no"
while end_game == "no":

    # Print heading and add 1 for each round played
    question_heading = "-- Question {} / {} --".format(rounds_played + 1, rounds)
    print(question_heading)
    rounds_played += 1

    # Randomly generate operator 
    if select_difficulty == "easy":
        operator = random.choice(comparisons)

    if select_difficulty == "normal":
        operator = random.choice(add_sub)

    if select_difficulty == "hard":
        operator = random.choice(mul)
    
    # Randomly generate numbers
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    # Generate question and evaluate correct answer and incorrect answer
    question = "{} {} {}".format(num1, operator, num2)
    correct_answer = eval(question)
    incorrect_answer = correct_answer - random.randint(1,7)

    # Make evaluate variables ('True' / 'False') equal to strings so 
    # user_choice can recognise answer for 'Easy Difficulty'
    if correct_answer == True:
        answer = "true"

    elif correct_answer == False:
        answer = "false"

    # Randomly choose between a correct or incorrect statment
    gen_question = random.choice(tf_questions)

    # If 'Easy Difficulty' was selected print out question without answer 
    # e.g 5 > 3 instead of 5 > 3 = True
    if select_difficulty == "easy":

        # Ask user (T/F) question
        print("{} ".format(question))
        user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or 'False'")

        # Compare choices and print "Correct" or "Incorrect"
        if user_choice == answer:
            print("Correct\n")
        else:
            print("INCORRECT\n")

    # If 'Easy Difficulty' is not selected, print out question with answer
    # e.g 5 + 5 = 10
    else:

        # If randomly generated question is "correct_question", 
        # print out a correct math statement
        if gen_question == "correct_question":

            # Ask user (T/F) question
            print("{} = {}".format(question, correct_answer))
            user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or 'False'")

            # Compare choices and print "Correct" or "Incorrect"
            if user_choice == true_answer:
                print("Correct\n")
            else:
                print("INCORRECT\n")

        # If randomly generated question is "incorrect_question", 
        # print out a correct math statment
        else:

            # Ask user (T/F) question
            print("{} = {}".format(question, incorrect_answer))
            user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or False'")

            # Compare choices and print "Correct" or "Incorrect"
            if user_choice == false_answer:
                print("Correct\n")
            else:
                print("INCORRECT\n")

    # End Loop if number of rounds have overlapped total rounds
    if rounds_played == rounds:
        break