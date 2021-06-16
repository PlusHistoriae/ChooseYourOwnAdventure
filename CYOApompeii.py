print ("Hello. This is the ChooseYourOwnAdventure speaking. You are playing ChooseYourOwnAdventure - Pompeii, an adventure inspired by the values shown by Pompeii. Can you stop the eruption, while fighting hellish beasts, or will you burn to a crisp in the volcanic ashes, along with all the rest of the city? Find out, with ChooseYourOwnAdventure - Pompeii.")

print ("Would you like to proceed with ChooseYourOwnAdventure? If yes, type 1. If no, type 2.")

proceed_question = input()
proceed_question_answer_proceed = 1
proceed_question_answer_stop = 2

if str(proceed_question) == proceed_question_answer_stop:
  print ("The CYOA has been stopped.")
elif str(proceed_question) == proceed_question_answer_proceed:
  print ("The CYOA shall proceed.")
