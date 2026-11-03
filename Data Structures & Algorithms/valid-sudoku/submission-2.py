class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if {i:row.count(i) for i in set(row) if i!='.'}!={i:1 for i in set(row) if i!='.'}: return False
        for i in range(9):
            col = [j[i] for j in board]
            if {i:col.count(i) for i in set(col) if i!='.'}!={i:1 for i in set(col) if i!='.'}: return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = [l for k in board[i:i+3] for l in k[j:j+3]]
                if {i:box.count(i) for i in set(box) if i!='.'}!={i:1 for i in set(box) if i!='.'}: return False
        return True