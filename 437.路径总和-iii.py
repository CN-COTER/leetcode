#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        from collections import defaultdict
        hash_sum = defaultdict(int)
        hash_sum[0] = 1
        def dfs(root, cur_sum):
            if not root:
                return 0
            cur_sum += root.val
            n = hash_sum[cur_sum - sum]
            hash_sum[cur_sum] += 1
            ln = dfs(root.left, cur_sum)
            rn = dfs(root.right, cur_sum)
            hash_sum[cur_sum] -= 1
            return ln+rn+n
        return dfs(root, 0)
        
# @lc code=end

