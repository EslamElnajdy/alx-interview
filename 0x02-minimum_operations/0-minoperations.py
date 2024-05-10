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
    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
