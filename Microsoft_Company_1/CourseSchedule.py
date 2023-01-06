from collections import deque


def canFinish(numCourses: int, prerequisites) -> bool:

    adjList = [[] for _ in range(numCourses)]
    # calculate indegrees for each node
    indegrees = [0 for _ in range(numCourses)]

    for u, v in prerequisites:
        adjList[v].append(u)
        indegrees[u] += 1

    q = deque()
    nodeChecked = 0
    # push all nodes with indegrees 0 to the Q
    # those nodes doesn't have any dependency
    for i in range(numCourses):
        if indegrees[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        nodeChecked += 1

        # simulate removal of node
        # thus the indegree for adj nodes will reduce
        for adj in adjList[node]:
            # reduce the indegree of adj
            indegrees[adj] -= 1
            if indegrees[adj] == 0:
                q.append(adj)

    # check if all the nodes are covered
    return nodeChecked == numCourses


n1 = 3
p1 = [[0, 1], [0, 2], [1, 2]]

n2 = 4
p2 = [[0, 1], [3, 2], [0, 2]]

n3 = 2
p3 = [[1, 0], [0, 1]]

print(canFinish(n2, p2))
