def rob(root) -> int:
    """
    Input: [3,4,5,1,3,null,1]
    input tree               dp tree:
        3                   [3+3+1,4+5]
        / \                 /        \
        4   5             [4,3]      [5,1]
        / \   \          /     \          \
        1   2   1   [1,0]    [2,0]       [1,0]
                    / \       /  \       /  \
                [0,0] [0,0] [0,0] [0,0] [0,0] [0,0]
    """
    # returns (now, later)
    # now returns max total if curr node is robbed
    # later returns max total if curr node is not robbed
    def dfsRob(node):
        if not node:
            return (0, 0)

        left, right = dfsRob(node.left), dfsRob(node.right)

        # add the curr node + not robbed val of left and right
        robNow = node.val + left[1] + right[1]
        # add the max value received from left and right
        robLater = max(left) + max(right)
        return (robNow, robLater)

    return max(dfsRob(root))
