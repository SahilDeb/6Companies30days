def maxMatrixSum(matrix) -> int:
    n = len(matrix)
    countNegs = 0
    for i in range(n):
        countNegs += sum(1 for i in matrix[i] if i < 0)

    totalSum = 0
    # let x = total number of negetive values in matrix
    # if x is Even, all negetive values can be made positive.
    # So total sum = sum of abs value of all cells
    if countNegs % 2 == 0:
        for i in range(n):
            totalSum += sum(abs(i) for i in matrix[i])
    else:
        # If x is odd
        # In this case, there will be one -ve value left
        # Now, to maximize the sum, the value having a -ve sign needs to be minimized.
        # To do this, move the -ve sign to the cell having minimum absolute value, say minVal.
        # Therefore, the maximum sum possible is sum of the absolute values of all cells – 2*minVal.
        # 2 * minVal -> as the abs total sum already includes that value once
        minVal = float("inf")
        for i in range(n):
            for j in range(n):
                minVal = min(minVal, abs(matrix[i][j]))
                totalSum += abs(matrix[i][j])

        totalSum -= 2 * minVal

    return totalSum


m = [[-3, 0, 0], [0, 0, 0], [0, 3, 2]]
print(maxMatrixSum(m))
