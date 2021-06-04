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


# Main Routine

rounds_played = 0
questions = "Question 1... Is this statement 'True' or 'False'? "

# List of valid responses
select_difficulty_list = ["easy", "normal", "hard", "xxx"]
select_difficulty = ""

# Ask user for selected difficulty
select_difficulty = choice_checker("Select between a 'Easy', 'Normal' or 'Hard' quiz... ", select_difficulty_list, "Please enter 'Easy', 'Normal' or 'Hard'.")


# Contiue game with selected difficulty
print()
if select_difficulty == "easy":
    rounds = 10
    heading = "{} Easy Math Questions".format(rounds)

elif select_difficulty == "normal":
    rounds = 15
    heading = "{} Normal Math Questions".format(rounds)

elif select_difficulty == "hard":
    rounds = 25
    heading = "{} Hard Math Quiz".format(rounds)

print(heading)