from typing import List

# 每一个硬币堆取硬币都是独立的操作，所以求所有取硬币的次数求和即可
class Solution:
    def minCount(self, coins: List[int]) -> int:
        return (sum([heap//2 if heap%2 == 0 else heap//2 + 1 for heap in coins]))