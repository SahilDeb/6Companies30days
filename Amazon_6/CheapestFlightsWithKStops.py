from collections import defaultdict
from heapq import heappop, heappush


def findCheapestPrice(n: int, flights, src: int, dst: int, k: int) -> int:
    adjList = defaultdict(list)

    for u, v, w in flights:
        adjList[u].append([v, w])

    # stops, dist, node
    pq = [(-1, 0, src)]
    dist = [float("inf")] * n
    dist[src] = 0

    while pq:
        stops, priceTillNow, node = heappop(pq)

        for nxt, w in adjList[node]:
            if stops + 1 <= k and priceTillNow + w < dist[nxt]:
                dist[nxt] = priceTillNow + w
                heappush(pq, (stops + 1, dist[nxt], nxt))

    return -1 if dist[dst] == float("inf") else dist[dst]


n = 4
g = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
s = 0
d = 3
k = 1

print(findCheapestPrice(n, g, s, d, k))
