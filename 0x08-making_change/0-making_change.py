#!/usr/bin/python3
"""Making Change."""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Returns the fewest number of coins needed to meet total."""
    if total <= 0:
        return 0

    count: int = 0
    summation: int = 0
    i: int = 0

    coins.sort(reverse=True)

    while True:
        if summation > total:
            return -1
        if summation == total:
            return count

        if (summation + coins[i]) > total:
            i += 1

        summation += coins[i]
        count += 1
