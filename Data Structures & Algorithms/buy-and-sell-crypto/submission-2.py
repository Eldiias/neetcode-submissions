class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_ = float("inf")
        miix = -1
        miax = len(prices)
        max_ = -float('inf')
        bp = 0
        for ix, i in enumerate(prices):
            print(min_, miix, max_, miax, bp)
            if i<min_: 
                min_ = i
                miix = ix
                if miax<ix:
                    miax = len(prices)
                    max_ = -float('inf')
            elif i==min_:
                continue
            else:
                if i>=max_:
                    max_ = i
                    miax = ix
                    
                    if bp<max_-min_:
                        bp = max_-min_
        return bp