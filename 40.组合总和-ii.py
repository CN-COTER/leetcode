#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        length = len(candidates)
        res = []

        def dfs(candidates, target, path, start):
            if sum(path) == target:
                # if path[:] not in res:
                #     res.append(path[:])
                res.append(path[:])
                return

            for i in range(start,length):
                if sum(path) > target:
                    break
                # 同一层出现相同的数的时候直接跳出过，防止出现相同情况
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(candidates, target, path, i+1)
                path.pop()
        dfs(candidates, target, [], 0)
        return res
# @lc code=end

