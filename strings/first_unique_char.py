from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_counter = Counter(s)
        for i, char in enumerate(s):
            if s_counter.get(char) == 1:
                return i
        return -1

    def firstUniqChar(self, s):
        """
        Time: N^2
        Space: N
        :type s: str
        :rtype: int
        """
        checked = set()
        for i, char in enumerate(s):
            if char not in checked and s.count(char, i) == 1:
                return i
            checked.add(char)
        return -1


if __name__ == '__main__':
    sol = Solution()
    ip = "leetcode"
    print(sol.firstUniqChar(ip))
    ip = "loveleetcode"
    print(sol.firstUniqChar(ip))
    ip = "nononononnooon"
    print(sol.firstUniqChar(ip))
