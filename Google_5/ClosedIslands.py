def closedIsland(grid) -> int:
    # how many islands we can find which does not touch the boundary
    m, n = len(grid), len(grid[0])

    def dfs(x, y, flag=False):
        grid[x][y] = 1
        flag = flag or x == 0 or x == m-1 or y == 0 or y == n-1

        if x > 0 and grid[x-1][y] == 0:
            flag = dfs(x-1, y, flag)
        if x < m-1 and grid[x+1][y] == 0:
            flag = dfs(x+1, y, flag)
        if y > 0 and grid[x][y-1] == 0:
            flag = dfs(x, y-1, flag)
        if y < n-1 and grid[x][y+1] == 0:
            flag = dfs(x, y+1, flag)
        return flag

    # mark all boundary connected lands to water
    # for i in range(m):
    #     for j in range(n):
    #         if (i == 0 or i == m-1 or j == 0 or j == n-1) and grid[i][j] == 0:
    #             dfs(i, j, 1)

    # count the islands
    islandCount = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and not dfs(i, j):
                islandCount += 1

    return islandCount


g = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [
    0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
print(closedIsland(g))
