class Solution:
    def countBits(self, n: int) -> List[int]:
        # # Bit manipulation solution
        # res = [0]*(n+1)
        # if n<4: return [0,1,1,2][:n+1]
        # k = 1

        # for i in range(1,n+1):
        #     k=i if k*2==i else k
        #     res[i] = res[i-k]+1
        # return res

        # # Lazy solution
        # return [bin(i).count('1') for i in range(n+1)]

        # # Bit manip using the Number of 1 bits solution
        # ans = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     ans[i] = ans[i >> 1] + (i & 1)
        # return ans

        # Bit manip quickest, 0ms
        if n<1:
            return [0]
        n_dig = len(bin(n))-2
        digs = [0]
        for i in range(n_dig-1):
            digs = digs + [v+1 for v in digs]
        return digs + [v+1 for v in digs[:n-(1<<(n_dig-1))+1]]
