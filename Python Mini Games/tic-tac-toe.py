# Define the game board
board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]]

# Define the players
player1 = "X"
player2 = "O"

# Define a function to print the game board
def print_board(board):
  print("\n")
  print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
  print("--+---+--")
  print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
  print("--+---+--")
  print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])

# Define a function to check if the game is over
def game_over(board):
  # Check for a horizontal win
  for i in range(3):
    if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != " ":
      return board[i][0]
  # Check for a vertical win
  for i in range(3):
    if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != " ":
      return board[0][i]
  # Check for a diagonal win
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
    return board[0][0]
  if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " ":
    return board[0][2]
  # Check for a tie
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        return False
  # If no win or tie, the game is still ongoing
  return None

# Define the main game loop
def play_game(board, player1, player2):
    # Print the initial game board
    print_board(board)
    # Start the game with player 1's turn
    current_player = player1
    # Keep playing until the game is over
    while not game_over(board):
      # Get the current player's move
      x, y = input("Player " + current_player + ", enter your move (row, column): ").split(",")
      x = int(x)
      y = int(y)
      # Make sure the move is valid
      if board[x][y] == " ":
        board[x][y] = current_player
        print_board(board)
        # Switch to the other player's turn
        if current_player == player1:
          current_player = player2
        else:
          current_player = player1
      # If the move is invalid, print an error message and let the player try again
      else:
        print("Invalid move! Please try again.")
    # Print a message to announce the winner or tie
    result = game_over(board)
    if result == player1:
      print("Player 1 wins!")
    elif result == player2:
      print("Player 2 wins!")
    else:
      print("It's a tie!")

play_game(board, player1, player2)

    

     
