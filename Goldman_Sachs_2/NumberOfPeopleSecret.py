def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    MOD = int(1e09 + 7)
    dp = [1] + [0] * (n-1)

    share = 0
    for day in range(1, n):
        # shared till now + members till (day - delay)th day - remove members who forgets on (day - forget)th day
        dp[day] = share = (share + dp[day - delay] - dp[day - forget]) % MOD

    return sum(dp[-forget:]) % MOD


n = 500
d = 2
f = 4
print(peopleAwareOfSecret(n, d, f))
