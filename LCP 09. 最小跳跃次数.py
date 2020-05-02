from typing import List
from queue import Queue

class Solution:
    def minJump(self, jump: List[int]) -> int:
        # visit = [0 for _ in range(len(jump))]
        # q = Queue()
        # q.put((0,0))
        # visit[0] = 1
        # max_left_idx = 0
        # while q:
        #     cur_idx, count = q.get()
        #     right_idx = cur_idx + jump[cur_idx]
        #     if right_idx >= len(jump):
        #         return count + 1
        #     else:
        #         if not visit[right_idx]:
        #             q.put((right_idx, count+1))
        #             visit[right_idx] = 1
        #     for i in range(max_left_idx+1, cur_idx):
        #         if not visit[i]:
        #             q.put((i, count+1))
        #             visit[i] = 1
        #     max_left_idx = max(max_left_idx, cur_idx)

        # 使用列表代替Queue，时间空间开销都变小了
        # 使用visit[i]记录索引i是否访问
        visit = [0 for _ in range(len(jump))]
        # q作为队列，记录元组数据：(当前位置, 当前步数)
        q = [(0,0)]
        visit[0] = 1
        # max_left_idx记录已访问过的最大index，对于 i<=max_left_idx，有 visit[i] = 1
        max_left_idx = 0
        # BFS遍历
        while q:
            cur_idx, count = q.pop(0)
            right_idx = cur_idx + jump[cur_idx]
            if right_idx >= len(jump):
                return count + 1
            else:
                if not visit[right_idx]:
                    q.append((right_idx, count+1))
                    visit[right_idx] = 1
            for i in range(max_left_idx+1, cur_idx):
                if not visit[i]:
                    q.append((i, count+1))
                    visit[i] = 1
            max_left_idx = max(max_left_idx, cur_idx)

        # # 更简洁的BFS写法，但内存消耗更大
        # max_left_idx, visited, q = 0, {0}, [(0,0)]
        # while q:
        #     cur_idx, step = q.pop(0)
        #     for r in ([cur_idx + jump[cur_idx]] + list(range(max_left_idx+1, cur_idx))):
        #         if r >= len(jump): return step+1
        #         if r in visited: continue
        #         q.append((r, step+1))
        #         visited.add(r)
        #     max_left_idx = max(max_left_idx, cur_idx)
        # return -1