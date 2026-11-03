class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rs = set()
        cs = set()
        m = len(matrix)
        n = len(matrix[0])
        for ix, row in enumerate(matrix):
            for jx, val in enumerate(row):
                if val==0:
                    rs.add(ix)
                    cs.add(jx)
        print(rs, cs)
        for row in rs:
            matrix[row] = [0]*n
        for col in cs:
            for row in range(m):
                # print(row, col)
                if row in rs:
                    continue
                matrix[row][col] = 0
        print(matrix)