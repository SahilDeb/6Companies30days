from heapq import heappop, heappush


class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def findParent(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        pA = self.findParent(a)
        pB = self.findParent(b)

        if pA == pB:
            return

        if self.rank[pA] < self.rank[pB]:
            self.parent[pA] = pB
        elif self.rank[pA] > self.rank[pB]:
            self.parent[pB] = pA
        else:
            self.parent[pB] = pA
            self.rank[pA] += 1


# TC = O(n^2)
def swimInWater(grid) -> int:
    n = len(grid)
    nodes = {}

    for i in range(n):
        for j in range(n):
            nodes[grid[i][j]] = (i, j)

    ds = Disjoint(n*n)
    # visited nodes
    visited = set()
    direc = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    for i in range(n*n):
        x, y = nodes[i]
        visited.add((x, y))

        for dx, dy in direc:
            nX = x+dx
            nY = y+dy
            if 0 <= nX < n and 0 <= nY < n and (nX, nY) in visited:
                # union new node and curr node
                # x * n to reach the correct row and +y to reach the correct col
                ds.union(nX*n + nY, x*n + y)

        # if the parent of both 0 and last node is same, return i
        # which is the max value required to reach n*n-1 node
        if ds.findParent(0) == ds.findParent((n*n) - 1):
            return i

    # DFS way - Easiest way
    # TC = (n^2 * log n)
    # n = len(grid)
    # heap = [(grid[0][0], 0, 0)]
    # visited = {(0, 0)}
    # direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # res = 0

    # for i in range(n*n):
    #     val, x, y = heappop(heap)
    #     res = max(res, val)

    #     if x == n-1 and y == n-1:
    #         return res

    #     for dx, dy in direc:
    #         nX = x + dx
    #         nY = y + dy
    #         if 0 <= nX < n and 0 <= nY < n and (nX, nY) not in visited:
    #             visited.add((nX, nY))
    #             heappush(heap, (grid[nX][nY], nX, nY))
    # return res


g = [[7, 34, 16, 12, 15, 0], [10, 26, 4, 30, 1, 20], [28, 27, 33, 35, 3, 8], [
    29, 9, 13, 14, 11, 32], [31, 21, 23, 24, 19, 18], [22, 6, 17, 5, 2, 25]]
print(swimInWater(g))
