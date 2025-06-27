#!/usr/bin/python3

from typing import List, Any


def isWinner(x: int, nums: List[int]) -> Any:
    """
    Determines the winner of the prime game played by Maria and Ben.

    Returns:
        str | None: The name of the player with the most wins
             ('Maria' or 'Ben'), or None if the game is a tie.
    """
    if x < 1 or not nums:
        return None

    n: int = max(nums)

    # Sieve of Eratosthenes to find prime numbers up to n
    primes: List[bool] = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Precompute the number of primes up to each i
    prime_count: list[int] = [0] * (n + 1)
    count: int = 0
    for i in range(n + 1):
        if primes[i]:
            count += 1
        prime_count[i] = count

    # Track the number of wins
    maria_wins: int = 0
    ben_wins: int = 0

    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
