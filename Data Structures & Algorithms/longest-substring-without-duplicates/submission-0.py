class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        _ = ""
        for ix, r in enumerate(s):
            if not (r in _):
                _+=r
                if ix==len(s)-1:
                    l = max(l, len(_))
            else:
                l = max(l, len(_))
                while r in _:
                    _ = _[1:]
                _+=r                
        return l