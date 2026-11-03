class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        l = re.findall(r'[a-zA-Z0-9]', s)
        t = ''.join(l).lower()
        print(t)
        return t==t[::-1]