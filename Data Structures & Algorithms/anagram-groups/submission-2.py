class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        
        dct={}
        for i in strs:
            print(''.join(sorted(i)))

            s = ''.join(sorted(i))
            if s in dct.keys():
                dct[s].append(i)
            else:
                dct[s]=[i]
        return list(dct.values())