from random import randrange


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        ans = self.nums[:]
        n = len(ans)
        for i in range(n - 1, 0, -1):
            j = randrange(0, i+1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans


c = ["Solution", "shuffle", "reset", "shuffle"]
n = [[[1, 2, 3]], [], [], []]
obj = Solution(n)
param_1 = obj.reset()
param_2 = obj.shuffle()
