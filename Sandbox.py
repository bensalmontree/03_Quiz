import random
import time
import sys

ans = 0   #variable to hold question answer
question = 0   #question number
user_score = 0  #user's score
userInput = int()   #where user enters the answer
lastName = str()   #holds last name
firstName = str()   #holds first name
form = str()    #holds user's form

def function(score,name):   #writes user's information to a .txt file
    sumOfStudent = (name + ' scored ' + str(user_score))
    classNameTxt = (className, '.txt.')
    f = open(className, 'a')
    f.write(sumOfStudent + form + '\n')
    f.close()

def multiplication():   #creates a multiplication question
    global ans
    numberOne, numberTwo  = random.randint(0,20), random.randint(0,20)
    print("What is" , numberOne , "*" , numberTwo)
    ans = (numberOne * numberTwo)

def subtraction():   #creates a subtraction question
    global ans
    numberOne, numberTwo  = random.randint(0,20), random.randint(0,20)
    print("What is" , numberOne , "-" , numberTwo)
    ans = (numberOne - numberTwo)

def addition():   #creates a addition question
    global ans
    numberOne, numberTwo  = random.randint(0,20), random.randint(0,20)
    print("What is" , numberOne , "+" , numberTwo)
    ans = (numberOne + numberTwo)

operation = [multiplication,subtraction,addition]   #holds all of the opperators
randOperation = random.choice(operation)    #chooses a random operator

lastName = input("Please enter your surname: ").title()
firstName = input("Please enter your first name: ").title()
className = input("Please enter your form: ").title()
print()

def main():   #main game loop - ask questions and checks it against answer, stops are a give amount of questions
    question = 0
    user_score = 0
    randOperation = random.choice(operation)

    while True:
        try:
            randOperation()
            randOperation = random.choice(operation)
            if question >= 10:
                break
            userInput = int(input("Enter the answer: "))
            if userInput == ans:
                print("Correct!" + "\n")
                user_score += 1
                question += 1
            else:
                print("Incorrect!" + "\n")
                question += 1
        except ValueError:
            print("I'm sorry that's invalid")
            question += 1

main()    #initializes the function

print(firstName, lastName , "you scored" , user_score , "out of 10")   #shows the user's score and name

user_name = firstName + ' ' + lastName
function(user_score,user_name)

def endMenu():
    while True:
        try:  
            options = int(input('''Press '1' to view users' scores,
            press '2' to restart the test,
            press '3' to exit the game,

            Enter option here: '''))
        except ValueError:
            print("I'm sorry that was invalid...")

        if options == 3:  #exits the game...
            sys.exit()

        elif options == 2:   #starts the game loop again because it's in a function
            main()

        elif options == 1:   #displays everything on the .txt file
            f = open('userScore.txt', 'r')
            print(f.read())
            print()
            endMenu()

        else:
            print("Sorry, I don't understand. Please try again...")
            print()
            endMenu()        

endMenu()