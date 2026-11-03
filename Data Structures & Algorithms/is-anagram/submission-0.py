class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {i:s.count(i) for i in s}
        d2 = {i:t.count(i) for i in t}
        if set(s)!=set(t):
            return False
        for i in d1.keys():
            if d1[i]!=d2[i]:
                return False
        return True