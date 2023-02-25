from collections import defaultdict
from heapq import heappop, heappush


def networkDelayTime(times, n: int, k: int) -> int:
    adjList = defaultdict(list)

    for u, v, w in times:
        adjList[u].append([v, w])

    dist = [float("inf") for _ in range(n+1)]
    dist[0] = 0
    dist[k] = 0
    minHeap = [(0, k)]

    while minHeap:
        tillNow, curr = heappop(minHeap)

        for nxt, time in adjList[curr]:
            if tillNow + time < dist[nxt]:
                tmp_time = tillNow + time
                dist[nxt] = tmp_time
                heappush(minHeap, (tmp_time, nxt))

    res = max(dist)
    if res == float("inf"):
        return -1
    return res


g = [[2, 1, 5], [2, 3, 1], [3, 4, 1], [3, 1, 1]]
n = 4
k = 2
print(networkDelayTime(g, n, k))
