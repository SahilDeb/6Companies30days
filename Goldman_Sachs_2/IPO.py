from heapq import heappush, heappop


def findMaximizedCapital(k: int, w: int, profits, capital) -> int:
    n = len(profits)
    projects = list(zip(capital, profits))
    projects.sort(key=lambda x: x[0])
    heap = []

    i = 0
    for _ in range(k):
        while i < n and projects[i][0] <= w:
            # to get the projects with max profit
            heappush(heap, -projects[i][1])
            i += 1

        if heap:
            # add the profit to curr capital
            w -= heappop(heap)
    return w


k = 1
w = 2
p = [1, 2, 3]
c = [1, 1, 2]
print(findMaximizedCapital(k, w, p, c))
