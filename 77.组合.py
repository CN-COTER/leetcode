#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        candidate = [i for i in range(1, n+1, 1)]
        if n == k:
            return [candidate]
        def dfs(tmp, index):
            # 体现剪枝思想
            if n-index < k-len(tmp):
                return
            if len(tmp) == k:
                self.res.append(tmp[:])
                return
            for i in range(index, n):
                tmp.append(candidate[i])
                dfs(tmp, i+1)
                #体现回溯思想，
                tmp.pop()
        dfs([], 0)
        return self.res
# @lc code=end

