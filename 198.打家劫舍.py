#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length < 3:
            return max(nums)
        dp = [0] * length
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

# @lc code=end

