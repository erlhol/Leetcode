class Solution:
    # Solution explaination:
    # 1. Set the correct neighbours
    # 2. Traverse each node, and check how many such iterations we have of unvisited nodes

    def numIslands(self, grid: List[List[str]]) -> int:
        graph = self.connect_nodes(grid)
        visited = set()
        count = 0
        for coord in graph:
            if coord not in visited:
                visited.update(self.DFS(graph, coord))
                count += 1

        return count

    def DFS(self, G, start):
        stack = [start]
        visited = {start}
        while stack:
            v = stack.pop()
            for u in G[v]:
                if u not in visited:
                    visited.add(u)
                    stack.append(u)
        return visited

    def connect_nodes(self, grid):
        G = dict()
        x = 0
        y = 0
        for row in grid:
            for element in row:
                boundaries = len(grid), len(row)
                if element == "1":
                    G[(x, y)] = set()
                    self.assign_neighbours(grid, x, y, G, boundaries)
                y += 1
            x += 1
            y = 0
        return G

    def assign_neighbours(self, grid, x, y, graph, boundaries):
        neighbours = self.find_neighbours(x, y)
        for neighbour in neighbours:
            x_neigh, y_neigh = neighbour
            x_boundary, y_boundary = boundaries
            if x_neigh < 0 or x_neigh >= x_boundary:
                continue
            if y_neigh < 0 or y_neigh >= y_boundary:
                continue
            if grid[x_neigh][y_neigh] == "1":
                graph[(x, y)].add((x_neigh, y_neigh))

    def find_neighbours(self, x, y):
        # A node have in total four neighbours
        above_cell = (x - 1, y)
        below_cell = (x + 1, y)
        left_cell = (x, y - 1)
        right_cell = (x, y + 1)
        return [above_cell, below_cell, left_cell, right_cell]
