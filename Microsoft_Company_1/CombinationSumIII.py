# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.


def combos(n, startNum, nums, k, res):
    if k == 0:
        if n == 0:
            res.append(list(nums))
        return

    for num in range(startNum, 0, -1):
        nums.append(num)
        combos(n-num, num-1, nums, k-1, res)
        nums.pop()


def combinationSum3(k: int, n: int):
    maxSum = (k * (k+1))//2

    if n < maxSum:
        return []

    res = []
    combos(n, min(n, 9), [], k, res)
    return res


n1 = 7
k1 = 3

n2 = 9
k2 = 3

n3 = 4
k3 = 1

print(combinationSum3(k1, n1))
