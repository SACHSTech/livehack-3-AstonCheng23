"""
Name: Problem 1
Date: 3/3/2021
Authour: Aston
"""
print(" ***** Welcome to the DoorDash Distance Tracker ****** \n")

total_mileage = 0
mileage = 0
average_distance = 0
days = 0

#This counts until the mileage passes 100. You can record your mileage here.
while total_mileage < 100:
  print("___Day " + str(days) + "___")
  mileage = float(input("Enter in the distance driven for today in Kilometers: "))
  total_mileage = mileage + total_mileage
  days = days + 1
  
#This is just to keep an easier record of wins and losses.
print("\nSummary:")
print("Total Mileage: " + str(total_mileage) + "km")
print("Days: " + str(days) + "days\n")

#This is to tell the user their average distance driven per day.
if total_mileage >= 100:
  average_distance = total_mileage/days
  print("It took " + str(days) + " days to surpass 100km driven.")
  print("The average distance driven per day is " + str(average_distance) + "km.")