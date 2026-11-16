class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        mxt = max(temperatures)

        for l in range(len(temperatures)):
            if temperatures[l]==mxt: continue
            for r in range(l+1, len(temperatures)):
                if temperatures[r]>temperatures[l]:
                    res[l]=r-l
                    break
        return res
            