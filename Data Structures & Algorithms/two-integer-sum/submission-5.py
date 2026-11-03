class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = dict()

        for ix,i in enumerate(nums):
            if target-i in dct.keys():
                print(dct)
                return [dct[target-i], ix]
            else:
                dct[i]=ix