class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        if n<4: return [0,1,1,2][:n+1]
        res[:4] = [0,1,1,2]
        k = 2
        t = 4
        while t<=n:
            k=t if k*2==t else k
            res[t] = res[t-k]+1
            t+=1
        return res