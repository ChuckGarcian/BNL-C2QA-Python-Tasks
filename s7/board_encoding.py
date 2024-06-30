# Title: board_encoding.py
# Author: Charles "Chuck" Garcia
import random


def check(board1, board2, base):
    """
    Returns True if board1 equals board true. False otherwise
    """
    res = True
    for row in range(base):
        res = res and all(x == y for x, y in zip(board1[row], board2[row]))

    return res


def show_board(board, base):
    """
    Displays the given board 'board'
    """
    for i in range(base):
        print(board[i])


def encode(board, base):
    """
    Returns integer encoding of the passed board
    """
    res = 0

    for row in range(base):
        for col in range(base):
            pow_val = (row * base) + col
            res += board[row][col] * (base**pow_val)

    return res


def decode(a, base):
    """
    Returns the decoded board encoded by integer 'a'
    """

    # Construct temp 1d arr
    arr = [0] * (base * base)
    for i in range(base * base):
        arr[i] = a % base
        a = a // (base)

    # Create a 2d array
    res = [[0 for _ in range(base)] for _ in range(base)]

    # Construct the board
    for row in range(base):
        for col in range(base):
            res[row][col] = arr[row * base + col]

    return res


def gen_random_board(base):
    """
    Generates a board of size base x base with random entries s.t
    every entry is [0, base)
    """
    res = [[0 for _ in range(base)] for _ in range(base)]

    for row in range(base):
        for col in range(base):
            res[row][col] = random.randint(0, base - 1)

    return res


def main():
    # Task - display boards 2271, 1638, and 12065
    print("Board Number: 2271")
    show_board(decode(2271, 3), 3)
    print("Board Number: 1638")
    show_board(decode(1638, 3), 3)
    print("Board Number: 12065")
    show_board(decode(12065, 3), 3)

    # Testing Suite
    print("\nRunning Testing Suite Now")
    base = 3
    num_tests = 1000
    verbous = False

    # Testing Suite Logic
    for test_num in range(num_tests):
        # Generate random board and encode it
        board_expected = gen_random_board(base)
        encoded_val = encode(board_expected, base)

        # Now we decode the encoding and check if it equals
        # the original expected board
        board_actual = decode(encoded_val, base)
        assert check(board_actual, board_expected, base)

        if verbous:
            print(f"\n ------ Test Number: {test_num} ------ ")
            print("Test Board:")
            show_board(board_expected, base)
            print(f"Test Board Encoding: {encoded_val}")
            print("Actual board:")
            show_board(board_actual, base)

    print(f"Passed Testing Suite! - Ran {num_tests:,} tests")


main()
