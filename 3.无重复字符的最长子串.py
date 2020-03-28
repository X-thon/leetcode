#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        max_len, left, right = 0, 0, 0

        for i, c in enumerate(s):
            if c not in s[left:right]:
                right += 1 # 右指针移动一位
            else:
                left += s[left:right].index(c) + 1
                right += 1
            max_len = max(max_len, right - left)
        return max_len

# @lc code=end

