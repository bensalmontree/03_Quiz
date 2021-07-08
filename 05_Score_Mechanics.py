# Quiz component

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

# Define select_difficulty and set 'rounds_played' to 0
select_difficulty = ""
rounds_played = 0

# Rounds set to 5 for testing purposes
rounds = 5
rounds_won = 0
rounds_lost = 0

# Empty list
quiz_summary = []

# Start of Loop
end_game = "no"
while end_game == "no":

    # Print heading and add 1 for each round played
    question_heading = "-- Question {} / {} --".format(rounds_played + 1, rounds)
    print(question_heading)
    rounds_played += 1
    
    # Generate question and evaluate correct answer and incorrect answer
    question = "1 + 1"
    correct_answer = eval(question)

    # Ask user (T/F) question
    print("{} = {}".format(question, correct_answer))
    user_choice = choice_checker("True or False? ", valid_responses, "Please choose between 'True' or 'False'")

    # Compare choices and print "Correct" or "Incorrect"
    if user_choice == true_answer:
        tf_answer = "true"
        print("Correct\n")
        rounds_won +=1
    else:
        print("INCORRECT\n")
        rounds_lost +=1
    

    outcome = "Round {}: {} - You said {}, the right answer is {}".format(rounds_played, question, user_choice, tf_answer)
    quiz_summary.append(outcome)

    # End Loop if number of rounds have overlapped total rounds
    if rounds_played == rounds:
        break

percent_correct = rounds_won / rounds * 100

print("-- Stats --")
print("You got {:.0f}% correct".format(percent_correct))
print("{} / {} \n".format(rounds_won, rounds))

game_history = choice_checker("Do you want to see game history? ", yes_no_list, "Please answer with 'Yes' no 'No' ")
if game_history == "yes":
    print("\n**** Game History****")
    for quiz in quiz_summary:
        print(quiz)

print("\nThanks for playing the quiz")

"true", "false"