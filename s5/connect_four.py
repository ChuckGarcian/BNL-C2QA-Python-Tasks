# Title: connect_four.py
# Author: Charles 'Chuck' Garcia


def checkLine(player, board, row, col, direction):
    """
    Checks win condition satisfaction at (row, col) in the given direction tuple[
    """
    delta_row = direction[0]
    delta_col = direction[1]
    success = True
    count = 1

    # Check the direction until we hit board limit or lose condition
    while row < len(board) and col < len(board[0]) and col >= 0 and count < 5:
        if board[row][col] != player:
            # Breaks pattern - i.e. lose cond.
            success = False
            break

        row += delta_row
        col += delta_col
        count = count + 1

    # Ensure count is 4 since we may have hit board limits
    return success and count == 4


def check_winner(player, board):
    """
    Returns True if player 'player' has won on the given board. False otherwise
    """
    # Encodes possible directions (e.g north, south ect)
    direction = {(0, 1), (1, 0), (1, 1), (1, -1)}

    # Traverses board searching for win condition
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                # Check all directions
                for dir in direction:
                    if checkLine(player, board, row, col, dir):
                        return True
    return False


def print_winner(board):
    print(*board, sep="\n")
    if check_winner(1, board):
        print("Player 1 wins!")
    else:
        if check_winner(2, board):
            print("Player 2 wins!")
        else:
            print("No winner yet")
    print()


def main():
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


main()
