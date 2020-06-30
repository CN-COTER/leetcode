#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        max_len = 1
        start, end = 0, 0

        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        start, end = i, j
                

        return s[start: end+1]


# @lc code=end

