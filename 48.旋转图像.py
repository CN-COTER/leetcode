#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
# 先算出最后的结果，再进行替换
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         row, col = len(matrix), len(matrix[0])
#         news = []
#         for j in range(col):
#             for i in range(row-1, -1, -1):
#                 news.append(matrix[i][j])
#         a = 0
#         for i in range(row):
#             for j in range(col):
#                 matrix[i][j] = news[a]
#                 a += 1


# 方法二，观察总结
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        p1, p2 = 0, len(matrix)-1
        while p1 < p2:
            add = 0
            while add < (p2-p1):
                matrix[p1][p1+add] , matrix[p1+add][p2], matrix[p2][p2-add], matrix[p2-add][p1] = matrix[p2-add][p1], matrix[p1][p1+add] , matrix[p1+add][p2], matrix[p2][p2-add]
                add += 1
            # print(matrix)
            p1 += 1
            p2 -= 1
# @lc code=end

