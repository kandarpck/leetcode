class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Time: O(n*m)
        Space: O(h) space of the internal dfs stack
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = '#'
        print(grid)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)


class Solution2:
    def numIslandsNonDestructive(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Time: O(n*m)
        Space: O(h) space of the internal dfs stack
        """

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j] or visited[i][j]:
                return
            visited[i][j] = True
            print(visited)
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        return count


if __name__ == '__main__':
    print(Solution().numIslands([[1, 0, 0, 0, 1, 0, 1],
                                 [1, 0, 0, 1, 1, 0, 0]]))

    print(Solution2().numIslandsNonDestructive([[1, 0, 0, 0, 1, 0, 1],
                                                [1, 0, 0, 1, 1, 0, 0]]))
