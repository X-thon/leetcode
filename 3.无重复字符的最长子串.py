#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用双指针方式模拟滑动窗口
        if not s: return 0
        max_len, left, right = 0, 0, 0

        for c in s:
            if c not in s[left:right]: # 如果字符不在[left:right]这个区间内，即c不是重复字符
                right += 1 # 右指针移动一位
            else: # 如果c字符是重复字符
                # .index(c)返回c在数组中第一次出现的位置，即与c产生重复的字符的位置; 
                # +1 表示将指针往前挪动一步，“避开”重复字符
                left += s[left:right].index(c) + 1 
                right += 1 # 右指针往前走一步，指向当前这个字符c(跳过旧的，指向新的)
            max_len = max(max_len, right - left) # 更新字串的长度: 比较看是之前存储的长度大，还是现在这个滑动窗口的长度大
        return max_len

# @lc code=end

