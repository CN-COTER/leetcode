#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        length = len(nums)
        sumation = sum(nums)
        if sumation < abs(S):
            return 0
        sums = sumation*2+1
        
        dp = [[0 for _ in range(sums)] for _ in range(length)]
        dp[0][sumation + nums[0]] = 1
        dp[0][sumation - nums[0]] += 1

        for i in range(1, length):
            for j in range(sums):
                l_j = dp[i-1][j-nums[i]] if 0 <= j - nums[i] < sums else 0
                r_j = dp[i-1][j+nums[i]] if 0 <= j + nums[i] < sums else 0
                dp[i][j] = l_j + r_j
        # print(dp)
        return dp[length-1][S+sumation]
# @lc code=end

