from collections import deque


def minMutation(startGene: str, endGene: str, bank) -> int:
    if startGene == endGene or endGene not in bank:
        return -1

    n = len(bank)
    q = deque()
    visited = {startGene}

    q.append((startGene, 0))

    while q:
        curr, dist = q.popleft()
        if curr == endGene:
            return dist

        for i in range(n):
            if bank[i] in visited:
                continue

            diff = 0
            for k in range(8):
                if curr[k] != bank[i][k]:
                    diff += 1

            if diff == 1:
                q.append((bank[i], dist+1))
                visited.add(bank[i])
    return -1
