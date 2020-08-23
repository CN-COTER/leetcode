#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        tmp = 0
        for i in range(row):
            tmp += grid[i][0]
            dp[i][0] = tmp
        tmp = 0
        for j in range(col):
            tmp += grid[0][j]
            dp[0][j] = tmp
        print(dp)

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]

# @lc code=end

