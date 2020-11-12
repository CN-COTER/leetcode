#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
# 方法 1
# 原始方法，复杂度较高。
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         res = []
#         for i in range(num+1):
#             a = bin(i)
#             tmp = 0
#             for i in a:
#                 if i == '1':
#                     tmp += 1
#             res.append(tmp)
#         return res

# 方法 2
# 使用 n &= n-1 用于消除二进制最低位上的一个1
# class Solution:
#     def countBits(self, num: int) -> List[int]:
        # res = []
        # for i in range(num+1):
        #     tmp = 0
        #     while i != 0:
        #         i  &= i-1
        #         tmp += 1
        #     res.append(tmp)
        # return res

# 方法 3
# 根据奇偶数规律+动态规划
# 偶数可以由之前的数（半数）左移一位得到， 奇数可以由之前的数左移一位加1得到
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         dp = [0] * (num+1)
#         if num == 0:
#             return [0]
#         if num == 1:
#             return [0, 1]
#         dp[0], dp[1] = 0, 1
#         for i in range(2, num+1):
#             if i % 2 == 0:
#                 dp[i] = dp[i//2]
#             else:
#                 dp[i] = dp[i//2] + 1
#         return dp

# 方法 4
# 方法2 结合 方法3 的动态规划
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        if num == 0:
            return [0]
        if num == 1:
            return [0 , 1]
        dp[0], dp[1] = 0, 1
        for i in range(2, num+1):
            dp[i] = dp[i&(i-1)]+1
        return dp
        
# @lc code=end

