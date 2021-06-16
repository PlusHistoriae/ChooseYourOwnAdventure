import random

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
    print("Choose your adventure! Your options are Pompey (at the time of the eruption), Britian (at the time of the Renaissance, Germany (at the time of WW2, Russia (at the time of the Russian Revoloution), France (at the time of Napoleon), and the USA (at the time of the revoloution. Type the number in which they are chronologicallly listed (for example Pompey 1, Britian 2, etc) for that specific ChooseYourOwnAdventure!")
else:
    print("Wrong!")

CYOA_question = input()

if CYOA_question == '1':
  import CYOApompeii
elif CYOA_question == '2':
  import CYOAbritian
elif CYOA_question == '3':
  import CYOAgermany
elif CYOA_question == '4':
  import CYOArussia
elif CYOA_question == '5':
  import CYOAfrance
elif CYOA_question == '6':
  import CYOAusa
else:
  print ("You have not entered a valid number/sentence/etc. If you wish to go forth, please reload the site, and enter a valid number/sentence/etc.")