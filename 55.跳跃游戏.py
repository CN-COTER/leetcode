#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#



# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_arrive = 0
        for i in range(len(nums)):
            if i + nums[i] > max_arrive and max_arrive >= i:
                max_arrive = i + nums[i]
            print(max_arrive)
        if max_arrive >= len(nums)-1:
            return True
        else:
            return False

# 暴力解法，超时
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True
#         flag_nums = [0] * len(nums)
#         flag_nums[0] = 1
#         for i in range(len(nums)):
#             for j in range(1, nums[i]+1):
#                 if i+j < len(nums):
#                     flag_nums[i+j] = 1
#             print(flag_nums)
        
#         if 0 in set(flag_nums):
#             return False
#         else:
#             return True


# 动态规划超时
# class Solution:x
        # dp = [False] * len(nums)
        # dp[0] = True
        # for i in range(len(nums)):
        #     # print(i)
        #     for j in range(0, i):
        #         # print('i : {0}'.format(i))
        #         # print('j : {0}'.format(j))
        #         if dp[j] and j+nums[j] >= i:
        #             dp[i] = True
        #             break
        # return dp[-1]
# @lc code=end

