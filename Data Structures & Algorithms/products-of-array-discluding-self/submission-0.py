class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        if set(nums)=={0}:return [0]*len(nums)
        for i in nums:
            if i:
                product *= i
        l = []
        if 0 not in nums:
            return [int(product/i) for i in nums]
        elif nums.count(0)==1:
            return [int(product) if i==0 else 0 for i in nums]
        else:
            return [0]*len(nums)
        