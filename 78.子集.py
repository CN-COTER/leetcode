#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        def dfs(meta_res, index):
            result.append(meta_res)
            # print(meta_res)
            for i in range(index, length):
                dfs(meta_res+[nums[i]], i+1)
                
        dfs([], 0)
        return result
# @lc code=end

