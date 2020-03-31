# 实际上为爬楼梯的换皮问题
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return a % 1000000007 # 题目要求答案需要取模