class Solution:
    def reverseBits(self, n: int) -> int:
        # # This is string manip solution. 
        # if n==0: return 0
        # n = str(bin(n))[2:].zfill(32)
        # jj = n.index('1')
        # n = n.lstrip('0')
        # n = n[::-1]
        # n = n + '0'*jj
        # return int(n,2)

        # This is bit manip solution
        result = 0
        for _ in range(32):
            # Step 1: shift result left to make space
            result <<= 1
            # Step 2: take the last bit of n
            result |= (n & 1)
            # Step 3: remove the last bit from n
            n >>= 1
        
        return result