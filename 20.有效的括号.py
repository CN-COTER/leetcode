#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'}':'{', ')':'(', ']':'['}
        a = set(['(', '[', '{'])
        for char in s:
            if char in a:
                stack.append(char)
            else:
                if stack:
                    c = stack.pop()
                    if c != d[char]:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
# @lc code=end

