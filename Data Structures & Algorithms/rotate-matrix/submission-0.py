class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # matrix = list(reversed(matrix))

        for i in range(n//2):
            matrix[i], matrix[-i-1] = matrix[-i-1], matrix[i]

        # print(matrix)
        for i in range(n):
            for k in range(n):
                if i==k:
                    break
                
                matrix[i][k], matrix[k][i] = matrix[k][i], matrix[i][k]
        # print(matrix)
        