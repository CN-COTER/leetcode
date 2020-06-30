#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False 
        slow, fast = head, head
        while (not slow is None) and (not fast is None) and (not fast.next is None):
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
        
# @lc code=end

