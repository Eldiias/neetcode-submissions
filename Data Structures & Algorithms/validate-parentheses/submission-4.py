class Solution:
    # beats 100% in leetcode. 0ms
    def isValid(self, s: str) -> bool:
        asd = []
        dct = {'(':')', '[':']', '{':'}'}
        if not (s[0] in dct): return False
        for i in s:
            if i in dct:
                asd.append(i)
            else:
                if asd:
                    if dct[asd[-1]]!=i:
                        return False
                    else:
                        asd.pop()
                else:
                    return False
        if asd:
            return False
        else:
            return True
        