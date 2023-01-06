def largestDivisibleSubset(nums):
    n = len(nums)
    # Sorting the array to make sure the divisiblity condition holds between all pairs
    # say [a, b, c] => If b%a == 0 and c%b == 0 THEN, c%a == 0
    # So just need to check divisibility with prev element
    # and at the number accordingly
    nums.sort()
    # example - nums = [4,5,8,12,16,20].
    # res[0] = [4], the biggest divisible subset has size 1.
    # res[1] = [5], because 5 % 4 != 0.
    # res[2] = [4,8], because 8 % 4 = 0.
    # res[3] = [4,12], because 12 % 4 = 0.
    # res[4] = [4,8,16], because 16 % 8 = 0 and 16 % 4 = 0 and we choose 8, because it has longer set.
    # res[5] = [4,20] (or [5,20] in fact, but it does not matter). We take [4,20], because it has the biggest length and when we see 5, we do not update it.
    # Finally, answer is [4,8,16].
    res = [[num] for num in nums]
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(res[i]) < len(res[j]) + 1:
                res[i] = res[j] + [nums[i]]

    print(res)
    return max(res, key=len)


n1 = [3, 4, 16, 8]
n2 = [1, 2, 4, 8]
n3 = [3, 2, 6, 4, 8, 9]
n4 = [4, 5, 8, 12, 16, 20]
print(largestDivisibleSubset(n4))
