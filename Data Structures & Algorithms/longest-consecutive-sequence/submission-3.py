class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        z = list(set(nums))
        z.sort()
        if not z: return 0
        k = []
        for ix, i in enumerate(z):
            if ix==0:
                pass
            else:
                k.append(i - z[ix-1]-1)
        print(k)
        max_l = -1
        kk = 0
        for i in k:
            print(kk, max_l, i)
            if i==0:
                kk+=1
            else:
                if kk>max_l:
                    max_l=kk
                kk = 0
        if kk>max_l:
            max_l=kk
        return max_l+1