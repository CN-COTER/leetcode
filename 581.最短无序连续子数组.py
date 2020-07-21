#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        new = sorted(nums)
        l, r = 0, 0
        for i in range(length):
            if nums[i] != new[i]:
                l = i
                break
        print(l)
        for j in range(length-1, -1, -1):
            if nums[j] != new[j]:
                r = j
                break
        print(r)
        if l >= r:
            return 0
        else:
            return r-l+1        
# @lc code=end

