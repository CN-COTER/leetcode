#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        news = []
        for j in range(col):
            for i in range(row-1, -1, -1):
                news.append(matrix[i][j])
        a = 0
        for i in range(row):
            for j in range(col):
                matrix[i][j] = news[a]
                a += 1

# @lc code=end

