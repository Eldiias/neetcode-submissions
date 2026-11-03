class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        past = (l,r)
        while l<=r:
            if nums[l]==target: return l
            if nums[r]==target: return r

            m = (l+r)//2
            if nums[m]==target: return m
            if nums[m]>target:
                r=m
                if past==(l,r):
                    return -1
            else:
                l=m
                if past==(l,r):
                    return -1
            past = (l,r)
        return -1