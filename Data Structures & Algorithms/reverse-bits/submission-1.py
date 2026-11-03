class Solution:
    def reverseBits(self, n: int) -> int:
        if n==0: return 0
        n = str(bin(n))[2:].zfill(32)
        jj = n.index('1')
        n = n.lstrip('0')
        n = n[::-1]
        n = n + '0'*jj
        return int(n,2)