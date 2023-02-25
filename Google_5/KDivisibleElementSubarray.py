def countDistinct(nums, k: int, p: int) -> int:
    n = len(nums)
    # set to store unique substrings
    subarrays = set()
    for start in range(n):
        cnt = 0
        tmp = ''
        for i in range(start, n):
            # keep track of elements divisible by k
            if nums[i] % p == 0:
                cnt += 1

            tmp += str(nums[i]) + ","
            # if cnt crosses k, break
            if cnt > k:
                break
            # keep adding curr substring to result set
            subarrays.add(tmp)

    # print(subarrays)
    return len(subarrays)


a = [1, 2, 3, 2, 1]
k = 4
p = 2
print(countDistinct(a, k, p))
