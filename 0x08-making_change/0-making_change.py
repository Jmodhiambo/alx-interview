#!/usr/bin/python3
from typing import List, Union


def makeChange(coins: List[int], total: int) -> int:
    """Returns the fewest number of coins needed to meet total using DP."""
    if total <= 0:
        return 0

    dp: List[Union[int, float]] = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return int(dp[total]) if dp[total] != float('inf') else -1
