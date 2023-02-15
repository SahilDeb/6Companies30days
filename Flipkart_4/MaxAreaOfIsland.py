from collections import defaultdict


class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.maxSize = 1

    def findParent(self, node):
        if self.parent[node] == node:
            return node

        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, a, b):
        pA = self.findParent(a)
        pB = self.findParent(b)

        if pA == pB:
            return

        if self.size[pA] > self.size[pB]:
            self.size[pA] += self.size[pB]
            self.parent[pB] = pA
            self.maxSize = max(self.maxSize, self.size[pA])
        else:
            self.size[pB] += self.size[pA]
            self.parent[pA] = pB
            self.maxSize = max(self.maxSize, self.size[pB])


def maxAreaOfIsland(grid) -> int:
    m, n = len(grid), len(grid[0])

    # using Disjoint set
    # nodeDict = defaultdict(int)
    # ds = Disjoint(m*n)

    # def dfs(x, y):
    #     if grid[x][y]:
    #         grid[x][y] = 0

    #         direc = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    #         for d in direc:
    #             nX = x + d[0]
    #             nY = y + d[1]

    #             if nX >= 0 and nX < m and nY >= 0 and nY < n and grid[nX][nY]:
    #                 curr = nodeDict[(x, y)]
    #                 nxt = nodeDict[(nX, nY)]
    #                 ds.unionBySize(curr, nxt)
    #                 dfs(nX, nY)

    # nodeNum = 0
    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j] == 1:
    #             nodeDict[(i, j)] = nodeNum
    #             nodeNum += 1

    # if nodeNum == 0:
    #     return 0

    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j]:
    #             dfs(i, j)

    # return ds.maxSize

    def dfs(x, y):
        currArea = 0
        if grid[x][y] == 1:
            grid[x][y] = 0
            if x > 0 and grid[x-1][y] == 1:
                currArea += dfs(x-1, y)
            if y > 0 and grid[x][y-1] == 1:
                currArea += dfs(x, y-1)
            if x < m-1 and grid[x+1][y] == 1:
                currArea += dfs(x+1, y)
            if y < n-1 and grid[x][y+1] == 1:
                currArea += dfs(x, y+1)
            return 1 + currArea
        return 0

    maxArea = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                maxArea = max(maxArea, dfs(i, j))

    return maxArea


g = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(maxAreaOfIsland(g))
