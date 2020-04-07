from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> str:
        # 解法1，使用遍历，对每个字符使用.count()，
        # 但实际上每一次.count()都扫描了一次字符串，会非常慢
        # for i in s:
        #     if s.count(i) == 1: return i
        # return " "

        # 解法2，使用哈希表辅助，最坏情况下只需要扫描一遍字符串
        d = Counter(s)
        for i in s:
            if d[i] == 1: return i
        return " "