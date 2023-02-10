def findGap(n, p, q):
    # by observation we see that
    # the gap between 2 consecutive integers increases linearly
    # p     q       gap
    # 2     3       1
    # 20    30      11
    # 200   300     111 and so on
    gap = 0
    while p <= n:
        minDiff = min(n+1, q) - p
        gap += max(0, minDiff)
        p *= 10
        q *= 10
    return gap


# O((log n)^2)
# log n -> number of digits in n
# log n -> incrementing the range by 10 every time
def findKthNumber(n: int, k: int) -> int:
    # we can visualize this as a n-ary tree where for each number there is 10 children
    # 0 -> 1, 2, ..., 9
    # 1 -> 10, 11, ..., 19
    # 10 -> 100, 101, ..., 109
    # so need to calculate how many elements to move to reach kth element

    ans = 1
    # k-1 th element will be the answer
    k -= 1
    while k > 0:
        gap = findGap(n, ans, ans+1)
        if gap <= k:
            # move to next level of tree
            ans += 1
            k -= gap
        else:
            # move row wise for each number
            # as there is 10 numbers for each
            ans *= 10
            k -= 1
    return ans


n = 12121
k = 212
print(findKthNumber(n, k))
