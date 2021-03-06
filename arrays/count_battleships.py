class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        # Time:  O(m * n)
        # Space: O(1)

        """
        if not board or not board[0]:
            return 0

        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                cnt += int(board[i][j] == 'X' and
                           (i == 0 or board[i - 1][j] != 'X') and
                           (j == 0 or board[i][j - 1] != 'X'))
        return cnt


if __name__ == '__main__':
    pass
