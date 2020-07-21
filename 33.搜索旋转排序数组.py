#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    # 按照mid划分，一侧一定是有序的，只需要在另一侧无序的一侧进行判断就行。
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l, r = 0, length-1
        while l <= r:
            print(l, r)
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid

            # 判断哪一块是有序的，左侧有序，
            elif nums[mid] >= nums[l]:
                # 此时再去判断是在有序的一侧，还是在无序的一侧。
                if target >= nums[l] and target <= nums[mid]:
                    r = mid
                else:
                    l = mid+1
            else:
                if target >= nums[mid] and target <= nums[r]: 
                    l = mid
                else:
                    r = mid-1
        return -1
                
# @lc code=end

