#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums)-1
        first, last = -1, -1
        #先求左边界
        
        # 还是记得加 ‘=’
        while left <= right:
            
            mid = (left+right) // 2
            # print(left, right, mid)

            # mid等于目标值且（mid位于最左侧或mid的左边都不是目标值）
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                first = mid
                break 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        # print(first)
        
        left, right = first, len(nums)-1

        # 再求右边界

        while left <= right:
            mid = (left+right) // 2
            # print(left, right, mid)
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
                last = mid
                break

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        # print(last)

        if first == -1 or last == -1:
            return [-1, -1]
        else:
            return [first, last]
# @lc code=end

