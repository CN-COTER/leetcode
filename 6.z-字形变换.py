#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [''] * numRows
        i, flag = -1, 1
        for char in s:
            if flag:
                i += 1
                res[i] += char
            else:
                i -= 1
                res[i] += char

            if i == numRows-1:
                flag = 0
            if i == 0:
                flag = 1

        return ''.join(res)
# @lc code=end

