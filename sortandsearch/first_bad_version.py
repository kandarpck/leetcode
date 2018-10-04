class Solution:

    def isBadVersion(self, version):
        if version >= 4:
            return True

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    print(Solution().firstBadVersion(10))
