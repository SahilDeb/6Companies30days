from heapq import heappush, heappop


def countPaths(n: int, roads) -> int:
    adjList = [[] for _ in range(n)]
    for u, v, t in roads:
        adjList[u].append([v, t])
        adjList[v].append([u, t])

    minTime = [float("inf") for _ in range(n)]
    ways = [0 for _ in range(n)]
    pq = []
    # time, node
    heappush(pq, (0, 0))
    ways[0] = 1

    res = 0
    while pq:
        t, node = heappop(pq)
        if node == n-1:
            res = ways[node] % int(1e09+7)
            break

        minTime[node] = min(minTime[node], t)

        for adj, time in adjList[node]:
            newTime = t + time
            # if the minimum time to reach a node is found again
            # increase number of ways by count of ways to reach prev node
            if newTime == minTime[adj]:
                ways[adj] += ways[node]
            # if a better time to reach a node is found
            # push to heap with new time
            # update the minTime to reach that node
            # re-initialize the count of ways with count from prev node
            elif newTime < minTime[adj]:
                minTime[adj] = newTime
                heappush(pq, (newTime, adj))
                ways[adj] = ways[node]
    return res


n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
         [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
print(countPaths(n, roads))
