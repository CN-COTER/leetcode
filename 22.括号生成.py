#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        count_left, count_right = 0, 0

        def dfs(string, count_left,count_right):
            if count_left == n and count_right == n:
                res.append(string)
            elif count_left > n:
                return
            else:
                if count_left > count_right:
                    dfs(string+'(', count_left+1, count_right)
                else:
                    dfs(string+'(', count_left+1, count_right)
        res = []
        dfs('', 0, 0)
        return res
# @lc code=end

