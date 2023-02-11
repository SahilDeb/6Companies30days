def findTheWinner(n: int, k: int) -> int:
    if n == 1:
        return 1

    friends = [i for i in range(1, n+1)]

    pickIdx = 0
    while len(friends) > 1:
        n = len(friends)
        moves = k % n
        pickIdx = (pickIdx + (moves - 1)) % n
        friends.pop(pickIdx)
    return friends.pop()


n = 5
k = 3
print(findTheWinner(n, k))
