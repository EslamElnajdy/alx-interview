#!/usr/bin/python3
"""
docs
"""


def winnerIs(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p]):
            for i in range(p * p, n+1, p):
                prime[i] = False
            p += 1
    if (prime.count(True) - 2) == 0:
        return 'Ben'
    if (prime.count(True) - 2) % 2 == 0:
        return 'Ben'
    return 'Maria'


def isWinner(x, nums):
    """
    docs
    """
    numOfWinToMaria = 0
    numOfWinToBen = 0
    for round_num in nums:
        winner = winnerIs(round_num)
        if (winner == 'Maria'):
            numOfWinToMaria += 1
        elif (winner == 'Ben'):
            numOfWinToBen += 1
    if numOfWinToMaria > numOfWinToBen:
        return 'Maria'
    elif numOfWinToMaria < numOfWinToBen:
        return 'Ben'
    else:
        return None
