class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        for i in strs:
            hl = [0]*26
            for ix,jx in Counter(i).items():
                hl[ord(ix)-97] = jx
            s[tuple(hl)].append(i)
            
        return list(s.values())