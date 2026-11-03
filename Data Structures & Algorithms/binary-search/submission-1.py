class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)
        if nums[a]==target: return a
        if nums[b-1]==target: return b-1
        m_1 = a
        m = b
        while a<b:
            m = (a+b)//2
            if m_1==m: return -1
            # print(m, nums[m])
            if nums[m]==target: return m
            if nums[m]>target:
                b = m
            else:
                a = m
            m_1=m
            

        return -1