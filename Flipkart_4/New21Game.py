def new21Game(n: int, k: int, maxPts: int) -> float:
    # end within n with prob 1
    if k == 0 or n >= k + maxPts - 1:
        return 1.0

    # dp[i]: prob of "points" >= i, where i <= n
    # dp[0] = 1 always as the game always starts with 0
    dp = [1.0] + [0.0] * n

    # pSum stores the sum of dp[i - maxPts : i]
    pSum = 0.0
    for i in range(1, n + 1):
        # continue to draw cards
        if i <= k:
            # update pSum to include dp[i-1]
            pSum += dp[i-1]

        # exclude dp[i-1 - maxPts] if it is out of range
        if i > maxPts:
            pSum -= dp[i-1 - maxPts]

        dp[i] = pSum / maxPts

    # sum of all probabilities to reach k or more
    return round(sum(dp[k:]), 5)


n = 21
k = 17
m = 10
print(new21Game(n, k, m))
