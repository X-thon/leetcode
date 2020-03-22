#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(filter(str.isalnum, s))
        # start = 0
        # for i in range(len(s)-1, 0, -1):
        #     if s[i] != s[start]:
        #         return False
        #     start += 1
        # return True
        if s != s[::-1]:
            return False
        return True
# @lc code=end

