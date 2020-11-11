#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归法（前序遍历，但是做不到原地修改只能先生成数组，最后再重新生成数组）
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        pre_arr = []
        def first_search(root, pre_arr):
            if not root:
                return
            else:
                pre_arr.append(root)
            first_search(root.left, pre_arr) 
            first_search(root.right, pre_arr)
        first_search(root, pre_arr)
        head = pre_arr.pop(0)
        while pre_arr:
            head.left = None
            tmp = pre_arr.pop(0)
            head.right = tmp
            head = tmp
# 普通遍历
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         while root:
#             if root.left:
#                 sub_left = root.left
#                 while sub_left.right:
#                     sub_left = sub_left.right
#                 # 将root的右子树拼接到其左子树的最右节点后面
#                 sub_left.right = root.right
#                 # 将左子树反转到右子树下
#                 root.right = root.left
#                 # 将左子树置空
#                 root.left = None
#             root = root.right
        
# @lc code=end

