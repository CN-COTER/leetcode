#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
#快速幂操作, 将幂由10进制转化为2进制
class Solution:
    def myPow(self, x: float, n: int) -> float:
        a = []
        if n < 0:
            x = 1/x
            n = -1 * n
        res, tmp = 1, x
        while n != 0:
            if n&1 == 0:
                a.append(0)
            else:
                a.append(1)
            n = n >> 1
        for i in a:            
            if i == 1:
                res *= tmp
            tmp = tmp * tmp
        return res
# @lc code=end

