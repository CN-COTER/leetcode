#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x), bin(y)
        x, y = x[2:], y[2:]
        res = 0
        length = len(x) if len(x)> len(y) else len(y)
        x = x if len(x) == length else '0' * (length - len(x)) + x
        y = y if len(y) == length else '0' * (length - len(y)) + y
        
        for i in range(length):
            if x[i] != y[i]:
                res += 1
            else:
                pass
        return res
        
# @lc code=end

