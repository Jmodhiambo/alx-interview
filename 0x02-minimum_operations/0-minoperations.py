#!/usr/bin/python3
"""
This module provides a function to determine the minimum number of operations
needed to produce exactly `n` characters 'H' in a text file using only
'Copy All' and 'Paste' operations.
"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    if n < 2:
        return 0

    operations = 0
    body = 1
    clipboard = 0

    while body < n:
        if n % body == 0:
            clipboard = body
            body *= 2
            operations += 2  # Copy All + Paste
        else:
            body += clipboard
            operations += 1  # Just Paste

    if body != n:
        return 0

    return operations
