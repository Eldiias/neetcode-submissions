# class Solution:
# # This solution performed 47ms, 34.42MB, beating 73.77%
#     def longestConsecutive(self, nums: List[int]) -> int:
#         z = list(set(nums))
#         z.sort()
#         if not z: return 0
#         k = []
#         for ix, i in enumerate(z):
#             if ix==0:
#                 pass
#             else:
#                 k.append(i - z[ix-1]-1)
#         max_l = -1
#         kk = 0
#         for i in k:
#             if i==0:
#                 kk+=1
#             else:
#                 if kk>max_l:
#                     max_l=kk
#                 kk = 0
#         if kk>max_l:
#             max_l=kk
#         return max_l+1

class Solution:
# 
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        z = sorted(list(set(nums)))
        k = []
        max_ = 0
        for ix, i in enumerate(z):
            k.append(i)
            z = 1
            while True:
                if i-z in k:
                    z+=1
                else:
                    break
            max_ = max(max_, z)
        return max_
            