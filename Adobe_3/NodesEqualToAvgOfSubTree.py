def findAverage(node, res):
    if not node:
        return 0, 0

    left, countLeft = findAverage(node.left, res)
    right, countRight = findAverage(node.right, res)

    totalVal = node.val + left + right
    totalNodes = 1 + countLeft + countRight
    if totalVal//totalNodes == node.val:
        res[0] += 1

    return totalVal, totalNodes


def averageOfSubtree(root) -> int:
    res = [0]
    findAverage(root, res)

    return res[0]
