# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
            设链表长度为n，快指针先走k步，随后快慢指针一块走；
            当快指针指向None时，慢指针指向倒数第k个节点；
            即，快指针先走k步后，再走了n-k步到链表为末尾，慢指针也走了n-k步，即指向倒数第k个节点；
        """
        fast, slow = head, head
        while fast and k != 0:
            fast = fast.next
            k -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        return slow