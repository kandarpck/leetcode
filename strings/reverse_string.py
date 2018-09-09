class Solution:
    def reverseString(self, s):
        """
        Time: N - iterate over elems
        Space: 1
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverseStringRecursive(self, s):
        """
        Time:
        :return:
        """
        if len(s) < 2:
            return s
        return self.reverseStringRecursive(s[len(s) // 2:]) + self.reverseStringRecursive(s[:len(s) // 2])


if __name__ == '__main__':
    sol = Solution()
    ip = "hello"
    print(sol.reverseString(ip))
    print(sol.reverseStringRecursive(ip))
