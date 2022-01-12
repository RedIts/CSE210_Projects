'''
Tic-Tac-Toe
Author: Dean Redito
'''

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or a_draw(board)):
        display_board(board)
        player_move(player, board)
        player = next_player(player)
    display_board(board)

def create_board():
    board = []
    for box in range (9):
        board.append(box + 1)
    return board

def display_board(board):
    print()
    print(" ———————————")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f" —— + — + —— ")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f" —— + — + —— ")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print(" ———————————")
    print()

def player_move(player, board):
    box = int(input(f"{player}'s turn to play. Choose a square (1-9): "))
    board[box - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current =="x":
        return "o"

def has_winner(board):
    return (board[0] == board[1] == board[2] or #Top 1|2|3
            board[3] == board[4] == board[5] or #Middle 4|5|6
            board[6] == board[7] == board[8] or #Bottom 7|8|9
            board[0] == board[3] == board[6] or #Left 1|4|7
            board[1] == board[4] == board[7] or #Middle 2|5|8
            board[2] == board[5] == board[8] or #Right 3|6|9
            board[0] == board[4] == board[8] or #Diagonal 1|5|9
            board[2] == board[4] == board[6])   #Diagonal 3|5|7

def a_draw(board):
    for box in range(9):
        if board[box] != "x" and board[box] != "o":
            return False
    return True

if __name__ == "__main__":
    main()