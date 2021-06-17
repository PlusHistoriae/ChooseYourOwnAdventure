import random

choice_1a_answer_2 = "You have chosen pacifism. You feel good about yourself. Now that you have done this, maybe it is time to instate pacifism in the rest of the city, and join the magistratus; the police. Or you could report the Divine Hand to the authorities.They werent the best of groups anyways, causing chaos. In fact that would help with your goal of instating peace, and prosperity to the city. Type 1 for joining the guard. Type 2 for reporting the Divine Hand."
choice_1a_answer_4 = "You head to the guard building, a huge towering structure with big windows, all with shutters closing them off from the peering eyes of travelers. You knock on the door, and a small, gruff man with pointy ears and ridid legs comes out. 'Hello?' he asks. Do you tell the truth about you being in the Divine Hand, or do you just tell him it exists? Type 1 for the truth, and 2 for leaving out your membership."

print ("Hello. This is the OnlineGameBook speaking. You are playing OnlineGameBook - Pompeii, an adventure inspired by the values shown by Pompeii. Can you stop the eruption, while fighting hellish beasts, or will you burn to a crisp in the volcanic ashes, along with all the rest of the city? Find out, with OnlineGameBook - Pompeii.")

print ("Would you like to proceed with OnlineGameBook? If yes, type 1. If no, type 2.")

proceed_question = input()

if proceed_question == '2':
  print("You stopped the OnlineGameBook.")

if proceed_question == '1':
  print ("The OnlineGameBook shall proceed.")
  print ("You will be reffered to as Kim Oustil for the length of the program.")
  print ("You walk down the streets of Pompeii, wondering, thinking, and procrastinating about your recent ousting. You were once part of the secret illegal society known as the 'Divine Hand', a religious group, with you as chancellor of the society, but the lowers ousted you, and you are now just a peasant, living off the streets. Ideas of revenge flow through your mind, but part of you wants them to prosper, maybe let them be, and after a while re-join the society. What will you do? Type 1 for revenge, and 2 for pacifism")

choice_1a = input()

if choice_1a == '1':
  print ("You have always been a bad chancellor. Now you realize why they ousted you. You are pretty sure they are either located in the sewers, or in a warehouse near the side of the road. But somthing tuggs at your mind: they didn't mean for bad intentions. They just wanted a better leader. But ideas of revenge still swirl through your head. Maybe you could report it to the authoriies! That would teach them. Type 1 for searching in the sewers to confront them. Type 2 for searching in the warehouse for them. Type 3 for pacifism. Type 4 for reporting them to the authorities.")

choice_2a = input()

if choice_2a == '1':
  print("The sewers smell terrible.")
if choice_2a == '2':
  print("You had a feeling they were in here.")
if choice_2a == '3':
  print(choice_1a_answer_2)
if choice_2a == '4':
  print(choice_1a_answer_4)

if choice_1a == '2':
  print(choice_1a_answer_2)

  choice_2b = input()
