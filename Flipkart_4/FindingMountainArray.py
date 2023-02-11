def findInMountainArray(target: int, mountain_arr: 'MountainArray') -> int:
    n = mountain_arr.length()
    if n < 3:
        return -1

    # find peak
    l, r = 0, n-1
    pIdx = -1
    while l <= r:
        mid = l + (r - l)//2
        curr = mountain_arr.get(mid)
        prev, nxt = float("-inf"), float("inf")
        if mid-1 >= 0:
            prev = mountain_arr.get(mid-1)

        if mid+1 < n:
            nxt = mountain_arr.get(mid+1)
        # print(mid, curr, prev, nxt)

        if curr > prev and curr > nxt:
            pIdx = mid
            if curr == target:
                return mid
            break
        elif curr > prev and curr < nxt:
            l = mid + 1
        elif curr < prev and curr > nxt:
            r = mid - 1

    print(pIdx)
    if pIdx == -1:
        return -1

    l, r = 0, pIdx-1
    while l <= r:
        mid = l + (r - l)//2
        curr = mountain_arr.get(mid)

        if curr == target:
            return mid
        elif curr < target:
            l = mid + 1
        else:
            r = mid - 1

    l, r = pIdx+1, n-1
    while l <= r:
        mid = l + (r - l)//2
        curr = mountain_arr.get(mid)

        if curr == target:
            return mid
        elif curr > target:
            l = mid + 1
        else:
            r = mid - 1

    return -1
