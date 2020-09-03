#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         a = [(string, ''.join(sorted(string))) for string in strs]
#         d = {}
#         tmp = []
#         for string, sort_string in a:
#             if sort_string not in tmp:
#                 d[sort_string] = [string]
#                 tmp.append(sort_string)
#             else:
#                 d[sort_string].append(string)
#         res = list(d.values())
#         return res

# 改进
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            sort_string = ''.join(sorted(string))
            if d.get(sort_string):
                d[sort_string].append(string)
            else:
                d[sort_string] = [string]
        return list(d.values())
# @lc code=end

