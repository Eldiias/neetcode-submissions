class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {i:nums.count(i) for i in nums}
        out = []
        for i in range(k):
            z = [i for i,j in dct.items() if j==max(dct.values())][0]
            out.append(z)
            dct.pop(z)
        return out