class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        if not grid:
            return 0

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            
            while q:
                r, c = q.popleft()
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    qr = r + dr
                    qc = c + dc

                    if (qr in range(rows) and
                        qc in range(cols) and 
                        grid[qr][qc] == "1" and
                        (qr, qc) not in visit):
                        q.append((qr, qc))
                        visit.add((qr, qc))

            
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1" and (r,c) not in visit):
                    bfs(r,c)
                    islands += 1
        
        return islands