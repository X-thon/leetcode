#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

from typing import List

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 使用贪心算法
        n = len(nums)
        # max_position记录下一跳可以跳到的最远位置
        # cur_step_border记录当前跳数内的可选范围
        max_position, cur_step_border, step = 0, 0, 0
        for i in range(n - 1):
            if max_position >= i:
                max_position = max(max_position, i + nums[i])
                if i == cur_step_border:
                    cur_step_border = max_position
                    step += 1     
        return step
# @lc code=end

