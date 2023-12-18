"""
In a game of chess, a queen is the most powerful piece on the board. She can move an unlimited number of squares in a
straight line in any of 8 directions (forwards, backwards, left, right, and each of the four diagonals in between).

The diagram below shows the queen's influence from her current position - she would be able to take any piece on a
square marked with an 'X'.

Image from: https://www.pinterest.com/pin/567453621770398092/

An opponent's king who can be taken by the queen is said to be in 'check', and would then need to find some way to
escape this situation.

In any normal game of chess, the queen would work with her army on a 8x8 board to threaten the king in this way,
and ultimately try to win the game. However, for this kata, the queen will work by herself on a 5x5 board.

The 5x5 chessboard will be represented as a 2 dimensional array, (ie: an array containing 5 other arrays, each
containing 5 single character elements). Empty spaces within each sub-array will be represented by an asterix: "*",
while one of these 25 elements will be represented by a "q" (queen) and a "k" (king). Both will be represented in
lower case.

The 2 dimensional chessboard array would look something like this:
var board = [ [ '*', '*', '*', '*', '*' ],
              [ '*', '*', '*', '*', 'k' ],
              [ '*', '*', '*', '*', '*' ],
              [ '*', 'q', '*', '*', '*' ],
              [ '*', '*', '*', '*', '*' ] ]

Your task is to write a function which will return true if the king is in check, and false if he isn't.
"""


def check(board):
    [q] = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 'q']
    [k] = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 'k']
    return q[0] == k[0] or q[1] == k[1] or abs(q[0] - k[0]) == abs(q[1] - k[1])


if __name__ == '__main__':
    board1 = [['*', 'q', '*', '*', 'k'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
    board2 = [['*', '*', '*', '*', '*'], ['*', 'k', '*', 'q', '*'], ['*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
    board3 = [['k', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['q', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
    board4 = [['*', 'q', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', 'k', '*', '*', '*'],
              ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
    board5 = [['*', 'k', '*', '*', '*'], ['*', '*', 'q', '*', '*'], ['*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
    board6 = [['*', '*', 'k', '*', '*'], ['*', 'q', '*', '*', '*'], ['*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
    board7 = [['*', '*', '*', 'q', '*'], ['*', '*', 'k', '*', '*'], ['*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
    board8 = [['*', '*', 'q', '*', '*'], ['*', '*', '*', 'k', '*'], ['*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
    board9 = [['*', '*', 'q', '*', '*'], ['k', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]
    board10 = [['*', '*', '*', '*', '*'], ['*', '*', '*', 'q', '*'], ['k', '*', '*', '*', '*'],
               ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]

    print(type(check(board1)) is bool)
    print(check(board1) is True)
    print(check(board2) is True)
    print(check(board3) is True)
    print(check(board4) is True)
    print(check(board5) is True)
    print(check(board6) is True)
    print(check(board7) is True)
    print(check(board8) is True)
    print(check(board9) is False)
    print(check(board10) is False)
