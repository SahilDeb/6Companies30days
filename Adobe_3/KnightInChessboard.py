def knightProbability(n: int, k: int, row: int, column: int) -> float:
    dir = [[-2, 1], [-1, 2], [1, 2], [2, 1],
           [2, -1], [1, -2], [-1, -2], [-2, -1]]
    dp = [[[-1 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]
    # recur for k steps

    def recur(k, r, c):
        # base case
        if r < 0 or r >= n or c < 0 or c >= n:
            return 0
        if k == 0:
            return 1

        if dp[r][c][k] != -1:
            return dp[r][c][k]

        res = 0
        for d in dir:
            # moving to each position is a probability
            # if a successful move then add up the probability
            res += (1/8) * recur(k - 1, r + d[0], c + d[1])

        dp[r][c][k] = res
        return res

    return recur(k, row, column)


n = 3
k = 2
r = 0
c = 0
print(knightProbability(n, k, r, c))
