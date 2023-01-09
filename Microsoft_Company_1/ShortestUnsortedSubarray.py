def findUnsortedSubarray(nums) -> int:
    n = len(nums)
    if n == 1:
        return 0

    i, j = 0, n-1
    while i < n-1 and nums[i] <= nums[i+1]:
        i += 1

    while j > 0 and nums[j] >= nums[j-1]:
        j -= 1

    # Sorted array
    if i > j:
        return 0

    # need to run another set of loop to find lower bound and upper bound
    # for example [1, 3, 7, 2, 5, 4, 6, 10]
    # after 1st round, i = 2, j = 5
    # but it's wrong as the values 3 and 6 will not be included in sort
    tmp = nums[i:j+1]
    tmpMin = min(tmp)
    tmpMax = max(tmp)

    # run a the loops in opposite direction to increase the bound
    while i > 0 and tmpMin < nums[i-1]:
        i -= 1

    while j < n-1 and tmpMax > nums[j+1]:
        j += 1

    return j - i + 1
