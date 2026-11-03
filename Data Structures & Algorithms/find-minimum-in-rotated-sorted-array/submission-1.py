class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        if len(nums)==2: return nums[0] if nums[0]<nums[1] else nums[1]
        l = 0
        r = len(nums) - 1
        search = True
        if nums[-1]>nums[0]: return nums[0]
        
        while search:
            mid = (r-l)//2
            if nums[mid]<nums[mid-1]: return nums[mid]
            if nums[mid]>nums[l]:
                l = mid
            else: 
                r = mid
