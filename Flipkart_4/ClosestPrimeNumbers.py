from collections import deque
from math import sqrt


def closestPrimes(left: int, right: int):
    # find prime numbers within given range
    # sieve of Eratosthenes

    # non_primes = set()
    # primes = []
    # for i in range(2, right+1):
    #     if i not in non_primes:
    #         if i >= left:
    #             primes.append(i)

    #         for j in range(i*i, right+1, i):
    #             non_primes.add(j)

    # if len(primes) < 2:
    #     return [-1, -1]

    # # check for valid pairs
    # # consider the min diff pair
    # minPair = [-1, -1]
    # minDiff = float("inf")
    # for i in range(1, len(primes)):
    #     if primes[i] == primes[i-1]:
    #         continue

    #     currDiff = primes[i] - primes[i-1]
    #     if minDiff > currDiff:
    #         minDiff = currDiff
    #         minPair = [primes[i-1], primes[i]]

    # return minPair

    def check_prime(n):
        if n < 2:
            return False

        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    q = deque()
    diff = float('inf')
    pair = [-1, -1]

    for i in range(left, right+1):
        if check_prime(i):
            q.append(i)

        if len(q) >= 2:
            if abs(q[0]-q[1]) < diff:
                diff = abs(q[0] - q[1])
                pair = [q[0], q[1]]

            if diff <= 2:
                return pair
            q.popleft()
    return pair


l = 114343
r = 549874
print(closestPrimes(l, r))
