class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        u = len(matrix)
        if target in matrix[l]: return True
        if target in matrix[u-1]: return True
        m_1 = 0
        while l<u:
            m = l + ((u-l)//2)
            if m_1==m: return False
            if target in matrix[m]: return True
            if target>matrix[m][-1]:
                l = m+1
            if target<matrix[m][0]:
                u = m-1
            m_1=m
        return False