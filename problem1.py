"""
Name: Problem 1
Date: 3/3/2021
Authour: Aston
"""

print("*********TOURNAMENT TRACKER*********\n")
print("While inputing, please enter in your wins and losses as \"w\", and \"l\". \n")

win_counter = 0
loss_counter = 0
final_results = " "
games = 0 

for games in range(6):
  results = input("Please enter in the results of your six games: \n")
  if results == "w":
    win_counter = win_counter + 1
  elif results == "l":
    loss_counter = loss_counter + 1
  elif results != "w" or results != "l":
    print("Please input either \"w\" or \"l\". ")
  final_results = str(results) + str(final_results)

print(final_results)
print("You won " + str(win_counter) + " times, and lost " + str(loss_counter) + " times.")

if win_counter == 6 or win_counter == 5 and loss_counter < 2: 
  print("Your team is in Group 1")
if win_counter == 3 or win_counter == 4 and loss_counter < 3:
  print("Your team is in Group 2")
if win_counter == 1 or win_counter == 2 and loss_counter < 6:
  print("Your team is in Group 3")
if win_counter == 0 and loss_counter < 7:
  print("You are eliminated.")