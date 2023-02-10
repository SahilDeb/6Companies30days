def shoppingOffers(price, special, needs):
    n = len(price)
    sLen = len(special)
    dp = {}

    def combos(idx, needs):
        key = str(idx) + ' '.join([str(i) for i in needs])
        if idx < 0:
            return sum(x*y for x, y in zip(price, needs))

        if key in dp:
            return dp[key]

        readyForPick = True
        for i in range(n):
            if needs[i] < special[idx][i]:
                readyForPick = False
                break

        pick = float("inf")
        if readyForPick:
            new_needs = [needs[i] - special[idx][i] for i in range(n)]
            pick = special[idx][n] + combos(idx, new_needs)

        notPick = combos(idx - 1, needs)
        dp[key] = min(pick, notPick)
        return dp[key]

    return combos(sLen - 1, needs)


p = [2, 3, 4]
s = [[1, 1, 0, 4], [2, 2, 1, 9]]
n = [1, 2, 1]

print(shoppingOffers(p, s, n))
