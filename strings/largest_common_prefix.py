class Solution:
    def longestCommonPrefix(self, strs):
        """
        Time: N log N
        Space 1
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        while first:
            if last.find(first) == 0:
                return first
            else:
                first = first[:-1]
        return ''


if __name__ == '__main__':
    sol = Solution()
    ip = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(ip))