#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 车的可用捕获量
#
from typing import List
# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def find():
            for i in range(8):
                for j in range(8):
                    if board[i][j] == "R": 
                        return i, j
        r, c = find()
        catch = 0
        for i in range(r+1, 8):
            if board[i][c] == "p":
                catch += 1
                break
            elif board[i][c] == "B": break
        for i in range(r-1, -1, -1):
            if board[i][c] == "p":
                catch += 1
                break
            elif board[i][c] == "B": break
        for j in range(c+1, 8):
            if board[r][j] == "p":
                catch += 1 
                break
            elif board[r][j] == "B": break
        for j in range(c-1, -1, -1):
            if board[r][j] == "p":
                catch += 1
                break
            elif board[r][j] == "B": break
        return catch

# @lc code=end

