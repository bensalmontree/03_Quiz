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

select_difficulty = ""
rounds_played = 0
choose_instruction = "'Math Statement' - Is this True or False? "

comparisons = ["<", ">", "=="]
add_sub = ["+", "-", "*"]
mul_div = ["*", "/"]
true_false_list = ["true", "t", "false", "f"]
difficulty_list = ["easy", "normal", "hard", "xxx"]

select_difficulty = choice_checker("Select between a 'Easy', 'Normal', or 'Hard' quiz... ", difficulty_list, "Please enter 'Easy', 'Normal' or 'Hard'... ")


print()
if select_difficulty == "easy":
    rounds = 10
    heading = "--- 10 Easy Math Questions ---\n"
    print(heading)

    end_game = "no"
    while end_game == "no":

        num_1 = random.randint(1,50)
        num_2 = random.randint(1,50)
      
        print("Question {}".format(rounds_played +1, rounds))
        rounds_played +=1

        operator = random.choice(comparisons)
        question = "{} {} {}".format(num_1, operator, num_2)
        answer = eval(question)

        if answer == True:
            answer = "true"
        else:
            answer = "false"

        user_choice = choice_checker("(T/F) {} = ".format(question), true_false_list, "Please enter 'True' or 'False")
        
        if user_choice == answer:
            print("Correct\n")
        else:
            print("Sorry that is the wrong answer\n")

        if rounds_played == rounds:
            break

elif select_difficulty == "normal":
    rounds = 15
    heading = "--- 15 Normal Math Questions ---\n"
    print(heading)
    
    end_game = "no"
    while end_game == "no":

        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
      
        print("Question {}".format(rounds_played +1, rounds))
        rounds_played +=1

        operator = random.choice(add_sub)
        question = "{} {} {}".format(num_1, operator, num_2)
        answer = eval(question)

        user_choice = int(input("{} = ".format(question)))
        
        if user_choice == answer:
            print("Correct\n")
        else:
            print("Sorry that is the wrong answer\n")

        if rounds_played == rounds:
            break
     
else:
    rounds = 25
    heading = "--- 25 HARD Math Questions ---\n"
    print(heading)
    
    end_game = "no"
    while end_game == "no":

        num_1 = random.randint(1,20)
        num_2 = random.randint(1,20)
      
        print("Question {}".format(rounds_played +1, rounds))
        rounds_played +=1

        operator = random.choice(mul_div)
        question = "{} {} {}".format(num_1, operator, num_2)
        answer = eval(question)

        user_choice = int(input("{} = ".format(question)))
        
        if user_choice == answer:
            print("Correct\n")
        else:
            print("Sorry that is the wrong answer\n")

        if rounds_played == rounds:
            break