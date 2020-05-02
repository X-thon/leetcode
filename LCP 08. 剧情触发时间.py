import bisect
from typing import List


class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        n = len(increase)+1
        C, R, H = [0], [0], [0]
        for c, r, h in increase:
            C.append(C[-1]+c)
            R.append(R[-1]+r)
            H.append(H[-1]+h)
        res = []
        for rc, rr, rh in requirements:
            # bisect.bisect_left(a,x, lo=0, hi=len(a)) 
            # 使用二分法来排序，它会将一个元素插入到一个有序列表的合适位置，这使得不需要每次调用 sort 的方式维护有序列表。
            # 默认是使用整个列表，如果 x 已经存在，在其左边插入。返回值为 index，并未实际插入
            # 如果 x 比 a 中所有数都小，返回0；比 a 中所有数都大，返回 len(a)+1；
            resC = bisect.bisect_left(C, rc)
            resR = bisect.bisect_left(R, rr)
            resH = bisect.bisect_left(H, rh)
            r = max(resC, resR, resH)
            if r == n:
                r = -1
            res.append(r)
        return res
        

