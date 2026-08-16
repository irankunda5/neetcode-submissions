class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            m = (top + bot) // 2
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bot = m - 1
            else:
                break
        if not (top <= bot):
            return False

        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            mm = (l + r) // 2
            if matrix[m][mm] < target:
                l = mm + 1
            elif matrix[m][mm] > target:
                r = mm - 1
            else:
                return True
        return False