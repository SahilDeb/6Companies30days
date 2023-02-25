def merge(left, right):
    res = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res


def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = int(len(nums)/2)
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)


def sortArray(nums):
    mergeSort(nums)
    return nums


a = [2, 4, 1, 5, 2]
print(sortArray(a))
