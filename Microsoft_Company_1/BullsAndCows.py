# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

from collections import defaultdict, Counter


def getHint(secret: str, guess: str) -> str:
    # Create freq maps for each strings
    count_secret, count_guess = Counter(secret), Counter(guess)

    bulls = cows = 0
    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
            # reduce the count in both maps
            count_secret[s] -= 1
            count_guess[g] -= 1

    # Iterate all the chars of guess
    for ch, count in count_guess.items():
        # If present in secret, take the min count from either maps
        if ch in count_secret:
            cows += min(count_secret[ch], count)

    return str(bulls) + 'A' + str(cows) + 'B'

    # n = len(secret)
    # bulls = 0
    # cows = 0

    # charFreq = defaultdict(int)
    # for i in range(n):
    #     sChar = secret[i]
    #     gChar = guess[i]

    #     if sChar == gChar:
    #         bulls += 1
    #     else:
    #         # using char count as +ve for secret and -ve for guess
    #         cows += int(charFreq[sChar] < 0) + int(charFreq[gChar] > 0)
    #         charFreq[sChar] += 1
    #         charFreq[gChar] -= 1

    # return str(bulls) + "A" + str(cows) + "B"
