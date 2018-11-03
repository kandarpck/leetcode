class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """

        def win(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in xrange(3)):
                    return True
                if all(board[j][i] == player for j in xrange(3)):
                    return True

            return (player == board[1][1] == board[0][0] == board[2][2] or
                    player == board[1][1] == board[0][2] == board[2][0])


if __name__ == '__main__':
    pass
