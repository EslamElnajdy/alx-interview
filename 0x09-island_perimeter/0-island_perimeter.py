#!/usr/bin/python3
"""
0-island
"""

def island_perimeter(grid):
  """
  fun
  """
  n = len(grid)
  m = len(grid[0])
  perimeter = 0
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1:
        if i != 0:
          if grid[i - 1][j] == 0:
            perimeter += 1
        else:
          perimeter += 1
        if j != 0:
          if grid[i][j - 1] == 0:
            perimeter += 1
        else:
          perimeter += 1
        if i != n-1:
          if grid[i+1][j] == 0:
            perimeter += 1
        else:
          perimeter += 1
        if j != m-1:
          if grid[i][j+1] == 0:
            perimeter += 1
        else:
          perimeter += 1
  return perimeter
