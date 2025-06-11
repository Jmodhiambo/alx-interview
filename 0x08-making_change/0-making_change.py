#!/usr/bin/python3
"""Making Change
This module provides a function to determine the fewest number of coins
needed to meet a given amount total using dynamic programming.
"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet total using DP."""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return int(dp[total]) if dp[total] != float('inf') else -1
