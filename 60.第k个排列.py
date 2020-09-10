#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def cal_mul(n):
            m = 1
            for i in range(n):
                m *= i+1
            return m

        res = []
        tmp_list = [i+1 for i in range(n)]
        tmp = 1
        k = k-1
        while k != 0 and n > 1:
            n = n-1
            # tmp 
            tmp = k // cal_mul(n)
            res.append(tmp_list[tmp])
            tmp_list.pop(tmp)
            k = k % cal_mul(n)
        res += tmp_list
        # print(res)
        return ''.join(map(str, res))
# @lc code=end

