#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        visited = [False] * length
        res = []
        def dfs(path, nums, visited, res):
            if len(path) == length:
                res.append(path.copy())
                return
            for i in range(length):
                if not visited[i]:
                    path.append(nums[i])
                else:
                    continue
                visited[i] = True
                dfs(path, nums, visited, res)
                path.pop()
                visited[i] = False
        dfs([], nums, visited, res)
        return res
# @lc code=end

