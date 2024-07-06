#!/usr/bin/python3
"""
This script determines the winner of a game based on prime numbers.
"""


def winnerIs(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p]):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime_count = prime.count(True) - 2
    if prime_count == 0 or prime_count % 2 == 0:
        return 'Ben'
    else:
        return 'Maria'


def isWinner(x, nums):
    """
    Determines the overall winner after x rounds based on the nums list.
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
