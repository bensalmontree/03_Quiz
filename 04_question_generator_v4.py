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


# List of opereators
comparisons = ["<", ">", "=="]
add_sub = ["+", "-", "*"]
mul_div = ["*"]

# List of valid responses
valid_responses = ["true", "false"]
difficulty_list = ["easy", "normal", "hard", "xxx"]

# Define correct and incorrect questions + List
tf_questions = ["incorrect_question", "correct_question"]
true_answer = "true"
false_answer = "false"

# Define select difficulty and rounds_played
select_difficulty = ""
rounds_played = 0

# Ask user what difficulty of questions they want to play
select_difficulty = choice_checker("Select between a 'Easy', 'Normal', or 'Hard' quiz... ", difficulty_list, "Please enter 'Easy', 'Normal' or 'Hard'... \n")
print()

# If user chooses 'easy' run Easy Difficulty Quiz (greater / lower)
if select_difficulty == "easy":
    
    # Set rounds to 10 and print heading
    rounds = 10
    heading = "--- 10 Easy Difficulty Math Questions ---\n"
    print(heading)

    # Start of Loop
    end_game = "no"
    while end_game == "no":


        # Print heading and add 1 for each round played
        question_heading = "-- Question {} / {} --".format(rounds_played + 1, rounds)
        print(question_heading)
        rounds_played += 1

        # Randomly generate numbers and operator
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        operator = random.choice(comparisons)

        # Generate question and evaluate answer
        question = "{} {} {}".format(num1, operator, num2)
        correct_answer = eval(question)

        # Make evaluate variables ('True' / 'False') equal to strings so user_choice can recognise answer
        if correct_answer == True:
            answer = "true"

        else:
            answer = "false"
        
        # Ask user (T/F) question
        print("{} ".format(question, correct_answer))
        user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or 'False'")

        # Compare choices and print "Correct" or "Incorrect"
        if user_choice == answer:
            print("Correct\n")
        else:
            print("INCORRECT\n")
    
        # End Loop if number of rounds have overlapped total rounds
        if rounds_played == rounds:
            break

# If user chooses 'normal' run Normal Difficulty Quiz (addition / subtraction)
if select_difficulty == "normal":

    # Set rounds to 15 and print heading
    rounds = 15
    heading = "--- 15 Normal Difficulty Math Questions ---\n"
    print(heading)

    # Start of Loop
    end_game = "no"
    while end_game == "no":

        # Print heading and add 1 for each round played
        question_heading = "-- Question {} / {} --".format(rounds_played + 1, rounds)
        print(question_heading)
        rounds_played += 1

        # Randomly generate numbers and operator
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        operator = random.choice(add_sub)

        # Generate question and evaluate correct answer and incorrect answer
        question = "{} {} {}".format(num1, operator, num2)
        correct_answer = eval(question)
        incorrect_answer = correct_answer - 1

        # Randomly choose between a correct / incorrect math statement
        gen_question = random.choice(tf_questions)

        # If randomly generated question is "correct_question", print out a correct math statement
        if gen_question == "correct_question":

            # Ask user (T/F) question
            print("{} = {}".format(question, correct_answer))
            user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or 'False'")

            # Compare choices and print "Correct" or "Incorrect"
            if user_choice == true_answer:
                print("Correct\n")
            else:
                print("INCORRECT\n")

        # If randomly generated question is "incorrect_question", print out a correct math statement
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

# If user chooses 'hard' run Hard Difficulty Quiz (mul / div)
if select_difficulty == "hard":
    
    # Set rounds to 25 and print heading
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

        # randomly generate numbers and operator
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        operator = random.choice(mul_div)

        # Generate question and evaluate correct answer and incorrect answer
        question = "{} {} {}".format(num1, operator, num2)
        correct_answer = eval(question)
        incorrect_answer = correct_answer - 1

        # Randomly choose between a correct / incorrect math statement
        gen_question = random.choice(tf_questions)

        # If randomly generated question is "correct_question", print out a correct math statement
        if gen_question == "correct_question":

            # Ask user (T/F) question
            print("{} = {}".format(question, correct_answer))
            user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or 'False'")

            # Compare choices and print "Correct" or "Incorrect"
            if user_choice == true_answer:
                print("Correct\n")
            else:
                print("INCORRECT\n")

        # If randomly generated question is "incorrect_question", print out a incorrect math statement
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