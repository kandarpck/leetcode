import re


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        else:
            s = re.sub('[^A-Za-z0-9]+', '', s)
            return s.lower() == s.lower()[::-1]


if __name__ == '__main__':
    sol = Solution()
    ip = 'harsh'
    print(sol.isPalindrome(ip))
    ip2 = 'nitin'
    print(sol.isPalindrome(ip2))
