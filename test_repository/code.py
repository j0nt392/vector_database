# Create an empty game board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if a player has won
def check_win(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        print_board()
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the chosen cell is empty
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        # Check if the current player has won
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a tie
        if all(cell != ' ' for row in board for cell in row):
            print_board()
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()