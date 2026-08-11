class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Create unique identifiers for the row, column, and 3x3 box
                row_check = (val, "row", r)
                col_check = (val, "col", c)
                box_check = (val, "box", r // 3, c // 3)
                
                # If we've already seen this value in any of the 3 constraints, it's invalid
                if row_check in seen or col_check in seen or box_check in seen:
                    return False
                
                # Otherwise, record all the states
                seen.add(row_check)
                seen.add(col_check)
                seen.add(box_check)
                
        return True
