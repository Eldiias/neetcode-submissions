class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        if set(s)!=set(t): return False

        d1=dict()
        d2=dict()
        for i in s:
            if i in d1.keys():
                d1[i]+=1
            else:
                d1[i]=1
        for i in t:
            if i in d2.keys():
                d2[i]+=1
            else:
                d2[i]=1
        
        return d1==d2