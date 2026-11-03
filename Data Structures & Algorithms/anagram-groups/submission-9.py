class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict()
        for i in strs:
            hl = [0 for _ in range(26)]
            for ix,jx in Counter(i).items():
                hl[ord(ix)-97] = jx
            j = tuple(hl)
            if j not in s:
                s[j] = []
            s[j].append(i)
            
        return [i for i in s.values()]