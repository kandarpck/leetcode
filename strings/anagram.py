from collections import defaultdict


class Solution:
    def isAnagram(self, s, t):
        """
        Time: N
        Space: 1
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        for char in t:
            if char not in count:
                count[char] = -1
            else:
                count[char] -= 1
            if count[char] < 0:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    ip = 'harsh'
    ip2 = 'srhah'
    print(sol.isAnagram(ip, ip2))
    ip = 'aacc'
    ip2 = 'ccac'
    print(sol.isAnagram(ip, ip2))
