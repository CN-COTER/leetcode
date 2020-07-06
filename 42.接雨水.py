#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
# class Solution:
#     # 暴力方法
#     def trap(self, height: List[int]) -> int:
        # length = len(height)
        # def left_max(height, i):
        #     l_max = 0
        #     if i == 0:
        #         return 0
        #     while i >= 0:
        #         l_max = max(l_max, height[i])
        #         i -= 1
        #     return l_max
        
        # def right_max(height, j):
        #     r_max = 0
        #     if j == length-1:
        #         return  0
        #     while j < length:
        #         r_max = max(r_max, height[j])
        #         j += 1
        #     return r_max
        
        # res = 0
        # for i in range(length):
        #     l = left_max(height, i)
        #     r = right_max(height, i)
        #     # print(i)
        #     # print('-----------')
        #     # print(l)
        #     # print(r)
        #     if min(l, r) > height[i]:
        #         # print(f'{i} : {min(l, r)- height[i]}')
        #         res += min(l, r)- height[i]
        # return res

class Solution:
    # DP
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        length = len(height)
        max_left, max_right = [0]*length, [0]*length
        max_left[0], max_right[-1] = 0, 0
        for i in range(1, length):
            max_left[i] = max(max_left[i-1], height[i-1])
        for j in range(length-2, -1, -1):
            max_right[j] = max(max_right[j+1], height[j+1])
        # print(max_left)
        # print(max_right)
        # print('-----------------------------')
        for i in range(length):
            m = min(max_left[i], max_right[i])
            # print(height[i])
            if height[i] < m:
                # print(m-height[i])
                res += m-height[i]
            
        return res

# @lc code=end

