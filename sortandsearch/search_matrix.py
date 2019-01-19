class Solution(object):
    def search_matrix(self, matrix, target):
        """
        :param matrix: List[List[int]]
        :param target: int
        :return: List[int]
        Time: O(m + n)
        Space: O(1)
        """
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return [row, col]
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return [-1, -1]


if __name__ == '__main__':
    ip = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(Solution().search_matrix(ip, 0))
