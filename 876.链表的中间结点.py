#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # double traverse
    # def middleNode(self, head: ListNode) -> ListNode:
    #     p, middleNode, length = head, head, 0
    #     while p.next:
    #         length += 1
    #         p = p.next
    #     length += 1
    #     for i in range(length//2):
    #         middleNode = middleNode.next
    #     return middleNode

    # fast and slow pointer
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
# @lc code=end

