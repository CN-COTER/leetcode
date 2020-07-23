#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
# dfs超时
# class Solution:
#     def numSquares(self, n: int) -> int:

#         import math
#         ce = math.ceil(math.sqrt(n))
#         if ce == math.sqrt(n):
#             return 1
#         candidates = [i**2 for i in range(1, ce+1)]
#         # print(candidates)
#         length = len(candidates)
#         depth = float('inf')
#         res = []

#         def dfs(n, tmp_path, candidates, depth):
#             if sum(tmp_path) == n:
#                 res.append(len(tmp_path))

#             for i in range(length):
#                 if sum(tmp_path) > n:
#                     break
#                 tmp_path.append(candidates[i])
#                 dfs(n, tmp_path, candidates, depth)
#                 tmp_path.pop()

#         dfs(n, [], candidates, depth)
#         return min(res)

# dp
class Solution:
    def numSquares(self, n: int) -> int:
        import math
        if math.ceil(math.sqrt(n)) == math.sqrt(n):
            return 1
        ce = math.ceil(math.sqrt(n))
        candidates = [i**2 for i in range(1, ce+1)]
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            # print(dp)
            tmp = []
            for j in candidates:
                if i - j >= 0:
                    tmp.append(dp[i-j])
            dp[i] = min(tmp)+1
        return dp[-1]
                
# @lc code=end

