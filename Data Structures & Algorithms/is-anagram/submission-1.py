class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {i:s.count(i) for i in s}
        d2 = {i:t.count(i) for i in t}
        if set(s)!=set(t):
            return False
        
        return d1==d2