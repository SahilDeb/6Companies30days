def validation(perm, A):
    n = len(A)
    for i in range(n):
        # We only need to take care the statements of good person
        if perm[i] == '1':
            for j in range(n):
                # ignore the no statement person
                if A[i][j] == 2:
                    continue

                # If our current guess is contradicted
                if str(A[i][j]) != perm[j]:
                    return False
    return True

# Time complexity:
# O(2 ^ N) for trying all possible guesses
# O(N ^ 2) for validating each guess
# Total: O((N ^ 2) * (2 ^ N))


def maximumGood(statements) -> int:
    n = len(statements)
    ans = 0

    # For example, if we only have 3 people (N = 3), one guess could be [0, 1, 0] which means person 1, 3 are bad, person 2 is good. All the possible guesses would be [0, 0, 0], [0, 0, 1], [0, 1, 0], ... [1, 1, 1].
    # We can take these states as binary code 000, 001, 010, 011, ... 111, which means digital 0~7.
    # So we only need to iterate i from 0 to 2^N-1 and
    # then transform each num from digital format to binary format and fill the leading zeros.
    # 2^N could also be written as 1<<N
    for num in range(1 << n, 1 << (n + 1)):
        print(1 << n, 1 << (n+1), num)
        permutation = bin(num)[3:]
        if validation(permutation, statements):
            # count the max amount of good persons
            ans = max(ans, permutation.count('1'))
    return ans


s = [[2, 1, 2], [1, 2, 2], [2, 0, 2]]
print(maximumGood(s))
