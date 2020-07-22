#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        res = []
        def dfs(candidates, target, path, begin):
            if sum(path) == target:
                res.append(path[:]) 
                return

            for i in range(begin, length):
                if sum(path) > target:
                    break
                    
                path.append(candidates[i])
                dfs(candidates, target, path, i)
                path.pop()
        dfs(candidates, target, [], 0)
        return res
# @lc code=end

