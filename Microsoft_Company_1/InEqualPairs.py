from sortedcontainers import SortedList


def numberOfPairs(nums1, nums2, diff: int) -> int:
    n = len(nums1)

    sl = SortedList()
    pairsCount = 0

    for i in range(n):
        delta = nums1[i] - nums2[i]
        # find the rightmost index where this can be inserted
        idx = sl.bisect_right(delta + diff)
        pairsCount += idx
        sl.add(delta)

    return pairsCount


n1 = [3, 2, 5]
n2 = [2, 2, 1]
d1 = 1

print(numberOfPairs(n1, n2, d1))
