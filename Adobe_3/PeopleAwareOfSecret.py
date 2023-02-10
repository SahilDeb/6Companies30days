def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    MOD = int(1e09)+7

    dp = [0 for _ in range(n)]
    shared = 0
    dp[0] = 1

    for day in range(1, n):
        # shared till now + dp[day - delay] - dp[day - forget]
        shared = (shared + dp[day - delay] - dp[day - forget]) % MOD
        dp[day] = shared
    return sum(dp[-forget:]) % MOD


n = 6
d = 2
f = 4
print(peopleAwareOfSecret(n, d, f))
