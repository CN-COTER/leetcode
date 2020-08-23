#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 用slow得到0元素索引，之后再交换此前的0元素和当前元素
        length = len(nums)
        slow = 0
        for i in range(length):
            if nums[i] != 0:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow += 1
        return

#利用索引位置变化为来处理
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         length = len(nums)
#         index = 0
#         for i in range(length):
#             if nums[i-index] == 0:
#                 nums.pop(i - index)
#                 index += 1
#                 nums.append(0)
#         return 
                
# @lc code=end

