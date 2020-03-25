#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
from typing import List
# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # cubes, faces = 0, 0
        # for row in range(0, n):
        #     for col in range(0, n):
        #         cubes += grid[row][col]
        #         if grid[row][col] > 0: 
        #             faces += grid[row][col] - 1
        #         if row > 0:
        #             faces += min(grid[row-1][col], grid[row][col])
        #         if col > 0:
        #             faces += min(grid[row][col-1], grid[row][col])
        # return 6 * cubes - 2 * faces

        # 解法2
        area, n = 0, len(grid)
        for row in range(0, n):
            for col in range(0, n):
                if grid[row][col]: area += grid[row][col] * 4 + 2 
                if row < n-1 and grid[row+1][col]: area -= min(grid[row+1][col], grid[row][col]) * 2
                if col < n-1 and grid[row][col+1]: area -= min(grid[row][col+1], grid[row][col]) * 2
        return area



# @lc code=end

