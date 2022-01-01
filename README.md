```python
# Trying to make a game like Sabrina did in this video!
# https://www.youtube.com/watch?v=xvOkXXprG2g

from typing import List
import random
import operator
from math import isclose
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 3
getcontext().rounding = ROUND_HALF_UP

Rules = "Rules:\nResponses must be a number (whole or with decimals). Hit the \
enter button if you wish to skip a question. If you wish to end the game, \
respond with 'end'. \n\
Note: In the event of a long decimaled answer, it will be rounded to the \
nearest hundreth. You do not have to respond as such.\n|\n\
If you wish to replay without running the program again, make sure the \
previous game has been ended and enter 'math_game()'.\n"

end = 'end'
num = '-.0123456789'

def math_game() -> List[list]:
    """ Use prompt to ask the user for a response to a mental math question 
    and continue asking until the user ends the program. Return a history of 
    the questions and reponses. """
    my_ans = ''
    list_of_qs = []
    q_num = 1
    operation = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/':
                 operator.truediv}
    op_list = list(operation)
    while my_ans != end:
        op = random.choice(op_list)
        if op == '+' or op == '-':
            MIN_R, MAX_R = -20, 21 
        elif op == '*':
            MIN_R, MAX_R = -10, 21 
        elif op == '/':
            MIN_R, MAX_R = 1, 21
            
        a, b = random.randrange(MIN_R, MAX_R), random.randrange(MIN_R, MAX_R)
        
        question = f"{a} {op} {b}"
        
        ans = operation[op](a, b)
        if type(ans) == float:
            if ans.is_integer():
                ans = int(ans)
                
        my_ans = input(f"Q{q_num}: {a} {op} {b} = ")
        
        non_numeric = False 
        for char in my_ans:
            if char not in num:
                non_numeric = True
                          
        if non_numeric and my_ans != end and my_ans != "":
            print("*Responses may only be numbers*")
            correctness = "Incorrect"
        elif my_ans == '':
            correctness = "SKIPPED"
            my_ans = '__'
        elif my_ans == end:
            continue
        elif (float(my_ans) == ans):
            correctness = "Correct"
        elif '.' in str(ans) and isclose(float(my_ans), ans, rel_tol=0.2):
            correctness = "Correct"
        else:
            correctness = "Incorrect"
        
        if type(ans) == float:
            ans = float(Decimal(ans).quantize(Decimal('0.01'), ROUND_HALF_UP))
            
        list_of_qs.append([f'Q{q_num}: {question} | Answer: {ans} '
                           f'| Your answer: {my_ans} | {correctness}'])
        q_num += 1
    if len(list_of_qs) > 0:
        print('\n-----------------\nResults')
        for i in range(len(list_of_qs)):
            print(*list_of_qs[i])

print(Rules)
math_game()
```
