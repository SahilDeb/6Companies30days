# def optimalPath( x, y, m, n, dungeon, currSum, minHealth, res):
#     currSum += dungeon[x][y]
#     if currSum < 0:
#         minHealth = max(minHealth, abs(currSum))

#     if x == m-1 and y == n-1:
#         res[0] = min(res[0], minHealth)
#         return

#     # bottom move
#     if x + 1 < m:
#         optimalPath(x+1, y, m, n, dungeon, currSum, minHealth, res)

#     # right move
#     if y + 1 < n:
#         optimalPath(x, y+1, m, n, dungeon, currSum, minHealth, res)

def calculateMinimumHP(dungeon) -> int:
    m, n = len(dungeon), len(dungeon[0])
    # res = [float("inf")]
    # optimalPath(0, 0, m, n, dungeon, 0, 0, res)
    # return res[0]+1

    # dp[i][j] = min HP required to reach bottom right corner starting from (i, j)

    dp = [[float("inf")] * (n+1) for _ in range(m+1)]
    # base condition
    # putting 1 in the neighbouring cells of princess
    # if we have negative number like -5 in this cell, we need 6 hp to survive, if we have non-negative number in this cell, we need 1 hp to survive.
    dp[m][n-1] = dp[m-1][n] = 1

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            choose = min(dp[i][j+1], dp[i+1][j])
            dp[i][j] = max(choose - dungeon[i][j], 1)

    return dp[0][0]


m = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(calculateMinimumHP(m))
