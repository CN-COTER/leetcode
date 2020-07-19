#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs_sum(root, sumation):
            if not root:
                return False
            if not root.left and not root.right:
                if root.val == sumation:
                    return True
            # print('---------')
            return dfs_sum(root.left, sumation-root.val) or  dfs_sum(root.right, sumation-root.val)
        return dfs_sum(root, sum)
# @lc code=end

