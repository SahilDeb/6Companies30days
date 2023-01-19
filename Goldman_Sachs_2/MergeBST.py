def inorder(self, node, res):
    if node is None:
        return

    self.inorder(node.left, res)
    res.append(node.val)
    self.inorder(node.right, res)


def getAllElements(self, root1, root2):
    arr1 = []
    arr2 = []
    self.inorder(root1, arr1)
    self.inorder(root2, arr2)

    m, n = len(arr1), len(arr2)
    i, j = 0, 0

    res = []
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    if i < m:
        res += arr1[i:]

    if j < n:
        res += arr2[j:]

    return res
