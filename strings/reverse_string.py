class Solution:
    def reverseString(self, s):
        """
        Time: N - iterate over elems
        Space: N
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

    def reverseStringNormal(self, s):
        """
        Time: N
        Space: N
        :param s:
        :return:
        """
        string_list = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            string_list[i], string_list[j] = string_list[j], string_list[i]
            i += 1
            j -= 1
        return "".join(string_list)


if __name__ == '__main__':
    sol = Solution()
    ip = "hello"
    print(sol.reverseString(ip))
    print(sol.reverseStringRecursive(ip))
    print(sol.reverseStringNormal(ip))
