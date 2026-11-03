class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)-1
        l = 0

        if len(nums)==1: return 0 if nums[0]==target else -1
        if len(nums)==2: return 0 if nums[0]==target else 1 if nums[1]==target else -1

        if nums[l]==target: return l
        if nums[r]==target: return r

        while r-l>1:
            mid = (l+r)//2
            
            if nums[mid]==target: return mid
            
            # print(nums[l],nums[mid],nums[r])
            if nums[l]<=nums[mid]:
                if nums[mid]>target>=nums[l]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid]<target<=nums[r]:
                    l = mid
                else:
                    r = mid
        return -1
