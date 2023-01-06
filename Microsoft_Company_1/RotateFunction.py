def maxRotateFunction(nums) -> int:
    # from given pattern
    # derived the formula for F(k) as follows
    # F(k) = F(k-1) + SUM + N * arr[N - k]

    n = len(nums)
    S = sum(nums)

    prefixSum = 0
    for i, val in enumerate(nums):
        prefixSum += (i * val)

    maxVal = prefixSum
    for i in range(1, n):
        prefixSum = prefixSum + S - (n * nums[-i])
        maxVal = max(maxVal, prefixSum)

    return maxVal


n1 = [4, 3, 2, 6]
n2 = [100]

print(maxRotateFunction(n1))
