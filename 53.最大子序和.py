#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

from typing import List

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 普通dp方法
        # size = len(nums)
        # if not size: return 0
        # dp = [0 for _ in range(size)]

        # dp[0] = nums[0]
        # for i in range(1, size):
        #     dp[i] = max(nums[i], dp[i-1]+nums[i])
        
        # return max(dp)

        # 压缩空间的dp方法
        size = len(nums)
        if not size: return 0
        pre = nums[0]
        res = pre
        for i in range(1, size):
            pre = max(pre+nums[i], nums[i])
            res = max(res, pre)
        return res

# @lc code=end

