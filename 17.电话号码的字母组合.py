#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
# 深度遍历回溯
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
             '8': 'tuv', '9': 'wxyz'}
        str_list = []

        def dfs(tmp ,nexts):
            if not nexts:
                str_list.append(tmp)

            else: 
                for j in d[nexts[0]]:
                    dfs(tmp+j, nexts[1:])
        dfs('', digits)
        return str_list
# @lc code=end

