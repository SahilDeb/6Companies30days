# We focus on the middle element of the triplet.
# For an element a, how many triplets are centered at a

# This problem equals to:
# How many elements on a's left in both A and B
# How many elements on a's right in both A and B

# Therefore, for each element a, we could count how many elements on a's left in both two arrays A and B.
# Similarly, count how many elements on a's right in both two arrays A and B (and get their product).

from sortedcontainers import SortedList
from bisect import bisect_left


def goodTriplets(nums1, nums2) -> int:
    # pos[i]: idx for the number i present in nums2
    pos = [0] * len(nums1)
    for idx, b in enumerate(nums2):
        pos[b] = idx
    # print(pos)

    # pre_a[i]: number of elements on a[i]'s left in both nums1 and nums2
    # pos_in_b: sorted indexes (in nums2) of all the visited elements in nums1
    pre_a = [0]
    pos_in_b = SortedList([pos[nums1[0]]])

    for a in nums1[1:]:
        pos_in_b.add(pos[a])
        # idx: among all the elements before a in nums1, there is idx elements before a in nums2
        idx = pos_in_b.bisect_left(pos[a])
        # print("For val", a, "of nums1, it's position in b is",
        #   pos[a], "which has", idx, "element(s) before it in both arrays")
        pre_a.append(idx)
    # print(pre_a)

    # Build suf_a[i]: number of elements on a[i]'s right in both nums1 and nums2
    suf_a = [0]
    pos_in_b = SortedList([pos[nums1[-1]]])
    for a in reversed(nums1[:len(nums1) - 1]):
        # idx: among all the elements after a in nums1, there is idx elements after a in nums2
        idx = pos_in_b.bisect_right(pos[a])
        # print("For val", a, "of nums1, it's position in b is",
        #   pos[a], "which has", idx, "element(s) after it in both arrays")
        suf_a.append(len(pos_in_b) - idx)
        pos_in_b.add(pos[a])
    suf_a.reverse()

    # print(suf_a)

    tripletCount = 0
    for x, y in zip(pre_a, suf_a):
        tripletCount += x * y
    return tripletCount


n1 = [4, 0, 1, 3, 2]
n2 = [4, 1, 0, 2, 3]
print(goodTriplets(n1, n2))
