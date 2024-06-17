#!/usr/bin/python3

"""
  rotate_2d_matrix - function that rotates a 2D matrix 90deg clockwise
  matrix: a 2D list representing the matrix to rotate
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    new_arr = []
    for i in range(n):
        temp = []
        for j in range(n - 1, -1, -1):
            temp.append(matrix[j][i])
        new_arr.append(temp)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = new_arr[i][j]
