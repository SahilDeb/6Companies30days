def canPartitionKSubsets(nums, k: int) -> bool:
    n = len(nums)
    targetSum, r = divmod(sum(nums), k)
    if r != 0:
        return False

    nums.sort(reverse=True)
    partitions = [0] * k

    def walk(i):
        if i == n:
            # check if the value in all partitions is same
            return len(set(partitions)) == 1

        for j in range(k):
            partitions[j] += nums[i]
            if partitions[j] <= targetSum and walk(i+1):
                return True

            # backtrack
            partitions[j] -= nums[i]
            # if value of any partition becomes 0
            # indicates no value could fit in this partition
            if partitions[j] == 0:
                break
        return False

    return walk(0)


a = [3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2]
k = 10
print(canPartitionKSubsets(a, k))
