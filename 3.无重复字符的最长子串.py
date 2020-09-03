#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        max_len = 0
        for i in range(len(s)):
            if s[i] not in window:
                window.append(s[i])
            else:
                window[:] = window[window.index(s[i])+1:]
                # print('---------------')
                # print(''.join(window))
                window.append(s[i])
            # print(''.join(window))
            max_len = max(max_len, len(window))
        return max_len if max_len != 0 else 0    



'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        a = {}
        tmp_str = ''
        max_length = -1 * float("inf")

        for i in range(len(s)):
            
            if (s[i] not in a.keys()) or (s[i] not in tmp_str) :
                a[s[i]] = i
                tmp_str += s[i]
                max_length = max(max_length, len(tmp_str))

            else:
                
                last_i_index = a[s[i]]
                tmp_str = s[last_i_index+1:i+1]
                a[s[i]] = i
 
        return max_length
'''

# @lc code=end

