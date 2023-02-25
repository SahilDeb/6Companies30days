# time complexity - O((2^n) * m * n)
from functools import lru_cache


def maxCompatibilitySum(students, mentors) -> int:
    m, n = len(students), len(students[0])
    score_dp = [[0 for _ in range(m)] for _ in range(m)]

    def compute(sIdx, mIdx):
        return sum(1 for i in range(n) if students[sIdx][i] == mentors[mIdx][i])

    # using mask to find permutations which matches mentor
    # use the @lru_cache to save values to save time.
    @lru_cache(None)
    def dp(mask, mIdx):
        ans = 0
        # base
        # if all the students are assigned
        if mask == 0:
            return ans

        # loop through all students
        for i in range(m):
            # checking & with powers of 2
            if mask & (1 << i):
                currScore = score_dp[i][mIdx] + dp(mask - (1 << i), mIdx + 1)
                ans = max(ans, currScore)
        return ans

    for i in range(m):
        for j in range(m):
            score_dp[i][j] = compute(i, j)

    # start from all students yet to be assigned
    # set bits (1s) represent the ids of the students yet to be assigned
    return dp((1 << m) - 1, 0)


s = [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0]]
m = [[1, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0]]
print(maxCompatibilitySum(s, m))
