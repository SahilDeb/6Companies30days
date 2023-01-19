from collections import defaultdict


def minimumCardPickup(cards) -> int:
    n = len(cards)
    cardsPicked = defaultdict(int)
    minGap = float("inf")
    for i in range(n):
        if cards[i] in cardsPicked:
            minGap = min(minGap, i - cardsPicked[cards[i]] + 1)
        cardsPicked[cards[i]] = i

    return minGap if minGap != float("inf") else -1


n1 = [3, 4, 2, 3, 4, 7]
n2 = [1, 0, 5, 3]
print(minimumCardPickup(n1))
