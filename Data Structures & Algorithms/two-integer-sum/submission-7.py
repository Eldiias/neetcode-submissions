class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct=dict()
        for ix,i in enumerate(nums):
            if i in dct.keys():
                return [dct[i], ix]
            dct[target-i] = ix
        