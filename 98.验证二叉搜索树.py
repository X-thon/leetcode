#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, pre_val = [], float('-inf')
        while root or len(stack):
            while root:
                stack.append(root)
                root = root.left
            # 如果root.left为空
            root = stack.pop()
            if root.val <= pre_val:
                return False
            pre_val = root.val
            root = root.right
        return True
# @lc code=end

