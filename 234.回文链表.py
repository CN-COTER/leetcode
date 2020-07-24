#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 直接输出看反转之后一样与否
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         p = head
#         tmp_list = []
#         while p:
#             tmp_list.append(p.val)
#             p = p.next
#         if tmp_list == tmp_list[::-1]:
#             return True
#         else:
#             return False

# 快慢指针+栈
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        stack = []
        while fast and fast.next:
            stack.append(slow)
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        while stack:
            tmp = stack.pop()
            if tmp.val == slow.val:
                slow = slow.next
            else:
                return False
        return True
            
        
# @lc code=end

