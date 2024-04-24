"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Peter Dudáš
email: hawk.pe@gmail.com
discord: hellscythee
"""

def print_board(board):
    print("========================================")
    print("+---+---+---+")
    for row in board:
        print("|", " | ".join(row), "|")
        print("+---+---+---+")
    print("========================================")

def check_winner(board, player):
    # Check horizontal, vertical, and two diagonal conditions
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def get_move(board):
    while True:
        try:
            position = int(input("Please enter your move number (1-9): ")) - 1
            if position not in range(9):
                print("Invalid move. Please choose a number between 1 and 9.")
            elif board[position // 3][position % 3] != ' ':
                print("This cell is already taken. Please try again.")
            else:
                return position
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tic Tac Toe")
    print("GAME RULES:\nEach player can place one mark (or stone)\nper turn on the 3x3 grid. The WINNER is\nwho succeeds in placing three of their\nmarks in a:\n* horizontal,\n* vertical or\n* diagonal row")
    print("Let's start the game")

    moves_count = 0
    while moves_count < 9:
        print_board(board)
        print(f"Player {current_player} |")
        position = get_move(board)
        board[position // 3][position % 3] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations, the player {current_player} WON!")
            return
        current_player = 'O' if current_player == 'X' else 'X'
        moves_count += 1

    print_board(board)
    print("The game is a draw.")

play_game()
