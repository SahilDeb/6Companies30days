from collections import defaultdict
# DFS for finding dist from 0 and parent for each node


def dfs1(node, par, currDist, distance, parent, adjList):
    distance[node] = currDist
    parent[node] = par

    for adj in adjList[node]:
        if adj == par:
            continue

        dfs1(adj, node, currDist + 1, distance, parent, adjList)

# DFS for max path sum


def dfs2(node, par, adjList, amount):
    ans = float("-inf")

    for adj in adjList[node]:
        if adj != par:
            ret = dfs2(adj, node, adjList, amount)
            ans = max(ans, ret)

    # leaf node
    if ans == float("-inf"):
        return amount[node]

    return ans + amount[node]


def mostProfitablePath(edges, bob: int, amount) -> int:
    n = len(amount)
    adjList = defaultdict(list)

    for u, v in edges:
        adjList[u].append(v)
        adjList[v].append(u)

    # logic
    # find the distance and parent for each nodes starting from 0
    # which will help in bob's traversal and marking the amount to 0 or 1/2 based on distance from alice
    # finally find max sum path from node 0

    # step 1 -> Fill distance and parent starting from node 0
    # step 2 -> Do bob's traversal and modify the amount array accordingly
    # step 3 -> Get max sum path from node 0

    dist = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]

    dfs1(0, -1, 0, dist, parent, adjList)

    # Bob's traversal
    curr = bob
    currDistOfBob = 0
    while curr != 0:
        # distance[cur] here denotes How away Alice in right now from Bob
        if currDistOfBob < dist[curr]:
            amount[curr] = 0
        elif currDistOfBob == dist[curr]:
            amount[curr] //= 2

        curr = parent[curr]
        currDistOfBob += 1

    # find maximum sum path from 0
    return dfs2(0, -1, adjList, amount)
