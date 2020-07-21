#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#


# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        people.sort(key=lambda x: (-1*x[0], x[1]))
        # people.sort(key=lambda x: x[1])
        # print(people)
        res = [people[0]]
        for i in range(1, len(people)):
                res.insert(people[i][1], people[i])
        return res
# @lc code=end

