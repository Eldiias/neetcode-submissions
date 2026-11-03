class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        mi = r

        ceil = lambda x,y: x//y + (1 if x%y else 0)
        if sum(piles)<h: return 1
        while l<=r:
            m = (l+r)//2
            mm = sum(ceil(x,m) for x in piles)
            if mm<=h:
                mi=m
                r = m-1
            else:
                l=m+1
        return mi