#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return int((sum(set(nums))*3 - sum(nums)) / 2)
        hash_arr = {}
        for n in nums:
            hash_arr[n] = hash_arr.get(n, 0) + 1
        for k, v in hash_arr.items():
            if v == 1:
                return k
# @lc code=end

