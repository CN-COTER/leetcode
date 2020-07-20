#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        0: [0: zero）
        1: [zero: i)
        2: [i, two)
        '''
        i, zero = 0, 0
        two = len(nums)
        if two < 2:
            return
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        while i < two:
            if nums[i] == 0:
                swap(i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                swap(two, i)
            print()
        return nums
# @lc code=end

