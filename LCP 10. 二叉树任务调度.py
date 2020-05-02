# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        # 参考"失火的夏天"题解
        def execTime(node: TreeNode, n: int) -> List:
            if not node:
                return [0, 0]
            left_time = execTime(node.left, n)
            right_time = execTime(node.right, n)
            sum_time = left_time[1] + right_time[1]
            min_time = max(left_time[0], right_time[0], sum_time/n) + node.val
            return [min_time, sum_time+node.val]
        res = execTime(root, 2)
        return res[0]