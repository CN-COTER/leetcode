#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        if not grid:
            return 0
        count = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    count += 1
                    # print('-----------------')
                    queue =  deque()
                    queue.append((i, j))
                    while len(queue) > 0:
                        a, b = queue.pop()
                        for af, bt in [[a+1, b], [a, b+1], [a-1, b], [a, b-1]]:
                            if  0 <= af <= row-1 and 0 <= bt <= col-1 and grid[af][bt] == '1':
                                queue.appendleft([af, bt])
                                grid[af][bt] = '0'
        return count
# @lc code=end

