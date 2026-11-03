class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        z = []
        for i in nums:
            if i in z:
                return True
            else:
                z.append(i)
        return False