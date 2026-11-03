class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {i:s.count(i) for i in s}
        d2 = {i:t.count(i) for i in t}
        return d1==d2