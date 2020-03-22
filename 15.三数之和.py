#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, k = [], 0
        if len(nums) < 3 or not nums: return res # Judgement of special inputs speeds up execution
        nums.sort() # pre work
        for k in range(len(nums)-2):
            if nums[k] > 0: break # nums[k] <= nums[i] <= nums[j]
            if k > 0 and nums[k] == nums[k-1]: continue # skip the 'same'
            i, j = k+1, len(nums)-1
            while i < j: # double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                elif s > 0: 
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return res



# @lc code=end

