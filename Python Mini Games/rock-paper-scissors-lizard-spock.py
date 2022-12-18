# import the random module
import random
import time

"""
The game has a set of rules that determine the winner:
Rock beats scissors and lizard.
Paper beats rock and spock.
Scissors beats paper and lizard.
Lizard beats paper and spock.
Spock beats rock and scissors.
If both players choose the same option, it is a tie.
"""



# create a list of options
options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

# create a dictionary to map the options to their corresponding rules
rules = {
  'rock': ['scissors', 'lizard'],
  'paper': ['rock', 'spock'],
  'scissors': ['paper', 'lizard'],
  'lizard': ['paper', 'spock'],
  'spock': ['rock', 'scissors']
}

# create variables to store the scores
player_wins = 0
computer_wins = 0
ties = 0

# create a function to play the game
def play_game():
    # ask the player to choose an option
    #   player_choice = input('Choose rock, paper, scissors, lizard, or spock: ')
    player_choice = random.choice(options)
    
    # check if the player's choice is valid
    if player_choice not in options:
        print('Invalid choice!')
        return

    # generate a random choice for the computer
    
    computer_choice = random.choice(options)

    # determine the winner
    if player_choice == computer_choice:
        print('It is a tie!')
        global ties
        ties += 1
    elif computer_choice in rules[player_choice]:
        print('You win!')
        global player_wins
        player_wins += 1
    else:
        print('You lose!')
        global computer_wins
        computer_wins += 1

# ask the player how many games they want to play
num_games = int(input('Enter the number of games you want to play: '))

# play the specified number of games
for i in range(num_games):
    play_game()
    time.sleep(1)

# print the final scores
print(f'Player wins: {player_wins}')
print(f'Computer wins: {computer_wins}')
print(f'Ties: {ties}')
