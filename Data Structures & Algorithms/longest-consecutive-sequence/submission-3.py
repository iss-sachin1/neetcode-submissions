class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)

        if len(s) == 1:
            return 1
        elif len(nums) == 0:
            return 0
        
        t_count = 1
        f_count = 0

        for num in s:
            while num - t_count in s:
                t_count += 1
            if t_count > f_count:
                f_count = t_count
            t_count = 1
        return f_count
        