class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ix=0
        nums.reverse()
        while len(nums):
            i = nums.pop()
            nums.reverse()
            if target-i in nums:
                return [ix, nums.index(target-i)+ix+1]
            ix+=1
            nums.reverse()