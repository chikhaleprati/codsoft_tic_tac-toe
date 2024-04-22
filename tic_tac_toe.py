import random

def display_board(board):
    """
    Displays the current state of the Tic Tac Toe board.

    Args:
        board (list): The current state of the Tic Tac Toe board.
    """
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    """
    Checks if the given player has won the game.

    Args:
        board (list): The current state of the Tic Tac Toe board.
        player (str): The player whose win condition is being checked.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def play_game():
    """
    Runs the Tic Tac Toe game.
    """
    board = [" "] * 9
    player = "X"
    computer = "O"

    while True:
        display_board(board)

        # Player turn
        print(f"{player}'s turn.")
        while True:
            move = int(input("Enter a position (1-9): "))
            if board[move-1] == " ":
                board[move-1] = player
                break
            else:
                print("That position is already taken. Try again.")

        # Check for a winner
        if check_win(board, player):
            display_board(board)
            print(f"{player} wins!")
            break
        if " " not in board:
            display_board(board)
            print("It's a tie!")
            break

        #  computer's turn
        print(f"{computer}'s turn.")
        while True:
            move = random.randint(0, 8)
            if board[move] == " ":
                board[move] = computer
                break

        # Check for a winner
        if check_win(board, computer):
            display_board(board)
            print(f"{computer} wins!")
            break

play_game()