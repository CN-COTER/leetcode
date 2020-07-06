#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 中序遍历后得到的是有序的数组即为二叉搜索树
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        a = []
        def helper(root):
            if root is None:
                return
            if root.left:
                helper(root.left)
            a.append(root.val)
            if root.right:
                helper(root.right)
        helper(root)
        b = sorted(a)
        if len(set(b)) != len(a):
            return False
        print(a)
        print(a)
        if a == b:
            return True
        else:
            return False
# @lc code=end

