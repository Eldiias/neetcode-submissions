class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        gg = set()
        for ix,i in enumerate(nums):
            for jx,j in enumerate(nums[ix+1:-1]):
                if abs(i+j)>nums[-1]:
                    continue
                else:
                    if -(i+j) in nums[ix+jx+2:]:
                        gg.add((i,j,-(i+j)))
        
        return [list(i) for i in {tuple(sorted(i)) for i in gg}]