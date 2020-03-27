#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#
from typing import List
# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from fractions import gcd
        from functools import reduce
        val = Counter(deck).values()
        return reduce(gcd, val) >= 2
# @lc code=end

