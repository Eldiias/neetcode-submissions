class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = dict()

        for i in strs:
            j = ''.join(sorted(i))
            print(j)
            if j in dct.keys():
                dct[j].append(i)
            else:
                dct[j] = [i]
        return [j for i,j in dct.items()]