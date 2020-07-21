#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front, back, res, x, s = [1], [1],[], 1, 1 
        length = len(nums)
        # 下三角
        for i in range(length-1):
            x *= nums[i]
            front.append(x)
        for j in range(length-1, 0, -1):
            s *= nums[j]
            back.insert(0, s)
        for i, j in zip(front, back):
            res.append(i*j)
        return res
# @lc code=end

