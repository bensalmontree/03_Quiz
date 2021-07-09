question = "2 + 2"
correct_ans = eval(question)

wrong_ans = 5

wrong_statement = "2 + 2 = 5"
right_statement = "2 + 2 = 4"

gen_question = wrong_statement

user_choice = input("T / F: ")

if user_choice == "F" and gen_question == "wrong":
    outcome = "correct"
elif user_choice == "T" and gen_question == "correct":
    outcome = "correct"
else:
    outcome = "incorrect"

# If the difficulty is easy make (T) = right_statement and (F) = false statement

2 + 2 = 4
2 + 2 = 5

2 > 2
