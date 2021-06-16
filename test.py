import random

numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
operators = "*", "+", "-"

operand1 = random.choice(numbers)
operand2 = random.choice(numbers)
operator = random.choice(operators)

if operator == '+':
    answer = operand1 + operand2
elif operator == '-':
    answer = operand1 - operand2
else:
    answer = operand1 * operand2

user_input = input(str(operand1) + operator + str(operand2) + "? ")

if str(answer) == user_input:
    print('Correct!')
else:
    print('Wrong!')

import CYOApompeii