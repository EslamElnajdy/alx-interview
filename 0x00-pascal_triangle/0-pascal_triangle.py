#!/usr/bin/python3

"""
We want to create a function that return a list of lists
  of integers that representing the Pascal's triangle of `n`

  - return an empty list if n <= 0
  - you can assume n will be always an integer


"""

def pascal_triangle(n):
  p_list = [[1]]
  for i in  range(n-1):
    sub_list = [1]
    prev_sub_list = p_list[-1]

    for j in range(i):
      sub_list.append(prev_sub_list[j+1] + prev_sub_list[j])

    sub_list.append(1)
    p_list.append(sub_list)

  return p_list
