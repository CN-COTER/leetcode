#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        import functools
        @functools.lru_cache(None)
        def dfs_helper(s):
            if  s == '':
                return True
            flag = False
            length = len(s)
            for i in range(1, length+1):
                if s[:i] in wordDict:
                    # print(s[:i])
                    flag = dfs_helper(s[i:]) or flag
            return flag
        return dfs_helper(s)

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         import functools
#         @functools.lru_cache(None)
#         def back_track(s):
#             if(not s):
#                 return True
#             res=False
#             for i in range(1,len(s)+1):
#                 if(s[:i] in wordDict):
#                     res=back_track(s[i:]) or res
#             return res
#         return back_track(s)


# DP
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         wordDict = set(wordDict)
#         length = len(s)
#         dp = [False for _ in range(length+1)]
#         dp[0] = True
#         for i in range(length):
#             for j in range(i+1, length+1):
#                 if dp[i] and s[i:j] in wordDict:
#                     dp[j] = True   
#         return dp[-1]

# @lc code=end

