class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return all([self.is_valid_row(board), self.is_valid_col(board), self.is_valid_box(board)])

    def is_valid_row(self, board):
        for row in board:
            if not self.is_valid_unit(row):
                return False
        return True

    def is_valid_col(self, board):
        for col in zip(*board):
            if not self.is_valid_unit(col):
                return False
        return True

    def is_valid_box(self, board):
        for i in range(0, len(board[0]), 3):
            for j in range(0, len(board), 3):
                box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_valid_unit(box):
                    return False
        return True

    def is_valid_unit(self, board_part):
        elems = [x for x in board_part if x != "."]
        return len(set(elems)) == len(elems)


if __name__ == '__main__':
    sol = Solution()
    ip = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(sol.isValidSudoku(ip))
    ip2 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(sol.isValidSudoku(ip2))
