class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0,1], [0,-1], [1, 0], [-1,0]]
                for dr, dc in directions:
                    qr = row + dr
                    qc = col + dc
                    if (qr in range(rows) and
                        qc in range(cols) and 
                        grid[qr][qc] == "1" and 
                        (qr,qc) not in visit):
                        q.append((qr,qc))
                        visit.add((qr,qc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1                

        return islands