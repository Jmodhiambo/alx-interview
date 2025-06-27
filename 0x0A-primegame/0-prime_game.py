#!/usr/bin/python3


def isWinner(x, nums):
    """
    Determines the winner of the prime game played by Maria and Ben.
    """
    if x < 1 or not nums:
        return None

    n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max(n)
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Count number of primes up to each index
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(len(primes)):
        if primes[i]:
            count += 1
        prime_count[i] = count

    # Count wins
    maria_wins = 0
    ben_wins = 0

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
