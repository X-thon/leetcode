class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n <= 1: return n
        nums = [i for i in range(n)]
        step = 0
        while len(nums) > 1:
            step = (step+m-1) % len(nums)
            nums.pop(step)
        return nums[0]