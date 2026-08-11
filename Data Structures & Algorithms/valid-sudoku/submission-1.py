class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                elm = board[r][c]
                if elm == ".":
                    continue
                elif elm in rows[r]:
                    return False
                elif elm in cols[c]:
                    return False
                elif elm in squares[(r//3, c//3)]:
                    return False
                else:
                    rows[r].add(elm)
                    cols[c].add(elm)
                    squares[(r//3,c//3)].add(elm)
        return True