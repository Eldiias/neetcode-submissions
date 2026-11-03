class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if len(set(row)-set('.'))!=len([i for i in row if i!='.']):
                return False
        for i in range(9):
            col = [j[i] for j in board]
            if len(set(col)-set('.'))!=len([i for i in col if i!='.']):
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = [l for k in board[i:i+3] for l in k[j:j+3]]
                if len(set(box)-set('.'))!=len([i for i in box if i!='.']):
                    return False
        return True