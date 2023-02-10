def findUnsortedSubarray(nums) -> int:
    n = len(nums)
    start = 0
    end = n-1

    while start < n-1:
        if nums[start] > nums[start + 1]:
            break
        start += 1

    while end > 0:
        if nums[end] < nums[end - 1]:
            break
        end -= 1

    if start >= end:
        return 0

    minVal = min(nums[start:end+1])
    maxVal = max(nums[start:end+1])

    while start > 0 and nums[start-1] > minVal:
        start -= 1
        minVal = min(minVal, nums[start])

    while end < n-1 and nums[end+1] < maxVal:
        end += 1
        maxVal = max(maxVal, nums[end])

    return end - start + 1


a = [2, 4, 3, 1, 8, 19, 12, 15, 13]
print(findUnsortedSubarray(a))
