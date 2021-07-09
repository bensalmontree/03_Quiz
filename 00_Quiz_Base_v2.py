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
add_sub = ["+", "-"]
mul = ["*"]

# List of valid responses
valid_responses = ["true", "false"]
difficulty_list = ["easy", "normal", "hard", "xxx"]
yes_no_list = ["yes", "no"]

# Define correct and incorrect questions + list
tf_questions = ["incorrect_question", "correct_question"]
true_answer = "true"
false_answer = "false"

# Define select_difficulty and set 'questions_answered' to 0
select_difficulty = ""
questions_answered = 0

# Stuf
tf_answer = ""
questions_correct = 0
questions_incorrect = 0
quiz_summary = []

# Ask user what difficulty of questions they want to play
select_difficulty = choice_checker("Select between a 'Easy', 'Normal', or 'Hard' quiz... ", difficulty_list, "Please enter 'Easy', 'Normal' or 'Hard'... \n")
print()

# For selected difficulty print matching heading and questions_answered number
if select_difficulty == "easy":
    question_number = 10
    heading = "--- 10 Easy Difficulty Math Questions ---\n"
    print(heading)

if select_difficulty == "normal":
    question_number = 15
    heading = "--- 15 Normal Difficulty Math Questions ---\n"
    print(heading)

if select_difficulty == "hard":
    question_number = 25
    heading = "--- 25 HARD DIFFICULTY Math Questions ---\n"
    print(heading)

# Start of Loop
while questions_answered != question_number:

    print("Questions correct", questions_correct)

    # Print heading and add 1 for each question answered
    question_heading = "-- Question {} / {} --".format(questions_answered + 1, question_number)
    print(question_heading)
    questions_answered += 1

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

    if gen_question == "correct_question":
        ask_question = "{} = {}".format(question, correct_answer)
    elif gen_question == "incorrect_question":
        ask_question = "{} = {}".format(question, incorrect_answer)

    # Ask user (T/F) question
    print(ask_question)
    user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or 'False'")

    if user_choice == "false" and gen_question == "correct_question":
        outcome = "Correct"
    elif user_choice == "true" and gen_question == "incorrect_question":
            outcome = "Correct"
    else:
        outcome = "Incorrect"
    
    print(outcome)
    print()


# Generate correct and incorrect statement
# Generation question and ask user question
# Give Feedback