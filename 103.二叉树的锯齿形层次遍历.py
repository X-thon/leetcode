#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right: return [[root.val]]
        s1, s2, res = [], [], []
        s1.append(root)
        sign = -1 # -1表示下次从右往左遍历
        def addNode(s: List, sign: int):
            s_re, tmp = [], []
            if sign == -1: 
                while len(s) != 0:
                    node = s.pop()
                    tmp.append(node.val)
                    if node.right: s_re.append(node.right)
                    if node.left: s_re.append(node.left)
            elif sign == 1:
                while len(s) != 0:
                    node = s.pop()
                    tmp.append(node.val)
                    if node.left: s_re.append(node.left)
                    if node.right: s_re.append(node.right)
            tmp = tmp[::-1]
            sign = -sign
            return s_re, tmp, sign
        while len(s1) !=0 or len(s2) != 0:
            if len(s1) != 0:
                s2, tmp, sign = addNode(s1, sign)
                res.append(tmp)
            if len(s2) != 0:
                s1, tmp, sign = addNode(s2, sign)
                res.append(tmp)
        return res

# @lc code=end

