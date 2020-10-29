#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def helper(preorder, inorder):
            if not preorder or not inorder:
                return None
            root_val = preorder[0]
            root = TreeNode(root_val)
            root_index_in_inorder = inorder.index(root_val)
            root.left = helper(preorder[1: 1+root_index_in_inorder], inorder[:root_index_in_inorder])
            root.right = helper(preorder[1+root_index_in_inorder:], inorder[1+root_index_in_inorder:])
            return root
        root = helper(preorder, inorder)
        return root
# @lc code=end

