#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_length = 0
        #直径长度即某节点的最大左右深度和
        def helper(root):
            if not root:
                return 0
            else:
                a = helper(root.left)
                b = helper(root.right)
                if a + b > self.max_length:
                    self.max_length = a + b
                # print(root.val, max(a+1, b+1))
                return max(a+1, b+1)
        helper(root)
        return self.max_length
        
# @lc code=end

