#!/usr/bin/python3

"""
this module contains
    -> minOperations()
"""


def minOperations(n):
    """
    minOperations - function
    params:
        n: number
    return:
        number of operations
    """
    op = 0
    context = 'H'
    next = 'H'

    if n <= 0:
        return 0
    while (len(context) < n):
        if n % len(context) == 0:
            op += 2
            next = context
            context += context
        else:
            op += 1
            context += next

    return op
