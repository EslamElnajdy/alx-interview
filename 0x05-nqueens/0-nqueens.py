#!/usr/bin/python3

"""
module
"""

from sys import argv

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, solutions):
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, solutions) or res
            board[i][col] = 0

    return res

def nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)


if __name__ == '__main__':
  if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
  n = int(argv[1])
  if type(n) is not int:
    print("N must be a number")
    exit(1)
  if n < 4:
    print("N must be at least 4")
    exit(1)
  nqueens(n)
  