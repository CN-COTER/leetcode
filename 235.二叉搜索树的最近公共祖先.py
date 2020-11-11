#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
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
        if p.val > q.val:
            p, q = q, p
        def helper(root, p, q):
            if not root or root == p or root == q:
                return root
            if p.val < root.val < q.val:
                return root
            elif root.val < p.val:
                return helper(root.right, p, q)
            else :
                return helper(root.left, p, q)
        return helper(root, p, q)
# @lc code=end

