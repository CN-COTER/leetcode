#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if not root or root == p or root == q:
                return root
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            if not left and not right:
                return None
            elif not left and right:
                return right
            elif not right and left:
                return left
            else:
                return root
        return helper(root, p, q)  
# @lc code=end

