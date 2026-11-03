class Solution:
    def isValid(self, s: str) -> bool:
        # tre = [0,0,0]
        asd = ""
        dct = {'(':')', '[':']', '{':'}'}
        if not (s[0] in dct): return False
        for i in s:
            if i in dct:
                asd+=i
            else:
                if asd:
                    if dct[asd[-1]]!=i:
                        return False
                    else:
                        asd = asd[:-1]
                else:
                    return False
        # print(asd)
        if asd:
            return False
        else:
            return True
        # for i in asd:
        #     if i=='(':
        #         tre[0]+=1
        #     elif i==')':
        #         tre[0]-=1
        #     elif i=='[':
        #         tre[1]+=1
        #     elif i==']':
        #         tre[1]-=1
        #     elif i=='{':
        #         tre[2]+=1
        #     elif i=='}':
        #         tre[2]-=1
        # return not sum(tre)