#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(root):
            if root is None:
                return 0
            else:
                return  1+ max(helper(root.left), helper(root.right))
        return helper(root)
# @lc code=end

