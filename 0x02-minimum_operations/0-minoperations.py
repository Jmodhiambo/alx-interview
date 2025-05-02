#!/usr/bin/python3
"""
This module contains a function to calculate the minimum number of operations
needed to generate exactly `n` characters 'H' using only Copy All and Paste.
"""


def minOperations(n) -> int:
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters in the file.
    Returns the minimum number of operations, or 0 if impossible.
    """
    if n < 2:
        return 0

    operations: int = 0
    factor: int = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
