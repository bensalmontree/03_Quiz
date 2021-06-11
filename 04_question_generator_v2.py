from random import *

score = 0
for i in range(3):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    symbol = randint(1,3)
    
    gk_question = "{} + {}".format(num1, num2)
    gk_ans = eval(gk_question)
    print(gk_question)