#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
# 超时
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         length = len(nums)
#         res = 0
#         for i in range(length):
#             tmp_sum = 0
#             for j in range(i, -1, -1):
#                 tmp_sum += nums[j]
#                 if tmp_sum == k:
#                     res += 1
#         return res


# 超时
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         length = len(nums)
#         res = 0
#         tmp = [nums[0]]
#         for i in range(length):
#             if nums[i] == k:
#                 res += 1
#             if i == 0:
#                 continue
#             for j in range(i):
#                 tmp[j] += nums[i]
#                 if tmp[j] == k:
#                     res += 1
#             tmp.append(nums[i])
#         # print(tmp)
#         return res

# 前缀编码，用dict保留之前保存的和，利用当前的和减之前的和得到差为K，则res+=1
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_dict = {0:1}
        res = 0
        sumation = 0
        for i in nums:
            sumation += i
            num = hash_dict.get(sumation - k, 0)
            res += num
            hash_dict[sumation] = hash_dict.get(sumation, 0) + 1
        return res
# @lc code=end

