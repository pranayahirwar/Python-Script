# Import the random module
import random

# Define the main function
def roll_dice():
  # Generate a random number from 1 to 6
  dice_roll1 = random.randint(1, 6)
  dice_roll2 = random.randint(1, 6)
  # Print the result
  print("You Rolled " + str(dice_roll1) +" & "+ str(dice_roll2) + " = " + str(dice_roll1 + dice_roll2))
#   print("You rolled a " + str(dice_roll2) + ".")

# Call the main function to start the game
roll_dice()

