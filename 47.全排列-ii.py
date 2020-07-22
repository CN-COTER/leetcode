#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        visited = [False] * length
        res = []
        def dfs(nums, path, visited):
            if len(path) == length:
                # if path not in res:
                res.append(path[:])
                return

            for i in range(length):
                if visited[i] == True:
                    continue
                # 这里的剪枝采用先剪枝，即还没访问就剪枝， 如果使用visited
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs(nums, path, visited)
                path.pop()
                visited[i] = False

        dfs(nums, [], visited)
        return res
# @lc code=end

