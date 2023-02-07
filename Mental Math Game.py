# Trying to make a game like Sabrina did in this video!
# https://www.youtube.com/watch?v=xvOkXXprG2g

from typing import List
import random
import operator
from math import isclose
from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 3
getcontext().rounding = ROUND_HALF_UP

Rules = "Rules:\n\
Welcome to my first coded math game! It's just something to test your mental \
math skills, no timer.\n\
Responses may only be numbers (as in, no operations or simplifying fractions).\
To skip a question, hit the enter button. To end the game, respond with 'end'.\
 Your results will be displayed after you end the game.\
\nNote: The answer key will round to the nearest hundredth if it is \
has many decimals. You don't need to round your own answers.\n|||\n\
If you wish to replay without running the program again, make sure the \
previous game has been ended and enter 'math_game()'.\n"


# explain the actual rules of  the game!
# results will be displayed at the end

end = 'end'
num = '-.0123456789'


def math_game() -> None:
    """ Use prompt to ask the user for a response to a mental math question
    and continue asking until the user ends the program. Return a history of
    the questions and responses. """
    my_ans = ''
    list_of_qs = []
    q_num = 1
    correctness = ''
    operation = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/':
                 operator.truediv}
    op_list = list(operation)
    num_correct = 0

    while my_ans != end:
        if correctness == "Input Error":
            q_num -= 1
            my_ans = input(f"Q{q_num}: {a} {op} {b} = ")
            # ## ask the same question again

        else:
            op = random.choice(op_list)
            if op == '+' or op == '-':
                min_r, max_r = -20, 21
            elif op == '*':
                min_r, max_r = -10, 21
            else:
                min_r, max_r = 1, 21

            a, b = random.randrange(min_r, max_r), random.randrange(min_r, max_r)

            question = f"{a} {op} {b}"

            my_ans = input(f"Q{q_num}: {a} {op} {b} = ")

        ans = operation[op](a, b)
        if type(ans) == float:
            if ans.is_integer():
                ans = int(ans)

        non_numeric = False
        for char in my_ans:
            if char not in num:
                non_numeric = True

        if non_numeric and my_ans != end and my_ans != "":
            correctness = "Input Error"
            print("*Responses may only be numbers*")

        elif my_ans == '':
            correctness = "SKIPPED"
            my_ans = '__'
        elif my_ans == end:
            continue
        elif float(my_ans) == ans:
            correctness = "Correct"
            num_correct += 1
        elif '.' in str(ans) and isclose(float(my_ans), ans, rel_tol=0.2):
            correctness = "Correct"
            num_correct += 1
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
        print(f'\nQuestions attempted: {len(list_of_qs)}\
        \nCorrect responses: {num_correct}')


print(Rules)
math_game()
