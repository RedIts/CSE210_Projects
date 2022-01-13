"""
Tic-Tac-Toe
Author: Dean Redito
"""

def main():
    curr_player = next_player('')

    values = [' ' for x in range(9)]

    player_pos = {'X': [], 'O': []}

    while True:
        print_board(values)

        #Try Exception Block for wrong input on move variable
        try:
            print(f"Player {curr_player}'s turn. Choose a spot: ", end="")
            move = int(input())
        except ValueError:
            print("No such moves. Please Try Again.")
            continue

        #Input range check
        if move <1 or move >9:
            print("Values not on Board. Please Try Again.")
            continue

        #Check spot if not occupied by another player
        if values[move - 1] != " ":
            print("Spot taken. Please Try Again.")
            continue

        #Update board info
        values[move - 1] = curr_player

        player_pos[curr_player].append(move)

def print_board(values):
    """
    Function for displaying board.
    """
    print()
    print(" ———————————")
    print(f"| {values[0]} | {values[1]} | {values[2]} |")
    print(f" —— + — + —— ")
    print(f"| {values[3]} | {values[4]} | {values[5]} |")
    print(f" —— + — + —— ")
    print(f"| {values[6]} | {values[7]} | {values[8]} |")
    print(" ———————————")
    print()

def win_condition(player_pos, curr_player):
    """
    Check for win conditions.
    """
    #Possible win combinations
    combinations = [[1,2,3], [4,5,6], [7,8,9,], [1,4,7], [2,5,8], [3,6,9]]


def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
if __name__ == "__main__":
    main()