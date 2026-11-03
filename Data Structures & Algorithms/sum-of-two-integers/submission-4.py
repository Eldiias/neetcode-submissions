class Solution:
    def getSum(self, a: int, b: int) -> int:
        import numpy as np
        z1 = np.zeros(abs(a))
        z2 = np.zeros(abs(b))
        s1 = int(np.sign(a))
        s2 = int(np.sign(b))

        if a*b==0:
            return a if a else b
        if a*b>0:
            return s1*len(np.append(z1,z2))
        else:
            if len(z1)>len(z2):
                return len(z1[abs(b):])*s1
            else:
                return len(z2[abs(a):])*s2