#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#
from typing import List
# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        if not nums: return 0
        sum_for_nums = sum(nums)
        r = sum_for_nums % 3 # 将数组整个求和后取余
        if r == 0: return sum_for_nums # 如果余数为0，依照题意，直接返回数组和即可

        r1, r2 = [], [] # r1存数组中整除3余1的数，r2存数组中整除3余2的数
        for num in nums:
            if num % 3 == 1: r1.append(num)
            elif num % 3 == 2: r2.append(num)
        r1.sort() # 将列表从小到大排序
        r2.sort()

        sub = [] # sub存储 “将要被减去的数字”
        # 如果数组和整除3余1，那么可以考虑3种情况：
        # 1.删除掉一个数组中整除3余1的、最小的数字；
        # 2.删除掉两个数组中整除3余2的、和最小的数字； 1，2两种情况对比，哪个值小就执行哪一条；
        # 3.数组和整除3余1，并且数组中没有整除3余1的数字且没有两个整除3余2的数字（或只有一个4之类的余1的数），那么此时只能返回0值
        if r == 1: # 如果整个数组求和后整除3余1
            if r1: sub.append(r1[0]) # 此处判断条件等价于 if r1 != []: 
            
            # 如果除3余2的数字有两个，取最小的两个求和，用来与上一步中取得的数做比较(如果取到的话)
            # r2[:2]是一个切片操作，表示从头取到索引2之前一位的数字，即[0,2),是一个左闭右开区间
            if len(r2) >= 2: sub.append(sum(r2[:2])) 
            
            if not sub: # 第三种情况
                return 0 
            else:
                return sum_for_nums - min(sub) # 取1、2情况中最小的数(如果两种情况同时成立); 如果两种情况支成立一种，取min也不会报错
        else: # 等价于 elif r == 2: ; 同样存在三种情况
            if r2: sub.append(r2[0])
            if len(r1) >= 2: sub.append(sum(r1[:2]))

            if not sub: return 0
            else: return sum_for_nums - min(sub)


# @lc code=end

