class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_n = len(nums)
        while max_n>=0:
            if max_n in nums:
                max_n-=1
            else:
                return max_n
