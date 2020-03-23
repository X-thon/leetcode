from typing import List

class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums: return 0
        elif len(nums) == 1: return nums[0] # special input-value judge
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            a, b = dp[i-2]+nums[i], dp[i-1]
            dp[i] = max(a, b)
        return dp[-1]