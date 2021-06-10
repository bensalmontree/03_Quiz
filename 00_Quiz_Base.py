# Quiz component 0 - Base

# To do 
# Incorporate Choice checker + Instructions functions
# Ask user to select difficulty of quiz (easy, normal, hard)
# Implement rounds and give each difficulty varying # of rounds
# Generate T/F questions (e.g 2 + 2 = 4 or 2 + 2 = 5)
# Ask user if question is T/F
# Give user feedback (correct or incorrect)
# Implement Score Mechanics (e.g if user gets all questions right, score = 10/10)
# Implement End Quiz Summary (ask user if they want to see responses to questions)


# Functions go here

#  Check if response to question is valid
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

# Displays instuctions if asked
def instructions():
    print()
    print("This is a math quiz that will test your brains puzzle solving skills!\n")
    print("Choose between 3 different difficulties - Easy, Normal and Hard -")
    print("The quiz will display a statement, e.g '4 x 4 = 16', you will have to type 'True' or 'False' to answer them\n")
    print("Try and answer all the questions!")
    print("Good Luck!\n")
    return ""


# Main Routine

# Define select_difficulty
select_difficulty = ""

# List of valid responses
yes_no_list = ["yes", "no"]
true_false_list = ["true", "false"]
select_difficulty_list = ["easy", "normal", "hard", "xxx"]

# Ask user if they have played before
# If 'yes', show instructions
played_before = choice_checker("Have you played the "
                           "quiz before? ", yes_no_list, "Please enter yes or no")

if played_before == "no":
    instructions()

# Ask question
choose_instruction = "'Math Statement' - Is this True or False? "

# Ask user for selected difficulty
select_difficulty = choice_checker("Select between a 'Easy', 'Normal' or 'Hard' quiz... ", select_difficulty_list, "Please enter 'Easy', 'Normal' or 'Hard'.")

# Define rounds_played
rounds_played = 0

# Print out difficulty heading 
print()
if select_difficulty == "easy":
    rounds = 10
    heading = "--- 10 Easy Math Questions ---\n"

elif select_difficulty == "normal":
    rounds = 15
    heading = "--- 15 Normal Math Questions ---\n"
elif select_difficulty == "hard":
    rounds = 25
    heading = "--- 25 Hard Math Quiz ---\n"

print(heading)

end_game = "no"
while end_game == "no":

    # Start of Quiz Play Loop

    # Print Question Heading
    print("Question {}".format(rounds_played +1, rounds))
    choose = input(choose_instruction)

    # Print user's choice
    print("You chose {}\n".format(choose))
    rounds_played += 1

    # End quiz if # of rounds has been played
    if rounds_played == rounds:
        break

# End of game statement
print("Thank you for using your big brain :)\n")
