#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] 最低票价
#

from typing import List

# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 从前往后
        # dp = [0 for _ in range(days[-1]+1)]
        # idx, dur = 0, [1, 7, 30]
        # for i in range(1, len(dp)):
        #     # 如果该天不在计划出行的日期内
        #     if i != days[idx]:
        #         dp[i] = dp[i-1]
        #     else:
        #         dp[i] = min(dp[max(0, i-d)]+c for c, d in zip(costs, dur))
        #         idx += 1
        # return dp[-1]

        # 从后往前，递归
        day_set = set(days)
        dur = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in day_set: 
                return min(dp(i+d)+c for c, d in zip(costs, dur))
            else:
                return dp(i+1)

        return dp(1)


# @lc code=end

