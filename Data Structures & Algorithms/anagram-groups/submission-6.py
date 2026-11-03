class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        dct = dict()

        for i in strs:
            j = ''.join(sorted(i))

            if j in dct.keys():
                dct[j].append(i)
            else:
                dct[j] = [i]
        return list(dct.values())