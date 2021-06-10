import random


# Quiz component 1 - Choice checker (Ask user and confirm response. Instructions function displays if asked)

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
    print("Print Instructions")
    return ""


# Main Routine

# List of valid responses
yes_no_list = ["yes", "no"]
true_false_list = ["true", "false"]

# Ask user if they have played before
# If 'yes', show instructions
played_before = choice_checker("Have you played the "
                           "game before? ", yes_no_list, "Please enter yes or no")

if played_before == "no":
    instructions()

print()
print("Program Continues")