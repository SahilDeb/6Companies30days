from collections import defaultdict
import heapq
from typing import List


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    adjList = defaultdict(list)

    for u, v, w in edges:
        adjList[u].append([v, w])
        adjList[v].append([u, w])

    # print(adjList)

    # djikstra algorithm
    def find_neighbors(city):
        # edge case
        # no edges for this city
        if city not in adjList:
            return 0

        # to track the cities visited
        visited = set()
        distance = [float('inf')] * n
        distance[city] = 0
        heap = [(0, city)]

        while heap:
            curr_w, curr = heapq.heappop(heap)

            if curr_w > distance[curr]:
                continue

            visited.add(curr)

            for adj, w in adjList[curr]:
                new_w = w + curr_w
                if new_w <= distance[adj] and new_w <= distanceThreshold:
                    distance[adj] = new_w
                    heapq.heappush(heap, (new_w, adj))
        return len(visited)

    best = [-1, float("inf")]
    # traverse all nodes
    for city in range(n):
        res = find_neighbors(city)
        if res <= best[1]:
            best[1] = res
            best[0] = city

    return best[0]


n = 4
e = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
d = 4
print(findTheCity(n, e, d))
