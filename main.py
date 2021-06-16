import random

print ("Welcome to OnlineGameBook, the fluid, yet random online gamebook genre type program! Please fill out the following question to deter 4 year olds.")

numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
operators = "*", "+"

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
    print("Correct!")
    print("Choose your gamebook! Your options are Pompeii (at the time of the eruption), Britian (at the time of the Renaissance, Germany (at the time of WW2, Russia (at the time of the Russian Revoloution), France (at the time of Napoleon), and the USA (at the time of the revoloution. Type the number in which they are chronologicallly listed (for example Pompeii 1, Britian 2, etc) for that specific OnlineGameBook!")
else:
    print("Wrong!")

OGB_question = input()

if OGB_question == '1':
  import OGB_Pompeii
elif OGB_question == '2':
  import OGB_Britian
elif OGB_question == '3':
  import OGB_Germany
elif OGB_question == '4':
  import OGB_Russia
elif OGB_question == '5':
  import OGB_France
elif OGB_question == '6':
  import OGB_USA
else:
  print ("You have not entered a valid number/sentence/etc. If you wish to go forth, please reload the OnlineGameBook, and enter a valid number/sentence/etc.")