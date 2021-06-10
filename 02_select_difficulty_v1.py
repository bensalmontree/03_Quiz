# Quiz component 2 - Select difficulty

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

# List of valid responses
select_difficulty_list = ["easy", "normal", "hard", "xxx"]
select_difficulty = ""

# Ask user for selected difficulty
# Contiue game with selected difficulty
while select_difficulty != "xxx":
    select_difficulty = choice_checker("Select between a 'Easy', 'Normal' or 'Hard' quiz... ", select_difficulty_list, "Please enter 'Easy', 'Normal' or 'Hard'.")

    if select_difficulty == "easy":
        print("Continue with Easy quiz")
    elif select_difficulty == "normal":
        print("Continue with Normal quiz")
    elif select_difficulty == "hard":
        print("Continue with Hard quiz")