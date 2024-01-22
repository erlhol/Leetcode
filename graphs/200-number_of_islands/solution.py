class Solution:
    # Solution explaination:
    # Traverse each node, and check how many such iterations we have of unvisited nodes
    # Use recursion

    def numIslands(self, grid: List[List[str]]) -> int:
        X = len(grid)
        Y = len(grid[0])
        count = 0
        for x in range(X):
            for y in range(Y):
                if grid[x][y] == "1":
                    self.DFS(grid, x, y, X, Y)
                    count += 1
        return count

    def DFS(self, grid, x, y, X, Y):
        if x < 0 or y < 0 or x >= X or y >= Y or grid[x][y] != "1":
            return
        grid[x][y] = "x"  # Add as seen
        neighbours = self.find_neighbours(x, y)
        for neighbour in neighbours:
            n_x, n_y = neighbour
            self.DFS(grid, n_x, n_y, X, Y)

    def find_neighbours(self, x, y):
        # A node have in total four neighbours
        above_cell = (x - 1, y)
        below_cell = (x + 1, y)
        left_cell = (x, y - 1)
        right_cell = (x, y + 1)
        return [above_cell, below_cell, left_cell, right_cell]
