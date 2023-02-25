def matrixBlockSum(mat, k: int):
    m, n = len(mat), len(mat[0])
    prefixMat = [[0 for _ in range(n)] for _ in range(m)]

    # step 1
    for i in range(m):
        currSum = 0
        for j in range(n):
            currSum += mat[i][j]
            prefixMat[i][j] = currSum

    # step 2
    for j in range(n):
        currSum = 0
        for i in range(m):
            currSum += prefixMat[i][j]
            prefixMat[i][j] = currSum

    # Calculate
    res = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r = [max(0, i-k), min(m-1, i+k)]
            c = [max(0, j-k), min(n-1, j+k)]

            value = prefixMat[r[1]][c[1]]

            # if row lower bound >= 0, remove the prefix val of row[0] - 1
            if r[0] - 1 >= 0:
                value -= prefixMat[r[0] - 1][c[1]]
            # if col lower bound >= 0, remove the prefix val of col[0] - 1
            if c[0] - 1 >= 0:
                value -= prefixMat[r[1]][c[0] - 1]

            # as corner value maybe removed twice, so adding it back
            if r[0] - 1 >= 0 and c[0] - 1 >= 0:
                value += prefixMat[r[0]-1][c[0]-1]

            res[i][j] = value
    return res


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
print(matrixBlockSum(m, k))
