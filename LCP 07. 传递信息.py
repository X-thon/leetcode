import collections
from typing import List

# BFS方法
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        # 构造图
        d = collections.defaultdict(list)
        for source, target in relation:
            d[source].append(target)
        q = [0]
        while q:
            target_point_count = len(q)
            for _ in range(target_point_count):
                # 取出上一步中可到达点的所有可达点
                source = q.pop(0)
                targets = d[source]
                q.extend(targets)
            k -= 1
            # 走了k步时，计算可达点中是否含有目标点
            if k == 0:
                res = q.count(n-1)
                break
        return res


# 反向回溯法
class Solution2:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        # 构造反向回溯图
        d = collections.defaultdict(list)
        for source, target in relation:
            d[target].append(source)
        old = [n-1]
        # 回溯k步
        for _ in range(k):
            new = []
            if not old:
                return 0
            else:
                for target in old:
                    if target in d:
                        new.extend(d[target])
                old = new
        return old.count(0)