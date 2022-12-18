# Import the random module
import random
# Import the system module
import sys
import os

# Define the main function
def clear_screen():
    # Check the operating system
    if sys.platform == "win32":
        # If the operating system is Windows, use the cls command
        os.system("cls")
    else:
        # If the operating system is not Windows, use the clear command
        os.system("clear")

# Define the main function
def roll_dice(num_dice):

    # Print the result
    print("You rolled the following numbers:")
    xsum = 0
    for i in range(num_dice):
        # Generate a random number from 1 to 6
        dice_roll = random.randint(1, 6)
        xsum += dice_roll
        print(str(dice_roll), end=' | ')
    print(f"\nTotal Sum = {xsum}")


# Clearing screen for better view
clear_screen()
# Get the number of dice to roll from the user
num_dice = input("How many dice do you want to roll? ")
# Call the main function to start the game

roll_dice(int(num_dice))
